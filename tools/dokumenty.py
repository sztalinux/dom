#!/usr/bin/env python3
"""Dokumenty budowy: indeks folderu-centrum i paczka aktualnych plików dla claude.ai.

Folder-centrum (hub) to katalog, do którego wrzucasz wszystko od projektantów i wykonawców.
Domyślnie: dwa poziomy nad repozytorium (…/Dom/AI/dom → …/Dom), albo zmienna DOM_HUB.

    python3 tools/dokumenty.py                 # skan + przebudowa paczki + raport (uruchamia hook na starcie)
    python3 tools/dokumenty.py --dry-run       # to samo bez zapisu
    python3 tools/dokumenty.py ustaw "<ścieżka>" --eksport --nazwa "…" --opis "…" --kategoria "…"
    python3 tools/dokumenty.py ustaw "<ścieżka>" --bez-eksportu --opis "…"
    python3 tools/dokumenty.py lista [--nowe]  # stan indeksu
    python3 tools/dokumenty.py wgrane          # potwierdź: paczka wgrana do projektu na claude.ai

Zasady:
- Do paczki trafia tylko plik oznaczony --eksport (nowy plik nigdy nie trafia sam).
- Skrypt usuwa pliki wyłącznie w folderze paczki; plików w hubie nie przenosi i nie usuwa.
- Lista „do wgrania” liczona jest względem ostatniego potwierdzenia „wgrane”, nie ostatniego uruchomienia.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import logging
import warnings
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HUB = Path(os.environ.get("DOM_HUB", REPO.parent.parent)).expanduser().resolve()
CONF = HUB / ".dom"
INDEKS = CONF / "indeks.json"
WGRANE = CONF / "stan-wgrania.json"
PACZKA = HUB / "_Do claude.ai"
PRZYCHODZACE = HUB / "_Przychodzące"
SPIS = "00_SPIS.md"
POMIN_KATALOGI = {PACZKA, REPO.parent if REPO.parent != HUB else REPO}
KONTAKT = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+|(?<!\d)(\+48[\s-]?)?\d{3}[\s-]\d{3}[\s-]\d{3}(?!\d)")
WRAZLIWE_PESEL = re.compile(r"PESEL\D{0,5}\d{11}", re.I)
WRAZLIWE_KONTO = re.compile(r"(?<!\d)(PL)?\d{2}(\s?\d{4}){6}(?!\d)")
MAKS_LISTA = 15
NIESPRAWDZONE = "nie sprawdzono – "
LIMIT_MB = 30  # limit pojedynczego pliku na claude.ai
logging.getLogger("pypdf").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")


def nfc(s: str) -> str:
    """macOS zwraca nazwy w NFD – klucze indeksu trzymamy w NFC."""
    return unicodedata.normalize("NFC", s)


def sha1(p: Path) -> str:
    h = hashlib.sha1()
    with p.open("rb") as f:
        for blok in iter(lambda: f.read(1 << 20), b""):
            h.update(blok)
    return h.hexdigest()


def wczytaj(p: Path, domyslne):
    try:
        dane = json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return domyslne
    if "pliki" in dane:
        dane["pliki"] = {nfc(k): v for k, v in dane["pliki"].items()}
    return dane


def zapisz(p: Path, dane):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(dane, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(p)


def skanuj() -> dict:
    """{ścieżka względna: (rozmiar, mtime)} – bez ukrytych, paczki i katalogu z repozytorium."""
    out = {}
    for korzen, katalogi, pliki in os.walk(HUB):
        k = Path(korzen)
        katalogi[:] = [d for d in katalogi if not d.startswith(".") and (k / d).resolve() not in POMIN_KATALOGI]
        for n in pliki:
            if n.startswith(".") or n.startswith("~$"):
                continue
            p = k / n
            st = p.stat()
            out[nfc(p.relative_to(HUB).as_posix())] = (st.st_size, int(st.st_mtime))
    return out


def aktualizuj_indeks(ind: dict) -> dict:
    """Synchronizuje indeks z dyskiem. Zwraca zdarzenia do raportu."""
    pliki = ind.setdefault("pliki", {})
    dysk = skanuj()
    zd = {"nowe": [], "zmienione": [], "przeniesione": [], "usuniete": [], "duplikaty": []}

    for sciezka, (rozm, mt) in dysk.items():
        w = pliki.get(sciezka)
        if w and w["rozmiar"] == rozm and w["mtime"] == mt:
            continue
        h = sha1(HUB / sciezka)
        if w:
            if w["sha1"] != h:
                zd["zmienione"].append(sciezka)
                w["zmieniono"] = dt.date.today().isoformat()
            w.update(sha1=h, rozmiar=rozm, mtime=mt)
            continue
        pliki[sciezka] = {"sha1": h, "rozmiar": rozm, "mtime": mt, "status": "nowy",
                          "dodano": dt.date.today().isoformat()}

    # przeniesienia i usunięcia: wpis bez pliku na dysku
    for sciezka in [s for s in pliki if s not in dysk]:
        stary = pliki.pop(sciezka)
        cel = next((s for s, w in pliki.items() if w["status"] == "nowy" and w["sha1"] == stary["sha1"]), None)
        if cel:
            nowy = pliki[cel]
            pliki[cel] = {**stary, "sha1": nowy["sha1"], "rozmiar": nowy["rozmiar"], "mtime": nowy["mtime"]}
            zd["przeniesione"].append(f"{sciezka} → {cel}")
        else:
            zd["usuniete"].append(sciezka)

    # nowe pliki identyczne z już znanym → duplikat, bez eksportu
    for sciezka, w in pliki.items():
        if w["status"] != "nowy":
            continue
        org = next((s for s, x in pliki.items() if s != sciezka and x["status"] != "nowy" and x["sha1"] == w["sha1"]), None)
        if org:
            w.update(status="sklasyfikowany", eksport=False, kategoria="duplikat", opis=f"duplikat: {org}")
            zd["duplikaty"].append(sciezka)
        else:
            zd["nowe"].append(sciezka)
    return zd


def nazwa_w_paczce(sciezka: str, w: dict) -> str:
    n = w.get("nazwa") or Path(sciezka).name
    return n[:-4] + ".docx" if n.lower().endswith(".doc") else n


def tekst(p: Path) -> str:
    """Tekst dokumentu do kontroli danych wrażliwych ('' gdy nie da się odczytać)."""
    suf = p.suffix.lower()
    if suf == ".pdf":
        from pypdf import PdfReader  # noqa: PLC0415 – ImportError obsługuje dane_wrazliwe
    try:
        if suf == ".pdf":
            return "\n".join((s.extract_text() or "") for s in PdfReader(p).pages)
        if suf in (".doc", ".docx", ".rtf", ".odt"):
            return subprocess.run(["textutil", "-convert", "txt", "-stdout", str(p)],
                                  capture_output=True, text=True).stdout
        if suf in (".md", ".txt", ".csv"):
            return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:  # noqa: BLE001
        return ""
    return ""


def dane_wrazliwe(p: Path) -> str:
    """Jakie dane wrażliwe zawiera plik ('' gdy brak): arkusze – kontakty; dokumenty – PESEL, numer konta.
    Informacja dla inwestora, nie blokada."""
    if p.suffix.lower() in (".xlsx", ".xlsm"):
        try:
            import openpyxl  # noqa: PLC0415
        except ImportError:
            return NIESPRAWDZONE + "brak openpyxl (pip3 install --user openpyxl)"
        wb = openpyxl.load_workbook(p, data_only=True, read_only=True)
        n = sum(1 for ws in wb.worksheets for r in ws.iter_rows(values_only=True)
                for v in r if isinstance(v, str) and KONTAKT.search(v))
        return f"{n} komórek z e-mailem/telefonem" if n else ""
    try:
        t = tekst(p)
    except ImportError:
        return NIESPRAWDZONE + "brak pypdf (pip3 install --user pypdf)"
    if WRAZLIWE_PESEL.search(t):
        return "PESEL"
    if WRAZLIWE_KONTO.search(t):
        return "numer rachunku bankowego"
    return ""


def zbuduj_paczke(ind: dict, dry: bool) -> list:
    """Kopiuje pliki z eksportem do folderu paczki, usuwa nieaktualne, pisze spis. Zwraca ostrzeżenia."""
    ostrz = []
    plan = {}
    for sciezka, w in sorted(ind["pliki"].items()):
        if not w.get("eksport"):
            continue
        n = nazwa_w_paczce(sciezka, w)
        if n in plan:
            ostrz.append(f"Dwa pliki z tą samą nazwą w paczce „{n}”: {plan[n]} i {sciezka} – pominięto drugi")
            continue
        w = ind["pliki"][sciezka]
        if w["rozmiar"] > LIMIT_MB * 1024 * 1024:
            ostrz.append(f"{sciezka}: {w['rozmiar'] // 2**20} MB – powyżej limitu claude.ai ({LIMIT_MB} MB); "
                         "zapisz mniejszą wersję (Podgląd → Eksportuj → Filtr kwarcowy: Zmniejsz rozmiar pliku) "
                         "obok oryginału i oznacz ją do paczki")
            continue
        # Paczka idzie tylko do prywatnego projektu na claude.ai – dane osobowe są tam dozwolone (decyzja inwestora).
        # Kontrola tylko informuje, raz na wersję pliku; do repo dokumenty nie trafiają nigdy (hooki w .githooks/).
        if w.get("kontrola_sha1") != w["sha1"]:
            w["wrazliwe"] = dane_wrazliwe(HUB / sciezka)
            if not w["wrazliwe"].startswith(NIESPRAWDZONE):  # niesprawdzonego nie zapamiętujemy
                w["kontrola_sha1"] = w["sha1"]
                if w["wrazliwe"]:
                    ostrz.append(f"{sciezka}: zawiera {w['wrazliwe']} – dodano do paczki (paczka jest prywatna)")
        plan[n] = sciezka
    if dry:
        return ostrz
    PACZKA.mkdir(exist_ok=True)
    for f in PACZKA.iterdir():
        if f.is_file() and not f.name.startswith(".") and f.name not in plan and f.name != SPIS:
            f.unlink()
    for n, sciezka in plan.items():
        zr, cel = HUB / sciezka, PACZKA / n
        w = ind["pliki"][sciezka]
        if cel.exists() and w.get("w_paczce_sha1") == w["sha1"]:
            continue
        if zr.suffix.lower() == ".doc":
            r = subprocess.run(["textutil", "-convert", "docx", "-output", str(cel), str(zr)], capture_output=True)
            if r.returncode:
                ostrz.append(f"{sciezka}: konwersja .doc → .docx nieudana, skopiowano oryginał")
                shutil.copy2(zr, cel.with_suffix(".doc"))
        else:
            shutil.copy2(zr, cel)
        w["w_paczce_sha1"] = w["sha1"]
    pisz_spis(ind, plan)
    return ostrz


def pisz_spis(ind: dict, plan: dict):
    wiersze = ["# Spis dokumentów budowy", "",
               f"Wygenerowano: {dt.date.today().isoformat()} przez `tools/dokumenty.py`. Tylko aktualne wersje – "
               "starsze i robocze zostają lokalnie. Kolumna „Źródło” to ścieżka w folderze budowy na komputerze.", "",
               "| Plik | Kategoria | Co to jest | Data pliku | Źródło |", "|---|---|---|---|---|"]
    for n, sciezka in sorted(plan.items(), key=lambda x: (ind["pliki"][x[1]].get("kategoria", ""), x[0])):
        w = ind["pliki"][sciezka]
        data = dt.date.fromtimestamp(w["mtime"]).isoformat()
        wiersze.append(f"| {n} | {w.get('kategoria', '')} | {w.get('opis', '')} | {data} | {sciezka} |")
    (PACZKA / SPIS).write_text("\n".join(wiersze) + "\n", encoding="utf-8")


def stan_paczki() -> dict:
    if not PACZKA.exists():
        return {}
    return {f.name: sha1(f) for f in sorted(PACZKA.iterdir()) if f.is_file() and not f.name.startswith(".")}


def do_wgrania() -> dict:
    teraz, bylo = stan_paczki(), wczytaj(WGRANE, {})
    return {"dodaj": [n for n in teraz if n not in bylo],
            "podmien": [n for n in teraz if n in bylo and bylo[n] != teraz[n]],
            "usun": [n for n in bylo if n not in teraz]}


def lista(nazwy, maks=MAKS_LISTA):
    out = [f"    - {n}" for n in nazwy[:maks]]
    if len(nazwy) > maks:
        out.append(f"    … i {len(nazwy) - maks} więcej (`python3 tools/dokumenty.py lista --nowe`)")
    return out


def cmd_sprawdz(a):
    if not HUB.is_dir():
        print(f"[dokumenty] Brak folderu budowy {HUB} – ustaw DOM_HUB.")
        return 0
    ind = wczytaj(INDEKS, {"pliki": {}})
    zd = aktualizuj_indeks(ind)
    ostrz = zbuduj_paczke(ind, a.dry_run)
    if not a.dry_run:
        zapisz(INDEKS, ind)
    wg = do_wgrania()
    eksport = sum(1 for w in ind["pliki"].values() if w.get("eksport"))
    r = [f"[dokumenty] Folder budowy: {HUB} – {len(ind['pliki'])} plików, w paczce dla claude.ai: {eksport}."]
    if zd["nowe"]:
        r.append(f"  Nowe pliki do sklasyfikowania ({len(zd['nowe'])}) – procedura `dokumenty`:")
        r += lista(zd["nowe"])
    else:
        oczek = [s for s, w in ind["pliki"].items() if w["status"] == "nowy"]
        if oczek:
            r.append(f"  Czeka na klasyfikację: {len(oczek)} (procedura `dokumenty`).")
    zm = [s for s in zd["zmienione"] if ind["pliki"].get(s, {}).get("eksport")]
    if zm:
        r.append("  Zmieniona treść plików z paczki (sprawdź, czy to nowa wersja – ściąga, Notion):")
        r += lista(zm)
    for klucz, opis in (("przeniesione", "Przeniesione"), ("usuniete", "Usunięte z dysku"),
                        ("duplikaty", "Duplikaty (pominięte)")):
        if zd[klucz]:
            r.append(f"  {opis}: {len(zd[klucz])}")
    for o in ostrz:
        r.append(f"  ! {o}")
    if any(wg.values()):
        r.append(f"  Do wgrania w projekcie na claude.ai (folder „{PACZKA.name}”):")
        for k, opis in (("dodaj", "dodaj"), ("podmien", "podmień"), ("usun", "usuń")):
            if wg[k]:
                r.append(f"    {opis}: " + ", ".join(wg[k]))
        r.append("  Po wgraniu: `python3 tools/dokumenty.py wgrane`.")
    if a.dry_run:
        r.append("  (dry-run – nic nie zapisano)")
    print("\n".join(r))
    return 0


def cmd_ustaw(a):
    ind = wczytaj(INDEKS, {"pliki": {}})
    sciezka = Path(a.sciezka).expanduser()
    if sciezka.is_absolute():
        sciezka = sciezka.resolve().relative_to(HUB)
    klucz = nfc(sciezka.as_posix())
    if klucz not in ind["pliki"]:
        aktualizuj_indeks(ind)
    w = ind["pliki"].get(klucz)
    if not w:
        print(f"Nie ma w indeksie: {klucz}")
        return 1
    if a.eksport is not None:
        w["eksport"] = a.eksport
    for pole in ("nazwa", "opis", "kategoria"):
        if getattr(a, pole) is not None:
            w[pole] = getattr(a, pole)
    if w.get("eksport") and not w.get("opis"):
        print("Plik w paczce musi mieć --opis (trafia do spisu).")
        return 1
    w["status"] = "sklasyfikowany"
    zapisz(INDEKS, ind)
    print(f"{klucz}: eksport={'tak' if w.get('eksport') else 'nie'}"
          + (f", w paczce jako „{nazwa_w_paczce(klucz, w)}”" if w.get("eksport") else ""))
    return 0


def cmd_lista(a):
    ind = wczytaj(INDEKS, {"pliki": {}})
    for s, w in sorted(ind["pliki"].items()):
        if a.nowe and w["status"] != "nowy":
            continue
        znak = "E" if w.get("eksport") else ("?" if w["status"] == "nowy" else "-")
        print(f"{znak} {s}" + (f"  →  {nazwa_w_paczce(s, w)}" if w.get("eksport") else "")
              + (f"  [{w.get('kategoria')}] {w.get('opis', '')}" if w.get("kategoria") else ""))
    return 0


def cmd_wgrane(_a):
    zapisz(WGRANE, stan_paczki())
    print(f"Zapisano stan paczki jako wgrany ({len(stan_paczki())} plików).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    u = sub.add_parser("ustaw")
    u.add_argument("sciezka")
    g = u.add_mutually_exclusive_group()
    g.add_argument("--eksport", dest="eksport", action="store_true", default=None)
    g.add_argument("--bez-eksportu", dest="eksport", action="store_false")
    u.add_argument("--nazwa")
    u.add_argument("--opis")
    u.add_argument("--kategoria")
    lp = sub.add_parser("lista")
    lp.add_argument("--nowe", action="store_true")
    sub.add_parser("wgrane")
    a = ap.parse_args()
    return {"ustaw": cmd_ustaw, "lista": cmd_lista, "wgrane": cmd_wgrane}.get(a.cmd, cmd_sprawdz)(a)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001 – hook na starcie sesji nie może blokować pracy
        print(f"[dokumenty] Błąd skryptu: {e}")
        sys.exit(0)
