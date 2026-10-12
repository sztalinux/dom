---
name: inbox
description: Przetwarzanie luźnych wpisów inwestora z bazy „Inbox” w Notion (myśli, informacje, ustalenia wpisane w biegu, z telefonu) – wyjaśnienie niejasnych, dopytanie o źródło, rozłożenie do Notatnika, Bazy wiedzy, Dziennika, zadań, Excela. Używaj, gdy użytkownik mówi „przerób inbox”, „ogarnij inbox”, „co mam w inboxie”, „odpowiedziałem w inboxie”, gdy przegląd tygodnia pokazuje wpisy do przetworzenia, albo gdy użytkownik wkleja kilka luźnych notatek naraz i prosi o „wrzuć gdzie trzeba”.
---

# Inbox → właściwe miejsca

Cel: inwestor wpisuje luźne rzeczy do jednej bazy, bez zastanawiania się, gdzie to należy. Asystent rozkłada je
po właściwych miejscach **dopiero wtedy, gdy wpis jest jednoznaczny i ma źródło** – enigmatyczne wpisy wracają
do inwestora z pytaniami, nie trafiają dalej. Dzięki temu w Notatniku i Bazie wiedzy nie ma zagadek.

Baza: Notion → DOM → **Inbox** (`collection://16e53396-89ca-4053-8bd2-97061a1065c0`).
Pola: Wpis (tytuł), Status (Do przetworzenia / Do wyjaśnienia / Przetworzone / Odrzucone), Źródło, Pytania asystenta,
Odpowiedź, Trafiło do, Dodano, ID (IN-n). Treść strony wpisu = dłuższy tekst, zdjęcia, wklejki.

## Procedura

1. **Pobierz** wpisy ze Statusem „Do przetworzenia” oraz „Do wyjaśnienia”, które mają wypełnioną Odpowiedź
   (jedno zapytanie). Brak wpisów → jedna linia „Inbox pusty”.
2. **Dla każdego wpisu ustal** (czytaj też treść strony):
   - **Co to jest** – jedna z klas: ustalenie/decyzja, pytanie do kogoś, ryzyko, zadanie z terminem, relacja z dnia
     na budowie, wiedza ogólna (coś, co zobaczył/usłyszał), wydatek/koszt, oferta, dokument do posortowania,
     pomysł/do doczytania, poprawka sposobu pracy asystenta.
   - **Czy jest jednoznaczny** – da się go zapisać jako samodzielne zdanie: co, kogo/czego dotyczy, jaka liczba,
     warunek, kiedy. Skróty, pojedyncze słowa („reologia”, „0,96”), zaimki bez kontekstu, „to co mówił X” bez treści –
     **niejednoznaczne**.
   - **Czy ma źródło** – dla wiedzy ogólnej i ustaleń: kto powiedział / skąd (pole Źródło albo treść). Własne
     przemyślenie inwestora to też źródło („własne”), ale musi być nazwane.
   - **Czy to duplikat** – szukaj w docelowej bazie (Notatnik, Informacje, TASKS) 2–3 słów kluczowych.
3. **Niejednoznaczny albo bez źródła → nie przetwarzaj.** Wpisz w „Pytania asystenta” 1–3 konkretne pytania
   (co dokładnie, skąd, kiedy, czego dotyczy – zaproponuj interpretację do potwierdzenia: „Czy chodzi o X?”),
   Status „Do wyjaśnienia”. Jedna aktualizacja na wpis, wszystkie w jednym przebiegu.
   Wpis z Odpowiedzią inwestora – połącz Wpis + Odpowiedź w jedno i oceń ponownie; nadal niejasny → kolejne pytanie,
   ale wskaż, co już wiadomo.
4. **Jednoznaczny ze źródłem → przekaż do właściwej procedury** i wykonaj jej kroki (łącznie z duplikatami
   i polami); kilka klas w jednym wpisie → kilka procedur:
   | Klasa | Procedura | Uwaga |
   |---|---|---|
   | ustalenie, decyzja, pytanie, ryzyko, pomysł, doczytać | `notatka` | ustalenie z wiedzą techniczną → także `wiedza`, sekcja F |
   | zadanie z terminem | `notatka` (TASKS) | |
   | relacja z budowy, dostawa, usterka, godziny własne | `dziennik` | |
   | wiedza ogólna (usłyszał, przeczytał, obejrzał) | `wiedza` | Źródło z pola Źródło → Rozmowy i źródła; brak = krok 3 |
   | wydatek, faktura, koszt | `koszty` | wiersz do Excela – w Inboxie zostaje do czasu wpisania przez inwestora |
   | oferta, wycena | `oferta` | |
   | „dostałem plik” | `dokumenty` | w Claude Code – klasyfikacja; gdzie indziej – przypomnienie, żeby wrzucić do `_Przychodzące/` |
   | „asystent ma zawsze…” | `rozwoj-harnessu` | skrzynka „Zmiany do harnessu” |
5. **Zamknij wpis:** „Trafiło do” = linki do utworzonych/zaktualizowanych stron (albo „wiersz do Excela: …”),
   Status „Przetworzone”. Nieprzydatne lub zdublowane (już było w Notatniku) → „Odrzucone” z jednym zdaniem dlaczego
   w „Trafiło do”. Nie usuwaj wpisów.
6. **Zapisy wsadowo** (`budowa`, zasada 6): najpierw wszystkie odczyty, potem jedno wywołanie na bazę docelową,
   na końcu jedna aktualizacja statusów w Inboxie. Przy > 3 wpisach pokaż plan (tabela: IN-n | klasa | gdzie trafi |
   pytanie?) i poproś o „ok”, chyba że inwestor powiedział „bez pytania”.
7. **Podsumuj:** przetworzone (IN-n → gdzie), do wyjaśnienia (IN-n: pytania), odrzucone. Zmienione / Otwarte / Następny krok.

## Zasady

- Nigdy nie zgaduj znaczenia skrótowego wpisu i nie zapisuj go dalej „na wszelki wypadek” – lepiej jedno pytanie
  niż zagadka w Notatniku. Wyjątek: wpis jest skrótem, ale w Notatniku/Bazie wiedzy jest już wpis, który go wyjaśnia –
  wtedy dopisz go tam jako uzupełnienie (z linkiem w „Trafiło do”).
- Źródło przepisuj dosłownie do pola Źródło w Notatniku / Rozmów i źródeł; data wpisu (Dodano) to nie data zdarzenia –
  jeśli zdarzenie ma datę, zapytaj albo weź z treści.
- Zdjęcia we wpisie: relacja z budowy → `dziennik` (zdjęcia do folderu `Zdjęcia/`), dokument → `dokumenty`.
- Inbox to skrzynka wejściowa, nie archiwum: przetworzone wpisy zostają (historia), ale nic się do nich nie wraca.
