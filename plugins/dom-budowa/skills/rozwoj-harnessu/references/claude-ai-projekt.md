# Projekt „Dom” na claude.ai – konfiguracja

Projekt „Dom” na claude.ai (czat, telefon) ma dwie części:

| Część | Co tam jest | Skąd |
|---|---|---|
| **Instructions** (instrukcje projektu) | krótki tekst z sekcji niżej – każe przy każdej wiadomości użyć harnessu | ten plik (wersjonowany w repo); gotowa kopia z numerem wersji: `dist/claude-ai-projekt/instrukcje.md` z `tools/build.py` |
| **Wiedza projektu** (pliki) | może być pusta; opcjonalnie kopia awaryjna `00_SPIS.md` + `01_Sciaga-projektu.md` | paczka `_Do claude.ai/` (procedura `dokumenty`) |

Przewodnik po dokumentach i mapę Notion asystent czyta ze strony Notion „📑 Przewodnik po dokumentach i Notion” –
Claude Code aktualizuje ją sam (procedura `dokumenty`, sekcja C), więc po zmianach w dokumentach lub w strukturze Notion
nic nie trzeba wgrywać. Claude Code nie może zapisywać plików w wiedzy projektu na claude.ai (brak takiej możliwości),
ale może zapisywać w Notion, które claude.ai czyta na żywo.

Instrukcje są celowo tylko odnośnikiem: zasady i zachowanie (np. prośba o dokument) są w skillach i przychodzą
z pluginem, więc instrukcji nie trzeba wklejać na nowo przy każdej wersji – tylko gdy zmieni się tekst niżej
(CHANGELOG to zaznacza). Dawny plik `START.md` w wiedzy projektu – usuń.

## Aktualizacja pluginu na claude.ai

Wersję widać na stronie pluginu (Customize → Plugins → „Dom budowa”: „from dom · X.Y.Z”). Po pushu z podbitą wersją:

1. Jeśli jest opcja odświeżenia marketplace'u (wg dokumentacji „Check for updates” przy marketplace „dom”, nie przy
   samym pluginie; może jej nie być, gdy organizacja ogranicza pluginy) – użyj jej.
2. Jeśli nie ma: usuń plugin „Dom budowa” i marketplace „dom”, potem Add marketplace → `sztalinux/dom` → zainstaluj
   ponownie. Pobiera się bieżąca wersja z GitHuba.
3. Gdy organizacja blokuje marketplace'y: `python3 tools/build.py`, Add → Upload plugin → `dist/dom-budowa.plugin`.

## Wiedza projektu a kontekst

Dopóki pliki mieszczą się w kontekście, claude.ai dołącza je w całości do każdej rozmowy w projekcie (szybciej zużywa
limit konta); powyżej progu sam przełącza się na wyszukiwanie fragmentów (RAG). Zajętość widać we wskaźniku pojemności
wiedzy projektu. Co trafia do paczki, decyduje procedura `dokumenty` (sekcja A).

## Tekst instrukcji

<!-- instrukcje-start -->
Jesteś asystentem budowy domu inwestora. Pracujesz według harnessu – pluginu „dom-budowa” (skille).

1. Przy każdej wiadomości wczytaj skill `budowa` i według jego mapy procedur wczytaj właściwe skille
   (jedna wiadomość może wymagać kilku – po kolei). Nie czekaj, aż użytkownik wpisze „/”.
2. Raz na rozmowę (przy pierwszej wiadomości) sprawdź w Notion skrzynkę „Zmiany do harnessu” – opis w skillu `budowa`.
3. Dane naszej budowy są w Notion: strona DOM (ściąga „📐 Dane projektu”, „🔴 Do zamknięcia”) i strona
   „📑 Przewodnik po dokumentach i Notion” (3f6f5982-09e7-81f5-bade-ec877d8d936a) – pobierz ją przy pierwszej
   wiadomości. Pełnych dokumentów tu nie ma – gdy są potrzebne, poproś o konkretny plik (skill `dokumenty`).
   Szukaj najpierw w moich materiałach, potem w sprawach otwartych, na końcu w internecie – zawsze ze źródłem
   (skill `budowa`, zasada 10). Nie zgaduj.
4. Jeśli skille dom-budowa są niedostępne, napisz to w pierwszym zdaniu i nie zgaduj procedur.
<!-- instrukcje-koniec -->
