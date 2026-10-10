# Dziennik budowy w Notion – proponowany schemat (do utworzenia pod stroną DOM)

Stan: **propozycja** – baza jeszcze nie istnieje. Po utworzeniu wpisz jej `collection://` tutaj
i w `budowa/references/zrodla.md`, a status tego pliku zmień na „obowiązuje”.

## Baza „Dziennik budowy” – `collection://<do uzupełnienia>`

| Pole | Typ | Wartości / uwagi |
|---|---|---|
| Wpis | tytuł | `RRRR-MM-DD – <etap> – <krok w 3 słowach>` |
| Data | data | dzień na budowie |
| Etap | select | jak w Notatniku: Projekt i formalności, Stan zero, SSO, Deweloperski, Wykończenie, Teren i ogród, Cała budowa |
| Krok | tekst | np. „zbrojenie ścian piwnicy”, „murowanie parteru – ściana wschodnia” |
| Kto | multi-select | Ekipa, Ja, Kierownik budowy, Geotechnik, Geodeta, Instalator, Dostawa, Inspektor / urząd |
| Ekipa – osób | liczba | |
| Godziny własne | liczba | praca inwestora tego dnia |
| Pogoda | tekst | temperatura, opady, wiatr – ważne przy betonie, murowaniu, zasypce |
| Zrobione | tekst | konkretnie, z miejscem (oś, ściana, kondygnacja) |
| Dostawy | tekst | co, ile, od kogo, nr WZ; kwoty idą do Excela |
| Problemy / usterki | tekst | co, gdzie, zdjęcie, ustalona reakcja |
| Ustalenia z ekipą | tekst | kto, co, do kiedy – jeśli trwałe → Notatnik |
| Roboty dodatkowe | tekst | co, cena netto/brutto, czy uzgodnione na piśmie |
| Zdjęcia | tekst | ścieżka folderu `Zdjęcia/RRRR-MM-DD_<krok>/` + lista ujęć |
| Przed zakryciem OK | checkbox | zdjęcia z miarą zrobione dla elementów, które ten krok zakrywa |
| Powiązane | relacja → Notatnik budowy | wpisy, które powstały z tego dnia |
| Zadania | relacja → TASKS (2) | usterki / rzeczy do zrobienia |
| Dodano | czas utworzenia | auto |

## Widoki na stronie DOM

- „📓 Ostatnie 14 dni” (sortowanie po Dacie malejąco) – do przeglądu tygodnia.
- „⚠️ Otwarte problemy” (Problemy niepuste, powiązane zadania nie DONE).
- „🧮 Godziny własne” – suma per Etap (do porównania „sam vs ekipa”).

## Plan zapisu (minimum zatwierdzeń)

1. Dziennik – jedno wywołanie (wpis z relacjami ustawianymi od strony dziennika).
2. Notatnik – jedno wywołanie ze wszystkimi ustaleniami/pytaniami/ryzykami dnia.
3. TASKS – jedno wywołanie z usterkami i terminami.
Kwoty: wiersze do Excela w odpowiedzi (`koszty`, sekcja B) – inwestor wkleja.
