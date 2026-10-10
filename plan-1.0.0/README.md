# Plan wdrożenia harnessu 1.0.0 – instrukcja dla agenta

Ten folder to **jednorazowy plan**. Wykonujesz go w Claude Code w katalogu repo, w kolejności plików
`00` → `05`. Po zakończeniu zadania `04` folder `plan-1.0.0/` jest usuwany (nie jest częścią harnessu).

## Zanim zaczniesz

1. Przeczytaj `CLAUDE.md`, `AGENTS.md` i `plugins/dom-budowa/skills/budowa/SKILL.md` (zasady 6, 9, 10).
2. Przeczytaj `plugins/dom-budowa/skills/rozwoj-harnessu/SKILL.md` (sekcja B – wdrożenie) i
   `plugins/dom-budowa/skills/rozwoj-harnessu/references/pisanie-procedur.md`.
3. Upewnij się, że działa Notion (`/mcp` → „claude.ai Notion”). Bez Notion wykonaj tylko zadania 00, 01, 04 (część repo)
   i powiedz inwestorowi, które zostały.

## Zasady wykonywania

- **Jedno zadanie naraz.** Otwórz plik zadania, wykonaj kroki po kolei, odhaczaj `- [x]` w pliku w miarę postępu.
  Przerwana sesja = następna zaczyna od pierwszego nieodhaczonego kroku.
- **Nie wymyślaj.** Każdy tekst do wpisania jest podany w zadaniu. Gdy czegoś brakuje albo coś jest niejasne –
  zatrzymaj się i zapytaj inwestora jednym konkretnym pytaniem. Nie zgaduj ID baz, nazw pól ani treści.
- **STOP-punkty** (oznaczone `⛔ STOP`) wymagają wyraźnego „tak” inwestora w rozmowie. Bez „tak” nie wykonuj kroku –
  przejdź do następnego zadania, a STOP zostaw nieodhaczony i wymień go w podsumowaniu.
- **Repo jest publiczne.** W żadnym pliku repo nie mogą się znaleźć nazwiska, firmy, adresy, działki, telefony, e-maile,
  kwoty, treści notatek. Do Notion wolno zapisywać wszystko. Przed commitem przejrzyj `git diff`.
- **Notion – zapisy wsadowe** (zasada 6 w `budowa`): najpierw wszystkie odczyty, potem zapisy; wiele wierszy do jednej bazy
  = jedno wywołanie. Przed serią zapisów napisz: „Zapiszę: 1) … 2) … – N zatwierdzeń”.
- **Weryfikuj po każdej zmianie w Notion**: pobierz stronę/bazę ponownie i sprawdź, że wygląda jak w zadaniu.
- **Weryfikuj po każdej zmianie w repo**: `python3 tools/build.py --tylko-walidacja` musi kończyć się „Walidacja OK”.
- Nie usuwaj niczego w Notion. Porządek robisz statusami i scalaniem.
- Pisz po polsku. Odpowiedzi krótkie: co zrobiłeś, co czeka na „tak”, co dalej.

## Kolejność i czas

| Plik | Co | Notion? | Szacunek |
|---|---|---|---|
| `00-przygotowanie.md` | stan repo, scalenie gałęzi, walidacja | nie | 10 min |
| `01-harness.md` | poprawki w procedurach, CLAUDE.md, README | nie | 30–45 min |
| `02-notion-struktura.md` | baza „Dziennik budowy”, opcje skrzynki, strona DOM, strona przewodnika | tak | 45–60 min |
| `03-notion-porzadki.md` | Notatnik (statusy, luźne punkty), tematy startowe w Bazie wiedzy | tak, STOP-punkty | 30–60 min |
| `04-wersja-1.0.0.md` | wersja, CHANGELOG, build, commit, push, usunięcie planu | nie (+1 strona) | 15 min |
| `05-testy-i-checklista.md` | testy procedur na sucho + lista dla inwestora (claude.ai, paczka, zadanie tygodniowe) | częściowo | 30 min |

## Definicja ukończenia

- `main` = wersja 1.0.0, `python3 tools/build.py` przechodzi, push zrobiony, folder `plan-1.0.0/` usunięty.
- W Notion: baza „Dziennik budowy” istnieje i jej ID jest w `budowa/references/zrodla.md` oraz
  `dziennik/references/notion-dziennik.md`; skrzynka ma opcje `etap`, `dziennik`, `zakupy`; strona przewodnika mówi „1.0.0”.
- Podsumowanie dla inwestora: lista wykonanych zadań, lista STOP-punktów bez „tak”, lista rzeczy z `05` do zrobienia ręcznie.
