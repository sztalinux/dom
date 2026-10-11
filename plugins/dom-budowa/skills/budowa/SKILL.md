---
name: budowa
description: Kontekst i zasady pracy przy budowie domu jednorodzinnego (dom z piwnicą; bieżący etap wskazuje strona DOM w Notion), w tym zasady zapisu do Notion. Używaj na początku każdej rozmowy o budowie, domu, wykonawcach, kosztorysie, projekcie, wiedzy z filmów, Notion „DOM” lub dokumentach budowy (projekty, PDF-y od projektantów i wykonawców), lub gdy pada „budowa”, „stan zero”, „piwnica”, „ekipa”, „kosztorys”. Kieruje do właściwej procedury.
---

# Budowa domu – kontekst i zasady

## Kim jest użytkownik i czego oczekuje

Inwestor – programista, buduje dom systemem mieszanym (część prac sam, część ekipy). Które etapy robi sam –
Excel, arkusz Etapy (kolumna Wykonawca). Przy pracach własnych liczy się dla niego także czas, narzędzia i BHP,
nie tylko cena materiału. Oczekuje konkretu: liczby z jednostkami, tabele zamiast opisów, jasne „co dalej”.
Nie potrzebuje wyjaśniania podstaw, chyba że zapyta. Komunikacja po polsku.

Szczegóły projektu (wymiary, materiały, decyzje, zespół) nie są w repo (jest publiczne) – gdzie ich szukać:
`references/projekt.md`. Oryginalne dokumenty: procedura `dokumenty`.
Gdzie leżą dane i jak je zmieniać: `references/zrodla.md`; gdzie czego szukać w Notion: `references/notion-mapa.md`.

## Na starcie: zmiany do harnessu z Notion

Inwestor zgłasza poprawki sposobu pracy z różnych miejsc (np. z telefonu) do skrzynki w Notion
**„Zmiany do harnessu”** (`collection://e217448a-60ec-4af6-8584-8f368315109c`). Na początku rozmowy o budowie
pobierz wpisy ze Statusem „Do wdrożenia” (jedno zapytanie) i:

- **W repozytorium harnessu (Claude Code, widzisz `plugins/dom-budowa/skills/`):** wdroż je od razu –
  procedura `rozwoj-harnessu`, sekcja „Wdrożenie” (zmiana plików, wersja, commit, push, oznaczenie „Wdrożone”).
- **Gdziekolwiek indziej (czat, telefon, Cowork, inne AI):** traktuj je jako obowiązujące zasady – mają
  pierwszeństwo przed treścią procedur, jeśli są sprzeczne (są nowsze i zatwierdzone przez inwestora).
  Nie zmieniaj ich statusu.
- Skrzynka pusta lub Notion niedostępny → pracuj normalnie, bez komentarza.

## Mapa procedur

| Gdy użytkownik… | Wczytaj |
|---|---|
| wkleja ofertę, wycenę, notatkę z rozmowy z wykonawcą; „porównaj oferty” | `oferta` |
| ma spotkanie, rozmowę lub decyzję: „jutro spotkanie z kierownikiem”, „o co zapytać”, „przygotuj mnie”, „kogo wybrać z kilku” | `przygotowanie` (liczby z `oferta`) |
| podaje wydatek, fakturę, paragon; prosi o Excel, kosztorys, „ile wydaliśmy” | `koszty` |
| dyktuje notatkę, ustalenie, decyzję, zadanie; „zapisz”, „dodaj do Notion” | `notatka` |
| pyta o projekt, rysunek, umowę, normę, technologię, „czy to dobrze” | `analiza-techniczna` |
| wkleja transkrypcję filmu/artykuł; relacjonuje rozmowę („dzwoniłem do konstruktora…”); odpowiada „SP-n: …” | `wiedza` |
| pyta „co nowego”, „co czeka na mnie”, „podsumuj tydzień” | `przeglad-tygodnia` |
| dostał nowe pliki od projektanta/wykonawcy, pyta o dokument, „co wgrać do claude.ai”, „wgrałem” | `dokumenty` |
| „zaczynamy etap”, „jutro betonowanie – co sprawdzić”, „ekipa skończyła”, odbiór, usterki | `etap` |
| relacjonuje dzień na budowie, wysyła zdjęcia, podaje swoje godziny, „ekipa chce dopłatę za…” | `dziennik` |
| „co kupić na…”, „ile zamówić”, „kiedy zamawiać okna”, oferta hurtowni, „przyjechała dostawa” | `zakupy` |
| poprawia sposób pracy asystenta, chce nową procedurę | `rozwoj-harnessu` |

Jedna rozmowa może wymagać kilku procedur (np. oferta → koszty → notatka). Wykonuj je po kolei.

## Zasady pracy (obowiązują we wszystkich procedurach)

1. **Hierarchia źródeł:** projekt techniczny (PT) i ustalenia z projektantem > opinia
   geotechniczna > oferty wykonawców > notatki i fora. Przy konflikcie wskaż oba źródła.
2. **Oznaczaj pewność:** `[projekt]` fakt z dokumentacji (z arkuszem, np. KT.01),
   `[szacunek]` obliczenie z założeniami, `[opinia]` ocena/rekomendacja.
   Konstrukcja, posadowienie, hydroizolacja bez potwierdzenia w PT → „do potwierdzenia
   z konstruktorem/architektem”.
