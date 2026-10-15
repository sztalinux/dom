---
name: przeglad-dnia
description: Zaplanowane przebiegi bez inwestora (claude.ai, poza projektem) w dwóch trybach – SZYBKI (co godzinę lub co 2 godziny w ciągu dnia) rozkłada nowe wpisy z „📓 Dziennika” na bieżąco i kończy się od razu, gdy nic nie ma; WIECZORNY robi podsumowanie dnia i plan na jutro ze wszystkich obszarów (zadania prywatne, dziecko, praca, budowa) we wpisie „📆 Przeglądy dzienne” i linii „🤖” w Dzienniku, plus analizę nowych pomysłów. Używaj, gdy uruchamia go zaplanowane zadanie („Dziennik – szybki przebieg”, „Przegląd dnia”) albo użytkownik mówi „przegląd dnia”, „podsumuj dzień”, „plan na jutro”, „wieczorny przegląd”, „ogarnij dzisiejsze”.
---

# Przegląd dnia – tryb szybki i wieczorny

Dwa zaplanowane zadania na claude.ai, oba **poza projektem** (pliki projektu „Dom” nie doklejają się do przebiegu):

| Zadanie | Kiedy | Polecenie | Co robi |
|---|---|---|---|
| Dziennik – szybki przebieg | co 1–2 h w ciągu dnia (np. 8–22) | „Dziennik – szybki przebieg (skill przeglad-dnia z pluginu ja, tryb szybki)” | rozkłada nowe wpisy; pusto → koniec bez zapisów |
| Przegląd dnia | raz wieczorem (np. 21:30) | „Przegląd dnia (skill przeglad-dnia z pluginu ja, tryb wieczorny)” | ostatni szybki przebieg + podsumowanie dnia + plan na jutro + pomysły |

Ręcznie w rozmowie: „przerób dziennik” = tryb szybki, „przegląd dnia” / „podsumuj dzień” = tryb wieczorny.

## Zasady trybu bez inwestora (oba tryby)

- Nie ma kogo zapytać: niejasne → pytanie w Notion (Dziennik „❓”, strona pomysłu), nie tylko w odpowiedzi.
- Nie zapisuj decyzji inwestora, rozstrzygnięć sprzeczności (SP), zmian w Excelu ani zmian terminów kroków Harmonogramu
  budowy – zostaw w „❓” z pytaniem i propozycją. Nowy obszar Dziennika tylko proponuj w „❓”, nie dodawaj sam.
- Bez planu do akceptacji; zapisy wsadowo (`ja`, zasada 2); odczyt baz trybem rows/view, nie SQL.
- Błąd zapisu (brak uprawnień, limit) → nie ponawiaj w kółko; odnotuj „nie zapisano: …” i zakończ.
- W odpowiedzi (log zadania) bez treści emocji i notatek o dziecku – liczby i linki.

## A. Tryb szybki – ma być tani

1. **Jeden odczyt:** pobierz tylko stronę Dziennik (`3f8f5982-09e7-80c8-a154-c59aeb844e8f`). Nie pobieraj jeszcze Obszarów,
   przewodnika ani baz.
2. **Nic nowego → koniec.** Brak bloków/podstron na pierwszym poziomie (definicja w `wpisy`) i brak odpowiedzi inwestora pod
   pytaniami w „❓” → odpowiedz jedną linią „Dziennik: nic nowego (<godzina>)” i zakończ. **Zero zapisów** – nie dopisuj linii
   „🤖”, nie zmieniaj strony.
3. **Inwestor może jeszcze pisać:** strona edytowana mniej niż 15 minut temu (czas ostatniej edycji strony), a najnowszy wpis
   nie ma jeszcze kropki, wygląda na urwany albo jest pusty → „Dziennik: pomijam, świeże wpisy (<godzina>)” i zakończ.
   Następny przebieg je weźmie.
4. **Są wpisy:** procedura `wpisy`, kroki 2–7, bez pytań w rozmowie (wyjątki z zasad wyżej). Linia „🤖” w bloku dnia –
   krótka, z godziną: `🤖 11:00: przetworzono 2 (zadania 1, emocje 1), czeka na Ciebie 1`. Kolejne przebiegi tego dnia
   dopisują swoje linie pod spodem w tym samym bloku; tytuł bloku pokazuje sumę dnia.
