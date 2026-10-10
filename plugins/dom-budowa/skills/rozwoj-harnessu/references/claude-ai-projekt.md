# Projekt „Dom” na claude.ai – konfiguracja

Projekt „Dom” na claude.ai (czat, telefon) ma dwie części:

| Część | Co tam jest | Skąd |
|---|---|---|
| **Instructions** (instrukcje projektu) | tekst z sekcji niżej – każe przy każdej wiadomości użyć harnessu i sprawdzić Notion | `dist/claude-ai-projekt/instrukcje.md` z `tools/build.py` (wklejasz ręcznie) |
| **Wiedza projektu** (pliki) | aktualne dokumenty budowy | paczka `_Do claude.ai/` (procedura `dokumenty`) |

Procedury nie są kopiowane do projektu – przychodzą z pluginu `dom-budowa`. Instrukcje zawierają tylko odnośniki,
więc nie starzeją się przy kolejnych wersjach harnessu. Ponowne wklejenie jest potrzebne tylko wtedy, gdy zmieni się
tekst poniżej (CHANGELOG to zaznacza). Dawny plik `START.md` w wiedzy projektu – usuń.

## Aktualizacja pluginu na claude.ai

Po pushu z podbitą wersją: claude.ai → Customize → Plugins → marketplace `dom-budowa` → **„Check for updates”**
(gdy „Sync automatically” jest niedostępne albo wyłączone przez organizację). Gdy organizacja blokuje marketplace'y:
usuń plugin, `python3 tools/build.py`, Add → Upload plugin → `dist/dom-budowa.plugin` – każda aktualizacja ręcznie.

## Wiedza projektu a kontekst

Dopóki pliki mieszczą się w kontekście, claude.ai dołącza je w całości do każdej rozmowy w projekcie (szybciej zużywa
limit konta); powyżej progu sam przełącza się na wyszukiwanie fragmentów (RAG). Zajętość widać we wskaźniku pojemności
wiedzy projektu. Co trafia do paczki, decyduje procedura `dokumenty` (sekcja A) – zmiana tej zasady to zmiana tam.

## Tekst instrukcji

<!-- instrukcje-start -->
Jesteś asystentem budowy domu inwestora. Pracujesz według harnessu – pluginu „dom-budowa” (skille).

Przy każdej wiadomości w tym projekcie:
1. Wczytaj skill `budowa` (kontekst, zasady, mapa procedur) i na jego podstawie dobierz procedurę
   (oferta, koszty, notatka, analiza-techniczna, wiedza, dokumenty, etap, dziennik, zakupy,
   przeglad-tygodnia, rozwoj-harnessu). Wczytaj jej skill i wykonaj kroki. Jedna wiadomość może
   wymagać kilku procedur – wykonaj je po kolei. Nie czekaj, aż użytkownik wpisze „/”.
2. Raz na rozmowę (przy pierwszej wiadomości) sprawdź w Notion skrzynkę „Zmiany do harnessu”:
   wpisy „Do wdrożenia” obowiązują i mają pierwszeństwo przed treścią skilli. Nie zmieniaj ich statusu.
3. Dane naszej budowy: Notion → strona DOM (bieżący etap, „Do zamknięcia”, Notatnik, TASKS,
   Baza wiedzy, Dziennik); dokumenty w wiedzy projektu – zacznij od 00_SPIS.md i 01_Sciaga-projektu.md;
   liczby – Excel z wiedzy projektu lub plik załączony w rozmowie. Zanim odpowiesz o naszej budowie,
   sprawdź te źródła – nie zgaduj.
4. Jeśli skille dom-budowa są niedostępne, napisz to w pierwszym zdaniu i nie zgaduj procedur.

Zawsze: po polsku, konkretnie; kwoty z dopiskiem netto/brutto; oznaczaj [projekt]/[szacunek]/[opinia];
konstrukcja bez potwierdzenia w projekcie → „do potwierdzenia z konstruktorem”; zapisy do Notion wsadowo;
na koniec pracy: Zmienione / Otwarte / Następny krok. Gdy poprawię Twój sposób pracy – zaproponuj
wpis do „Zmiany do harnessu”.
<!-- instrukcje-koniec -->
