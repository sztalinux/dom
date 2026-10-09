# Changelog

Format: [wersja] – data – co i dlaczego. Wersjonowanie semver:
PATCH = poprawka treści, MINOR = nowa procedura/pole, MAJOR = zmiana struktury danych.

## [0.4.5] – 2026-10-10

- Zasada prywatności doprecyzowana (decyzja inwestora): imię i nazwisko inwestora w historii gita dozwolone;
  dane innych osób i e-maile – nigdy. Audyt całej historii publicznego repo (wszystkie obiekty): czysto.
- `CLAUDE.md`: nie przepisuj opublikowanej historii (force push zostawia stare commity po SHA), chyba że wyciekły
  dane – wtedy zatrzymaj się i zapytaj inwestora.

## [0.4.4] – 2026-10-09

- `dokumenty` / `tools/dokumenty.py`: dane osobowe w paczce dla claude.ai są dozwolone (paczka trafia tylko do prywatnego
  projektu – decyzja inwestora); kontrola PESEL/konta/kontaktów tylko informuje, raz na wersję pliku.
  Repo publiczne – bez zmian: hooki blokują dane osobowe.

## [0.4.3] – 2026-10-09

Pełna kontrola prywatności przed GitHubem (prośba inwestora).
- `.githooks/pre-commit`: oprócz plików sprawdza autora i commitera (imię z listy zakazanych, e-mail inny niż noreply).
- `.githooks/commit-msg`: wiadomość commita bez danych osobowych/projektowych.
- `.githooks/pre-push`: ostatnia kontrola każdego wysyłanego commita – metadane, wiadomość, treść zmienionych plików,
  także commitów zrobionych z `--no-verify`. Logika w `tools/build.py` (`--tozsamosc`, `--wiadomosc`, `--commity`).
- `rozwoj-harnessu`, `CLAUDE.md`, README: hooki i anonimowy autor commitów.

## [0.4.2] – 2026-10-09

- `tools/dokumenty.py`: kontrola danych wrażliwych nie przepuszcza plików, gdy brak `pypdf`/`openpyxl`
  (blokada „nie sprawdzono”, bez zapamiętania wyniku); `dokumenty`: skany oceniaj samodzielnie (skrypt czyta tylko tekst).

## [0.4.1] – 2026-10-09

Porządek w Notion przy rosnącym projekcie (prośba inwestora z Claude Code).
- `budowa`, zasada 10: na pierwszym planie bieżący etap (sekcja „Do zamknięcia przed …” na stronie DOM), sprawy
  krytyczne, terminy 14 dni i decyzje; zamknięte i odległe – drugi plan (licznik). Każdy wpis z Etapem i Priorytetem,
  aktualizacja zamiast dublowania, porządek statusami (bez usuwania), przestawienie strony DOM przy zmianie etapu.
- `przeglad-tygodnia`: nowa sekcja „Porządki” (duplikaty, braki pól, sprawy bez ruchu, stara „Nowa” wiedza,
  sprawy zakończonego etapu) – propozycje do zatwierdzenia jednym „tak”; wynik z „Na później” i „Porządki”.

## [0.4.0] – 2026-10-09

Folder budowy jako centrum dokumentów + repo publiczne bez danych osobowych
(scalone z wersją 0.4.0 przygotowaną na claude.ai).
- Nowe publiczne repo `sztalinux/dom` z czystą historią (claude.ai dodaje publiczny marketplace bez konektora GitHub).
- Nowa procedura `dokumenty`: pliki od projektantów i wykonawców trafiają do folderu budowy na komputerze;
  agent je klasyfikuje (kategoria, wersja, czy przydatne agentom), a `tools/dokumenty.py` buduje paczkę
  `_Do claude.ai/` z aktualnymi wersjami i spisem `00_SPIS.md` – do wgrania w wiedzy projektu „Dom” na claude.ai.
- Hook SessionStart w `.claude/settings.json`: przy każdym starcie Claude Code skan folderu budowy, przebudowa
  paczki i raport (nowe pliki, zmiany, co wgrać). Skrypt blokuje w paczce pliki z PESEL, numerem konta
  i kontaktami w arkuszach oraz pliki powyżej limitu claude.ai.
- Repo publiczne: usunięte dane osobowe (imię inwestora → „inwestor”, lokalizacja, numery działek, zespół);
  ściąga projektu przeniesiona do folderu budowy i paczki, `budowa/references/projekt.md` to teraz odnośnik
  (Notion / folder budowy / projekt na claude.ai); przykłady w `etapy`, `wiedza`, `notatka` uogólnione.
- `tools/build.py`: kontrola prywatności we wszystkich plikach tekstowych (telefon, e-mail, działka, kod pocztowy,
  adres, PESEL, pliki dokumentów w repo) + lista słów zakazanych poza repo (`.dom/zakazane-w-repo.txt` w folderze budowy).
