# 00 – Przygotowanie repo

Cel: `main` zawiera szkice z gałęzi `przeglad-2026-10`, walidacja przechodzi, pracujesz w jednej sesji.

- [ ] 1. Sprawdź, że nie działa inna sesja Claude Code w tym repo: `ps -axo pid,etime,command | grep "[c]laude"`.
      Jeśli jest więcej niż jeden proces `claude` – zatrzymaj się i zapytaj inwestora, czy drugą sesję można zamknąć.
- [ ] 2. `git status` musi być czysty (brak `M`/`??`). Jeśli nie – pokaż listę inwestorowi i zapytaj, co z tym zrobić. Nie commituj cudzych zmian.
- [ ] 3. `git config core.hooksPath` → `.githooks`; `git config user.email` → kończy się na `@users.noreply.github.com`.
- [ ] 4. `git checkout main && git pull`.
- [ ] 5. `git merge przeglad-2026-10` (powinno być fast-forward). Konflikt → zatrzymaj się i pokaż inwestorowi.
- [ ] 6. `python3 tools/build.py --tylko-walidacja` → „Walidacja OK (12 procedur)”.
- [ ] 7. `python3 tools/dokumenty.py --dry-run` – przeczytaj raport; zapamiętaj ostrzeżenia (wrócą w `05`).
- [ ] 8. Przeczytaj w całości nowe pliki (powstały jako szkic, Ty je dopracowujesz):
      `plugins/dom-budowa/skills/etap/SKILL.md` + `references/odbiory.md`, `references/formalnosci.md`;
      `plugins/dom-budowa/skills/dziennik/SKILL.md` + `references/notion-dziennik.md`;
      `plugins/dom-budowa/skills/zakupy/SKILL.md` + `references/wyprzedzenia.md`;
      `plugins/dom-budowa/skills/oferta/references/umowa.md`;
      wpis `[0.5.0]` w `CHANGELOG.md` (lista wszystkich zmian na gałęzi).
- [ ] 9. Napisz inwestorowi jedną linię: „00 gotowe – main na commicie <sha>, 12 procedur, walidacja OK”.
