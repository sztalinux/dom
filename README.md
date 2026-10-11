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
  _Do claude.ai/                  ← paczka (generowana): przewodnik po dokumentach + ściąga → wiedza projektu „Dom” na claude.ai
  Zdjęcia/                        ← zdjęcia z budowy (RRRR-MM-DD_<krok>/), poza indeksem i paczką
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
                                                               │ ręczne odświeżenie pluginu (claude-ai-projekt.md)
claude.ai (telefon, czat, Cowork) ◄── plugin dom-budowa ───────┘
                                  ◄── dokumenty: wgrywasz paczkę do projektu „Dom” (ręcznie)
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

## Start

1. Repo sklonowane do `Dom/AI/dom` (folder budowy = dwa poziomy wyżej; inny – zmienna `DOM_HUB`),
   `git config core.hooksPath .githooks`, `git config user.email <id>+<login>@users.noreply.github.com`
   (autor commitów jest publiczny; imię inwestora dozwolone, e-mail tylko noreply). Lista słów zakazanych: `Dom/.dom/zakazane-w-repo.txt`
   (nazwiska, firmy, miejscowość – po jednym w linii; plik poza repo).
2. Python 3 + `pip3 install --user openpyxl pypdf` (kontrola danych wrażliwych w paczce).
3. W `Dom/AI/dom` uruchom `claude`. `/mcp` – jeśli jest „claude.ai Notion”, gotowe.
4. claude.ai → Customize → Plugins → Add marketplace → `sztalinux/dom` → zainstaluj `dom-budowa`,
   włącz „Sync automatically” (jeśli organizacja na to pozwala). Usuń wcześniej wgrany z pliku plugin `dom-budowa`.
   Bez synchronizacji – jak pobrać nową wersję: `plugins/dom-budowa/skills/rozwoj-harnessu/references/claude-ai-projekt.md`.
5. claude.ai → projekt „Dom”:
   - **Instructions:** `python3 tools/build.py` i wklej `dist/claude-ai-projekt/instrukcje.md` – dzięki temu każda
     wiadomość w projekcie korzysta z harnessu i Notion bez wpisywania „/” (opis:
     `plugins/dom-budowa/skills/rozwoj-harnessu/references/claude-ai-projekt.md`). Dawny `START.md` usuń.
   - **Wiedza projektu:** wgraj zawartość `Dom/_Do claude.ai/` (przewodnik `00_SPIS.md` + ściąga), potem
     `python3 tools/dokumenty.py wgrane`. Pełne dokumenty asystent pobiera na prośbę – załączasz je do rozmowy.

## Na co dzień

- Nowy plik od projektanta/wykonawcy → wrzuć do `Dom/_Przychodzące/` i uruchom `claude` w `Dom/AI/dom`.
  Asystent go posortuje, opisze w przewodniku `00_SPIS.md` i powie, co podmienić w projekcie „Dom” (zwykle sam przewodnik).
  Po wgraniu napisz „wgrałem”. Gdy na telefonie asystent poprosi o dokument – załącz wskazany plik.
- Poprawki „na przyszłość” z telefonu trafiają do skrzynki w Notion; Claude Code wdroży je przy starcie.
- Dzień na budowie → powiedz asystentowi, co się działo (telefon wystarczy) – trafi do Dziennika budowy; zdjęcia wrzuć do `Dom/Zdjęcia/RRRR-MM-DD_<krok>/`.
- Przed krokiem „bez odwrotu” (beton, zasypka, tynki) zapytaj „co sprawdzić przed …” – dostaniesz bramkę z listą zdjęć do zrobienia.
- Każda zmiana w repo = podbita wersja w `plugins/dom-budowa/.claude-plugin/plugin.json` (inaczej claude.ai jej nie pobierze).
  Po pushu odśwież plugin na claude.ai (o ile nie działa synchronizacja) – `rozwoj-harnessu/references/claude-ai-projekt.md`.
- Procedury działają same – piszesz normalnie. `/` (np. `/oferta`, na claude.ai `dom-budowa:oferta`) tylko gdy chcesz wymusić procedurę.
