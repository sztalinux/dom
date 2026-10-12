---
name: inbox
description: Przetwarzanie luźnych wpisów inwestora z sekcji „📥 Inbox” na stronie DOM w Notion (myśli, informacje, ustalenia wpisane w biegu, z telefonu) – wyjaśnienie niejasnych, dopytanie o źródło, rozłożenie do Notatnika, Bazy wiedzy, Dziennika, zadań, Excela. Używaj, gdy użytkownik mówi „przerób inbox”, „ogarnij inbox”, „co mam w inboxie”, „odpowiedziałem w inboxie”, gdy przegląd tygodnia pokazuje wpisy do przetworzenia, albo gdy użytkownik wkleja kilka luźnych notatek naraz i prosi o „wrzuć gdzie trzeba”.
---

# Inbox → właściwe miejsca

Cel: inwestor wpisuje luźne rzeczy do jednej bazy, bez zastanawiania się, gdzie to należy. Asystent rozkłada je
po właściwych miejscach **dopiero wtedy, gdy wpis jest jednoznaczny i ma źródło** – enigmatyczne wpisy wracają
do inwestora z pytaniami, nie trafiają dalej. Dzięki temu w Notatniku i Bazie wiedzy nie ma zagadek.

Miejsce: strona **DOM** (`24af5982-09e7-806b-821a-e157ff33be42`) → rozwijany nagłówek **„📥 Inbox”** (pierwszy na stronie).
Inwestor pisze tam jak w notesie – punkt pod punktem, bez pól i statusów; źródło w nawiasie, jeśli je zna.
Pod spodem zwijany nagłówek **„Przetworzone”** – tam asystent przenosi załatwione wpisy. Układ:

```
## 📥 Inbox {toggle}
	- wpis inwestora (źródło, data – jeśli podał)
	- wpis niejasny
		- ❓ asystent (12.10): pytanie 1; pytanie 2 – propozycja interpretacji
		- odpowiedź inwestora (dopisana pod spodem albo poprawiony wpis)
	### Przetworzone {toggle}
		- ~~wpis~~ → Notatnik: <link> (12.10)
```
**Wpis = każdy blok pierwszego poziomu pod „📥 Inbox”** – akapit albo punkt (inwestor pisze różnie, np. akapit
zaczynający się od daty), z wyjątkiem rozwijanego „Jak używać”, pustych linii i „Przetworzone”. Jeden blok może zawierać
kilka spraw – rozłóż je osobno. Bloki zagnieżdżone pod wpisem to dialog (pytania „❓ asystent (data):” i odpowiedzi
inwestora). Nie zmieniaj treści wpisów inwestora – tylko dopisuj pod nimi i przenoś do „Przetworzone”.

## Procedura

1. **Pobierz** stronę DOM i weź wszystkie wpisy z „📥 Inbox” (definicja wyżej); wpis
   z punktem „❓ asystent” bez odpowiedzi pod spodem – pomiń (czeka na inwestora), z odpowiedzią – oceń ponownie.
   Brak wpisów → jedna linia „Inbox pusty” (+ liczba czekających na Twoją odpowiedź).
2. **Dla każdego wpisu ustal** (razem z dialogiem pod nim):
   - **Co to jest** – jedna z klas: ustalenie/decyzja, pytanie do kogoś, ryzyko, zadanie z terminem, relacja z dnia
     na budowie, wiedza ogólna (coś, co zobaczył/usłyszał), wydatek/koszt, oferta, dokument do posortowania,
     pomysł/do doczytania, poprawka sposobu pracy asystenta.
   - **Czy jest jednoznaczny** – da się go zapisać jako samodzielne zdanie: co, kogo/czego dotyczy, jaka liczba,
     warunek, kiedy. Skróty, pojedyncze słowa („reologia”, „0,96”), zaimki bez kontekstu, „to co mówił X” bez treści –
     **niejednoznaczne**.
   - **Czy ma źródło** – dla wiedzy ogólnej i ustaleń: kto powiedział / skąd (pole Źródło albo treść). Własne
     przemyślenie inwestora to też źródło („własne”), ale musi być nazwane.
   - **Czy to duplikat** – szukaj w docelowej bazie (Notatnik, Informacje, TASKS) 2–3 słów kluczowych.
3. **Niejednoznaczny albo bez źródła → nie przetwarzaj.** Dopisz pod wpisem punkt zagnieżdżony
   „❓ asystent (data): …” z 1–3 konkretnymi pytaniami (co dokładnie, skąd, kiedy, czego dotyczy – zaproponuj
   interpretację do potwierdzenia: „Czy chodzi o X?”). Inwestor odpowiada pod spodem albo poprawia wpis.
   Wpis z odpowiedzią – połącz wpis + odpowiedź i oceń ponownie; nadal niejasny → kolejne pytanie, ale wskaż, co już wiadomo.
   W rozmowie powtórz pytania (inwestor może odpowiedzieć od razu – wtedy dokończ w tym samym przebiegu).
