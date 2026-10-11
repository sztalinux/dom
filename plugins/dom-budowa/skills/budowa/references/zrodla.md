# Źródła prawdy – gdzie co leży

Zasada podziału: **harness = JAK pracujemy** (procedury, formaty, zasady) – to repozytorium.
**Dane = CO wiemy** (fakty, decyzje, liczby, wiedza) – Notion i Excel. Nie kopiuj danych do harnessu –
**repozytorium jest publiczne**.

## Mapa

| Co | Gdzie | Kto edytuje |
|---|---|---|
| Procedury, zasady, szablony | publiczne repo GitHub `sztalinux/dom` → plugin `dom-budowa` na koncie Claude (aktualizacja: ręczne odświeżenie lub synchronizacja – `rozwoj-harnessu/references/claude-ai-projekt.md`) | Claude Code (`rozwoj-harnessu`, sekcja B) |
| Zgłoszone zmiany harnessu (obowiązują od razu) | Notion → Asystent AI → Zmiany do harnessu | dowolny asystent (`rozwoj-harnessu`, sekcja A) |
| Liczby: kosztorys, wydatki, oferty, wykonawcy (z kontaktami) | Excel „Kosztorys_stan_zero.xlsx” – prowadzi inwestor | Inwestor; agent tylko na prośbę (`koszty`): w Claude Code plik z folderu budowy, na claude.ai plik załączony w rozmowie (w wiedzy projektu go nie ma) |
| Notatki, decyzje, pytania, ryzyka naszej budowy | Notion → DOM → Notatnik budowy | Inwestor + agent (`notatka`) |
| Zadania z terminem | Notion → DOM → TASKS (2) | Inwestor + agent (`notatka`) |
| Porównanie wykonawców (jakość, zakres, knock-out) | Notion → Wybór wykonawcy – stan zero → baza „Porównanie wykonawców” | agent (`oferta`) |
| Wiedza: tematy, informacje, rozmowy i filmy | Notion → DOM → Baza wiedzy (Tematy, Informacje, Rozmowy i źródła) | agent (`wiedza`), inwestor przegląda |
| Sprzeczności i dylematy (ADR) | Notion → Baza wiedzy → Rejestr sprzeczności | agent zgłasza, **decyduje inwestor** |
| Przeglądy tygodniowe | Notion → DOM → Przeglądy tygodniowe | agent (`przeglad-tygodnia`) |
| Dziennik inwestora (dni na budowie, dostawy, usterki, godziny własne) | Notion → DOM → Dziennik budowy (schemat: `dziennik/references/notion-dziennik.md`); zdjęcia w folderze budowy `Zdjęcia/` | inwestor + agent (`dziennik`) |
| Bramki i odbiory etapów | Notion → „Etapy budowy – przewodnik”, „Stan zero – punkty bez odwrotu”; protokoły w folderze budowy | agent przygotowuje (`etap`), odbiera inwestor z kierownikiem |
| Analizy dokumentów | Notion (strona pod DOM) lub dokument w projekcie Claude | agent (`analiza-techniczna`) |
| Dokumenty: projekty, opinie, oferty, umowy (PDF, Excel) | folder budowy na komputerze inwestora; w wiedzy projektu „Dom” na claude.ai tylko przewodnik `00_SPIS.md` (co jest w którym dokumencie) i ściąga; pełne dokumenty na prośbę | inwestor wrzuca, agent klasyfikuje (`dokumenty`); oryginały tylko odczyt |
| Ściąga projektu (najważniejsze liczby i decyzje) | `Ściąga projektu.md` w folderze budowy (w paczce jako `01_Sciaga-projektu.md`) + Notion „Dane projektu (ściąga)” | agent po nowym dokumencie (`dokumenty`, `analiza-techniczna`) |

## Notion – identyfikatory (konto prywatne inwestora)

| Element | ID |
|---|---|
| Strona DOM (pulpit) | `24af5982-09e7-806b-821a-e157ff33be42` |
| Notatnik budowy (data source) | `collection://7423414a-707b-415f-8751-c6ab7ebb6753` |
| TASKS (2) (data source) | `collection://2a9f5982-09e7-81be-91e8-000b0e10a05e` |
| Wybór wykonawcy – stan zero (strona) | `3f3f5982-09e7-81e8-b361-c7bee2e3847d` |
| Porównanie wykonawców – stan zero (data source) | `collection://f7ca5f38-8fc3-46e7-8345-8a32cc8b5215` |
| Etapy budowy – przewodnik (strona) | `3f3f5982-09e7-8161-b30e-fdcf2284554b` |
| Baza wiedzy (strona) | `3f4f5982-09e7-8193-a68e-fd35c9265012` |
| Tematy / Informacje / Rozmowy i źródła / Rejestr sprzeczności | `wiedza/references/notion-wiedza.md` |
| Przeglądy tygodniowe (strona) | `3f4f5982-09e7-8144-af5e-f9521a52ea9d` |
| Asystent AI – harness budowy (przewodnik) | `3f4f5982-09e7-81f5-b7f9-d6cf5d79bb34` |
| Zmiany do harnessu (data source) | `collection://e217448a-60ec-4af6-8584-8f368315109c` |
| Dziennik budowy (data source) | `collection://cc113d57-3eaa-4f52-80f6-e4b39a4b4c92` |

Schematy baz budowy (pola i dozwolone wartości): `skills/notatka/references/notion-schematy.md`.
Jeśli ID przestanie działać, wyszukaj stronę po nazwie i zaktualizuj tabelę.
