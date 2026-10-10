# 05 – Testy na sucho i lista dla inwestora

## A. Testy procedur na sucho (agent, bez zapisów do Notion/Excela)

Dla każdego scenariusza: wczytaj procedurę, wykonaj ją na podanym wejściu **bez zapisywania** (napisz „tryb testowy –
nie zapisuję”), sprawdź, czy wynik ma format z sekcji „Wynik w rozmowie” procedury, i zanotuj braki (co w procedurze
było niejasne albo czego brakowało). Wejścia są zmyślone.

- [ ] A1. `etap`, bramka: „W czwartek ekipa betonuje płytę fundamentową. Co muszę sprawdzić przed?”
      Oczekiwane: lista z Notion (bramka 3), punkty z Notatnika (Etap Stan zero, Krytyczne), kontrole z `odbiory.md`, zdjęcia przed zakryciem, kto obecny, zdanie „nie betonować dopóki…”, jeśli coś krytyczne otwarte.
- [ ] A2. `dziennik`: „Dziś byłem na budowie 4 h, ekipa 3 osoby kończyła zbrojenie ścian osi A–B, 12 °C bez deszczu, przyjechała stal 2 t (WZ jest), ekipa mówi, że za dodatkowy przepust chcą 350 zł netto, nie było jeszcze kierownika.”
      Oczekiwane: pola wpisu, roboty dodatkowe → sekcja B (cena na piśmie przed wykonaniem, propozycja SMS-a), wiersz do Excela (stal – kwota `?`), zadanie „odbiór zbrojenia przez kierownika przed betonowaniem”, pytanie o zdjęcia.
- [ ] A3. `zakupy`: „Co muszę kupić na ściany nośne parteru, które robię sam? Excel załączam.” (bez pliku – procedura ma poprosić o plik i pokazać, co policzy po jego otrzymaniu).
- [ ] A4. `oferta`, „Sam czy ekipa”: „Ekipa chce 18 000 zł brutto za ściany działowe z materiałem; sam kupiłbym materiał za 9 000 zł brutto i zrobił w 8 dni. Co wybrać?”
      Oczekiwane: zestawienie brutto do brutto (8 % vs 23 % już w kwotach), sprzęt, czas, ryzyko, brak gwarancji; bez decyzji za inwestora.
- [ ] A5. `wiedza`, tryb E: „Co wiemy o przerwie roboczej płyta–ściana?” Oczekiwane: odczyt Tematów/Informacji/Rejestru (po 03 prawdopodobnie pusto) → sekcja „luki” z propozycją, kogo zapytać.
- [ ] A6. `analiza-techniczna`, praca własna: „Jak ułożyć izolację poziomą pod pierwszą warstwą bloczków?”
      Oczekiwane: warunki wstępne, materiały z ilościami (`[szacunek]`), narzędzia, kroki z kontrolą, błędy, BHP, kiedy zapytać.
- [ ] A7. Braki z A1–A6 zapisz jako wpisy w skrzynce „Zmiany do harnessu” (Status „Do wdrożenia”, Procedura, Rodzaj „Poprawka”, Treść do wdrożenia, Dlaczego) – **jednym wywołaniem**, po pokazaniu listy inwestorowi (⛔ STOP). Wdrożenie: następna sesja (1.0.1).

## B. Lista dla inwestora (ręcznie, poza Claude Code)

Przekaż ją inwestorowi na końcu jako checklistę:

- [ ] B1. claude.ai → Customize → Plugins → `dom-budowa` pokazuje wersję **1.0.0** (synchronizacja po pushu; jeśli nie – wyłącz/włącz „Sync automatically”).
- [ ] B2. Paczka dokumentów: wgraj zawartość `Dom/_Do claude.ai/` do projektu „Dom” na claude.ai (lista z raportu `[dokumenty]`), potem w Claude Code powiedz „wgrałem” (uruchomi `python3 tools/dokumenty.py wgrane`).
- [ ] B3. Plik wyceny okien powyżej 30 MB: zapisz zmniejszoną kopię PDF obok oryginału (Podgląd → Eksportuj → Filtr kwarcowy „Zmniejsz rozmiar pliku”), wrzuć do `_Przychodzące/`, Claude Code ją sklasyfikuje do paczki zamiast oryginału.
- [ ] B4. Utwórz folder `Dom/Zdjęcia/` (zdjęcia z budowy: `RRRR-MM-DD_<krok>/`).
- [ ] B5. Porządek w korzeniu folderu budowy: duplikat kosztorysu „(1)”, archiwum `.zip`, luźne PDF-y – przenieś do folderów tematycznych lub do `_Przychodzące/` (skrypt sam nie przenosi plików poza `_Przychodzące/`).
- [ ] B6. Zadanie zaplanowane na claude.ai (poniedziałek 7:00), treść:
      „Wykonaj procedurę `przeglad-tygodnia` z pluginu dom-budowa: pobierz dane z Notion wg procedury, zapisz przegląd na górze strony „Przeglądy tygodniowe” i podaj go w odpowiedzi. Bez Excela sekcję płatności oznacz „wymaga pliku”.”
      Po pierwszym uruchomieniu sprawdź stronę „Przeglądy tygodniowe”.
- [ ] B7. Test z telefonu (claude.ai): „jutro ekipa betonuje chudziak – co sprawdzić?” → powinna zadziałać `etap`; „dziś na budowie: …” → `dziennik` (pierwszy prawdziwy wpis).
- [ ] B8. Pierwszy film o hydroizolacji piwnicy → `wiedza`; zmierz czas i liczbę zatwierdzeń. Jeśli ponad 30 minut – zgłoś do skrzynki „uprościć `wiedza`”.
- [ ] B9. Umowa ze stanem zero: przed podpisaniem wklej projekt umowy → `analiza-techniczna` (sekcja Umowy) + `oferta/references/umowa.md`.
