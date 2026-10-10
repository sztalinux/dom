---
name: dokumenty
description: Porządek w dokumentach budowy (folder budowy na komputerze inwestora) i paczka aktualnych plików dla claude.ai. Używaj, gdy raport „[dokumenty]” na starcie sesji pokazuje nowe lub zmienione pliki, gdy inwestor mówi „wrzuciłem plik”, „dostałem nowy projekt / ofertę / umowę”, „posortuj dokumenty”, „co mam wgrać do claude.ai”, „wgrałem”, albo pyta, gdzie jest dany dokument lub która wersja jest aktualna.
---

# Dokumenty budowy

Wszystkie pliki od projektantów, wykonawców i urzędów leżą w **folderze budowy** na komputerze inwestora
(katalog dwa poziomy nad repo harnessu; inny – zmienna `DOM_HUB`). Inwestor wrzuca je tam, najlepiej do `_Przychodzące/`.
Skrypt `tools/dokumenty.py` (uruchamiany automatycznie na starcie każdej sesji Claude Code) prowadzi indeks plików
i buduje folder `_Do claude.ai/` – paczkę **aktualnych** wersji do wgrania w wiedzy projektu „Dom” na claude.ai.

Podział pracy: skrypt wykrywa nowe/zmienione/przeniesione pliki, duplikaty i dane wrażliwe oraz kopiuje pliki do paczki.
Ty decydujesz, co to za dokument, czy trafia do paczki i co zastępuje. Bez Twojej decyzji nowy plik do paczki nie trafi.

## Gdzie jesteś

| Miejsce | Co robisz |
|---|---|
| Claude Code w repo (widzisz raport „[dokumenty]”) | klasyfikacja – sekcja A, aktualizacja paczki – sekcja B |
| claude.ai (czat, telefon) | dokumenty są w wiedzy projektu; zacznij od `00_SPIS.md` i `01_Sciaga-projektu.md` |
| Gdzie indziej, bez plików | poproś o załączenie konkretnego dokumentu (nazwa ze spisu) |

## A. Klasyfikacja nowych plików

1. Lista: raport ze startu sesji albo `python3 tools/dokumenty.py lista --nowe`.
2. Dla każdego pliku ustal: co to jest (nazwa, folder, w razie wątpliwości pierwsza strona), kategorię, czy jest
   nowszą wersją czegoś, co już jest w paczce.
3. Do paczki (`--eksport`) – tylko dokumenty przydatne agentom, w **jednej, najnowszej** wersji:
   projekty (architektura, konstrukcja, instalacje – najlepiej komplet w jednym PDF zamiast arkuszy), opinie
   geotechniczne, warunki i uzgodnienia, oferty i wyceny, umowy z wykonawcami, karty techniczne produktów,
   kosztorys Excel (najnowszy), ściąga projektu.
   Bez eksportu (`--bez-eksportu`, z opisem dlaczego): starsze wersje, pojedyncze arkusze zawarte w komplecie,
   archiwa `.zip`, notatki pisane przez AI (to opinie, nie dokumenty), faktury, pliki niezwiązane z budową.
   Dane osobowe w dokumentach (nazwiska, adres, PESEL, numer konta) **nie wykluczają** z paczki – trafia ona tylko
   do prywatnego projektu na claude.ai (decyzja inwestora). Skrypt raz informuje, co wykrył.
4. Nowa wersja dokumentu z paczki: nadaj jej **tę samą** `--nazwa` co poprzedniej, a starą oznacz `--bez-eksportu`
   z opisem „starsza wersja – zastąpiona przez …”. Nazwy w paczce są stałe – dzięki temu inwestor podmienia plik,
   a nie dokłada drugiego.
5. Zapisz decyzje (jedno wywołanie na plik):
   `python3 tools/dokumenty.py ustaw "<ścieżka>" --eksport --nazwa "<NN_Krotka-nazwa.ext>" --kategoria "<NN Kategoria>" --opis "<co to jest, z datą/wersją>"`
   Prefiksy nazw: 00 podsumowanie, 1x projekty, 2x grunt, 3x media i formalności, 4x koszty, 5x oferty, 6x umowy.
6. Pliki z `_Przychodzące/`: przenieś do właściwego folderu tematycznego (istniejącego albo nowego, o czytelnej
   nazwie). Plików poza `_Przychodzące/` nie przenoś ani nie zmieniaj ich nazw. Nigdy nic nie usuwaj.
7. Uruchom `python3 tools/dokumenty.py` – przebuduje paczkę i pokaże, co wgrać.

## B. Po klasyfikacji – wiedza i paczka

- Dokument, który zmienia fakty (nowa rewizja projektu, opinia, umowa, wybrana oferta): zaproponuj analizę
  (procedura `analiza-techniczna`) i aktualizację ściągi projektu (`Ściąga projektu.md` w folderze budowy)
  oraz Notion („Dane projektu (ściąga)”, Notatnik). Ściąga jest w paczce, więc telefon dostanie ją przy następnym wgraniu.
- Oferta wykonawcy → procedura `oferta`.
- Ostrzeżenia skryptu („powyżej limitu”, informacja o danych osobowych) przekaż inwestorowi jednym zdaniem z propozycją
  (np. zmniejszona kopia PDF obok oryginału, oznaczona do paczki zamiast niego).
- Na koniec podaj listę „dodaj / podmień / usuń” z raportu. Po słowach „wgrałem”: `python3 tools/dokumenty.py wgrane`.

## Zasady

- Paczka i folder budowy **nigdy** nie trafiają do repozytorium (repo jest publiczne) – dane osobowe są dozwolone
  w paczce, w repo nigdy.
- Nie przepisuj treści dokumentów do harnessu – fakty idą do ściągi i Notion.
- Zdjęcia z budowy leżą w `Zdjęcia/RRRR-MM-DD_<krok>/` (procedura `dziennik`); skrypt pomija foldery `Zdjęcia*`,
  więc nie trafiają do indeksu ani do paczki. Rysunek czy skan jako obraz → do folderu tematycznego, nie do Zdjęć.
- Gdy nie wiesz, czy plik jest nowszą wersją – zapytaj inwestora jednym pytaniem, zamiast zgadywać.
