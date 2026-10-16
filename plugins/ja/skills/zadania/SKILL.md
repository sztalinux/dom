---
name: zadania
description: Zadania inwestora poza budową (prywatne, dziecko, praca) we wspólnej bazie TASKS w Notion – nowe zadanie z terminem albo „kiedyś”, zmiana statusu po wpisie „zrobiłem X”, „zacząłem”, „czekam na”, „odpuszczam”, odczyt „co mam dziś / jutro / w tym tygodniu”. Używaj, gdy użytkownik mówi „muszę…”, „trzeba…”, „przypomnij mi…”, „kupić…”, „umówić…”, „zrobiłem…”, „zrobione”, „co mam jutro”, wkleja link do rzeczy do kupienia, albo gdy wpis z Dziennika ma obszar Zadanie, Status zadania lub Zakup. Zadania budowy prowadzą procedury notatka i harmonogram (plugin dom-budowa).
---

# Zadania (wszystkie obszary poza budową)

Jedna baza **TASKS** (`collection://2a9f5982-09e7-81be-91e8-000b0e10a05e`) dla domu i spraw prywatnych; obszar rozróżnia
pole **Obszar** (Dom / Prywatne / Dziecko / Praca; puste = Dom – stare wiersze). Zadania budowy i domu (Obszar = Dom)
tworzą procedury `notatka` i `harmonogram` z pluginu `dom-budowa` – tu ich nie dubluj; zmianę statusu („zrobiłem”) obsługujesz
dla wszystkich obszarów.

## A. Nowe zadanie

Najpierw ustal, czy to w ogóle zadanie. Nie zakładaj go w TASKS (także jako SOMEDAY), gdy wpis to – również w formie
„muszę przeczytać”, „trzeba obejrzeć”, „kupić X na prezent”:
- książka do przeczytania → Books, według obszaru „Książka do przeczytania” w bazie Obszary;
- film lub serial do obejrzenia → 🎬 Films, według obszaru „Film / serial do obejrzenia”;
- pomysł na prezent → strona dziecka „🎁 Prezenty” (`dziecko`) albo „💞 Relacja” → „🎁 Prezenty i niespodzianki”;
  prezent dla innej osoby → zapytaj, gdzie zapisać.
Zadanie załóż tylko przy terminie albo decyzji o zakupie („kupić prezent do 20.11”) – wtedy zadanie i pomysł na stronie osoby.
Bez tej kontroli takie wpisy lądowały w TASKS zamiast na listach i stronach osób.

1. Sprawdź duplikat: wyszukiwarka z parametrem bazy TASKS (1–2 słowa kluczowe), wśród niezakończonych.
   Jest → uzupełnij (termin, opis w treści), nie dubluj.
2. Pola:
   | Pole | Wartość |
   |---|---|
   | Name | krótko, bezokolicznik („Umówić stomatologa”) |
   | Obszar | Dziecko – gdy dotyczy dziecka; Praca – sprawy zawodowe; inaczej Prywatne. Budowa/działka/dom → nie tu, `budowa` |
   | When | termin z wpisu; „do piątku” licz od daty wpisu; brak terminu → puste |
   | PLANNED | z terminem lub „na dniach” → TO DO; „kiedyś”, link do produktu do sprawdzenia (nie film), zakup bez terminu → SOMEDAY |
   | Priority | domyślnie Medium; „pilne”, „koniecznie” → High; drobiazg / zakup bez terminu → Low |
   | Kategoria | Zakup / Zdrowie / Nauka / Inne |
   | Kto | Ja; ktoś inny ma coś zrobić → jego rola opisowo w Desc, Kto = Inny, PLANNED WAITING |
   | Desc | jedno zdanie (skąd, po co); linki, listy, szczegóły – w treści strony |
3. Termin względny bez daty wpisu (np. „w piątek” w wpisie bez @today) → pytanie, nie zgaduj.

## B. Status istniejącego zadania

| Inwestor pisze | PLANNED |
|---|---|
| „zrobiłem X”, „X zrobione”, „załatwione” | DONE |
| „zacząłem”, „w toku”, „robię” | IN PROGRESS |
| „czekam na … (od kogo)” | WAITING (+ kto w Desc albo Kto) |
| „przesuwam na …”, „w przyszłym tygodniu” | zostaje, When = nowy termin |
| „odpuszczam”, „nieaktualne” | ARCHIVED |

1. Szukaj we **wszystkich obszarach** wśród niezakończonych (wyszukiwarka z parametrem bazy TASKS – słowa z wpisu, potem porównanie treści i statusu).
2. Jedno trafienie → zmień status; w treści strony dopisz linię „<data>: <co się stało> (z Dziennika)”. Zadanie budowy
   (Obszar Dom/puste) z powiązanym krokiem Harmonogramu → status kroku zostaw procedurze `harmonogram` (przekaż jej sprawę).
3. Brak trafienia → Dziennik „❓”: „Nie znalazłem zadania »…« – utworzyć jako zrobione (ślad) czy pominąć?”.
4. Kilka trafień → „❓” z listą (nazwa, termin) do wyboru.

## C. Odczyt

„Co mam dziś / jutro / w tym tygodniu” → TASKS: widok „Today” (wszystkie obszary), „📅 Jutro – wszystko”, „🏠 Prywatne”
(prywatne, dziecko, praca), „🏗 ToDo/Doing – Dom” (budowa). Pokaż w tabeli: zadanie | obszar | termin | status; zadania po
terminie osobno na górze. SOMEDAY pokazuj tylko licznikiem, chyba że pyta o nie wprost.

## Zasady

- Porządek statusami, nie usuwaniem; zamykając, dopisz jednym zdaniem, jak się skończyło.
- Nie zakładaj zadań z rzeczy, które są tylko informacją albo emocją – to inne obszary.
- Zakup dla dziecka → Obszar Dziecko, Kategoria Zakup; pomysł na prezent bez terminu i decyzji o zakupie → strona osoby (sekcja A).
- Temat do przegadania z dzieckiem lub partnerką → strona osoby, zadanie tylko po świeżym zdarzeniu (`ja`, zasada 9).
