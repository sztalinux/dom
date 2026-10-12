---
name: przeglad-tygodnia
description: Cotygodniowy przegląd budowy i porządki w Notion – co nowego doszło do wiedzy, otwarte sprzeczności czekające na decyzję, pytania do projektantów, zadania i terminy na najbliższe dni, informacje do ponownej weryfikacji. Używaj, gdy uruchamia go zaplanowane zadanie lub użytkownik pyta „co nowego”, „podsumuj tydzień”, „co czeka na mnie”, „przegląd”.
---

# Przegląd tygodnia

Cel: w 2 minuty inwestor wie, co doszło, co czeka na jego decyzję i co trzeba zrobić w tym tygodniu.
Przegląd czyta i podsumowuje – niczego nie rozstrzyga. Statusy zmienia tylko w ramach porządków zatwierdzonych
przez inwestora (sekcja „Porządki”). Kolejność i pierwszy plan wg zasady 12 w procedurze `budowa`:
najpierw bieżący etap i pilne terminy, sprawy zamknięte i odległe tylko licznikiem.

## Dane (ID: `budowa/references/zrodla.md`, `wiedza/references/notion-wiedza.md`)

Pobierz w jak najmniejszej liczbie zapytań:
1. **Rozmowy i źródła** dodane w ostatnich 7 dniach.
2. **Informacje**: Status „Nowe” (wszystkie) – pogrupuj po Tematach; pokazuj Kluczowe i Ważne, Ciekawostki tylko liczbą.
   Osobno: Informacje z „Moim komentarzem” zmienionym w 7 dniach – sprzeciw/wątpliwość → propozycja działania (`wiedza`, sekcja H).
3. **Rejestr sprzeczności**: Status „Czeka na decyzję” i „Do sprawdzenia u projektanta” (z datą zgłoszenia – najstarsze pierwsze).
4. **Notatnik budowy**: Status „Otwarte” lub „Do omówienia” z Priorytetem Krytyczne/Ważne; wpisy z „Kiedy” w ciągu 14 dni lub po terminie.
5. **TASKS (2)**: niezakończone z „When” w ciągu 7 dni lub po terminie; osobno **czekam na** (PLANNED „WAITING”, Kto ≠ Ja) – po terminie = „przypomnij się”.
5a. **Harmonogram** (`collection://d7a479ab-1e23-453f-8f59-55f4097f7d04`): kroki startujące / kończące się w 14 dni, kroki po terminie
    bez statusu „Zrobione”, kroki „Bez odwrotu” w 14 dni (czy jest zadanie bramki), terminy „Szacunek” na najbliższe 14 dni
    (do potwierdzenia u wykonawcy).
5b. **Zamówienia i dostawy**: „Zamówić do” w 14 dni lub po terminie bez statusu „Zamówione”; dostawy w 7 dni.
5c. **Umowy i gwarancje**: Gwarancja do / Rękojmia do w ciągu 60 dni (przegląd przed upływem, zgłoszenie usterek).
6. **Informacje**: „Wrażliwe na czas” z Datą informacji starszą niż 12 miesięcy, jeśli dotyczą bieżącego etapu.
7. **Zmiany do harnessu** (`collection://e217448a-60ec-4af6-8584-8f368315109c`): wpisy „Do wdrożenia” starsze niż 7 dni
   – przypomnienie, żeby uruchomić Claude Code i je wdrożyć. **Pomysły na rozwój** (`collection://fdee4f05-8f43-4be4-a0d5-2b88642fa6d3`): liczba nowych
   bez analizy (przeanalizuj je – `rozwoj-harnessu`, sekcja C) i „Pytania do mnie”; nie namawiaj do wdrażania.
8. **Dziennik budowy** (ID: `dziennik/references/notion-dziennik.md`): wpisy z 7 dni – dni pracy ekipy
   i własne, otwarte problemy, kroki zakryte bez zdjęć („Przed zakryciem OK” odznaczone).
9. **Inbox** (strona DOM → „📥 Inbox”): liczba wpisów do przetworzenia i tych z pytaniem „❓ asystent” bez odpowiedzi
   (wymień wpis i pytanie); „Przetworzone” starsze niż 14 dni → do wyczyszczenia (Porządki).
