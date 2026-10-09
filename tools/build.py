#!/usr/bin/env python3
"""Walidacja i budowanie paczek harnessu dom-budowa.

    python3 tools/build.py                       # walidacja + dist/
    python3 tools/build.py --tylko-walidacja     # tylko walidacja
    python3 tools/build.py --kopiuj-dowiazania   # .agents/skills i .claude/skills jako kopie (Windows)

Wynik w dist/:
    dom-budowa.plugin         – plugin dla Claude (Cowork / claude.ai)
    gemini-gem/instrukcje.md  – instrukcje do wklejenia w Gem
    gemini-gem/wiedza/*.md    – po jednym pliku na procedurę (pliki wiedzy Gema)
"""
import argparse
import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "dom-budowa"
SKILLS = PLUGIN / "skills"
DIST = ROOT / "dist"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HUB = Path(os.environ.get("DOM_HUB", ROOT.parent.parent)).expanduser()
ZAKAZANE = HUB / ".dom" / "zakazane-w-repo.txt"  # poza repo: sama lista byłaby wyciekiem
TEKSTOWE = {".md", ".json", ".py", ".txt", ".toml", ".yml", ".yaml", ""}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def waliduj() -> list:
    bledy = []
    # manifesty i wersje
    try:
        plugin = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        gem = json.loads((ROOT / "gemini-extension.json").read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"Manifest JSON nieczytelny: {e}"]
    wpisy = [p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
    if not wpisy:
        bledy.append("marketplace.json: brak wpisu dla pluginu " + str(plugin.get("name")))
    elif not (ROOT / wpisy[0].get("source", "")).joinpath(".claude-plugin/plugin.json").exists():
        bledy.append("marketplace.json: source nie wskazuje katalogu pluginu")
    if not NAME_RE.match(plugin.get("name", "")):
        bledy.append("plugin.json: name nie jest kebab-case")
    if plugin.get("version") != gem.get("version"):
        bledy.append(f"Różne wersje: plugin.json {plugin.get('version')} vs gemini-extension.json {gem.get('version')}")
    if not re.match(r"^\d+\.\d+\.\d+$", plugin.get("version", "")):
        bledy.append("plugin.json: version nie jest semver X.Y.Z")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
    if f"[{plugin.get('version')}]" not in changelog:
        bledy.append(f"CHANGELOG.md: brak wpisu dla wersji [{plugin.get('version')}]")

    # procedury
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    router = (SKILLS / "budowa/SKILL.md").read_text(encoding="utf-8")
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        sk = d / "SKILL.md"
        if not sk.exists():
            bledy.append(f"{d.name}: brak SKILL.md")
            continue
        fm = frontmatter(sk)
        if fm.get("name") != d.name:
            bledy.append(f"{d.name}: name we frontmatter ({fm.get('name')}) ≠ nazwa katalogu")
        if not NAME_RE.match(d.name):
            bledy.append(f"{d.name}: nazwa katalogu nie jest kebab-case")
        desc = fm.get("description", "")
        if not desc:
            bledy.append(f"{d.name}: brak description")
        elif len(desc) > 1024:
            bledy.append(f"{d.name}: description ma {len(desc)} znaków (max 1024)")
        if d.name != "budowa":
            if f"plugins/dom-budowa/skills/{d.name}/SKILL.md" not in agents:
                bledy.append(f"{d.name}: brak w tabeli procedur w AGENTS.md")
            if f"`{d.name}`" not in router:
                bledy.append(f"{d.name}: brak w mapie procedur w skills/budowa/SKILL.md")
        linie = len(sk.read_text(encoding="utf-8").splitlines())
        if linie > 200:
            bledy.append(f"{d.name}: SKILL.md ma {linie} linii – przenieś szczegóły do references/")
        # odwołania do references/ muszą istnieć
        for ref in re.findall(r"`(references/[\w\-./]+)`", sk.read_text(encoding="utf-8")):
            if not (d / ref).exists():
                bledy.append(f"{d.name}: odwołanie do nieistniejącego {ref}")
    bledy += kontrola_prywatnosci()
    return bledy


# --- kontrola prywatności (repo jest publiczne) -------------------------------------------
POMIJANE_KATALOGI = {".git", "dist", "dane", "__pycache__", "node_modules", ".agents", ".idea"}
WZORCE = [
    (re.compile(r"(?<![\w-])(\+48[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{3}(?![\w-])"), "numer telefonu"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", re.I), "adres e-mail"),
    (re.compile(r"\b(dz\.?|działk\w*|nr ew\w*)\s*(nr\s*)?\d+/\d+", re.I), "numer działki"),
    (re.compile(r"\b\d{2}-\d{3}\b"), "kod pocztowy"),
    (re.compile(r"\b(ul\.|ulica)\s+[A-ZĄĆĘŁŃÓŚŹŻ]", re.U), "adres"),
    (re.compile(r"PESEL\D{0,5}\d{11}", re.I), "PESEL"),
]
DOZWOLONE = ["noreply@anthropic.com"]  # fragmenty dozwolone mimo dopasowania


def kontrola_prywatnosci() -> list:
    """Dane osobowe/projektowe w plikach repo: wzorce + lista słów zakazanych trzymana POZA repo
    (`.dom/zakazane-w-repo.txt` w folderze budowy; sama lista w repo byłaby wyciekiem)."""
    bledy, zakazane = [], []
    for lista in (ZAKAZANE, ROOT / "dane" / "prywatne.txt"):
        if lista.exists():
            zakazane += [w.strip().lower() for w in lista.read_text(encoding="utf-8").splitlines()
                         if w.strip() and not w.strip().startswith("#")]
    for f in sorted(ROOT.rglob("*")):
        rel = f.relative_to(ROOT)
        if not f.is_file() or set(rel.parts) & POMIJANE_KATALOGI or rel.as_posix().startswith(".claude/skills"):
            continue
        if f.suffix.lower() in {".xlsx", ".xls", ".pdf", ".doc", ".docx", ".jpg", ".jpeg", ".png", ".heic", ".zip"}:
            bledy.append(f"{rel}: plik z danymi w repo – dokumenty trzymaj w folderze budowy")
            continue
        if f.suffix.lower() not in TEKSTOWE:
            continue
        try:
            tekst = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for wzor in DOZWOLONE:
            tekst = tekst.replace(wzor, "")
        for nr, linia in enumerate(tekst.splitlines(), 1):
            for rx, opis in WZORCE:
                if rx.search(linia):
                    bledy.append(f"{rel}:{nr}: wygląda na {opis} – repo jest publiczne")
            niskie = linia.lower()
            if any(w in niskie for w in zakazane):
                bledy.append(f"{rel}:{nr}: słowo z listy zakazanych – repo jest publiczne, usuń lub uogólnij")
    if not zakazane:
        print(f"UWAGA: brak listy {ZAKAZANE} – sprawdzam tylko wzorce (telefon, e-mail, działka, kod, adres, PESEL)")
    return bledy


def zbuduj_plugin(wersja: str) -> Path:
    out = DIST / "dom-budowa.plugin"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(PLUGIN.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(PLUGIN).as_posix())
    return out


def zbuduj_gem(wersja: str) -> Path:
    gem = DIST / "gemini-gem"
    if gem.exists():
        shutil.rmtree(gem)
    (gem / "wiedza").mkdir(parents=True)
    instr = [f"<!-- dom-budowa {wersja} – wygenerowane przez tools/build.py, nie edytuj ręcznie -->",
             (ROOT / "AGENTS.md").read_text(encoding="utf-8"),
             "\n## Jak korzystać z plików wiedzy\n",
             "Każda procedura jest w osobnym pliku wiedzy `procedura-<nazwa>.md`. Gdy zadanie pasuje do procedury, "
             "przeczytaj ten plik w całości i wykonaj kroki. Ścieżki `skills/<nazwa>/...` w tekście oznaczają "
             "odpowiedni plik wiedzy. Narzędzia Notion mogą być niedostępne – wtedy przygotuj wpisy do wklejenia."]
    (gem / "instrukcje.md").write_text("\n".join(instr), encoding="utf-8")
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        czesci = [f"<!-- dom-budowa {wersja} / skills/{d.name} -->", (d / "SKILL.md").read_text(encoding="utf-8")]
        for ref in sorted((d / "references").glob("*.md")) if (d / "references").exists() else []:
            czesci.append(f"\n\n---\n# Plik: skills/{d.name}/references/{ref.name}\n")
            czesci.append(ref.read_text(encoding="utf-8"))
        (gem / "wiedza" / f"procedura-{d.name}.md").write_text("\n".join(czesci), encoding="utf-8")
    return gem


def kopiuj_dowiazania():
    for link in (ROOT / ".agents/skills", ROOT / ".claude/skills"):
        if link.is_symlink() or link.exists():
            if link.is_symlink() or link.is_file():
                link.unlink()
            else:
                shutil.rmtree(link)
        link.parent.mkdir(exist_ok=True)
        shutil.copytree(SKILLS, link)
        print(f"skopiowano skills/ → {link.relative_to(ROOT)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tylko-walidacja", action="store_true")
    ap.add_argument("--kopiuj-dowiazania", action="store_true")
    a = ap.parse_args()
    if a.kopiuj_dowiazania:
        kopiuj_dowiazania()
    bledy = waliduj()
    if bledy:
        print("WALIDACJA – BŁĘDY:")
        for b in bledy:
            print("  ✗", b)
        return 1
    n = len([p for p in SKILLS.iterdir() if p.is_dir()])
    print(f"Walidacja OK ({n} procedur).")
    if a.tylko_walidacja:
        return 0
    wersja = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
    DIST.mkdir(exist_ok=True)
    print("Zbudowano:", zbuduj_plugin(wersja).relative_to(ROOT))
    print("Zbudowano:", zbuduj_gem(wersja).relative_to(ROOT), "(instrukcje.md + wiedza/)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
