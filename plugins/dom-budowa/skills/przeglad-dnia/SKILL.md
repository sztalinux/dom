---
name: przeglad-dnia
description: Codzienny wieczorny przegląd bez inwestora (zaplanowane zadanie, np. 20:00 na claude.ai) – przerobienie Inboxu bez pytań w rozmowie, analiza nowych pomysłów na rozwój, krótka zapowiedź jutra; wynik jako linia „🤖” w Inboxie na stronie DOM (na górze „Przetworzone”). Używaj, gdy uruchamia go zaplanowane zadanie albo użytkownik mówi „przegląd dnia”, „wieczorny przegląd”, „ogarnij dzisiejsze”, „zrób codzienny przegląd”.
---

# Przegląd dnia

Cel: co wieczór, bez inwestora, porządek w tym, co wpadło w ciągu dnia – żeby rano zobaczył krótkie podsumowanie: co zrobione,
co czeka na niego, co jutro. Krótko i tanio: tylko to, co nowe od wczoraj. Szerokie podsumowania, wiedza „na teraz”
i porządki – w `przeglad-tygodnia`.

## Zasady trybu bez inwestora (wszystkie kroki)

- Nie ma kogo zapytać: niejasne → pytanie w Notion, tam gdzie inwestor je zobaczy (Inbox „❓”, strona pomysłu) – nie tylko w odpowiedzi.
- Nie zapisuj niczego, co jest decyzją inwestora, rozstrzygnięciem sprzeczności (SP), zmianą w Excelu ani zmianą terminów
  kroków Harmonogramu – zostaw to z pytaniem i propozycją.
- Bez planu do akceptacji; zapisy wsadowo (`budowa`, zasada 6); odczyt baz trybem rows/view, nie SQL (zasada 6 – limit).
- Błąd zapisu (brak uprawnień, limit) → nie ponawiaj w kółko; jeśli się da, odnotuj go w linii „🤖” („nie zapisano: …”) i zakończ.

## Kroki

1. **Inbox** – procedura `inbox`, kroki 1–6, z wyjątkami:
   - przetwarzaj tylko wpisy jednoznaczne ze źródłem; niejasne → do „❓ Czeka na Twoją odpowiedź” z pytaniem (krok 3);
   - wpis będący decyzją, rozstrzygnięciem SP albo zmianą w Excelu → do „❓” z pytaniem „potwierdź, że to decyzja: …”;
   - nowy termin kroku Harmonogramu → do „❓” z propozycją zmiany; zadania i „czekam na” (TASKS) zapisuj normalnie;
   - wpisy w „❓”, pod którymi inwestor odpowiedział – oceń ponownie (krok 1 `inbox`).
2. **Pomysły na rozwój** – `rozwoj-harnessu`, sekcja C: Status Nowy lub pusty → analiza (max 3 na wieczór, najstarsze
   pierwsze; reszta jutro); „Pytania do mnie” z odpowiedzią inwestora pod pytaniami → analizuj dalej. Niczego nie wdrażaj.
3. **Na jutro** (tylko odczyt): TASKS z When = jutro (moje i „czekam na”), kroki Harmonogramu startujące jutro (krok
   „bez odwrotu” → czy jest zadanie bramki), dostawy jutro, Zamówienia z „Zamówić do” = jutro lub po terminie.
   Nic nie ma → pomiń.
4. **Linia „🤖”** – w tej samej, jednej edycji strony DOM co krok 1: na górze „Przetworzone” zastąp poprzednią linię
   (z jej punktami) nową. Pierwszy poziom Inboxu zostaje pusty – gotowy na wpisy następnego dnia (`inbox`, krok 6):
   ```
   🤖 13.10 wieczór: inbox – przetworzono 3, czeka na Ciebie 2 (rozwiń ❓) · pomysły – przeanalizowano 1 · jutro: 2
   	- jutro: <sprawa – kto – kiedy>      ← max 3 punkty zagnieżdżone, tylko gdy są
   ```
   Pusty dzień → „🤖 13.10 wieczór: nic nowego”. Punkty pod linią „🤖” to nie wpisy Inboxu.
5. **Wpis w „📆 Przeglądy dzienne”** (strona w zakładce „Więcej” na DOM, `3f8f5982-09e7-815e-8b03-eacaa74db190`), gdy przebieg
   ma tam coś do dopisania (dziś / jutro, „rozkminka”, o którą inwestor prosi w Inboxie): zwijany nagłówek
   „Przegląd dnia – <dzień tygodnia> <data>” na górze strony (najnowszy pierwszy). **Ręczny przebieg** (inwestor prosi
   w rozmowie o przegląd albo o jego ponowne sprawdzenie) = **osobny wpis** z tą samą datą i dopiskiem „(ręczne)”,
   kolejne tego dnia „(ręczne 2)”, „(ręczne 3)”. Nigdy nie nadpisuj wcześniejszego wpisu – sprostowanie do starszego wpisu
   to jedna linia kursywą na jego górze z odesłaniem do nowego. Zakres treści wpisu i czas przechowywania – POM-7.
6. **Odpowiedź** (log zadania): treść linii „🤖” + lista zapisów (gdzie, link) i błędów.

## Rozszerzanie

Nowa rzecz codzienna (np. poranny brief, kontrola zdjęć, kopia zapasowa) = nowy krok przed „Linią 🤖” i jeden licznik
w linii. Warunek: tani odczyt, nic do decyzji inwestora; wszystko szersze – do `przeglad-tygodnia`.

## Uruchomienie

Zaplanowane zadanie na claude.ai (projekt „Dom”), codziennie wieczorem, polecenie: „Przegląd dnia (skill przeglad-dnia)”.
Ręcznie w dowolnej rozmowie: „zrób przegląd dnia”.
