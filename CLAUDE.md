@AGENTS.md

## Claude Code w tym repozytorium – obowiązkowo na starcie każdej sesji

To repozytorium jest źródłem harnessu. Procedury czytasz z `plugins/dom-budowa/skills/` (dowiązanie `.claude/skills`),
a nie z pluginu zainstalowanego na koncie (ten jest tu celowo wyłączony w `.claude/settings.json`).

Zanim zajmiesz się czymkolwiek innym:

0. Jednorazowo (jeśli `git config core.hooksPath` nie zwraca `.githooks`): `git config core.hooksPath .githooks`
   – włącza hooki prywatności: `pre-commit` (pliki + autor), `commit-msg` (wiadomość), `pre-push` (każdy wysyłany commit).
   Autor commitów: imię inwestora albo login – dozwolone; e-mail tylko `…@users.noreply.github.com` (historia jest publiczna).
   W historii nigdy nie mogą się znaleźć dane innych osób (projektanci, wykonawcy, urzędy) – raz wypchniętych
   nie da się skutecznie usunąć, więc kontrola musi zadziałać przed pushem. Nie przepisuj opublikowanej historii
   (force push zostawia stare commity dostępne po SHA) – chyba że wyciekły dane; wtedy zatrzymaj się i zapytaj inwestora.
1. `git pull` – żeby pracować na aktualnej wersji.
2. Sprawdź skrzynkę **„Zmiany do harnessu”** w Notion (`collection://e217448a-60ec-4af6-8584-8f368315109c`),
   wpisy ze Statusem „Do wdrożenia”.
3. Jeśli są – wdroż je od razu wg `plugins/dom-budowa/skills/rozwoj-harnessu/SKILL.md`, sekcja „Wdrożenie”
   (zmiana plików → wersja → CHANGELOG → `python3 tools/build.py` → commit → push → oznaczenie wpisów jako „Wdrożone”).
   Jeśli wpis jest niejasny albo sprzeczny z inną procedurą – zapytaj inwestora, zanim go wdrożysz.
4. Jeśli skrzynka jest pusta – napisz jedną linię „Harness aktualny (wersja X.Y.Z)”.
5. Raport „[dokumenty]” z hooka startowego (`tools/dokumenty.py`): jeśli są nowe pliki do sklasyfikowania –
   zaproponuj ich obsługę wg `plugins/dom-budowa/skills/dokumenty/SKILL.md` (jedna linia); jeśli jest lista
   „Do wgrania” – przypomnij o niej jedną linią. Potem przejdź do zadania.

**Repo jest publiczne** – przed każdym commitem sprawdź, że nie ma w nim danych osobowych ani danych projektu
(walidator i hook `pre-commit` pomagają, ale nie zastępują przejrzenia `git diff`).

Nie pomijaj tego kroku, nawet gdy pierwsza wiadomość dotyczy czegoś innego – wykonaj go najpierw, krótko.
