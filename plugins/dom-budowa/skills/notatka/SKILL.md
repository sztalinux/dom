---
name: notatka
description: Zapis notatek, ustaleń, decyzji, pytań, ryzyk i zadań budowy do Notion (Notatnik budowy, TASKS, Do zamknięcia). Używaj, gdy użytkownik dyktuje lub wkleja notatkę z budowy, rozmowy z projektantem/ekipą, mówi „zapisz”, „zanotuj”, „dodaj do Notion”, „przypomnij mi”, „ustaliliśmy że…”, „decyzja: …”, albo gdy inna procedura wygenerowała otwarte pytania lub decyzje.
---

# Notatka → Notion

Cel: żadna myśl nie zostaje jako luźny tekst. Każda trafia jako wiersz z typem, etapem,
branżą i adresatem, tak żeby dało się ją filtrować i zamknąć.

## Procedura

1. **Rozbij wejście na jednostki** – jedna myśl = jeden wiersz. Sklasyfikuj każdą:

   | Rodzaj | Gdzie | Typ / Status |
   |---|---|---|
   | pytanie do kogoś | Notatnik budowy | Typ „Pytanie”, Status „Otwarte”, Do kogo = adresat |
   | ustalenie / fakt / rzecz do przypilnowania na budowie | Notatnik budowy | Typ „Pamiętać”, Status „Ustalone” (to nie jest sprawa otwarta – wraca w checkliście etapu, procedura `etap`), Etap = kiedy ma wrócić |
   | decyzja | Notatnik budowy | Typ „Decyzja”, Status „Ustalone”; w Notatka: *co, dlaczego, alternatywy, kto zdecydował* |
   | ryzyko | Notatnik budowy | Typ „Ryzyko”, Priorytet wg wpływu |
   | do doczytania / pomysł | Notatnik budowy | Typ „Doczytać” / „Pomysł” |
   | konkretne działanie z terminem | TASKS (2) | PLANNED „TO DO”, When = termin |
   | relacja z dnia na budowie, dostawa, usterka, roboty dodatkowe | → procedura `dziennik` | stąd ustalenia i zadania wracają tu |
   | koszt / płatność | → procedura `koszty` | nie zapisuj kwot tylko w Notion |
   | oferta / wycena | → procedura `oferta` | |
   | rozmowa z projektantem/wykonawcą, film, artykuł – „kto co powiedział” | → procedura `wiedza` (Rozmowy i źródła, Informacje, Tematy) | stąd tylko działania do Notatnika |

2. **Sprawdź duplikaty:** wyszukaj w Notatniku 2–3 słowa kluczowe. Jeśli wpis istnieje –
   zaktualizuj go (status, dopisek z datą) zamiast tworzyć nowy.
3. **Pokaż plan zapisu** jako tabelę (Nazwa | Typ | Etap | Branża | Do kogo | Priorytet | Status).
   Przy 1–3 oczywistych wpisach zapisz od razu; przy więcej lub przy niepewnej klasyfikacji – poproś o „ok”.
4. **Zapisz jednym wywołaniem na bazę** (wiele stron w jednej operacji; zasada 6 z `budowa`), wartości pól dokładnie
   wg `references/notion-schematy.md`. Źródło = skąd to wiadomo (rozmowa z X dnia RRRR-MM-DD, PT KT.03, oferta Y).
5. **Krytyczne sprawy przed etapem** (blokują start etapu) dodaj też jako checkbox w sekcji
   „🔴 Do zamknięcia przed stanem zero” na stronie DOM – i odhacz, gdy zamknięte.
6. **Potwierdź:** lista utworzonych/zmienionych wpisów z linkami.

## Zasady

- Nazwa wiersza: krótka i samodzielna („Wysokość drzwi garażu 2,10 m – kolizja z belką”), bez „Notatka z…”.
- Daty jako daty Notion, nie tekst. Termin względny („za tydzień”) przelicz na datę.
- Nie zmieniaj ani nie usuwaj cudzych wpisów bez prośby; zamknięcie = Status „Zrobione”/„Odrzucone” + dopisek.
- Jeśli narzędzia Notion są niedostępne: przygotuj wpisy jako tabelę Markdown do wklejenia i powiedz o tym wprost.
