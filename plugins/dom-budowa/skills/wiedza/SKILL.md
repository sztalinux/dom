---
name: wiedza
description: Zapis wiedzy do Notion (Baza wiedzy – Tematy, Informacje, Rozmowy i źródła) z transkrypcji filmów YouTube, podcastów, artykułów ekspertów oraz z rozmów z konstruktorem, architektem, wykonawcami; wykrywanie sprzeczności (Rejestr sprzeczności) i ich rozstrzyganie po decyzji inwestora. Używaj, gdy użytkownik wkleja transkrypcję, napisy, link do filmu, notatki z filmu/artykułu, mówi „przerób ten film”, „wrzuć do wiedzy”, „dzwoniłem do konstruktora, powiedział…”, albo odpowiada na sprzeczność („SP-3: …”), albo pyta „co wiemy o…”, „co mówi baza wiedzy o…”, „jakie mamy sprzeczności w temacie…”.
---

# Wiedza – filmy, artykuły, rozmowy

Cel: z każdego źródła wyciągnąć **wszystko, co istotne, i nic poza tym**, przypiąć do właściwych tematów,
oznaczyć co nowe, co potwierdzone, a co sprzeczne – i niczego spornego nie rozstrzygać bez inwestora.

Struktura Notion, ID baz, pola i plan zapisu: `references/notion-wiedza.md`.
Ocena źródła: `references/ocena-zrodla.md`. Sprzeczności (ADR): `references/sprzecznosci.md`.
Zapisy wsadowe: `budowa`, zasada 6.

## A. Nowe źródło

1. **Metadane:** film/artykuł – tytuł, autor/kanał, link, data publikacji (z linku spróbuj odczytać tytuł i datę);
   rozmowa – z kim, forma, data. Czego nie da się ustalić – wpisz „?” i dopisz do „Do uzupełnienia” w odpowiedzi
   (nie blokuj pracy). Sprawdź w Rozmowach i źródłach, czy to źródło już było – jeśli tak, zapytaj, czy przetworzyć ponownie.
2. **Ocena źródła** wg `references/ocena-zrodla.md`: typ autora, konflikt interesów, wiarygodność 1–5.
   Nasz konstruktor/architekt = „Nasz projektant / wykonawca” – jego ustalenia dotyczą naszej budowy wprost.
3. **Ekstrakcja** – przeczytaj całość (długą transkrypcję w częściach, nic nie pomijaj w czytaniu):
   - jedna jednostka = jedna informacja zrozumiała bez filmu (co, warunek, liczba, dlaczego),
   - **zachowaj zawsze:** liczby z jednostkami, warunki i wyjątki („przy gruncie spoistym…”), nazwy systemów
     i produktów, kolejność prac, ostrzeżenia, uzasadnienia, koszty z datą,
   - **pomijaj:** wstępy, reklamy, anegdoty, powtórzenia, prośby o subskrypcję, dygresje bez treści,
   - popraw oczywiste błędy automatycznej transkrypcji w terminach (np. „ka em be” → KMB); niepewne oznacz `[niepewne w transkrypcji]`,
   - zachowaj znacznik czasu w polu Fragment, np. `12:40 – „…”` (cytat ≤ 20 słów).
   **Kontrola kompletności:** wypisz dla siebie wszystkie liczby, produkty i ostrzeżenia ze źródła i sprawdź, czy każde
   trafiło do jakiejś jednostki albo zostało świadomie pominięte (w odpowiedzi podaj, co pominięto i dlaczego).
4. **Tematy:** każdą jednostkę przypnij do 1–2 tematów z bazy Tematy (najpierw istniejące; nowy temat tylko gdy nic nie pasuje)
   oraz nadaj Branżę i Etap. Film o jednym temacie, który zahacza o inne – każda informacja idzie do swojego tematu.
