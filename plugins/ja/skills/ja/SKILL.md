---
name: ja
description: Kontekst osobisty użytkownika i mapa obszarów jego Dziennika w Notion (emocje, praca, dziecko, zadania, suplementy, książki, budowa). Używaj na początku każdej rozmowy o jego dniu, emocjach, pracy, dziecku, zadaniach, suplementach, Dzienniku, przeglądzie dnia albo o samym asystencie – gdy pada „zapisz w dzienniku”, „przerób dziennik”, „zrobiłem…”, „muszę…”, „przypomnij mi”, „czuję…”, „kończy się…”, „co mam jutro”, „przegląd dnia”, „zapamiętaj na przyszłość”, „mam pomysł na asystenta”. Przy tematach budowy kieruje do skilla budowa (plugin dom-budowa).
---

# Ja – kontekst i mapa procedur

## Kim jest użytkownik

Programista, buduje dom systemem mieszanym (budowę obsługuje plugin `dom-budowa`, skill `budowa`), ma dziecko w wieku
przedszkolnym i partnerkę. Prowadzi w Notion dziennik emocji, dziennik produktywności w pracy, listę zadań i bazę
suplementów. Woli pisać luźno niż wypełniać pola – porządek robi asystent. Oczekuje konkretu, po polsku, bez wyjaśniania
podstaw. Imiona i szczegóły prywatne są tylko w Notion (repo jest publiczne) – nie przepisuj ich do harnessu.

Gdzie co jest w Notion (ID baz, widoki, sekcje): `references/notion-mapa.md`; ta sama mapa jest na stronie Notion
„📑 Przewodnik po dokumentach i Notion” (`3f6f5982-09e7-81f5-bade-ec877d8d936a`) – poza Claude Code pobierz ją raz
na rozmowę, gdy potrzebujesz ID baz (Claude Code synchronizuje ją sam, więc jest aktualna także przed odświeżeniem pluginu).

## Na starcie rozmowy: zmiany do harnessu

Inwestor zgłasza poprawki sposobu pracy z różnych miejsc do skrzynki Notion **„Zmiany do harnessu”**
(`collection://e217448a-60ec-4af6-8584-8f368315109c`, oba pluginy). Na początku rozmowy pobierz (jedno zapytanie) wpisy ze
Statusem „Do wdrożenia” **albo pustym** – inwestor dodaje je też ręcznie bez wypełniania pól:

- **W repozytorium harnessu (Claude Code):** wdroż je – `rozwoj-harnessu`, sekcja B (najpierw uzupełnij puste pola).
- **Gdziekolwiek indziej:** traktuj je jako obowiązujące zasady, nadrzędne wobec procedur. Statusu nie zmieniaj.
- Skrzynka pusta lub Notion niedostępny → pracuj normalnie, bez komentarza.
- **Pomysły na rozwój** (`collection://fdee4f05-8f43-4be4-a0d5-2b88642fa6d3`) nie są zasadami. W Claude Code dopisz na starcie
  jedną linię „Pomysły: n nowych do analizy, m »Do zrobienia«” (pomiń przy zerach); analiza – `rozwoj-harnessu`, sekcja C.

## Mapa procedur

Podział wpisów na obszary **nie jest w harnessie** – jest w bazie Notion „🧭 Obszary Dziennika”
(`collection://253b7564-00ac-45b2-a3f4-956275e3a7e0`). Inwestor dopisuje tam nowe obszary sam; czytaj ją, nie zgaduj.

| Gdy użytkownik… | Wczytaj |
|---|---|
| „przerób dziennik”, „co mam w dzienniku”, wkleja kilka luźnych notatek naraz, „odpowiedziałem w dzienniku” | `wpisy` |
| opisuje emocję („czułem złość na 7…”), dzień w pracy, prosi o podsumowanie emocji | `emocje` |
| „muszę…”, „przypomnij mi…”, „zrobiłem X”, „czekam na…”, „co mam jutro / w tym tygodniu” (sprawy pozabudowlane) | `zadania` |
| mówi o dziecku: obserwacja, „porozmawiać z nią o…”, prezent, zabawa, zalecenie specjalisty | `dziecko` |
| „kończy się X”, „kupiłem X”, „zaczynam / przerwa od” (suplement) | `suple` |
| „przegląd dnia”, wieczorne zaplanowane zadanie | `przeglad-dnia` |
| „przegląd tygodnia”, „podsumuj tydzień”, tygodniowe zaplanowane zadanie, „posprzątaj dziennik” | `przeglad-tygodnia-osobisty` (uruchamia też przegląd budowy) |
| poprawia sposób pracy asystenta, „zapamiętaj na przyszłość”, „mam pomysł na…”, „zrób POM-n”, nowa procedura | `rozwoj-harnessu` |
| budowa domu: ekipa, projekt, kosztorys, działka, wiedza budowlana, dokumenty budowy | `budowa` (plugin `dom-budowa`) |

Jedna wiadomość może wymagać kilku procedur – wykonuj je po kolei. Rzecz z obszaru „ogólna” (np. książka do przeczytania)
zapisuj wprost według pól „Gdzie” i „Jak zapisać” w bazie Obszary.

## Zasady (wszystkie procedury pluginu)

1. **Notion jest źródłem prawdy i inwestor edytuje go ręcznie.** Przed zapisem czytaj aktualny stan; jego ręczna zmiana
   jest nadrzędna. Jedna informacja ma jedno miejsce – zanim dodasz, szukaj istniejącego wpisu (2–3 słowa) i aktualizuj.
2. **Zapisy wsadowe bez straty jakości:** najpierw wszystkie odczyty, potem jedno wywołanie na bazę i jedna edycja na stronę;
   przy więcej niż 2 zapisach jedna linia przed nimi: „Zapiszę: 1) … 2) … – N zatwierdzeń”. Nie skracaj treści, nie pomijaj pól.
3. **Odczyt baz:** zapytania w trybach rows i SQL mają wspólny limit w planie Notion (bywa wyczerpany); tryb **view**
   (zapisany widok) limitu nie ma. Kolejność: widok (brak pasującego → utwórz go z filtrem) → wyszukiwarka z parametrem bazy
   (duplikaty, pojedyncze wiersze) → rows → SQL. Błąd „usage limit” → bez ponawiania, przejdź na widok/wyszukiwarkę.
4. **Nie zgaduj:** niejasny wpis, brak daty przy terminie, nie wiadomo czego dotyczy → pytanie (w Dzienniku „❓”, w rozmowie
   wprost). Słowa względne („wczoraj”, „w piątek”) licz od daty we wpisie, nie od daty przetwarzania.
5. **Prywatność:** treść emocji, notatki o dziecku i zdrowiu zostają w Notion; w odpowiedziach nie cytuj ich ponad potrzebę.
   Repo harnessu jest publiczne – zero imion, treści wpisów i danych w plikach procedur, przykłady zmyślone.
6. **Porządek statusami, nie usuwaniem.** Nie usuwaj treści bez pytania; przed dużą reorganizacją zrób kopię strony.
7. **Pole tekstowe = jedno zdanie;** szczegóły, listy i dopiski z datą idą do treści strony (tak jak w procedurach budowy).

## Domknięcie rozmowy

Na koniec pracy, która coś zmieniła: **Zmienione** (co i gdzie, link) · **Otwarte** (pytania czekające na inwestora) ·
**Następny krok** (jedna rzecz). Gdy inwestor poprawił sposób pracy – zaproponuj wpis do skrzynki (`rozwoj-harnessu`, A).
