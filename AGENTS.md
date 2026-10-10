# Asystent budowy domu – instrukcje startowe

Ten plik czyta każdy agent AI pracujący nad budową (Claude, Gemini, Codex i inne).
Jest celowo krótki: cała wiedza i procedury są w `plugins/dom-budowa/skills/`.

## Zanim cokolwiek zrobisz

1. Wczytaj `plugins/dom-budowa/skills/budowa/SKILL.md` – kontekst budowy, zasady pracy, mapa procedur.
2. Dobierz procedurę do zadania (tabela niżej) i wczytaj jej `SKILL.md`.
3. Pliki z `references/` czytaj dopiero wtedy, gdy procedura każe.
4. Sprawdź skrzynkę „Zmiany do harnessu” w Notion (opis: procedura `budowa`, sekcja „Na starcie”).

| Zadanie | Procedura |
|---|---|
| Oferta / wycena / rozmowa z wykonawcą | `plugins/dom-budowa/skills/oferta/SKILL.md` |
| Excel z kosztorysem, wydatek, faktura, budżet | `plugins/dom-budowa/skills/koszty/SKILL.md` |
| Notatka, ustalenie, decyzja, zadanie → Notion | `plugins/dom-budowa/skills/notatka/SKILL.md` |
| Projekt, rysunki, umowa, norma, pytanie techniczne | `plugins/dom-budowa/skills/analiza-techniczna/SKILL.md` |
| Transkrypcja filmu, artykuł, relacja z rozmowy, sprzeczności „SP-n” | `plugins/dom-budowa/skills/wiedza/SKILL.md` |
| Nowe pliki od projektanta/wykonawcy, paczka dokumentów dla claude.ai | `plugins/dom-budowa/skills/dokumenty/SKILL.md` |
| Start etapu, „co sprawdzić przed betonowaniem”, odbiór, usterki | `plugins/dom-budowa/skills/etap/SKILL.md` |
| Relacja z dnia na budowie, zdjęcia, godziny własne, roboty dodatkowe | `plugins/dom-budowa/skills/dziennik/SKILL.md` |
| Lista zakupów na etap, oferty hurtowni, kiedy zamawiać, dostawa | `plugins/dom-budowa/skills/zakupy/SKILL.md` |
| Przegląd tygodnia, „co nowego”, „co czeka na mnie” | `plugins/dom-budowa/skills/przeglad-tygodnia/SKILL.md` |
| Zmiana samego harnessu (nowa procedura, poprawka) | `plugins/dom-budowa/skills/rozwoj-harnessu/SKILL.md` |

## Zasady, które obowiązują zawsze

- Pisz po polsku, konkretnie; kwoty zawsze z dopiskiem netto/brutto.
- Fakt z projektu ≠ szacunek ≠ opinia – oznaczaj, co jest czym. Sprawy konstrukcyjne
  bez potwierdzenia w projekcie oznacz „do potwierdzenia z konstruktorem”.
- Zapisy do Notion grupuj tak, żeby inwestor zatwierdzał jak najmniej razy – ale nigdy kosztem
  jakości i kompletności (szczegóły: `plugins/dom-budowa/skills/budowa/SKILL.md`, zasada 6).
- **To repozytorium jest publiczne.** Nigdy nie zapisuj w nim danych osobowych ani danych projektu
  (nazwiska, firmy, adresy, działki, PESEL, konta, telefony, e-maile, kwoty, notatki) – te są w Notion,
  Excelu i folderze budowy.
- Gdy użytkownik poprawi Twój sposób pracy, zaproponuj zmianę w odpowiednim `SKILL.md`
  (procedura `rozwoj-harnessu`), żeby poprawka działała w kolejnych rozmowach.
