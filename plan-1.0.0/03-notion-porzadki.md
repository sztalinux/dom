# 03 – Notion: porządki i start Bazy wiedzy (STOP-punkty)

Cel: Notatnik pokazuje tylko to, co naprawdę otwarte; luźne punkty z pulpitu mają swoje wpisy; Baza wiedzy ma tematy,
w które od razu wpadnie wiedza o wykonaniu piwnicy. **Każdy zapis w tym zadaniu wymaga „tak” inwestora.**

## A. Notatnik: „Pamiętać” nie jest sprawą otwartą

- [ ] A1. Zapytanie do `collection://7423414a-707b-415f-8751-c6ab7ebb6753`: wiersze z Typ = „Pamiętać” i Status = „Otwarte”
      (SQL: `SELECT url, "Name", "Etap", "Priorytet" FROM … WHERE "Typ"='Pamiętać' AND "Status"='Otwarte'`). Policz.
- [ ] A2. ⛔ STOP – pokaż inwestorowi liczbę i 5 przykładowych nazw; zapytaj: „Zmienić Status na „Ustalone” we wszystkich N wpisach „Pamiętać / Otwarte”? (zasada z procedury `notatka` 1.0.0)”.
- [ ] A3. Po „tak”: zaktualizuj każdy wiersz (Status = „Ustalone”). Narzędzie aktualizuje jedną stronę na wywołanie – napisz wcześniej
      „Zapiszę: N aktualizacji statusu”. Nie zmieniaj innych pól.
- [ ] A4. Zapytanie kontrolne: ile zostało „Pamiętać / Otwarte” → ma być 0.

## B. Notatnik: wpisy bez adresata

- [ ] B1. Zapytanie: wiersze z pustym „Do kogo” (`WHERE "Do kogo" IS NULL OR "Do kogo"=''`). Dla każdego zaproponuj adresata
      na podstawie Nazwy i Branży (Konstruktor / Architekt / Geotechnik / Kierownik budowy / Ekipa / Instalator / Dekarz / Ja).
- [ ] B2. ⛔ STOP – tabela: Nazwa | Typ | proponowane „Do kogo”. Po „tak” zaktualizuj (jedna strona = jedno wywołanie).

## C. Pulpit DOM: luźne punkty w „🔴 Do zamknięcia przed stanem zero”

Na liście są punkty dopisane szybko z telefonu (małe litery, bez linku do Notatnika), np. o rodzaju stropu, zbrojeniu
rozproszonym, zasypce z cementem, poziomie drenażu, stropach prefabrykowanych a rozpór dachu, XPS na chudziaku, słupach tarasu.

- [ ] C1. Pobierz stronę DOM, wypisz punkty bez `mention-page` i bez odnośnika do Notatnika.
- [ ] C2. Dla każdego przygotuj wpis do Notatnika wg `notatka`: Nazwa krótka i samodzielna (np. „Rodzaj stropu nad piwnicą: monolit / prefabrykat – decyzja”),
      Typ (Pytanie lub Decyzja), Status „Otwarte”, Priorytet „Krytyczne”, Etap „Stan zero”, Branża, Do kogo (zwykle Konstruktor),
      Notatka = oryginalny tekst punktu, Źródło = „pulpit DOM, 10.2026”. Sprawdź duplikaty (2–3 słowa kluczowe) – jeśli wpis istnieje, użyj go.
- [ ] C3. ⛔ STOP – pokaż tabelę planu zapisu. Po „tak”: utwórz wpisy **jednym wywołaniem**, potem zamień tekst każdego punktu na
      liście na nową Nazwę + odnośnik do strony wpisu (jedno wywołanie na stronę DOM).

## D. Baza wiedzy: tematy startowe pod piwnicę

Inwestor zbiera teraz wiedzę o poprawnym wykonaniu stanu zero. Tematy muszą istnieć, zanim wpadnie pierwszy film.

- [ ] D1. Pobierz bazę Tematy (`collection://718422ca-ed6f-4269-a38f-4e508eff286c`) i wypisz istniejące tematy.
- [ ] D2. Z listy niżej wybierz te, których **nie ma** (także pod podobną nazwą – wtedy nie twórz):
      1. Roboty ziemne, grunt wysadzinowy i odwodnienie wykopu – Branża: Grunt i woda; Etap: Stan zero
      2. Kanalizacja podposadzkowa i przepusty przez płytę i ściany – Wod-kan, Hydroizolacja; Stan zero
      3. Chudziak, izolacja pod płytą i warstwy posadzki piwnicy – Hydroizolacja, Konstrukcja; Stan zero
      4. Uziom fundamentowy i odgrom – Elektryka; Stan zero
      5. Beton wodoszczelny: zamawianie, betonowanie, pielęgnacja, pogoda – Konstrukcja; Stan zero
      6. Zbrojenie, startery i przerwa robocza płyta–ściana – Konstrukcja, Hydroizolacja; Stan zero
      7. Hydroizolacja ścian piwnicy (systemy, fasety, przejścia, ściągi) – Hydroizolacja; Stan zero
      8. Ocieplenie piwnicy XPS i ochrona izolacji przy zasypce – Hydroizolacja, Energooszczędność; Stan zero
      9. Drenaż opaskowy i podpłytowy – Drenaż, Grunt i woda; Stan zero
      10. Zasypka i zagęszczanie – Grunt i woda; Stan zero
      11. Strop nad piwnicą i schody – Konstrukcja; Stan zero
      12. Wybór, umowa i rozliczanie wykonawcy – Organizacja; Cała budowa
      13. Odbiory, kierownik budowy i dokumentacja przed zakryciem – Organizacja, Formalności; Cała budowa
      Pola: Temat, W skrócie = „(jeszcze brak informacji)”, Stan wiedzy = „Do sprawdzenia”, Branża, Etap, Kluczowe dla (Konstruktor / Ekipa / Kierownik budowy – wg tematu).
- [ ] D3. ⛔ STOP – pokaż listę tematów do utworzenia. Po „tak”: utwórz **jednym wywołaniem**.

## E. Podsumowanie

- [ ] E1. Do inwestora: co zmieniono (liczby), które STOP-punkty nie dostały „tak”.
