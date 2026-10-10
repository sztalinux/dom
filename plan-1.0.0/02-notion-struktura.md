# 02 – Notion: struktura (baza Dziennik, skrzynka, strona DOM, przewodnik)

Cel: Notion ma wszystko, czego wymagają procedury 1.0.0. ID baz: `plugins/dom-budowa/skills/budowa/references/zrodla.md`.
Zasada: najpierw pobierz (fetch) to, co zmieniasz; zmieniaj jedną sekcję na raz; po zmianie pobierz ponownie i sprawdź.

## A. Baza „Dziennik budowy”

- [ ] A1. Pobierz stronę DOM (`24af5982-09e7-806b-821a-e157ff33be42`) i bazy Notatnik budowy
      (`collection://7423414a-707b-415f-8751-c6ab7ebb6753`) oraz TASKS (2) (`collection://2a9f5982-09e7-81be-91e8-000b0e10a05e`) – potrzebujesz ich ID do relacji.
- [ ] A2. Utwórz bazę danych (narzędzie tworzenia bazy) jako podstronę strony DOM, tytuł **Dziennik budowy**, ikona 📓,
      z polami dokładnie wg tabeli w `plugins/dom-budowa/skills/dziennik/references/notion-dziennik.md`:
      Wpis (tytuł), Data (date), Etap (select: Projekt i formalności, Stan zero, SSO, Deweloperski, Wykończenie, Teren i ogród, Cała budowa),
      Krok (text), Kto (multi-select: Ekipa, Ja, Kierownik budowy, Geotechnik, Geodeta, Instalator, Dostawa, Inspektor / urząd),
      Ekipa – osób (number), Godziny własne (number), Pogoda (text), Zrobione (text), Dostawy (text), Problemy / usterki (text),
      Ustalenia z ekipą (text), Roboty dodatkowe (text), Zdjęcia (text), Przed zakryciem OK (checkbox),
      Powiązane (relation → Notatnik budowy, dwustronna), Zadania (relation → TASKS (2), dwustronna), Dodano (created_time).
      Jeśli narzędzie nie pozwala na relację dwustronną – zrób jednostronną i zanotuj to w podsumowaniu.
- [ ] A3. Pobierz nową bazę; zapisz jej `collection://…` (data source) i URL strony bazy.
- [ ] A4. Jeśli narzędzie pozwala tworzyć widoki: dodaj widok „📓 Ostatnie 14 dni” (sort Data malejąco, filtr Data w ciągu 14 dni)
      i „⚠️ Otwarte problemy” (filtr Problemy / usterki niepuste). Jeśli nie – pomiń i zanotuj.
- [ ] A5. W repo wpisz ID:
      - `plugins/dom-budowa/skills/dziennik/references/notion-dziennik.md`: zamień dwie pierwsze linie po tytule
        („Stan: **propozycja** …” do „…„obowiązuje”.”) na `Stan: obowiązuje od 1.0.0. Baza pod stroną DOM.`
        i w nagłówku bazy wstaw `collection://<ID>` zamiast `<do uzupełnienia>`.
      - `plugins/dom-budowa/skills/budowa/references/zrodla.md`: w wierszu „Dziennik inwestora” usuń „(**do utworzenia**, schemat: …)”
        i zostaw „Notion → DOM → Dziennik budowy (schemat: `dziennik/references/notion-dziennik.md`)”; w tabeli „Notion – identyfikatory”
        dodaj wiersz `| Dziennik budowy (data source) | \`collection://<ID>\` |`.
- [ ] A6. Wykonaj krok D1 z `01-harness.md`.
- [ ] A7. `python3 tools/build.py --tylko-walidacja` → OK.

## B. Skrzynka „Zmiany do harnessu” – nowe opcje

- [ ] B1. W bazie `collection://e217448a-60ec-4af6-8584-8f368315109c` dodaj do pola **Procedura** (select) opcje:
      `etap`, `dziennik`, `zakupy` (narzędzie aktualizacji schematu bazy; istniejące opcje zostają bez zmian).
- [ ] B2. Pobierz bazę i sprawdź, że pole ma 13 opcji.

## C. Strona DOM

- [ ] C1. Pobierz stronę DOM. Po toggle’u „✅ Zadania” (a przed „🗂 Strony i materiały”) dodaj toggle:
      `## 📓 Dziennik budowy` z tekstem kursywą `*Co się działo na budowie: dni ekipy i własne, dostawy, problemy, zdjęcia. Mów asystentowi po każdej wizycie.*`
      i osadzoną bazą Dziennik budowy (inline).
- [ ] C2. W toggle’u „📁 Dokumenty i linki” zamień trzy punkty („Kosztorys (Excel)…”, „Projekt techniczny…”, „Opinie geotechniczne…”) na:
      `- Oryginały: folder budowy na komputerze (indeks i paczka: \`tools/dokumenty.py\`, procedura \`dokumenty\`). Spis aktualnych wersji: \`00_SPIS.md\` w paczce.`
      `- Na telefonie / w czacie: projekt „Dom” na claude.ai → wiedza projektu (ściąga \`01_Sciaga-projektu.md\`, projekty, opinie, oferty, kosztorys).`
      `- Zdjęcia z budowy: folder budowy → \`Zdjęcia/RRRR-MM-DD_<krok>/\` (wpis w Dzienniku podaje folder).`
- [ ] C3. Pobierz stronę ponownie i sprawdź obie sekcje. Niczego innego na stronie DOM nie zmieniaj (sekcja „Do zamknięcia” – zadanie 03).

