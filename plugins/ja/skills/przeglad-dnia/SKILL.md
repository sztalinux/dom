---
name: przeglad-dnia
description: Codzienny wieczorny przegląd bez inwestora (zaplanowane zadanie, np. 20:00 na claude.ai, poza projektem) – przerobienie Dziennika według obszarów bez pytań w rozmowie, analiza nowych pomysłów na rozwój, zapowiedź jutra ze wszystkich obszarów (zadania prywatne, dziecko, praca, budowa); wynik jako linia „🤖” w Dzienniku (zwijany blok dnia w „Przetworzone”) i wpis w „📆 Przeglądy dzienne”. Używaj, gdy uruchamia go zaplanowane zadanie albo użytkownik mówi „przegląd dnia”, „wieczorny przegląd”, „ogarnij dzisiejsze”, „zrób codzienny przegląd”.
---

# Przegląd dnia

Cel: co wieczór, bez inwestora, porządek w tym, co wpadło w ciągu dnia – żeby rano zobaczył krótkie podsumowanie: co zrobione,
co czeka na niego, co jutro. Tylko to, co nowe od wczoraj. Szerokie podsumowania budowy i porządki – `przeglad-tygodnia`
(plugin dom-budowa).

## Zasady trybu bez inwestora (wszystkie kroki)

- Nie ma kogo zapytać: niejasne → pytanie w Notion, tam gdzie inwestor je zobaczy (Dziennik „❓”, strona pomysłu).
- Nie zapisuj niczego, co jest decyzją inwestora, rozstrzygnięciem sprzeczności (SP), zmianą w Excelu ani zmianą terminów
  kroków Harmonogramu budowy – zostaw to z pytaniem i propozycją.
- Bez planu do akceptacji; zapisy wsadowo (`ja`, zasada 2); odczyt baz trybem rows/view, nie SQL.
- Na starcie pobierz stronę „📑 Przewodnik po dokumentach i Notion” (`3f6f5982-09e7-81f5-bade-ec877d8d936a`) – aktualne ID baz.
- Błąd zapisu (brak uprawnień, limit) → nie ponawiaj w kółko; jeśli się da, odnotuj go w linii „🤖” („nie zapisano: …”) i zakończ.

## Kroki

1. **Dziennik** – procedura `wpisy`, kroki 1–7, z wyjątkami:
   - przetwarzaj tylko wpisy jednoznaczne; niejasne → „❓” z pytaniem;
   - wpis będący decyzją budowlaną, rozstrzygnięciem SP albo zmianą w Excelu → „❓” z pytaniem „potwierdź, że to decyzja: …”;
   - nowy termin kroku Harmonogramu → „❓” z propozycją zmiany; zadania i „czekam na” (TASKS) zapisuj normalnie;
   - nowy obszar (krok 4 `wpisy`) tylko proponuj w „❓”, nie dodawaj sam;
   - wpisy w „❓”, pod którymi inwestor odpowiedział – oceń ponownie.
2. **Pomysły na rozwój** – `rozwoj-harnessu`, sekcja C: Status Nowy lub pusty → analiza (max 3 na wieczór, najstarsze
   pierwsze); „Pytania do mnie” z odpowiedzią inwestora → analizuj dalej. Niczego nie wdrażaj.
3. **Na jutro** (tylko odczyt):
   - TASKS, widok „📅 Jutro – wszystko” (wszystkie obszary) oraz zadania po terminie (When < dziś, niezakończone);
   - część budowlana: skill `budowa` (plugin dom-budowa), sekcja „Wieczorem” – kroki Harmonogramu, bramki, dostawy, zamówienia.
   Nic nie ma → pomiń.
4. **Linia „🤖”** – w tej samej, jednej edycji strony Dziennik co krok 1: na górze zwijanego bloku dzisiejszego dnia
   w „Przetworzone” (tytuł bloku „📅 15.10 czw · 🤖 <skrót tej linii>”). Pierwszy poziom Dziennika zostaje pusty:
   ```
   🤖 15.10 wieczór: dziennik – przetworzono 4 (budowa 1, emocje 1, zadania 2), czeka na Ciebie 1 · pomysły – 1 · jutro: 3
   	- jutro: <sprawa – kto – kiedy>      ← max 3 punkty zagnieżdżone, budowa i prywatne razem, najważniejsze pierwsze
   ```
   Pusty dzień → „🤖 15.10 wieczór: nic nowego”. Punkty pod linią „🤖” to nie wpisy Dziennika.
5. **Wpis w „📆 Przeglądy dzienne”** (`3f8f5982-09e7-815e-8b03-eacaa74db190`, podstrona Dziennika), gdy przebieg ma tam coś
   do dopisania (dziś / jutro, „rozkminka”, o którą inwestor prosi we wpisie): zwijany nagłówek „Przegląd dnia – <dzień
   tygodnia> <data>” na górze strony (najnowszy pierwszy), sekcje „Dziś” i „Jutro” z podziałem Budowa / Prywatne.
   **Ręczny przebieg** (inwestor prosi w rozmowie) = **osobny wpis** z tą samą datą i dopiskiem „(ręczne)”, kolejne
   „(ręczne 2)”… Nigdy nie nadpisuj wcześniejszego wpisu – sprostowanie to jedna linia kursywą na jego górze z odesłaniem.
6. **Odpowiedź** (log zadania): treść linii „🤖” + lista zapisów (gdzie, link) i błędów – bez treści emocji i notatek o dziecku.

## Rozszerzanie

Nowa rzecz codzienna (np. poranny brief, kontrola suplementów do kupienia) = nowy krok przed „Linią 🤖” i jeden licznik w linii.
Warunek: tani odczyt, nic do decyzji inwestora. Nowy obszar Dziennika nie wymaga zmian tutaj – obsługuje go `wpisy`.

## Uruchomienie

Zaplanowane zadanie na claude.ai **poza projektem** (żeby nie doklejać plików projektu „Dom” do każdego przebiegu), codziennie
wieczorem, polecenie: „Przegląd dnia (skill przeglad-dnia z pluginu ja)”. Ręcznie w dowolnej rozmowie: „zrób przegląd dnia”.
