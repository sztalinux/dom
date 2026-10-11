---
name: rozwoj-harnessu
description: Zgłaszanie i wdrażanie zmian w harnessie budowy (procedury, zasady, szablony w repozytorium harnessu) przez skrzynkę „Zmiany do harnessu” w Notion. Używaj, gdy użytkownik poprawia sposób pracy asystenta („zawsze rób X”, „nie rób Y”, „źle to zapisałeś”, „zapamiętaj na przyszłość”), chce nową procedurę, zmienia strukturę Notion/Excela, mówi „wdróż zmiany”, „zaktualizuj harness”, albo pyta o przeniesienie harnessu do innego AI.
---

# Rozwój harnessu

Źródło harnessu: **publiczne** repozytorium GitHub `sztalinux/dom` (marketplace z pluginem `dom-budowa`). Claude na koncie (czat, telefon, Cowork)
pobiera z niego plugin – po nowej wersji inwestor odświeża go ręcznie (albo synchronizacja, jeśli organizacja pozwala).
Konfiguracja projektu „Dom” na claude.ai (instrukcje, wiedza): `references/claude-ai-projekt.md`. Zmiany trafiają do repo dwiema drogami:

| Gdzie jesteś | Co robisz |
|---|---|
| Czat, telefon, Cowork, inne AI (bez repo) | **Zgłoszenie** do skrzynki w Notion – sekcja A |
| Claude Code w folderze repo | **Wdrożenie** skrzynki do plików + push – sekcja B (robisz to też na starcie każdej sesji) |

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
   Przy nowej procedurze lub zmianie zasad zaktualizuj też stronę „Asystent AI – harness budowy” (ID w `budowa/references/zrodla.md`):
   linia „Wersja” w ramce i tabela procedur – jednym wywołaniem; nowa procedura = nowa opcja w polu „Procedura” skrzynki.
8. Podsumuj w 2–4 liniach: wersja, co weszło, co odrzucone/odłożone i dlaczego. Dopisz przypomnienie:
   „odśwież plugin na claude.ai (`references/claude-ai-projekt.md`, sekcja „Aktualizacja pluginu”)”; jeśli zmienił się tekst instrukcji
   w `references/claude-ai-projekt.md` – także „wklej na nowo `dist/claude-ai-projekt/instrukcje.md` w projekt »Dom«”.

Zmiany, o które inwestor prosi bezpośrednio w Claude Code, wdrażasz od razu tymi samymi krokami 2–8 (bez skrzynki).

## Nowa procedura – minimum

- Katalog `plugins/dom-budowa/skills/<nazwa-kebab-case>/SKILL.md` z frontmatter `name` (= nazwa katalogu)
  i `description` (co robi + kiedy używać + typowe frazy, < 1024 znaki).
- Wpis w tabeli procedur w `AGENTS.md` i w „Mapie procedur” w `skills/budowa/SKILL.md`; nowa opcja w polu
  „Procedura” skrzynki w Notion.
- Szczegóły, schematy, szablony → `references/`.

## Przeniesienie do innego dostawcy

Opis adapterów (Claude, Gemini CLI, Gemini w przeglądarce, Codex): `references/dostawcy.md`.