## D. Strona „Asystent AI – harness budowy” (`3f4f5982-09e7-81f5-b7f9-d6cf5d79bb34`)

Zmieniaj sekcję po sekcji (jedno wywołanie na sekcję), resztę strony zostaw.

- [ ] D1. **Ramka na górze (callout):** zamień dwa punkty na:
      `- Repozytorium: https://github.com/sztalinux/dom (publiczne; plugin \`dom-budowa\` w marketplace)`
      `- Wersja: **1.0.0** (<dzisiejsza data>) – pierwsza stabilna: 12 procedur, w tym etapy (bramki i odbiory), dziennik budowy, zakupy, umowa z wykonawcą.`
      W tekście ramki zamień „repo GitHub **dom-budowa-harness**” na „repo GitHub **sztalinux/dom**”.
- [ ] D2. **Sekcja 2 „Architektura”** – w punkcie o `tools/build.py` zamień „słowa z lokalnej listy \`dane/prywatne.txt\`” na
      „słowa z listy \`.dom/zakazane-w-repo.txt\` w folderze budowy (poza repo)”, a „Hook \`.githooks/pre-commit\` uruchamia ją przed każdym commitem.”
      na „Hooki \`.githooks/\` (pre-commit, commit-msg, pre-push) powtarzają kontrolę przy commicie i przed pushem.”
      Dodaj punkt: `- \`tools/dokumenty.py\` – indeks folderu budowy i paczka \`_Do claude.ai/\` dla projektu „Dom” (uruchamiany na starcie każdej sesji Claude Code).`
- [ ] D3. **Sekcja 3** – nagłówek na „3. Procedury (wersja 1.0.0)”. W tabeli zaktualizuj wiersze i dodaj nowe (kolumny: Procedura | Kiedy się włącza | Co robi | Gdzie zapisuje):
      - oferta → Co robi: dopisz „; „sam czy ekipa”; po wyborze – zakres do umowy (lista kontrolna umowy)”.
      - koszty → Co robi: dopisz „; płatności, transze po odbiorach, kredyt”.
      - analiza-techniczna → Kiedy: dopisz „, „jak to zrobić samemu””; Co robi: dopisz „; instrukcja pracy własnej (materiały, narzędzia, kroki, BHP)”.
      - wiedza → Kiedy: dopisz „; „co wiemy o…””; Co robi: dopisz „; odczyt stanu wiedzy z lukami”.
      - nowy: **dokumenty** | nowe pliki od projektanta/wykonawcy, „wgrałem”, „gdzie jest…” | klasyfikuje pliki w folderze budowy, buduje paczkę dla claude.ai, pilnuje aktualnych wersji | folder budowy, `_Do claude.ai/`
      - nowy: **etap** | „zaczynamy etap”, „jutro betonowanie – co sprawdzić”, „ekipa skończyła”, usterki | plan etapu (sam/ekipa, blokady, ludzie, pogoda), bramki „bez odwrotu” ze zdjęciami przed zakryciem, protokół odbioru; płatność dopiero po odbiorze | Notatnik, TASKS, strony bramek, dziennik
      - nowy: **dziennik** | „dziś na budowie…”, zdjęcia, godziny własne, „ekipa chce dopłatę” | wpis z dnia (kto, co, pogoda, dostawy, problemy, ustalenia, zdjęcia), roboty dodatkowe na piśmie przed wykonaniem | Dziennik budowy, wiersze do Excela, Notatnik, TASKS
      - nowy: **zakupy** | „co kupić na…”, „kiedy zamawiać”, oferta hurtowni, „przyjechała dostawa” | lista z kosztorysu + drobnica + zapas, terminy z wyprzedzeniem, zapytania i porównanie dostawców | wiersze do Excela, TASKS
- [ ] D4. **Sekcja 10** – zamień całą listę kroków na dwa punkty:
      `- Konfiguracja została wykonana (10.2026). Nowy komputer lub nowe konto: \`README.md\` w repo, sekcja „Start”.`
      `- Po każdej zmianie harnessu: Claude Code podbija wersję i robi push; claude.ai pobiera plugin sam („Sync automatically”).`
- [ ] D5. **Sekcja 11 „Kolejne procedury (pomysły)”** – zamień listę na:
      `- **harmonogram** – osobna procedura tylko jeśli po SSO plan etapu w \`etap\` + wyprzedzenia w \`zakupy\` nie wystarczą.`
      `- **Płatności** jako arkusz w Excelu (umowa, transza, warunek, termin, zapłacono) zamiast wierszy „Planowane”.`
      `- **Ewaluacje procedur** na 3–4 prawdziwych wejściach (oferta, dzień na budowie, bramka) po każdej większej zmianie.`
- [ ] D6. **Sekcja 12 „Decyzje i historia”** – dopisz na końcu:
      `- 10.2026: wersja 1.0.0 – harness obejmuje fazę wykonywania: etapy (bramki, odbiory), dziennik budowy, zakupy, umowa; VAT 8% liczony dla usługi z materiałem; „Pamiętać” w Notatniku ma status „Ustalone”.`
      `- 10.2026: jedna sesja Claude Code w repo naraz; commit tylko własnych plików.`
- [ ] D7. Pobierz stronę i sprawdź wszystkie sześć sekcji.

## E. Podsumowanie

- [ ] E1. Jedna linia do inwestora: „02 gotowe – Dziennik budowy: <link>, skrzynka +3 opcje, DOM i przewodnik zaktualizowane; ID wpisane w repo”.
