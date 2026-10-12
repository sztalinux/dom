---
name: koszty
description: Kosztorys, wydatki i oferty w Excelu inwestora (Kosztorys_stan_zero.xlsx – źródło prawdy dla liczb, prowadzone ręcznie). Używaj, gdy użytkownik załącza aktualny plik .xlsx, pyta „ile wydaliśmy”, „ile zostało”, „plan vs wydane”, prosi o analizę lub sprawdzenie kosztorysu, podaje wydatek/fakturę do dopisania, albo prosi o zmianę w arkuszu (nowa kolumna, formuła, poprawka).
---

# Koszty i kosztorys (Excel)

Excel prowadzi inwestor – to **jedyne źródło prawdy dla liczb**. Asystent:
- czyta i analizuje plik załączony w bieżącej rozmowie,
- zmienia go tylko na wyraźną prośbę i oddaje nową wersję pliku,
- nie trzyma własnej kopii danych (żadnych JSON-ów, generatorów, „zapamiętanych” kwot z poprzednich rozmów).

Układ arkuszy i kolumn: `references/arkusze.md`.

## Gdzie jest plik

- **Claude Code:** plik leży w folderze budowy (dwa poziomy nad repo); aktualną wersję wskazuje indeks dokumentów
  (`python3 tools/dokumenty.py lista`, wpis `40_Kosztorys-stan-zero.xlsx` w przewodniku). Nigdy nie kopiuj go do repo.
- **claude.ai w projekcie „Dom”:** Excela nie ma w wiedzy projektu (kopia szybko się starzeje) – poproś o załączenie
  aktualnego pliku; z przewodnika po dokumentach wiesz, które arkusze są potrzebne.
- **Czat / telefon / Cowork poza projektem:** plik załączony w bieżącej rozmowie.

## A. Pytanie o liczby („ile wydaliśmy”, „porównaj oferty”, „co przekracza plan”)

1. Potrzebny aktualny plik (patrz „Gdzie jest plik”). Jeśli go nie ma – poproś o załączenie (jedno zdanie). Nie odpowiadaj
   z pamięci ani z danych sprzed tygodni.
2. Odczytaj wartości z przeliczonego pliku (jeśli komórki formuł nie mają zapisanych wyników – przelicz kopię
   w LibreOffice, oryginału nie zmieniaj).
3. Odpowiedz w trzech warstwach: PLAN (Kosztorys/Etapy) | UMÓWIONE (Oferty „Wybrana”) | WYDANE (Wydatki „Zrealizowane”),
   plus zobowiązania (Wydatki „Planowane”) i 3 największe odchylenia z komentarzem.

## B. Dopisanie wydatku / oferty

1. Wyciągnij dane z wejścia (faktura, paragon, oferta): data, kwota, etap, typ, sposób płatności, opis.
   Niepewne przypisanie etapu → zaproponuj i zapytaj.
2. Domyślnie **podaj gotowe wiersze do wklejenia** (tabela w kolejności kolumn arkusza) – inwestor wpisuje sam.
3. Jeśli inwestor poprosi „dopisz do pliku” i plik jest załączony: dopisz wiersze w pierwszym wolnym wierszu
   zakresu wejściowego, zachowując formaty, listy wyboru i formuły; oddaj plik jako nową wersję
   (nazwa z datą, np. `Kosztorys_stan_zero_2026-10-12.xlsx`).

## C. Zmiana w arkuszu (formuła, kolumna, nowy arkusz)

1. Opisz zmianę i jej wpływ (które arkusze/formuły się zmienią) – przy większych zmianach poczekaj na „ok”.
2. Pracuj na kopii (openpyxl, bez utraty formuł, walidacji, formatowania warunkowego, nazw zdefiniowanych).
3. Przelicz w LibreOffice i sprawdź brak błędów (#REF!, #NAME?, #VALUE!, #DIV/0!, #N/A) w całym pliku.
4. Zachowaj zgodność z Arkuszami Google (SUMIFS, SUMPRODUCT, COUNTIFS, INDEX/MATCH, IFERROR; nowsze funkcje z `_xlfn.`).
5. Oddaj plik + krótka lista zmian (arkusz, zakres, co).
Jeśli dostępna jest procedura/skill do plików xlsx – użyj jej do technicznej części pracy.

## D. Płatności, transze, kredyt

1. Harmonogram płatności z umowy (zaliczka, transze po odbiorach, zatrzymanie – `oferta/references/umowa.md`) → arkusz
   **Płatności** (układ: `references/arkusze.md`); po odbiorze (`etap`, sekcja C) i fakturze → Status „Zapłacona” i wiersz
   Wydatków „Zrealizowane” z nr FV. Przed każdą transzą sprawdź, czy jest protokół odbioru – bez niego powiedz to wprost.
   Plik bez arkusza Płatności → zaproponuj go (inwestor dodaje sam) i do tego czasu używaj Wydatków „Planowane”.
2. Roboty dodatkowe (`dziennik`, sekcja B) → osobny wiersz Oferty i Wydatku, nigdy „w transzy”.
3. Kredyt: jeśli wypłata jest w transzach po etapach – na pytanie „co do banku” zestaw: etap, stan wg Excela (Realizacja),
   dokumenty (faktury, zdjęcia, wpisy kierownika), termin kontroli. Szczegóły wymagań banku są w umowie kredytowej
   (folder budowy) – nie zgaduj ich.
4. Na pytanie „ile potrzebuję w tym miesiącu”: suma Planowanych z datą w miesiącu + zamówienia z `zakupy` z terminem
   w miesiącu, osobno zobowiązania bez daty.

## Zasady

- Kwoty w wydatkach = tyle, ile zapłacono (zwykle brutto). Oferty = netto + VAT.
- Ceny rynkowe: z widełkami min–max i źródłem z datą; nie wymyślaj cen – wyszukaj.
- Nie zmieniaj ilości ani cen bez wskazania źródła (przedmiar, zestawienie stali, oferta).
- Wiedza o kosztach z filmów trafia do Informacji w Bazie wiedzy (procedura `wiedza`, Rodzaj „Koszt / cena”, „Wrażliwe na czas”),
  a do Excela tylko na prośbę inwestora.
