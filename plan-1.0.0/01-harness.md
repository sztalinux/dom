# 01 – Poprawki w harnessie (tylko repo)

Cel: harness gotowy do 1.0.0 – bez „propozycji”, z zasadą jednej sesji, bezpiecznym commitem, trybem odczytu
Bazy wiedzy i README opisującym procedury. Po każdym kroku: `python3 tools/build.py --tylko-walidacja`.

## A. `CLAUDE.md` – jedna sesja, bezpieczny commit

- [ ] A1. Po punkcie 0 (hooki) dodaj nowy punkt – wklej dokładnie:

```
0a. **Jedna sesja Claude Code w tym repo naraz.** Przed startem: `ps -axo pid,command | grep "[c]laude"` –
    jeśli działa inna sesja w tym katalogu, zapytaj inwestora, zanim cokolwiek zmienisz. Commituj tylko pliki,
    które sam zmieniłeś w tej sesji (`git add <pliki>`, nie `git add -A`); obce zmiany w `git status` zostaw i zgłoś.
```

- [ ] A2. Sprawdź, że numeracja dalszych punktów (1–5) jest bez zmian.

## B. `rozwoj-harnessu/SKILL.md` – commit bez `-A`

- [ ] B1. W sekcji B, krok 6 zamień
      `6. \`git add -A && git commit -m "Harness <wersja>: HZ-… <skrót>" && git push\`.`
      na
      `6. \`git add <zmienione pliki> && git commit -m "Harness <wersja>: HZ-… <skrót>" && git push\` – tylko pliki z tej sesji; obce zmiany zgłoś.`

## C. `wiedza/SKILL.md` – tryb odczytu („co wiemy o…”)

Dziś procedura tylko zapisuje. Inwestor zbiera teraz wiedzę o wykonaniu piwnicy i będzie pytał „co wiemy o X”.

- [ ] C1. W `description` (frontmatter) po `albo odpowiada na sprzeczność („SP-3: …”)` dopisz:
      `, albo pyta „co wiemy o…”, „co mówi baza wiedzy o…”, „jakie mamy sprzeczności w temacie…”`.
      Sprawdź, że description ma mniej niż 1024 znaki (`python3 tools/build.py --tylko-walidacja`).
- [ ] C2. Przed sekcją `## B. Odpowiedź po przetworzeniu` NIE dodawaj nic. Na końcu pliku (po sekcji D) dodaj:

```
## E. Pytanie do bazy („co wiemy o drenażu?”)

1. Znajdź temat(y) w Tematach (nazwa i „W skrócie”); pobierz ich Informacje (Status ≠ Nieaktualne) i wpisy Rejestru
   (Status ≠ Zastąpione) – jednym zapytaniem na bazę. Dodaj decyzje z Notatnika (Typ „Decyzja”) o tej branży.
2. Odpowiedz w kolejności: **co obowiązuje u nas** (decyzje, rozstrzygnięcia SP, projekt – ze źródłem) → **stan wiedzy**
   (punkty z WI-x, liczby z warunkami; przy rozbieżnych warunkach podaj oba) → **otwarte sprzeczności** (SP-n, od kiedy czekają)
   → **luki** (czego baza nie wie – zaproponuj, kogo zapytać lub jakie źródło przerobić).
3. Nie dopisuj wiedzy z własnej pamięci do odpowiedzi jako „z bazy”. Własne uzupełnienie oznacz `[opinia]` i zaproponuj
   zapis dopiero po potwierdzeniu źródłem.
4. Nic nie zapisuj (tryb tylko do odczytu), chyba że inwestor poprosi o zanotowanie luki jako „Doczytać” (`notatka`).
```

- [ ] C3. Sprawdź długość pliku: `wc -l plugins/dom-budowa/skills/wiedza/SKILL.md` < 200.

## D. `przeglad-tygodnia/SKILL.md` – dziennik już istnieje (po zadaniu 02)

- [ ] D1. (Wykonaj po `02`.) W punkcie 8 usuń nawias „(gdy baza istnieje – `dziennik/references/notion-dziennik.md`)”
      i zostaw: `8. **Dziennik budowy** (ID: \`dziennik/references/notion-dziennik.md\`): wpisy z 7 dni – …`.

