# Changelog

Format: [wersja] – data – co i dlaczego. Wersjonowanie semver:
PATCH = poprawka treści, MINOR = nowa procedura/pole, MAJOR = zmiana struktury danych.

## [1.4.4] – 2026-10-12

- `inbox`: Notion nie zapisuje daty dopisania punktu – data zdarzenia tylko z wpisu (`@today` albo data tekstem);
  „dziś/wczoraj” bez daty → pytanie z propozycją daty, nie zgadywanie. Podpowiedź w Inboxie na stronie DOM.

## [1.4.3] – 2026-10-12

- Strona DOM uproszczona: Inbox i Zadania u góry; zakładki Etap (checklista „Do zamknięcia” + bramki, plan przepustów,
  etapy budowy), Notatnik, Dziennik, Wiedza, Wykonawcy, Więcej; na dole zwinięta sekcja „🤖 Dla asystenta” (przewodnik,
  harness, ściąga „📐 Dane projektu”). Nazwy sekcji używane w procedurach bez zmian; mapa Notion i `projekt.md` zaktualizowane.

## [1.4.2] – 2026-10-12

- Strona DOM: Inbox i Zadania jako rozwijane nagłówki, reszta w zakładkach (Do zamknięcia, Notatnik, Dziennik, Wiedza,
  Wykonawcy, Projekt ze ściągą, Rzadko) – mapa Notion zaktualizowana.

## [1.4.1] – 2026-10-12

- `inbox`: Inbox to sekcja „📥 Inbox” (toggle, wolny tekst) na stronie DOM, nie baza – inwestor pisze punkt pod punktem;
  pytania asystenta jako punkt „❓ asystent (data)” pod wpisem, odpowiedź pod spodem; załatwione wpisy przenoszone do
  „Przetworzone” (ślad z linkiem), które czyści przegląd tygodnia. Baza Inbox z 1.4.0 usunięta (decyzja inwestora).
- Strona DOM: kolejność Inbox → Zadania → reszta bez zmian; sekcja „📐 Dane projektu” wróciła na poziom główny
  (była zagnieżdżona pod „Asystent AI”); podstrony Stan zero i Plan przepustów w „Strony i materiały”; prototypy układu usunięte.
- `przeglad-tygodnia`, `notion-mapa.md`, `zrodla.md`, README: zgodnie z powyższym.

## [1.4.0] – 2026-10-12

Inbox, spójność przy ręcznych zmianach w Notion, mniej miejsc z tą samą informacją.
- Nowa procedura `inbox` + baza Notion „Inbox” (DOM): luźne wpisy inwestora; asystent przetwarza je na „przerób inbox” –
  wpis niejednoznaczny albo bez źródła wraca z pytaniami (Status „Do wyjaśnienia”, pola Pytania asystenta / Odpowiedź),
  jednoznaczny trafia przez właściwą procedurę do Notatnika / Bazy wiedzy / Dziennika / TASKS / Excela („Trafiło do”).
- `budowa`, zasada 11 (dawna 11 → 12): Notion jest źródłem prawdy i inwestor edytuje go ręcznie – czytaj przed zapisem,
  nie poprawiaj ręcznych zmian bez pytania; ściąga ma jedno źródło: Notion „📐 Dane projektu” (plik w folderze = kopia).
- `przeglad-tygodnia`: liczniki Inboxu (w tym pytania czekające na inwestora) i sekcja „Spójność” – rozjazdy między
  Notatnikiem, Bazą wiedzy, checklistą „Do zamknięcia”, Dziennikiem i TASKS, proponowane w „Porządkach”.
- Notion: strona „Asystent AI – harness budowy” skrócona do ramki z wersją + skrzynka (opis procedur jest w README repo);
  opcja `inbox` w polu Procedura skrzynki; mapa Notion z Inboxem.
- `rozwoj-harnessu`: krok 7 aktualizuje tylko linię „Wersja”.

## [1.3.0] – 2026-10-11

Bez wgrywania plików na claude.ai; kolejność szukania odpowiedzi; wiedza zawsze ze źródłem.
- Przewodnik po dokumentach i mapa Notion na stronie Notion „📑 Przewodnik po dokumentach i Notion” – Claude Code
  aktualizuje ją sam (`tools/dokumenty.py` generuje `.dom/przewodnik-notion.md`, raport mówi, kiedy przepisać stronę;
  `dokumenty.py notion-ok`). Claude Code nie może zapisywać plików w wiedzy projektu na claude.ai, ale Notion claude.ai
  czyta na żywo. Paczka `_Do claude.ai/` – tylko kopia awaryjna. `CLAUDE.md`: synchronizacja na starcie sesji bez pytania.
- `budowa`: przewodnik z Notion raz na rozmowę; nowa zasada 10 – kolejność szukania odpowiedzi: materiały inwestora →
  sprawy nierozstrzygnięte (Notatnik, sprzeczności, rozmowy, dziennik, archiwum) → internet z oznaczeniem `[internet]`,
  źródłem, datą, typem autora i oceną wiarygodności (zasady 10–11 przenumerowane; odwołania w `etap`, `przeglad-tygodnia`).
