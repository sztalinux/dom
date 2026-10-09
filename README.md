# dom-budowa – harness AI dla budowy domu

Procedury i zasady, według których asystenci AI (Claude, Gemini, Codex…) pracują przy budowie domu.
Repozytorium mówi tylko **jak** pracować. Dane (notatki, wiedza, decyzje) są w Notion, liczby w Excelu,
dokumenty w folderze budowy na komputerze.

> **Repo jest publiczne.** Nie trafiają tu żadne dane osobowe ani dane projektu (nazwiska, firmy, adres,
> działki, telefony, e-maile, kwoty, notatki). Pilnują tego `tools/build.py` i hook `.githooks/pre-commit`
> – ale przed każdym commitem i tak przejrzyj `git diff`.

## Struktura

```
Dom/                              ← folder budowy (centrum dokumentów, poza gitem)
  _Przychodzące/                  ← tu wrzucasz nowe pliki od projektantów i wykonawców
  _Do claude.ai/                  ← paczka aktualnych dokumentów (generowana) → wiedza projektu „Dom” na claude.ai
  Ściąga projektu.md              ← najważniejsze liczby i decyzje (trafia do paczki)
  .dom/                           ← indeks dokumentów, stan wgrania, lista słów zakazanych w repo
  … foldery tematyczne (projekt, konstrukcja, instalacje, wyceny…)
  AI/dom/                         ← to repozytorium
    CLAUDE.md, AGENTS.md, GEMINI.md   ← punkty wejścia agentów
    .claude-plugin/marketplace.json   ← repo jest marketplace'em dla claude.ai
    plugins/dom-budowa/skills/        ← JEDYNE źródło procedur
    .claude/settings.json             ← zezwolenia + hook startowy (tools/dokumenty.py)
    .githooks/                        ← pre-commit (pliki, autor), commit-msg (wiadomość), pre-push (każdy wysyłany commit)
    tools/build.py                    ← walidacja (w tym dane osobowe) + paczki dist/
    tools/dokumenty.py                ← indeks folderu budowy i paczka dla claude.ai
```

## Jak to działa

```
Telefon / czat ── poprawka sposobu pracy ──► Notion „Zmiany do harnessu” (obowiązuje od razu)
                                                   │
Claude Code (komputer, start sesji) ◄──────────────┘
   ├─ hook: skan folderu budowy → paczka `_Do claude.ai/` + lista „do wgrania”
   ├─ klasyfikuje nowe dokumenty (procedura `dokumenty`)
   └─ wdraża zmiany harnessu → wersja → commit → push ──► GitHub sztalinux/dom
                                                               │ automatyczna synchronizacja
claude.ai (telefon, czat, Cowork) ◄── plugin dom-budowa ───────┘
                                  ◄── dokumenty: wgrywasz paczkę do projektu „Dom” (ręcznie)
```

## Start

1. Repo sklonowane do `Dom/AI/dom` (folder budowy = dwa poziomy wyżej; inny – zmienna `DOM_HUB`),
   `git config core.hooksPath .githooks`, `git config user.name <login>`,
   `git config user.email <id>+<login>@users.noreply.github.com` (autor commitów jest publiczny). Lista słów zakazanych: `Dom/.dom/zakazane-w-repo.txt`
   (nazwiska, firmy, miejscowość – po jednym w linii; plik poza repo).
2. Python 3 + `pip3 install --user openpyxl pypdf` (kontrola danych wrażliwych w paczce).
3. W `Dom/AI/dom` uruchom `claude`. `/mcp` – jeśli jest „claude.ai Notion”, gotowe.
4. claude.ai → Customize → Plugins → Add marketplace → `sztalinux/dom` → zainstaluj `dom-budowa`,
   włącz „Sync automatically”. Usuń wcześniej wgrany z pliku plugin `dom-budowa`.
   Gdyby organizacja blokowała marketplace z GitHuba: `python3 tools/build.py` i wgraj `dist/dom-budowa.plugin`
   przez „Upload plugin” (wtedy aktualizacje ręcznie).
5. claude.ai → projekt „Dom” → wiedza projektu: wgraj zawartość `Dom/_Do claude.ai/`.

## Na co dzień

- Nowy plik od projektanta/wykonawcy → wrzuć do `Dom/_Przychodzące/` i uruchom `claude` w `Dom/AI/dom`.
  Asystent go posortuje i powie, co podmienić w projekcie „Dom” na claude.ai. Po wgraniu napisz „wgrałem”.
- Poprawki „na przyszłość” z telefonu trafiają do skrzynki w Notion; Claude Code wdroży je przy starcie.
- Każda zmiana w repo = podbita wersja w `plugins/dom-budowa/.claude-plugin/plugin.json` (inaczej claude.ai jej nie pobierze).
