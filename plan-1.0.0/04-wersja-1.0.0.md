# 04 – Wersja 1.0.0: CHANGELOG, build, commit, push

Warunek: zadania 00–02 wykonane (03 może mieć otwarte STOP-punkty – nie blokuje).

- [ ] 1. Wersja `1.0.0` w `plugins/dom-budowa/.claude-plugin/plugin.json` i `gemini-extension.json` (oba muszą być równe).
- [ ] 2. `CHANGELOG.md`: nagłówek `## [0.5.0] – 2026-10-10 (PROPOZYCJA – gałąź przeglad-2026-10, do zatwierdzenia przez inwestora)`
      zamień na `## [1.0.0] – <dzisiejsza data>`; pierwszy akapit pod nim zamień na:
      `Pierwsza stabilna wersja – baza do dalszego rozwoju. Harness obejmuje teraz także fazę wykonywania budowy (budowa mieszana: część prac sam, część ekipy).`
      Zostaw istniejące punkty i dopisz:
      `- \`wiedza\`: tryb odczytu „co wiemy o…” (stan wiedzy, co obowiązuje u nas, otwarte sprzeczności, luki).`
      `- \`CLAUDE.md\`, \`rozwoj-harnessu\`: jedna sesja Claude Code w repo naraz; commit tylko własnych plików.`
      `- Notion: baza „Dziennik budowy”, opcje \`etap\`/\`dziennik\`/\`zakupy\` w skrzynce, pulpit DOM i strona przewodnika zaktualizowane.`
      `- README: tabela procedur.`
- [ ] 3. `CHANGELOG.md`, sekcja „Do zrobienia”: usuń punkty o bazie Dziennik i opcjach skrzynki (zrobione w 02). Zostaw „Po ~10 filmach…”.
      Dopisz: `- [ ] Pierwszy przegląd tygodnia uruchomiony z claude.ai (zadanie zaplanowane) – sprawdzić format i czas.`
- [ ] 4. `grep -rn "PROPOZYCJA\|do utworzenia\|do uzupełnienia\|0\.5\.0" plugins/ CHANGELOG.md AGENTS.md README.md CLAUDE.md` – poza historią w CHANGELOG nic nie może zostać.
- [ ] 5. `git rm -r plan-1.0.0` (plan był jednorazowy; przegląd inwestora leży poza repo).
- [ ] 6. `python3 tools/build.py` (pełny: walidacja + `dist/`) → „Walidacja OK (12 procedur)”. `dist/` jest w `.gitignore`.
- [ ] 7. `git status` – wszystkie zmiany są Twoje (z zadań 00–04). Przejrzyj `git diff` pod kątem danych osobowych (nazwiska, firmy, kwoty).
- [ ] 8. `git add -A && git commit -m "Harness 1.0.0: etapy, dziennik, zakupy, umowa, płatności – pierwsza stabilna wersja"`.
      Hooki muszą przejść; zablokowany hook = popraw dane, nigdy `--no-verify`.
- [ ] 9. `git push`. Sprawdź `git log origin/main -1`. `git branch -d przeglad-2026-10`.
- [ ] 10. Skrzynka „Zmiany do harnessu” jest pusta – nic do oznaczania. Jeśli w międzyczasie coś przybyło ze statusem „Do wdrożenia”,
       wdroż wg `rozwoj-harnessu` jako 1.0.1 (osobny commit).
- [ ] 11. Do inwestora: „1.0.0 na GitHubie (<sha>). Następne: 05 – testy i lista ręczna.”