- `wiedza`: każda informacja ma źródło (Źródła albo Notatnik); sekcja F – ustalenie z Notatnika → Informacja z relacją
  do wpisu; sekcja G – notatki własne i archiwum jako źródło („Notatki własne”); odpowiedź „co wiemy” podaje źródła.
- `notatka`: ustalenie z wiedzą techniczną → od razu także Informacja w Bazie wiedzy (krok 6).
- Notion: Informacje ↔ Notatnik (relacja „Notatnik” / „Wiedza”), Forma „Notatki własne” w Rozmowach i źródłach.
- **Instrukcje projektu zmienione – wklej ponownie** (`dist/claude-ai-projekt/instrukcje.md`); wiedza projektu może być pusta.

## [1.2.0] – 2026-10-11

- Nowa procedura `przygotowanie`: karta przygotowania do spotkania, rozmowy lub decyzji (cel, 3 najważniejsze rzeczy,
  co wiemy u nas, pytania z „dobrą odpowiedzią” i czerwonymi flagami, macierz decyzji przy wyborze, co zabrać,
  czego nie obiecywać, słowniczek, zapis po spotkaniu); `references/sytuacje.md` – kierownik budowy, wybór wykonawcy
  z finalistów (rozmowa finałowa, referencje), konstruktor/architekt, węzeł betoniarski, hurtownia, odbiór, urząd.
  „Kogo wybrać” przechodzi z `oferta` do `przygotowanie` (liczby nadal z `oferta`).
- Nowy `budowa/references/notion-mapa.md`: struktura Notion z perspektywy „czego szukasz” (strony, bazy, widoki, pola,
  słowniki); `tools/dokumenty.py` dołącza ją do przewodnika `00_SPIS.md`, więc jest w kontekście każdej rozmowy
  w projekcie „Dom”. `rozwoj-harnessu`: zmiana struktury Notion = aktualizacja mapy.
- Instrukcje projektu bez zmian (nie trzeba wklejać ponownie); `00_SPIS.md` – wgraj nową wersję.

## [1.1.0] – 2026-10-11

Lekki projekt „Dom” na claude.ai: przewodnik po dokumentach zamiast pełnych dokumentów w kontekście każdej rozmowy.
- `tools/dokumenty.py`: nowe pole `--zawartosc` (na jakie pytania odpowiada dokument, gdzie szukać); `00_SPIS.md` to teraz
  **przewodnik po dokumentach** – każdy dokument z opisem zawartości lub eksportem, z informacją, czy jest w wiedzy projektu,
  czy tylko na komputerze; przepisywany tylko przy zmianie treści (wcześniej codziennie lądował na liście „podmień”);
  raport startowy liczy dokumenty bez opisu zawartości.
- `dokumenty`: paczka = przewodnik + ściąga; pełne dokumenty i Excel tylko na wyraźną prośbę inwestora (decyzja inwestora);
  nowa sekcja „Prośba o dokument” – gdy brakuje treści, asystent jawnie prosi o konkretny plik (nazwa, ścieżka,
  strona/arkusz, po co) i nie odpowiada z pamięci; w Claude Code czyta plik z folderu.
- `budowa` (zasada 7), `projekt.md`, `zrodla.md`, `koszty`: to samo zachowanie; Excel na claude.ai zawsze załączany aktualny.
- `claude-ai-projekt.md`: instrukcje projektu skrócone do odnośników (zasady są w skillach, więc rzadko trzeba je wklejać
  ponownie). **Wklej instrukcje na nowo** (`dist/claude-ai-projekt/instrukcje.md`). Aktualizacja pluginu: opcja
  odświeżenia marketplace'u, jeśli jest; inaczej usuń i dodaj marketplace ponownie (opcji „Check for updates” może nie być).
- `marketplace.json`: opis pluginu zgodny z `plugin.json` (claude.ai pokazywał stary opis).

## [1.0.3] – 2026-10-10

- `rozwoj-harnessu/references/claude-ai-projekt.md`: sekcja „Wiedza projektu a kontekst” tylko opisuje działanie
  (kontekst / RAG, wskaźnik pojemności) – o zawartości paczki decyduje wyłącznie `dokumenty` (usunięta sprzeczna reguła z 1.0.2).
  Tekst instrukcji projektu bez zmian.

## [1.0.2] – 2026-10-10

claude.ai na co dzień: instrukcje projektu zamiast `START.md`, ręczna aktualizacja pluginu.
- Nowy `rozwoj-harnessu/references/claude-ai-projekt.md`: tekst instrukcji projektu „Dom” (przy każdej wiadomości skill
  `budowa` → procedura, raz na rozmowę skrzynka „Zmiany do harnessu”, dane z Notion i wiedzy projektu, bez „/”;
  gdy skille są niedostępne – powiedz to i nie zgaduj procedur), aktualizacja pluginu przez „Check for updates”,
  wiedza projektu a kontekst. **Wklej instrukcje na nowo** (`dist/claude-ai-projekt/instrukcje.md`), usuń `START.md`.
