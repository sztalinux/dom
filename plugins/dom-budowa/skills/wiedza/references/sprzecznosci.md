# Rejestr sprzeczności – jak ADR

Każdy wpis SP to mini-ADR: kontekst → stanowiska → opcje → rekomendacja → **decyzja inwestora** → konsekwencje.
Asystent przygotowuje wszystko do decyzji, ale **nigdy nie wypełnia pola Decyzja sam**.

## Kiedy otworzyć wpis

- Nowe źródło mówi coś innego niż istniejąca wiedza **dla tych samych warunków** (Źródło vs źródło).
- Źródło podważa projekt techniczny (Źródło vs projekt) – priorytet zwykle „Krytyczne” lub „Ważne”.
- Źródło podważa naszą decyzję zapisaną w Notatniku/Rejestrze (Źródło vs nasza decyzja).
- Źródło podważa ofertę lub technologię wykonawcy (Źródło vs oferta wykonawcy).
- Brak sprzeczności, ale jest realny wybór z kompromisami, który trzeba podjąć (Dylemat bez sprzeczności).

Nie otwieraj wpisu dla różnic w szczegółach bez znaczenia praktycznego (np. 8 vs 10 cm zakładu, gdy obie wartości mieszczą się w wymaganiach) – zapisz wtedy obie wartości w Szczegółach wiedzy.

## Wypełnienie przy zgłoszeniu

| Pole | Treść |
|---|---|
| Dylemat | pytanie w jednym zdaniu („Taśma pęczniejąca wystarczy w przerwie roboczej przy gruncie spoistym?”) |
| Stanowisko A | dotychczasowe: treść + źródło (WI-x / ZRD-y / projekt KT.0x / decyzja z Notatnika) |
| Stanowisko B | nowe: treść + ZRD-y + fragment z minutą |
| Kontekst naszej budowy | dlaczego to ma znaczenie u nas, czego dotyczy w projekcie i ofertach |
| Opcje | 2–4 opcje z kosztem / ryzykiem / wpływem na harmonogram |
| Rekomendacja asystenta | wybór + uzasadnienie (wiarygodność źródeł, warunki, ryzyko błędu, koszt) |
| Pytanie do inwestora | jedno konkretne pytanie, na które da się odpowiedzieć krótko |
| Status | „Czeka na decyzję” |

## Rozstrzygnięcie – po odpowiedzi inwestora

1. Odpowiedź jasna? Jeśli nie – dopytaj jednym pytaniem.
2. „Zapytam konstruktora/architekta” → Status „Do sprawdzenia u projektanta” + wpis Typ „Pytanie” w Notatniku budowy (Do kogo = adresat). Koniec.
3. Decyzja → uzupełnij: Decyzja (co wybrano), Uzasadnienie (słowa inwestora + argumenty), Data decyzji, Status „Rozstrzygnięte”,
   Konsekwencje (co zmieniono i gdzie). Jeśli źródłem rozstrzygnięcia jest rozmowa (np. z konstruktorem) – dodaj ją do Rozmów i źródeł i podepnij.
4. Wiersze wiedzy: zwycięskie → „Przejrzane”; przegrane → „Nieaktualne” z dopiskiem w Szczegółach „odrzucone w SP-n”
   (jeśli przegrane jest poprawne w innych warunkach – zostaw „Przejrzane” i dopisz warunek).
5. Skutki: decyzja dotycząca naszej budowy → wpis Typ „Decyzja” w Notatniku; zmiana zakresu/kosztu → uwaga do Excela
   (procedura `koszty`); temat → aktualizacja „W skrócie” i sekcji „Sprzeczności i rozstrzygnięcia”.
6. Nowy argument przeciw wcześniejszej decyzji → nowy wpis SP ze Stanowiskiem A = stara decyzja (SP-n), a stary dostaje
   Status „Zastąpione” dopiero po nowej decyzji inwestora.
