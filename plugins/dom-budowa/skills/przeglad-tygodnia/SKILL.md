---
name: przeglad-tygodnia
description: Cotygodniowy przegląd budowy – co nowego doszło do wiedzy, otwarte sprzeczności czekające na decyzję, pytania do projektantów, zadania i terminy na najbliższe dni, informacje do ponownej weryfikacji. Używaj, gdy uruchamia go zaplanowane zadanie lub użytkownik pyta „co nowego”, „podsumuj tydzień”, „co czeka na mnie”, „przegląd”.
---

# Przegląd tygodnia

Cel: w 2 minuty inwestor wie, co doszło, co czeka na jego decyzję i co trzeba zrobić w tym tygodniu.
Przegląd tylko czyta i podsumowuje – niczego nie rozstrzyga i nie zmienia statusów.

## Dane (ID: `budowa/references/zrodla.md`, `wiedza/references/notion-wiedza.md`)

Pobierz w jak najmniejszej liczbie zapytań:
1. **Rozmowy i źródła** dodane w ostatnich 7 dniach.
2. **Informacje**: Status „Nowe” (wszystkie) – pogrupuj po Tematach; osobno „Dotyczy nas = Tak”.
3. **Rejestr sprzeczności**: Status „Czeka na decyzję” i „Do sprawdzenia u projektanta” (z datą zgłoszenia – najstarsze pierwsze).
4. **Notatnik budowy**: Status „Otwarte” lub „Do omówienia” z Priorytetem Krytyczne/Ważne; wpisy z „Kiedy” w ciągu 14 dni lub po terminie.
5. **TASKS (2)**: niezakończone z „When” w ciągu 7 dni lub po terminie.
7. **Zmiany do harnessu** (`collection://e217448a-60ec-4af6-8584-8f368315109c`): wpisy „Do wdrożenia” starsze niż 7 dni
   – przypomnienie, żeby uruchomić Claude Code i je wdrożyć.
6. **Informacje**: „Wrażliwe na czas” z Datą informacji starszą niż 12 miesięcy, jeśli dotyczą bieżącego etapu.

## Wynik

```
## Przegląd budowy – tydzień <RRRR-Www> (<data>)
**Do decyzji (n):** SP-x <dylemat> – od <n> dni … (najstarsze/krytyczne pierwsze)
**Nowa wiedza (n z m źródeł):** <Temat>: 1–2 najważniejsze punkty z WI-x; … (max 8 punktów)
**Dotyczy naszej budowy:** • …
**Pytania do projektantów (n):** Konstruktor: …; Architekt: …
**Terminy 7 dni:** <zadanie – data>; **Po terminie:** …
**Do ponownej weryfikacji:** WI-x <cena/przepis z roku …>
**Harness – czeka na wdrożenie:** HZ-x … (uruchom Claude Code)
**Sugestia na ten tydzień:** 1–3 konkretne kroki.
```

Zapis: dopisz przegląd na górze strony Notion „Przeglądy tygodniowe” (pod DOM) jako zwijany nagłówek
z tytułem tygodnia – **jedno wywołanie**. W rozmowie podaj ten sam tekst.
Pusty tydzień (brak nowych rzeczy i terminów) → krótka informacja „bez zmian”, bez zapisu do Notion.