- `tools/build.py`: generuje `dist/claude-ai-projekt/instrukcje.md` z numerem wersji.
- `rozwoj-harnessu`: po wdrożeniu przypomnienie o „Check for updates” (i o ponownym wklejeniu instrukcji, gdy się zmieniły).
- README, `dostawcy.md`, `zrodla.md`: aktualizacja pluginu nie jest automatyczna (organizacja może blokować synchronizację);
  hooki pluginu działają w Cowork i Claude Code, nie w czacie; `/` tylko do wymuszenia procedury.

## [1.0.1] – 2026-10-10

Poprawki po testach na sucho procedur 1.0.0.
- `etap`: sprawy etapu obejmują też wpisy Typ „Pamiętać” niezależnie od Statusu („Ustalone”); bramka sprawdza poprzednie bramki
  i pogodę na dzień kroku.
- `dziennik`: data względna → data, sprawdzenie duplikatu wpisu z tego dnia, zasada pola „Przed zakryciem OK”.
- `zakupy`: bez pliku Excela – prośba o plik i lista tego, co zostanie policzone.
- `oferta`: „Sam czy ekipa” – przeliczenie brutto → netto i format wyniku (tabela ekipa vs sam, różnica w zł i dniach).
- `wiedza`: tryb odczytu pokazuje Status decyzji i zgłasza nakładające się tematy.
- `analiza-techniczna`: praca własna – ilości na jednostkę przy braku wymiarów, kontrole z `etap/references/odbiory.md`.

## [1.0.0] – 2026-10-10

Pierwsza stabilna wersja – baza do dalszego rozwoju. Harness obejmuje teraz także fazę wykonywania budowy (budowa mieszana: część prac sam, część ekipy).
- Nowa procedura `etap`: plan etapu (zależności sam/ekipa, blokady, ludzie, pogoda), bramki „bez odwrotu” z listą
  zdjęć przed zakryciem, odbiór z protokołem i płatnością dopiero po odbiorze; `references/odbiory.md` (co sprawdzać
  krok po kroku), `references/formalnosci.md` (urzędy, dziennik, kierownik, kto musi być obecny).
- Nowa procedura `dziennik`: wpis z dnia na budowie (kto, co, pogoda, dostawy, godziny własne, problemy, zdjęcia),
  roboty dodatkowe tylko na piśmie przed wykonaniem; schemat bazy Notion „Dziennik budowy” (`references/notion-dziennik.md`).
- Nowa procedura `zakupy`: lista zakupów na etap z kosztorysu + drobnica + zapas, zapytania i porównanie ofert hurtowni,
  terminy zamówień; `references/wyprzedzenia.md` (wyprzedzenia, czasy technologiczne, okna pogodowe).
- `oferta`: sekcje „Sam czy ekipa” i „Po wyborze – zakres do umowy”; `references/umowa.md` – lista kontrolna umowy z wykonawcą.
- `koszty`: sekcja D „Płatności, transze, kredyt” (transza tylko po protokole odbioru, roboty dodatkowe osobno).
- `analiza-techniczna`: tryb „Praca własna – jak to zrobić” (materiały, narzędzia, kroki z kontrolą, błędy, BHP).
- `budowa`: zasada 3 – 8% VAT obejmuje usługę z materiałem, porównania brutto do brutto; opis inwestora (Sam/Ekipa z Excela).
- `notatka`: „Pamiętać” ze Statusem „Ustalone” (nie zaśmieca „otwartych”), wraca w checkliście etapu.
- `przeglad-tygodnia`: poprawiona numeracja źródeł; sekcje „Budowa w tym tygodniu” i „Zamówić / zapłacić do 14 dni”.
- `rozwoj-harnessu`: po wdrożeniu aktualizacja strony przewodnika w Notion (wersja, tabela procedur).
- `dokumenty` / `tools/dokumenty.py`: foldery `Zdjęcia*` pomijane (zdjęcia nie trafiają do indeksu ani paczki).
- `wiedza`: tryb odczytu „co wiemy o…” (stan wiedzy, co obowiązuje u nas, otwarte sprzeczności, luki).
- `notatka`: przy duplikacie nie powstaje drugi wpis ani link – zostaje jedno źródło prawdy; nowe źródło dopisuje się do pola Źródło.
- `CLAUDE.md`, `rozwoj-harnessu`: jedna sesja Claude Code w repo naraz; commit tylko własnych plików.
- Notion: baza „Dziennik budowy”, opcje `etap`/`dziennik`/`zakupy` w skrzynce, pulpit DOM i strona przewodnika zaktualizowane.
- README: tabela procedur.

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

- [ ] Po ~10 filmach: przegląd jakości ekstrakcji (czy nic ważnego nie ginie, czy nie ma duplikatów) i korekta procedury `wiedza`.
- [ ] Pierwszy przegląd tygodnia uruchomiony z claude.ai (zadanie zaplanowane) – sprawdzić format i czas.
