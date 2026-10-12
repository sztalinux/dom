---
name: rozwoj-harnessu
description: Zgłaszanie i wdrażanie zmian w harnessie budowy (procedury, zasady, szablony w repozytorium harnessu) przez skrzynkę „Zmiany do harnessu” w Notion oraz analiza pomysłów na rozwój setupu (baza „Pomysły na rozwój”). Używaj, gdy użytkownik poprawia sposób pracy asystenta („zawsze rób X”, „nie rób Y”, „źle to zapisałeś”, „zapamiętaj na przyszłość”), chce nową procedurę, zmienia strukturę Notion/Excela, mówi „wdróż zmiany”, „zaktualizuj harness”, „mam pomysł na…”, „przeanalizuj pomysły”, „zrób POM-3”, albo pyta o przeniesienie harnessu do innego AI.
---

# Rozwój harnessu

Źródło harnessu: **publiczne** repozytorium GitHub `sztalinux/dom` (marketplace z pluginem `dom-budowa`). Claude na koncie (czat, telefon, Cowork)
pobiera z niego plugin – po nowej wersji inwestor odświeża go ręcznie (albo synchronizacja, jeśli organizacja pozwala).
Konfiguracja projektu „Dom” na claude.ai (instrukcje, wiedza): `references/claude-ai-projekt.md`. Zmiany trafiają do repo dwiema drogami:

| Gdzie jesteś | Co robisz |
|---|---|
| Czat, telefon, Cowork, inne AI (bez repo) | **Zgłoszenie** do skrzynki w Notion – sekcja A |
| Claude Code w folderze repo | **Wdrożenie** skrzynki do plików + push – sekcja B (robisz to też na starcie każdej sesji) |
| Większy pomysł na rozwój (nowa funkcja, automatyzacja, zdjęcia, Excel) | **Pomysł** do bazy „Pomysły na rozwój” → analiza → wdrożenie na polecenie – sekcja C |

Skrzynka = konkretna reguła, wchodzi od razu. Pomysł = coś do przemyślenia; nic nie wchodzi samo, decyduje inwestor.

Skrzynka: Notion → „Zmiany do harnessu”, `collection://e217448a-60ec-4af6-8584-8f368315109c`.
Pola: Zmiana (tytuł), Status (Do wdrożenia / Wdrożone / Odrzucone), Procedura, Rodzaj (Nowa zasada, Poprawka,
Nowa procedura, Zmiana struktury Notion / Excela, Usunięcie), Treść do wdrożenia, Dlaczego, Wdrożono w wersji,
Data wdrożenia, ID (HZ-n).

## Kiedy proponować zmianę (pętla uczenia)

Gdy inwestor w rozmowie:
- poprawia wynik w sposób, który powtórzy się w przyszłości (format, pole, zasada),
- dwa razy prosi o to samo dodatkowe działanie,
- zmienia strukturę danych (nowe pole w Notion, nowa kolumna w Excelu, nowy etap),
- mówi wprost „zapamiętaj to na przyszłość”,

zaproponuj na końcu odpowiedzi jedną linię: „Dopisać to do harnessu (procedura `<nazwa>`)?”.
Bez zgody nic nie zapisuj. Jednorazowe prośby to nie zmiany harnessu.

## A. Zgłoszenie (z dowolnego miejsca)

1. Sformułuj zmianę tak, żeby dało się ją wdrożyć bez tej rozmowy:
   - **Zmiana:** krótki tytuł („Oferta: zawsze pytaj o fasety”),
   - **Procedura** i **Rodzaj**,
   - **Treść do wdrożenia:** gotowy tekst reguły w trybie rozkazującym, tak jak ma trafić do procedury,
   - **Dlaczego:** 1–2 zdania kontekstu z rozmowy (data).
2. Sprawdź w skrzynce, czy podobny wpis już nie czeka – jeśli tak, uzupełnij go zamiast dublować.
3. Zapisz jednym wywołaniem, Status „Do wdrożenia”. Od tej chwili zmiana obowiązuje wszędzie
   (procedura `budowa`, sekcja „Na starcie”).