5. Bez analizy pomysłów, bez „jutra”, bez wpisu w Przeglądach dziennych – to robi wieczór.

## B. Tryb wieczorny – podsumowanie i plan

1. **Ostatni szybki przebieg** – jak A.1–A.4, ale bez reguły 15 minut (wieczorem przetwórz wszystko, co jednoznaczne).
2. **Pomysły na rozwój** – `rozwoj-harnessu`, sekcja C: Status Nowy lub pusty → analiza (max 3, najstarsze pierwsze);
   „Pytania do mnie” z odpowiedzią → analizuj dalej. Niczego nie wdrażaj.
3. **Dziś** (tylko odczyt): blok dzisiejszego dnia w „Przetworzone” (co rozłożono, liczby per obszar), TASKS zamknięte dziś
   (PLANNED DONE, ostatnia edycja dziś – wszystkie obszary), Dziennik budowy z dzisiejszą datą, liczba wpisów emocji z dziś
   (bez treści), wpisy w „❓” czekające na inwestora.
4. **Jutro** (tylko odczyt): TASKS „📅 Jutro – wszystko” i zadania po terminie (When < dziś, niezakończone); część budowlana –
   skill `budowa` (plugin dom-budowa), sekcja „Wieczorem” (Harmonogram, bramki, dostawy, zamówienia). Na stronie przewodnika
   (`3f6f5982-09e7-81f5-bade-ec877d8d936a`) sprawdź ID, jeśli któryś odczyt się nie powiedzie.
5. **Wpis w „📆 Przeglądy dzienne”** (`3f8f5982-09e7-815e-8b03-eacaa74db190`) – **codziennie**, także w spokojny dzień:
   zwijany nagłówek „Przegląd dnia – <dzień tygodnia> <data>” na górze strony (najnowszy pierwszy), w środku:
   ```
   **Dziś:** 3–6 punktów – co się wydarzyło i co zamknięte (budowa / prywatne / dziecko / praca)
   **Czeka na Ciebie:** n pytań w ❓ (rozwiń w Dzienniku), decyzje budowy
   **Jutro – plan:** lista wg godzin/priorytetu: zadania z terminem, kroki budowy, „przypomnij się <komu>”, po terminie na górze
   **Rozkminka** (tylko gdy inwestor prosił we wpisie albo dzień przyniósł decyzję do przemyślenia): 2–5 zdań
   ```
   **Ręczny przebieg** (prośba w rozmowie) = osobny wpis z tą samą datą i dopiskiem „(ręczne)”, kolejne „(ręczne 2)”…
   Nigdy nie nadpisuj wcześniejszego wpisu – sprostowanie to jedna linia kursywą na jego górze z odesłaniem.
6. **Linia „🤖”** – na górze dzisiejszego bloku w „Przetworzone”, w tej samej edycji Dziennika co krok 1:
   ```
   🤖 15.10 wieczór: dziś przetworzono 6 · czeka na Ciebie 1 · pomysły – 1 · jutro: 3 → Przeglądy dzienne
   	- jutro: <sprawa – kto – kiedy>      ← max 3 najważniejsze punkty, budowa i prywatne razem
   ```
7. **Odpowiedź** (log zadania): linia „🤖” + lista zapisów (gdzie, link) i błędów.

## Koszt i częstotliwość

Każdy przebieg to osobna sesja – nawet pusty zużywa limit konta na start (instrukcje, opisy skilli, narzędzia Notion) i jeden
odczyt Dziennika. Dlatego tryb szybki ma wyjście w kroku A.2 bez dalszych odczytów i zapisów, a strona Dziennik ma zostać
krótka (przegląd tygodnia czyści „Przetworzone” starsze niż 14 dni). Zacznij od co 2 godzin; częściej – gdy limit pozwala.

## Rozszerzanie

Nowa rzecz codzienna (np. poranny brief, suplementy do kupienia) = nowy krok trybu wieczornego przed wpisem w Przeglądach
i jeden licznik w linii „🤖”. Tryb szybki zostaje minimalny. Nowy obszar Dziennika nie wymaga zmian tutaj – obsługuje go `wpisy`.