4. **Jednoznaczny ze źródłem → przekaż do właściwej procedury** i wykonaj jej kroki (łącznie z duplikatami
   i polami); kilka klas w jednym wpisie → kilka procedur:
   | Klasa | Procedura | Uwaga |
   |---|---|---|
   | ustalenie, decyzja, pytanie, ryzyko, pomysł, doczytać | `notatka` | ustalenie z wiedzą techniczną → także `wiedza`, sekcja F |
   | zadanie z terminem, „do piątku dam znać…” | `harmonogram` (D) → TASKS, Kto = Ja | |
   | ktoś ma coś zrobić / przyjść / dostarczyć w dniu X | `harmonogram` (D) → TASKS WAITING; krok budowy → Harmonogram | |
   | relacja z budowy, dostawa, usterka, godziny własne | `dziennik` | |
   | wiedza ogólna (usłyszał, przeczytał, obejrzał) | `wiedza` | Źródło z pola Źródło → Rozmowy i źródła; brak = krok 3 |
   | wydatek, faktura, koszt | `koszty` | wiersz do Excela – w Inboxie zostaje do czasu wpisania przez inwestora |
   | oferta, wycena | `oferta` | |
   | „dostałem plik” | `dokumenty` | w Claude Code – klasyfikacja; gdzie indziej – przypomnienie, żeby wrzucić do `_Przychodzące/` |
   | „asystent ma zawsze…” | `rozwoj-harnessu` (A) | skrzynka „Zmiany do harnessu” |
   | „pomysł: …” na asystenta, Notion, Excel, zdjęcia, automatyzację | `rozwoj-harnessu` (C) | baza „Pomysły na rozwój”, od razu z analizą |
5. **Zamknij wpis:** przenieś go (z dialogiem) do „Przetworzone” jako `~~wpis~~ → <gdzie>: <link> (data)`
   (albo „→ wiersz do Excela: …”). Zdublowane / nieprzydatne → `~~wpis~~ → pominięte: <jedno zdanie>`. Nie usuwaj.
6. **Zapisy wsadowo** (`budowa`, zasada 6): najpierw wszystkie odczyty, potem jedno wywołanie na bazę docelową,
   na końcu **jedna** edycja strony DOM (pytania pod wpisami + przeniesienia do „Przetworzone”). Edytuj tylko sekcję
   „📥 Inbox” – reszta strony DOM nietknięta. Przy > 3 wpisach pokaż plan (tabela: wpis | klasa | gdzie trafi |
   pytanie?) i poproś o „ok”, chyba że inwestor powiedział „bez pytania”.
7. **Podsumuj:** przetworzone (wpis → gdzie), do wyjaśnienia (wpis: pytania), pominięte. Zmienione / Otwarte / Następny krok.
   „Przetworzone” czyści przegląd tygodnia (wpisy starsze niż 14 dni, po zgodzie) – linki są już w docelowych miejscach.

## Tryb wieczorny (zaplanowane zadanie, bez inwestora)

Inbox może przerabiać zaplanowane zadanie (np. codziennie o 20:00 na claude.ai). Wtedy nie ma kogo zapytać w rozmowie:
- przetwarzaj tylko wpisy jednoznaczne ze źródłem; niejasne → pytanie „❓ asystent” pod wpisem (krok 3), bez czekania;
- nie pokazuj planu do akceptacji (krok 6) – ale nie zapisuj niczego, co jest decyzją inwestora, rozstrzygnięciem
  sprzeczności (SP) ani zmianą w Excelu: takie wpisy zostaw z pytaniem „❓ asystent: potwierdź, że to decyzja”;
- nie zmieniaj Harmonogramu (terminy kroków) – zaproponuj zmianę pytaniem pod wpisem; zadania i „czekam na” zapisuj;
- potem przeanalizuj nowe pomysły w bazie „Pomysły na rozwój” (Status Nowy lub pusty) – `rozwoj-harnessu`, sekcja C;
- na końcu dopisz na górze Inboxu jedną linię: „🤖 <data>: przetworzono n, pytania przy m; pomysły przeanalizowane: k”
  – inwestor widzi to rano.

## Zasady

- Nigdy nie zgaduj znaczenia skrótowego wpisu i nie zapisuj go dalej „na wszelki wypadek” – lepiej jedno pytanie
  niż zagadka w Notatniku. Wyjątek: wpis jest skrótem, ale w Notatniku/Bazie wiedzy jest już wpis, który go wyjaśnia –
  wtedy dopisz go tam jako uzupełnienie (z linkiem w „Trafiło do”).
- **Daty.** Notion nie zapisuje, kiedy dopisano pojedynczy punkt (widać tylko ostatnią edycję całej strony), więc data
  przetwarzania to nie data wpisu. Data zdarzenia = wzmianka daty we wpisie (`@today` w Notion wstawia datę jednym
  ruchem) albo data wpisana tekstem. Słowa względne („dziś”, „wczoraj”, „w piątek”, „za tydzień”) licz od tej daty.
  Słowo względne bez daty we wpisie → nie zgaduj: przy zdarzeniu z budowy, terminie albo kosztach zapytaj
  („❓ asystent: czy »wczoraj« to 11.10?”), przy wiedzy ogólnej bez znaczenia daty – pomiń datę.
- Źródło przepisuj dosłownie do pola Źródło w Notatniku / Rozmów i źródeł.
- Zdjęcia we wpisie: relacja z budowy → `dziennik` (zdjęcia do folderu `Zdjęcia/`), dokument → `dokumenty`.
- Inbox to skrzynka wejściowa, nie archiwum: po przetworzeniu wpis żyje w docelowym miejscu, „Przetworzone” to tylko ślad na kilka dni.
- Inwestor woli pisać niż wypełniać pola – nie proponuj zamiany Inboxu na bazę.
