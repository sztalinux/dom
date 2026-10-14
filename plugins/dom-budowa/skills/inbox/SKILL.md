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
Trzy strefy, żeby nowe wpisy nie mieszały się ze starymi – **na wierzchu zawsze tylko to, czego asystent jeszcze nie widział**:

```
## 📥 Inbox {toggle}
	<details> Jak używać </details>
	- nowy wpis inwestora (źródło, data – jeśli podał)  ← NOWE: pierwszy poziom; po przebiegu pusto (tylko puste linie do pisania)
	### ❓ Czeka na Twoją odpowiedź {toggle}
		- wpis niejasny
			- ❓ asystent (12.10): pytanie 1; pytanie 2 – propozycja interpretacji
			- odpowiedź inwestora (pod pytaniem)
	### Przetworzone {toggle}
		▸ 📅 13.10 wt · 🤖 przetworzono 3 · czeka na Ciebie 2 · jutro 1   ← zwijany blok dnia, najnowszy na górze
			🤖 13.10 wieczór: inbox – przetworzono 3, … (pełna linia z punktami „jutro”)
			- ~~wpis~~ → Notatnik: <link>
		▸ 📅 12.10 pn · 🤖 …                                             ← starsze dni zwinięte
```
**Nowy wpis = każdy blok pierwszego poziomu pod „📥 Inbox”** – akapit albo punkt (inwestor pisze różnie, np. akapit
zaczynający się od daty), z wyjątkiem „Jak używać”, pustych linii i dwóch zwijanych nagłówków (także gdy
inwestor dopisze coś pod nimi na pierwszym poziomie – to też nowy wpis). Jeden blok może zawierać kilka spraw – rozłóż je
osobno. W „❓ Czeka na Twoją odpowiedź” bloki zagnieżdżone pod wpisem to dialog (pytania „❓ asystent (data):” i odpowiedzi
inwestora). Nie zmieniaj treści wpisów inwestora – tylko dopisuj pod nimi i przenoś między strefami.

## Procedura

1. **Pobierz** stronę DOM i weź: nowe wpisy (pierwszy poziom, definicja wyżej) oraz wpisy z „❓ Czeka na Twoją
   odpowiedź”, pod których ostatnim pytaniem inwestor coś dopisał (albo poprawił wpis) – te oceń ponownie. Wpisy w „❓”
   bez odpowiedzi – pomiń (czekają na inwestora). Brak obu → jedna linia „Inbox pusty” (+ liczba czekających w „❓”).
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
3. **Niejednoznaczny albo bez źródła → nie przetwarzaj.** Przenieś wpis do „❓ Czeka na Twoją odpowiedź” i dopisz pod nim
   punkt zagnieżdżony „❓ asystent (data): …” z 1–3 konkretnymi pytaniami (co dokładnie, skąd, kiedy, czego dotyczy – zaproponuj
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
5. **Zamknij wpis:** przenieś go (z dialogiem, z pierwszego poziomu albo z „❓”) do „Przetworzone”, do **zwijanego bloku
   dzisiejszego dnia** (`<details>`, tytuł „📅 <dd.mm> <dzień> · <skrót linii 🤖>”; brak – utwórz na górze, nad starszymi dniami),
   jako `~~wpis~~ → <gdzie>: <link>` (albo „→ wiersz do Excela: …”). Zdublowane / nieprzydatne → `~~wpis~~ → pominięte: <jedno zdanie>`. Nie usuwaj.
6. **Zapisy wsadowo** (`budowa`, zasada 6): najpierw wszystkie odczyty, potem jedno wywołanie na bazę docelową,
   na końcu **jedna** edycja strony DOM (przeniesienia do „❓” z pytaniami, do „Przetworzone”, linia „🤖”).
   Po niej **pierwszy poziom Inboxu jest pusty** – poza „Jak używać”, dwoma zwijanymi nagłówkami i 1–2 pustymi liniami do
   pisania nie zostaje tam nic: ani wpis, który asystent widział, ani linia „🤖” (ta idzie na górę bloku dnia w „Przetworzone”; kolejny przebieg tego
   samego dnia, np. ręczny – druga linia „🤖 … (ręczne)” w tym samym bloku, tytuł bloku ze skrótem ostatniego przebiegu).
   Edytuj tylko sekcję „📥 Inbox” – reszta strony DOM nietknięta: w edycji typu „znajdź i zamień” nie obejmuj nagłówka
   następnej sekcji („✅ Zadania”) – Notion potrafi wtedy zdjąć mu zwijanie i wyciągnąć bazę TASKS na wierzch. Przy > 3 wpisach pokaż plan (tabela: wpis | klasa | gdzie trafi |
   pytanie?) i poproś o „ok”, chyba że inwestor powiedział „bez pytania”.
7. **Podsumuj** (także przy ręcznym przebiegu dopisz linię „🤖” w bloku dnia w „Przetworzone”): przetworzone (wpis → gdzie), do wyjaśnienia (wpis: pytania), pominięte. Zmienione / Otwarte / Następny krok.
   „Przetworzone” czyści przegląd tygodnia (bloki dni starsze niż 14 dni, po zgodzie) – linki są już w docelowych miejscach.

## Bez inwestora

Codziennie wieczorem Inbox przerabia zaplanowany **przegląd dnia** (`przeglad-dnia`) – bez pytań w rozmowie, z wyjątkami
od kroków 3 i 6 opisanymi tam; on też ustawia linię „🤖”.

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
