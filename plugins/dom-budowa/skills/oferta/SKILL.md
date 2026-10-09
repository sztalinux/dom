---
name: oferta
description: Przyjęcie, rozbicie i ocena oferty wykonawcy budowy (stan zero, SSO i kolejne). Używaj, gdy użytkownik wkleja ofertę, wycenę, PDF, zdjęcie kosztorysu, notatkę z rozmowy telefonicznej z ekipą, pyta „co sądzisz o tej ofercie”, „porównaj wykonawców”, „kogo wybrać”, „jakie pytania zadać wykonawcy”.
---

# Oferta wykonawcy

Cel: każda oferta trafia do danych w jednym formacie, z jawnym zakresem, brakami
i pytaniami – tak, żeby oferty dało się uczciwie porównać.

## Wejście

Tekst, PDF, zdjęcie, notatka z rozmowy (także ustna wycena). Jeśli nie wiadomo, kto
jest wykonawcą lub której fazy dotyczy oferta – zapytaj jednym pytaniem.

## Procedura

1. **Wczytaj stan:** arkusze Oferty i Wykonawcy z aktualnego Excela (jeśli nie załączono – poproś;
   bez pliku porównuj tylko z kartami w Notion „Porównanie wykonawców” i zaznacz to w odpowiedzi).
   Sprawdź, czy wykonawca już istnieje (porównuj nazwy bez wielkości liter i form prawnych).
2. **Rozbij ofertę na pozycje** w kolumnach arkusza Oferty (`koszty/references/arkusze.md`):
   - robocizna i materiał tej samej firmy = osobne wiersze (Materiał w cenie?: „Nie” / „Tylko materiał”),
   - kwoty netto + stawka VAT; jeśli podano tylko brutto – wpisz brutto i VAT 0%, zaznacz w Uwagach,
   - Obejmuje etapy = numery etapów z `references/etapy.md`, które pozycja pokrywa,
   - wycena ustna → Nr „ustnie RRRR-MM-DD”, Zgodna z projektem „Do sprawdzenia”.
   Niczego nie dopisuj od siebie do zakresu – jeśli czegoś nie ma w ofercie, to tego nie ma.
3. **Sprawdź zakres i zgodność** z `references/etapy.md` (lista etapów i punkty krytyczne projektu):
   - każdy etap: ✓ wyceniony / ◐ w pakiecie bez kwoty / ✗ brak,
   - niezgodności z projektem (np. murowane ściany piwnicy zamiast żelbetu W8) → Zgodna z projektem „Nie” i wyraźnie w podsumowaniu,
   - knock-out i czerwone flagi: Notion → „Wybór wykonawcy – stan zero”, sekcja Runda 1,
   - technologia wykonawcy sprzeczna z Bazą wiedzy lub rozstrzygnięciem SP → wpis w Rejestrze sprzeczności
     (Rodzaj „Źródło vs oferta wykonawcy”, procedura `wiedza`); rozstrzyga inwestor.
4. **Porównaj liczby:**
   - z planem (kosztorys – suma etapów objętych ofertą, ta sama warstwa: robocizna do robocizny),
   - z innymi ofertami na ten sam zakres; braki wyceń z kosztorysu, żeby porównanie było „jabłka do jabłek”,
   - nietypowo niskie/wysokie pozycje (±30% od planu lub mediany ofert) → oznacz do dopytania.
5. **Przygotuj pytania do wykonawcy** – tylko te, na które oferta nie odpowiada.
   Źródło pytań: Notion „Wybór wykonawcy – stan zero” (Rundy 1–3, Umowa). Maksymalnie 10, od najważniejszych.
6. **Zapisz:**
   - Excel: podaj gotowe wiersze do arkuszy Oferty (i Wykonawcy, jeśli nowa firma) do wklejenia;
     dopisz do pliku tylko na prośbę (procedura `koszty`, sekcja B),
   - Notion → baza „Porównanie wykonawców – stan zero”: utwórz/zaktualizuj kartę
     (pola i wartości: `notatka/references/notion-schematy.md`),
   - aktualizuj sekcję „Co już wiem z rozmów i ofert” na stronie „Wybór wykonawcy” jednym wpisem.
   Zapisy do Notion grupuj wg zasady 6 z `budowa`.

## Wynik w rozmowie

```
**<Wykonawca> – <zakres w 5 słowach>**: <netto> netto (<brutto> brutto), VAT <x>%
Zakres: ✓ 02 05 07 … | ◐ 03 | ✗ 04 10   Zgodność: Tak/Nie/Do sprawdzenia
vs plan: +/-X% (robocizna) | vs najtańsza porównywalna: +/-Y%
Ryzyka: …
Pytania do wykonawcy: 1. … 2. …
```

Potem tabela porównawcza wszystkich aktywnych ofert dla tej fazy (kolumny: wykonawca, zakres,
robocizna netto, materiał netto, braki doliczone z planu, razem porównywalne, zgodność, status).

## Czego nie robić

- Nie wybieraj wykonawcy za użytkownika – rekomenduj z uzasadnieniem wg kryteriów z wagami (Notion, sekcja „Kryteria i wagi oceny”).
- Nie zapisuj telefonów i e-maili nigdzie poza arkuszem Wykonawcy w Excelu.
- Nie zmieniaj statusu oferty na „Wybrana” bez wyraźnej decyzji użytkownika.