4. Potwierdź jedną linią: „Zapisane jako HZ-n – obowiązuje od teraz, wejdzie do repo przy następnej sesji Claude Code”.

## B. Wdrożenie (tylko Claude Code w folderze repo)

1. `git pull`. Pobierz wpisy „Do wdrożenia” (najstarsze pierwsze).
2. Dla każdego wpisu: znajdź właściwe miejsce (`plugins/dom-budowa/skills/<procedura>/SKILL.md` lub `references/`),
   wprowadź zmianę zgodnie z `references/pisanie-procedur.md`. Nie kopiuj treści mechanicznie – wpasuj w strukturę
   procedury, usuń sprzeczne stare zapisy. Wpis niejasny lub sprzeczny z inną procedurą → zapytaj inwestora przed wdrożeniem.
3. Podbij wersję w `plugins/dom-budowa/.claude-plugin/plugin.json` i `gemini-extension.json` (muszą być równe):
   PATCH = poprawka treści, MINOR = nowa procedura/pole, MAJOR = zmiana struktury danych.
   **Bez podbicia wersji telefon i Cowork nie dostaną aktualizacji.**
4. Dopisz wpis w `CHANGELOG.md` (wersja, data, lista HZ-n z jednym zdaniem każdy).
5. `python3 tools/build.py` – musi przejść walidację, w tym kontrolę prywatności (wzorce + lista słów zakazanych
   `.dom/zakazane-w-repo.txt` w folderze budowy). Hooki w `.githooks/` powtarzają ją przy commicie (pliki, autor,
   wiadomość) i przed pushem (każdy wysyłany commit). Zablokowany hook = popraw dane, nigdy `--no-verify`.
   Przejrzyj `git diff`: zero nazwisk, firm, adresów, działek, telefonów, e-maili, kwot i treści notatek.
   Jeśli wpis ze skrzynki zawiera takie dane – wdroż regułę w wersji ogólnej („Firma A”), a konkret zostaw w Notion.
6. `git add <zmienione pliki> && git commit -m "Harness <wersja>: HZ-… <skrót>" && git push` – tylko pliki z tej sesji; obce zmiany zgłoś.
7. W Notion oznacz wdrożone wpisy jednym przebiegiem: Status „Wdrożone”, Wdrożono w wersji, Data wdrożenia.
   Zaktualizuj linię „Wersja” na stronie „Asystent AI – harness budowy” (ID w `budowa/references/zrodla.md`; strona jest
   tylko ramką nad skrzynką – opis procedur jest w README repo); nowa procedura = nowa opcja w polu „Procedura” skrzynki.
   Zmiana struktury Notion (baza, widok, pole) → zaktualizuj `budowa/references/notion-mapa.md` (trafia do przewodnika w Notion przy następnym `tools/dokumenty.py` – zsynchronizuj go, `dokumenty`, sekcja C).
8. Podsumuj w 2–4 liniach: wersja, co weszło, co odrzucone/odłożone i dlaczego. Dopisz przypomnienie:
   „odśwież plugin na claude.ai (`references/claude-ai-projekt.md`, sekcja „Aktualizacja pluginu”)”; jeśli zmienił się tekst instrukcji
   w `references/claude-ai-projekt.md` – także „wklej na nowo `dist/claude-ai-projekt/instrukcje.md` w projekt »Dom«”.

Zmiany, o które inwestor prosi bezpośrednio w Claude Code, wdrażasz od razu tymi samymi krokami 2–8 (bez skrzynki).

## C. Pomysły na rozwój

Baza: Notion → DOM → „💡 Pomysły na rozwój”, `collection://fdee4f05-8f43-4be4-a0d5-2b88642fa6d3` (widok „💡 Tablica”).
Pola: Pomysł (tytuł), Status (Nowy / Pytania do mnie / Przeanalizowany / Do zrobienia / Zrobione / Odłożone / Odrzucone;
**pusty = Nowy**), Obszar, Nakład (S/M/L), Wymaga ode mnie, Przeanalizowano, Zrobiono w wersji, ID (POM-n).
Treść strony: pomysł inwestora (nie zmieniaj), pod nim sekcja „Analiza” pisana przez asystenta.