## E. `README.md` – procedury i struktura

- [ ] E1. W bloku „Struktura” po linii `plugins/dom-budowa/skills/        ← JEDYNE źródło procedur` nic nie zmieniaj,
      ale w opisie folderu budowy (góra bloku) dodaj linię po `_Do claude.ai/`:
      `  Zdjęcia/                        ← zdjęcia z budowy (RRRR-MM-DD_<krok>/), poza indeksem i paczką`
- [ ] E2. Po sekcji „## Jak to działa” (przed „## Start”) dodaj sekcję:

```
## Procedury

| Procedura | Kiedy | Co robi |
|---|---|---|
| `budowa` | każda rozmowa o budowie | kontekst, zasady, mapa procedur, skrzynka zmian |
| `oferta` | oferta / wycena / rozmowa z ekipą | rozbicie, zakres 01–13, zgodność z projektem, porównanie, pytania; „sam czy ekipa”; zakres do umowy |
| `koszty` | Excel, wydatek, faktura, „ile wydaliśmy” | plan / umówione / wydane, wiersze do wklejenia, płatności i transze |
| `notatka` | „zapisz”, „ustaliliśmy”, „decyzja” | Notatnik budowy, TASKS, „Do zamknięcia” |
| `analiza-techniczna` | projekt, rysunek, umowa, pytanie techniczne, „jak to zrobić samemu” | [projekt]/[szacunek]/[opinia], pytania do projektanta, instrukcja pracy własnej |
| `wiedza` | transkrypcja, artykuł, „dzwoniłem do…”, „SP-n: …”, „co wiemy o…” | Baza wiedzy, sprzeczności (ADR), odczyt stanu wiedzy |
| `dokumenty` | nowe pliki, „wgrałem”, „gdzie jest…” | folder budowy, indeks, paczka dla claude.ai |
| `etap` | „zaczynamy etap”, „jutro betonowanie”, odbiór, usterki | plan etapu, bramki „bez odwrotu”, protokół odbioru |
| `dziennik` | „dziś na budowie…”, zdjęcia, godziny własne, roboty dodatkowe | Dziennik budowy w Notion, przekazanie kosztów/zadań |
| `zakupy` | „co kupić na…”, „kiedy zamawiać”, oferta hurtowni, dostawa | lista z kosztorysu, wyprzedzenia, porównanie dostawców |
| `przeglad-tygodnia` | poniedziałek / „co nowego” | decyzje, nowa wiedza, terminy, budowa, zamówienia, porządki |
| `rozwoj-harnessu` | „zapamiętaj na przyszłość”, nowa procedura | skrzynka w Notion → wdrożenie do repo |
```

- [ ] E3. W sekcji „## Na co dzień” dodaj dwa punkty na końcu:
      `- Dzień na budowie → powiedz asystentowi, co się działo (telefon wystarczy) – trafi do Dziennika budowy; zdjęcia wrzuć do \`Dom/Zdjęcia/RRRR-MM-DD_<krok>/\`.`
      `- Przed krokiem „bez odwrotu” (beton, zasypka, tynki) zapytaj „co sprawdzić przed …” – dostaniesz bramkę z listą zdjęć do zrobienia.`

## F. Porządek w tekstach „propozycja”

- [ ] F1. `plugins/dom-budowa/skills/dziennik/references/notion-dziennik.md` – nagłówek i ID uzupełnisz w `02`. Teraz nic.
- [ ] F2. `grep -rn "PROPOZYCJA\|do utworzenia\|do uzupełnienia" plugins/ CHANGELOG.md AGENTS.md README.md` – zapisz listę miejsc;
      wszystkie znikną w `02` (ID bazy) i `04` (CHANGELOG). Jeśli po `04` coś zostanie – popraw.

## G. Walidacja

- [ ] G1. `python3 tools/build.py --tylko-walidacja` → OK. `git diff --stat` – tylko pliki z tego zadania.
- [ ] G2. Nie commituj jeszcze (commit zbiorczy w `04`). Jedna linia do inwestora: „01 gotowe – zmienione: CLAUDE.md, rozwoj-harnessu, wiedza, README”.