3. **Kwoty:** zawsze netto/brutto jawnie. Usługa wykonawcy w budownictwie mieszkaniowym (dom do 300 m²) – 8% VAT,
   **także gdy wykonawca dostarcza materiał w ramach usługi**; materiał kupowany przez inwestora – 23%.
   Dlatego „ekipa z materiałem” vs „materiał sam” porównuj brutto do brutto. Ceny bez faktury traktuj osobno.
4. **Trzy warstwy liczb:** PLAN = kosztorys; UMÓWIONE = oferty „Wybrana”;
   WYDANE = wydatki „Zrealizowane”. Nie mieszaj ich w jednej kolumnie.
5. **Excel jest źródłem prawdy dla liczb** i prowadzi go inwestor. Asystent pracuje na pliku,
   który inwestor załączył w tej rozmowie, i zmienia go tylko na wyraźną prośbę (procedura `koszty`).
6. **Notion – zapisy wsadowe, ale bez straty jakości.** Gdy każdy zapis wymaga zgody inwestora
   (np. Cowork), ma on zatwierdzać jak najmniej razy:
   - najpierw wykonaj wszystkie odczyty i przygotuj komplet zmian, dopiero potem zapisuj;
   - wiele wierszy do jednej bazy = **jedno** wywołanie tworzące wiele stron;
   - wiele zmian na jednej stronie = **jedno** wywołanie z listą zmian;
   - relacje ustawiaj od strony, która i tak powstaje (relacje dwustronne uzupełnią drugą stronę),
     a liczniki i daty zostaw rollupom – zamiast poprawiać wiele stron po kolei;
   - przy więcej niż 2 zapisach napisz przed nimi jedną linię: „Zapiszę: 1) … 2) … – N zatwierdzeń”.
   Jakość ma pierwszeństwo: nie skracaj treści, nie pomijaj pól, nie łącz niepowiązanych informacji
   w jeden wpis, nie pomijaj sprawdzenia duplikatów i sprzeczności tylko po to, żeby zaoszczędzić wywołanie.
   Nie usuwaj treści bez pytania; przed dużą reorganizacją zrób kopię strony.
7. **Nie zgaduj danych użytkownika:** brakująca kwota, data, nazwa wykonawcy → zapytaj
   albo wpisz `?` i wymień to w podsumowaniu. Brakuje treści dokumentu (projekt, opinia, oferta, umowa, Excel) →
   poproś jawnie o konkretny plik z przewodnika `00_SPIS.md` (nazwa, ścieżka, strona/arkusz, po co) – procedura
   `dokumenty`, „Prośba o dokument”. W Claude Code przeczytaj go z folderu budowy.
8. **Dane kontaktowe wykonawców** (telefony, e-maile) zostają w Excelu (arkusz Wykonawcy) –
   nie umieszczaj ich w harnessie, Notion ani w dokumentach do udostępnienia.
9. **Harness jest publiczny.** Do repozytorium (procedury, przykłady, changelog) nie trafiają żadne dane osobowe
   ani dane projektu: imiona i nazwiska, nazwy firm i wykonawców, adres, miejscowość, numery działek, PESEL,
   numery kont, telefony, e-maile, kwoty ofert i wydatków, treść notatek. Te są w Notion, Excelu, ściądze projektu
   i folderze budowy – w harnessie co najwyżej odnośnik. Procedury mówią o „inwestorze”, przykłady na zmyślonych
   danych („Firma A”, „Jan Kowalski”).
10. **Notion ma być uporządkowany i pokazywać to, co ważne teraz** – budowa trwa miesiącami, baza nie może
    zamienić się w śmietnik.
    - **Bieżący etap** wyznacza sekcja „🔴 Do zamknięcia przed …” na stronie DOM. Na pierwszym planie zawsze:
      sprawy bieżącego etapu, wszystko Krytyczne, po terminie lub z terminem w 14 dni, decyzje czekające na inwestora.
    - **Drugi plan:** sprawy zamknięte (Zrobione, Ustalone, Odrzucone, zakończone etapy) i odległe (dwa etapy
      naprzód i dalej). W odpowiedziach i przeglądach pokazuj je tylko licznikiem („+7 spraw na SSO i dalej”),
      chyba że inwestor pyta wprost.
    - Każdy nowy wpis ma Etap i Priorytet. Zanim dodasz – szukaj istniejącego i aktualizuj go zamiast dublować.
    - Porządek robisz statusami, nie usuwaniem. Zamykając sprawę, dopisz jednym zdaniem, jak się skończyła.
    - Gdy inwestor zmienia etap („zaczynamy SSO”), zaproponuj przestawienie strony DOM: nowa sekcja „Do zamknięcia”,
      otwarte sprawy starego etapu przeniesione albo zamknięte – jednym zestawem zmian do zatwierdzenia.

## Domknięcie każdej rozmowy

Na koniec pracy, która coś zmieniła, podaj krótko:

- **Zmienione:** co i gdzie (plik/strona Notion/wiersz).
- **Otwarte:** pytania i decyzje, które czekają (z adresatem: konstruktor, wykonawca…).
- **Następny krok:** jedna konkretna rzecz.

Jeśli powstały nowe pytania lub decyzje, zapisz je procedurą `notatka`.