**Zapis pomysłu** („mam pomysł…”, wpis w Inboxie „pomysł: …” o asystencie, Notion, Excelu, plikach, automatyzacji):
sprawdź, czy podobny już jest (uzupełnij zamiast dublować); nowy wiersz – tytuł, Obszar, w treści „## Pomysł (kto, data)”
i słowa inwestora. Status pusty/Nowy. Poprawka sposobu pracy (jedna reguła) to nie pomysł – sekcja A.

**Analiza** (wpisy Nowy lub pusty; w trybie wieczornym `inbox` automatycznie, inaczej na prośbę i na starcie Claude Code):
1. Przeczytaj pomysł i przejrzyj, co już jest: procedury (`budowa` – mapa procedur, odpowiednie `SKILL.md`), mapa Notion
   (`budowa/references/notion-mapa.md`), inne pomysły (zależności, duplikaty).
2. Niejasne, co inwestor chce → dopisz „### ❓ Pytania (data)” z 1–3 pytaniami i propozycją interpretacji, Status
   „Pytania do mnie”. Odpowiedź inwestora pod pytaniami → przy następnym przebiegu analizuj dalej.
3. Jasne → dopisz pod pomysłem sekcję (nie nadpisuj wcześniejszych):
   ```
   ## Analiza (asystent, data)
   **Co rozumiem:** 1–2 zdania.
   **Co już jest:** procedury / bazy / pola, które to częściowo robią; czego brakuje.
   **Co trzeba zrobić:** Harness (pliki procedur) · Notion (bazy, pola, widoki) · Excel · narzędzia w repo · Ty (decyzje,
     aplikacje, konta) – lista numerowana, kolejność wdrożenia dla Claude Code.
   **Ograniczenia:** czego się nie da / co wymaga zgody (np. connector do nowej usługi → najpierw zgłoszenie IT
     w organizacji inwestora; nie proponuj obejść), koszty usług, prywatność (repo publiczne).
   **Nakład:** S (jedna sesja) / M (kilka) / L (projekt). **Zależności:** POM-n.
   **Do decyzji przed startem:** … **Rekomendacja:** zrobić teraz / przed <etapem> / odłożyć – dlaczego.
   ```
   Ustaw: Status „Przeanalizowany”, Nakład, Obszar, „Wymaga ode mnie” (krótko), Przeanalizowano = data.
4. Analiza to plan, nie wdrożenie: nie zmieniaj procedur, baz ani plików. Bez dostępu do repo (claude.ai) opieraj się
   na skillach z pluginu – Claude Code i tak sprawdzi pliki przed wdrożeniem.

**Wdrożenie** – tylko gdy inwestor powie w Claude Code „zrób POM-n” (albo ustawi „Do zrobienia” i poprosi o to):
przeczytaj stronę pomysłu z analizą, potwierdź decyzje z „Do decyzji przed startem”, potem kroki B.2–B.8. Na końcu Status
„Zrobione”, „Zrobiono w wersji”, w treści linia „Wdrożone w <wersja> (data): co weszło, co pominięto”.

## Nowa procedura – minimum

- Katalog `plugins/dom-budowa/skills/<nazwa-kebab-case>/SKILL.md` z frontmatter `name` (= nazwa katalogu)
  i `description` (co robi + kiedy używać + typowe frazy, < 1024 znaki).
- Wpis w tabeli procedur w `AGENTS.md` i w „Mapie procedur” w `skills/budowa/SKILL.md`; nowa opcja w polu
  „Procedura” skrzynki w Notion.
- Szczegóły, schematy, szablony → `references/`.

## Przeniesienie do innego dostawcy

Opis adapterów (Claude, Gemini CLI, Gemini w przeglądarce, Codex): `references/dostawcy.md`.