10. **Spójność** (inwestor edytuje Notion ręcznie – wychwyć rozjazdy, nie naprawiaj bez zgody):
    - Notatnik „Ustalone”/„Zrobione” z wiedzą techniczną bez relacji „Wiedza” → kandydaci do `wiedza`, sekcja F;
    - Informacje bez Tematów albo bez Źródeł i bez Notatnika; Tematy, których „W skrócie” przeczy nowszym Informacjom
      lub decyzjom; Informacje „Sporne” bez wpisu w Rejestrze;
    - checkboxy w „🔴 Do zamknięcia” odhaczone, a wpis w Notatniku nadal „Otwarte” (i odwrotnie);
    - Dziennik: problemy bez wpisu w Notatniku/TASKS; TASKS „DONE”, a powiązany wpis Notatnika otwarty.
11. **Zamówienia z wyprzedzeniem**: pozycje na najbliższe dwa etapy, których termin zamówienia (`zakupy/references/wyprzedzenia.md`)
   wypada w ciągu 14 dni; **płatności** – Wydatki „Planowane” z datą w 14 dni i transze po odbiorach, jeśli Excel jest
   dostępny w tym miejscu (inaczej napisz, że to wymaga aktualnego pliku).

## Wynik

```
## Przegląd budowy – tydzień <RRRR-Www> (<data>)
**Do decyzji (n):** SP-x <dylemat> – od <n> dni … (najstarsze/krytyczne pierwsze)
**Nowa wiedza (n z m źródeł; k kluczowych, c ciekawostek):** <Temat>: 1–2 najważniejsze punkty z WI-x; … (max 8 punktów)
**Twoje komentarze do wiedzy:** WI-x – <komentarz> → proponuję: …
**Dotyczy naszej budowy:** • …
**Pytania do projektantów (n):** Konstruktor: …; Architekt: …
**Harmonogram 14 dni:** <krok – od–do – kto>; **Bez odwrotu:** <krok – data – bramka gotowa?>
**Terminy 7 dni:** <zadanie – data>; **Po terminie:** …
**Czekam na:** <kto – co – termin> (po terminie: przypomnij się)
**Gwarancje (60 dni):** <umowa – do kiedy>
**Budowa w tym tygodniu:** dni ekipy / własne, problemy otwarte, braki zdjęć przed zakryciem
**Zamówić / zapłacić do 14 dni:** <pozycja – do kiedy – skąd>
**Do ponownej weryfikacji:** WI-x <cena/przepis z roku …>
**Inbox:** n do przetworzenia („przerób inbox”), m czeka na Twoją odpowiedź: <wpis> – <pytanie>
**Harness – czeka na wdrożenie:** HZ-x … (uruchom Claude Code)
**Pomysły:** n przeanalizowanych, m z pytaniami do Ciebie: POM-x – <pytanie>
**Sugestia na ten tydzień:** 1–3 konkretne kroki.
**Na później (n):** licznik spraw z dalszych etapów – bez listy.
**Porządki (n):** propozycje z sekcji „Porządki” – do zatwierdzenia jednym „tak”.
```

## Porządki (raz w tygodniu, max 10 pozycji)

Znajdź i zaproponuj – nie wykonuj bez zgody; po „tak” wykonaj wsadowo (zasada 6):
- duplikaty w Notatniku i TASKS (to samo zagadnienie dwa razy) → scal w starszy wpis;
- wpisy bez Etapu lub Priorytetu → uzupełnij;
- sprawy po terminie albo bez zmian od 30 dni → zamknąć, przesunąć termin czy zostawić (pytanie zbiorcze);
- Informacje „Nowe” starsze niż 30 dni → „Przejrzane” albo „Nieaktualne”;
- otwarte sprawy zakończonego etapu → przenieść do bieżącego albo zamknąć;
- „Przetworzone” w Inboxie starsze niż 14 dni → usunąć (linki są już w docelowych miejscach);
- rozjazdy z punktu „Spójność” → dopisać relację Wiedza / Informację (`wiedza`, F), uzgodnić statusy, poprawić „W skrócie”.
Niczego nie usuwaj – porządek tylko statusami i scalaniem (z dopiskiem, co scalono).

Zapis: dopisz przegląd na górze strony Notion „Przeglądy tygodniowe” (pod DOM) jako zwijany nagłówek
z tytułem tygodnia – **jedno wywołanie**. W rozmowie podaj ten sam tekst.
Pusty tydzień (brak nowych rzeczy i terminów) → krótka informacja „bez zmian”, bez zapisu do Notion.