5. **Porównanie z tym, co wiemy** – dla każdej jednostki przeszukaj: Informacje (te same Tematy + słowa kluczowe),
   „W skrócie” tematów, Rejestr sprzeczności (także rozstrzygnięte), decyzje w Notatniku budowy, ściągę projektu
   (`budowa/references/projekt.md`). Sklasyfikuj:
   | Wynik | Działanie |
   |---|---|
   | NOWE | nowy wiersz, Status „Nowe” |
   | POTWIERDZENIE (to samo twierdzenie) | bez nowego wiersza – podepnij istniejący wiersz pod nowe źródło (Potwierdzenia liczą się same) |
   | UZUPEŁNIENIE (nowy szczegół) | nowy wiersz „Nowe” z dopiskiem „uzupełnia WI-x” |
   | SPRZECZNOŚĆ | nowy wiersz ze Statusem „Sporne” + wpis w Rejestrze („Czeka na decyzję”) |
   | ZGODNE / SPRZECZNE Z ROZSTRZYGNIĘCIEM | nie otwieraj sporu ponownie, chyba że źródło wnosi nowy argument – wtedy nowy SP z odwołaniem do starego |
   Różne zalecenia dla **różnych warunków** (inny grunt, inna technologia) to nie sprzeczność – zapisz warunek w treści.
6. **Dla naszej budowy:** oceń „Dotyczy nas” i w 1–2 zdaniach napisz, co to znaczy u nas (parametry budynku, gruntu i instalacji:
   `budowa/references/projekt.md`). Wymaga działania (pytanie do konstruktora, ryzyko,
   rzecz do pilnowania na budowie) → wpis w Notatniku budowy (procedura `notatka`, Źródło = „ZRD-x <tytuł>, <minuta>”).
7. **Zapis do Notion** – kolejność i grupowanie wg „Plan zapisu” w `references/notion-wiedza.md` (zwykle 4–6 zatwierdzeń).
   Wiedza bez konfliktu zapisuje się od razu.
8. **Tematy – podsumowanie:** aktualizuj „W skrócie” i treść strony tematu tylko gdy temat dostał ≥ 3 nowe informacje,
   rozstrzygnięcie albo informacja zmienia „co obowiązuje dziś”. Pozostałe są widoczne w relacji Informacje tematu.

## B. Odpowiedź po przetworzeniu

```
**ZRD-x „<tytuł>”** – <autor>, <data> | wiarygodność <n>/5 | konflikt interesów: <…>
Zapisano: <n> nowych, <n> potwierdzeń, <n> uzupełnień → tematy: <lista>
Najważniejsze dla nas: • … • … (3–5 punktów, z WI-x)
⚠️ Sprzeczności – czekają na Twoją odpowiedź:
  SP-n <dylemat>: A) <stanowisko + źródło> vs B) <stanowisko + źródło>. Rekomenduję <…>, bo <…>.
  ❓ <pytanie> – odpowiedz np. „SP-n: B” albo „SP-n: zapytam konstruktora”.
Do Notatnika: <wpisy> | Pominięto: <co i dlaczego> | Do uzupełnienia: <np. data publikacji>
```

## C. Rozstrzygnięcie sprzeczności (po odpowiedzi inwestora)

Tylko po wyraźnej odpowiedzi; niejasna → dopytaj, nie zgaduj. Kroki: `references/sprzecznosci.md`.

## D. „Przejrzałem nowe”

Zmień Status „Nowe” → „Przejrzane” dla wskazanych wierszy (albo wszystkich z danego źródła/tematu).

## E. Pytanie do bazy („co wiemy o drenażu?”)

1. Znajdź temat(y) w Tematach (nazwa i „W skrócie”); pobierz ich Informacje (Status ≠ Nieaktualne) i wpisy Rejestru
   (Status ≠ Zastąpione) – jednym zapytaniem na bazę. Dodaj decyzje z Notatnika (Typ „Decyzja”) o tej branży.
   Gdy dwa tematy pokrywają ten sam zakres, nie łącz ich wiedzy po cichu – zgłoś to inwestorowi jako sprawę porządkową.
2. Odpowiedz w kolejności: **co obowiązuje u nas** (decyzje z ich Statusem – „Do omówienia” to jeszcze nie ustalenie;
   rozstrzygnięcia SP, projekt – ze źródłem) → **stan wiedzy**
   (punkty z WI-x, liczby z warunkami; przy rozbieżnych warunkach podaj oba) → **otwarte sprzeczności** (SP-n, od kiedy czekają)
   → **luki** (czego baza nie wie – zaproponuj, kogo zapytać lub jakie źródło przerobić).
3. Nie dopisuj wiedzy z własnej pamięci do odpowiedzi jako „z bazy”. Własne uzupełnienie oznacz `[opinia]` i zaproponuj
   zapis dopiero po potwierdzeniu źródłem.
4. Nic nie zapisuj (tryb tylko do odczytu), chyba że inwestor poprosi o zanotowanie luki jako „Doczytać” (`notatka`).
