# Schematy baz Notion (stan: 2026-10-09)

ID baz: `budowa/references/zrodla.md`. Jeśli zapis zwróci błąd pola – pobierz aktualny schemat
bazy (fetch data source) i zaktualizuj ten plik.

## Notatnik budowy – `collection://7423414a-707b-415f-8751-c6ab7ebb6753`

| Pole | Typ | Wartości |
|---|---|---|
| Name | tytuł | |
| Typ | select | Pamiętać, Pytanie, Decyzja, Ryzyko, Doczytać, Pomysł |
| Status | select | Otwarte, Do omówienia, Ustalone, Zrobione, Odrzucone |
| Priorytet | select | Krytyczne, Ważne, Zwykłe |
| Etap | select | Projekt i formalności, Stan zero, SSO, Deweloperski, Wykończenie, Teren i ogród, Cała budowa |
| Branża | multi-select | Konstrukcja, Grunt i woda, Hydroizolacja, Drenaż, Elektryka, Wod-kan, Ogrzewanie, Wentylacja, Dach, Okna i drzwi, Elewacja, Ściany, Wnętrza, Smart home, Ogród, Formalności, Energooszczędność, Organizacja |
| Do kogo | select | Konstruktor, Architekt, Geotechnik, Kierownik budowy, Ekipa, Instalator, Dekarz, Ja |
| Kiedy | data | termin lub moment budowy |
| Notatka | tekst | szczegóły, kontekst, co ustalono |
| Źródło | tekst | skąd to wiem |

## TASKS (2) – `collection://2a9f5982-09e7-81be-91e8-000b0e10a05e`

| Pole | Typ | Wartości |
|---|---|---|
| Name | tytuł | |
| PLANNED | status | TO DO, PLANNED, IN PROGRESS, WAITING, ON HOLD, BLOCKED, SOMEDAY, DONE, ARCHIVED |
| Priority | select | Highest, High, Medium, Low |
| Kategoria | select | Media, Kredyt, Czyszczenie działki, Stan zero, SSO, Ogrodzenie, Teren, Przygotowanie do budowy, Wiata kontener, Projektowanie, Zakup działki, Inne, Ogród |
| When | data | |
| Desc | tekst | |

## Porównanie wykonawców – stan zero – `collection://f7ca5f38-8fc3-46e7-8345-8a32cc8b5215`

| Pole | Typ | Wartości |
|---|---|---|
| Wykonawca | tytuł | nazwa jak w Excelu (arkusz Wykonawcy) |
| Status | select | Czekam na wycenę, Wycena ustna, Oferta pisemna, Finał – spotkanie, Wybrany, Odpada |
| Zakres | select | Pełny 01–13, Częściowy, Tylko część robocizny, ? |
| Zgodny z projektem | select | Tak, Nie, Do sprawdzenia |
| Ściany piwnicy | select | Żelbet monolit, TBW / bloczki szalunkowe, Murowane – niezgodne, ? |
| Przerwa robocza | select | Taśma/blacha, Wąż iniekcyjny, Taśma pęczniejąca, Brak / nie wie, ? |
| Fasety | select | Tak, Nie, ? |
| Ochrona izolacji | select | Kubełek, XPS + kubełek, Brak, ? |
| VAT | select | 8%, 23%, bez faktury, ? |
| Ocena technologia, Ocena ogólna | select | 1–5 |
| Knock-out OK | checkbox | żelbet zgodny z projektem, umowa + faktura, OC, termin |
| Robocizna netto, Materiał netto | liczba | (Razem netto = formuła, tylko odczyt) |
| Brakuje w zakresie, Do dopytania, Drenaż opaskowy, Hydroizolacja (system), Szalunki i sprzęt, Gwarancja, Płatności / zaliczka, Termin startu / czas, Referencje (piwnice), Wrażenie / uwagi | tekst | |