- Hook `.githooks/pre-commit` blokuje commit z danymi (`git config core.hooksPath .githooks`).
- Zasada 9 w `budowa`, `AGENTS.md`, `CLAUDE.md`, `pisanie-procedur.md`: harness publiczny, przykłady na zmyślonych danych;
  `rozwoj-harnessu`: dane z wpisów skrzynki uogólniaj („Firma A”), konkret zostaje w Notion.
- `koszty`, `zrodla.md`, `dostawcy.md`, README: Excel i dokumenty w folderze budowy zamiast `dane/` w repo;
  nazwa repo `sztalinux/dom`.
- `.claude/settings.local.json` (lokalnie): wyłączona synchronizacja pluginów z claude.ai w folderze repo.

## [0.3.0] – 2026-10-09

Repo jako marketplace + skrzynka zmian w Notion.
- Repo = prywatny marketplace (`.claude-plugin/marketplace.json`), plugin w `plugins/dom-budowa/`. claude.ai (czat, telefon,
  Cowork) pobiera go z GitHuba z automatyczną synchronizacją – bez ręcznego wgrywania.
- Skrzynka „Zmiany do harnessu” w Notion: zgłoszenia z dowolnego miejsca obowiązują od razu (`budowa`, „Na starcie”),
  Claude Code wdraża je do repo na starcie każdej sesji (`CLAUDE.md`, `rozwoj-harnessu` sekcja B) i robi push.
- `.claude/settings.json`: zezwolenia na git i build; plugin z konta wyłączony w folderze repo (bez dublowania skilli).
- `koszty`: w Claude Code Excel z lokalnego katalogu poza gitem, w czacie – plik załączony.
- `przeglad-tygodnia`: przypomina o zmianach czekających na wdrożenie.

## [0.2.0] – 2026-10-09

Wiedza z filmów + Excel jako źródło prawdy.
- Nowa procedura `wiedza`: transkrypcje filmów/artykułów → Notion (Źródła, Baza wiedzy, strony tematyczne);
  klasyfikacja nowe / potwierdzenie / uzupełnienie / sprzeczność; ocena wiarygodności i konfliktu interesów;
  „Dotyczy nas” z przekazaniem działań do Notatnika; Rejestr sprzeczności jak ADR – rozstrzyga tylko inwestor.
- Nowa procedura `przeglad-tygodnia` (+ zaplanowane zadanie w poniedziałki).
- `budowa`, zasada 6: zapisy do Notion wsadowo (jak najmniej zatwierdzeń), ale nigdy kosztem jakości.
- `koszty` i `oferta`: rezygnacja z generatora i plików JSON – Excel prowadzi inwestor, asystent pracuje na
  załączonym pliku i zmienia go tylko na prośbę. Usunięto `koszty/scripts/generuj.py` i schematy JSON.
- Notion: istniejąca Baza wiedzy (Tematy + Rozmowy i źródła) rozszerzona o bazy Informacje i Rejestr sprzeczności;
  Rozmowy i źródła dostały pola Link, Typ autora, Konflikt interesów, Wiarygodność, ID (ZRD); rollupy liczą potwierdzenia i datę informacji.
- `wiedza` obsługuje też relacje z rozmów („dzwoniłem do konstruktora…”) – jeden przepływ dla filmów i rozmów.

## [0.1.0] – 2026-10-09

Pierwszy szkielet harnessu.
- Procedury: `budowa` (kontekst, zasady, mapa), `oferta`, `koszty`, `notatka`, `analiza-techniczna`, `rozwoj-harnessu`.
- Adaptery: plugin Claude, `CLAUDE.md`, `GEMINI.md`, `gemini-extension.json`, `.agents/skills`, `.claude/skills`.
- `tools/build.py`: walidacja (nazwy, opisy, wersje, odwołania, brak telefonów) + paczki `dist/`.
- `koszty/scripts/generuj.py`: generowanie Excela z JSON + przeliczenie + kontrola błędów formuł.
- Zasady pracy przeniesione z dokumentu „jak-pracujemy-z-plikami” (projekt Claude „Dom”).

## Do zrobienia

- [ ] Procedura `etap` – checklisty „przed startem / w trakcie / odbiór” (Etapy budowy – przewodnik + Baza wiedzy, Rodzaj „Kontrola / odbiór”).
- [ ] Procedura `odbior` – protokół odbioru etapu ze zdjęciami i listą usterek.
- [ ] Po ~10 filmach: przegląd jakości ekstrakcji (czy nic ważnego nie ginie, czy nie ma duplikatów) i korekta procedury `wiedza`.
