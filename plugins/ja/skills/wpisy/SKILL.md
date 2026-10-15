---
name: wpisy
description: Przetwarzanie luźnych wpisów inwestora ze strony „📓 Dziennik” w Notion (myśli, emocje, zadania, sprawy budowy, dziecko, suplementy, książki – wpisane w biegu, z telefonu) – rozpoznanie obszaru według bazy „🧭 Obszary Dziennika”, wyjaśnienie niejasnych, przekazanie do właściwej procedury, ślad w „Przetworzone”. Używaj, gdy użytkownik mówi „przerób dziennik”, „ogarnij dziennik”, „co mam w dzienniku”, „odpowiedziałem w dzienniku”, „przerób inbox”, gdy przegląd dnia lub tygodnia pokazuje wpisy do przetworzenia, albo gdy wkleja kilka luźnych notatek naraz i prosi „wrzuć gdzie trzeba”.
---

# Dziennik → właściwe miejsca

Cel: inwestor wpisuje wszystko w jedno miejsce, bez zastanawiania się, gdzie to należy. Asystent rozpoznaje obszar według
bazy w Notion i przekazuje wpis do właściwej procedury – **dopiero gdy wpis jest jednoznaczny**. Niejasne wracają do inwestora
z pytaniem. Podział na obszary żyje w Notion, więc nowy rodzaj wpisu nie wymaga zmiany harnessu.

Miejsce: strona **📓 Dziennik** (`3f8f5982-09e7-80c8-a154-c59aeb844e8f`). Strefy (na wierzchu zawsze tylko to, czego asystent
jeszcze nie widział):

```
📓 Dziennik
	<details> Jak używać </details>
	- nowy wpis inwestora (albo podstrona)              ← NOWE: pierwszy poziom; po przebiegu pusto
	### ❓ Czeka na Twoją odpowiedź {toggle}
		- wpis niejasny
			- ❓ asystent (12.10): pytanie – propozycja interpretacji
			- odpowiedź inwestora (pod pytaniem)
	### Przetworzone {toggle}
		▸ 📅 13.10 wt · 🤖 przetworzono 3 · czeka na Ciebie 1 · jutro 2   ← zwijany blok dnia, najnowszy na górze
			🤖 13.10 wieczór: dziennik – przetworzono 3 (emocje 1, zadania 2), … (pełna linia)
			- ~~wpis~~ → Wpisy emocji: <link>
	### 🧭 Dla asystenta {toggle}  ← baza Obszary; nie ruszaj
	📆 Przeglądy dzienne (podstrona) ← nie jest wpisem
```

**Nowy wpis** = każdy blok pierwszego poziomu (akapit, punkt) **albo podstrona** (tytuł + treść = wpis; podstronę po
przetworzeniu przenieś do bloku dnia jako `<page>` – nie usuwaj), z wyjątkiem „Jak używać”, pustych linii, trzech zwijanych
nagłówków i podstrony „Przeglądy dzienne”. Jeden blok może zawierać kilka spraw – rozłóż je osobno. Nie zmieniaj treści
wpisów inwestora – tylko dopisuj pod nimi i przenoś między strefami.

## Procedura

1. **Pobierz** stronę Dziennik: nowe wpisy oraz wpisy z „❓”, pod których ostatnim pytaniem inwestor coś dopisał (albo
   poprawił wpis) – te oceń ponownie. Wpisy w „❓” bez odpowiedzi pomiń. Brak obu → „Dziennik pusty” (+ liczba czekających w „❓”).
2. **Pobierz Obszary** (`collection://253b7564-00ac-45b2-a3f4-956275e3a7e0`, Aktywny = tak, tryb rows, sort Kolejność).
3. **Dla każdego wpisu ustal** (razem z dialogiem pod nim):
   - **Obszar** – porównaj treść z „Rozpoznawanie” i „Przykład”. Jeden wpis może dotyczyć kilku obszarów (emocja + zadanie,
     budowa + emocja) – rozłóż na części. Przy remisie wygrywa niższa „Kolejność”.
   - **Czy jest jednoznaczny** – da się go zapisać jako samodzielne zdanie: co, kogo/czego dotyczy, kiedy. Pojedyncze słowa,
     skróty, zaimki bez kontekstu, „asdf” – **niejednoznaczne**.
   - **Data zdarzenia** – wzmianka daty we wpisie (`@today`) albo data tekstem; słowa względne licz od niej. Notion nie zapisuje,
     kiedy dopisano pojedynczy punkt, więc data przetwarzania to nie data wpisu. Słowo względne bez daty przy terminie lub
     zdarzeniu z budowy → zapytaj („czy »wczoraj« to 11.10?”); przy emocji bez daty – data przetwarzania z dopiskiem
     „(data przetworzenia)”.
4. **Niejednoznaczny albo bez obszaru → nie przetwarzaj.** Przenieś do „❓” i dopisz pod nim „❓ asystent (data): …” z 1–3
   pytaniami i propozycją („Czy to zadanie prywatne na ten tydzień?”). Wpis z odpowiedzią – połącz i oceń ponownie.
   Odpowiedź opisuje rodzaj wpisu, którego nie ma w Obszarach → przetwórz go i **zaproponuj nowy wiersz Obszarów**
   („Dodać obszar »…« z rozpoznawaniem »…«, zapis do …?”); po zgodzie dodaj go (bez zmiany harnessu). Gdy nowy obszar wymaga
   własnej logiki, której nie da się opisać w polu „Jak zapisać” – zaproponuj pomysł (`rozwoj-harnessu`, C).
5. **Jednoznaczny → wykonaj obszar:**
   - Procedura = nazwa skilla (`budowa`, `emocje`, `zadania`, `dziecko`, `suple`, `rozwoj-harnessu`) → wczytaj ten skill
     i wykonaj jego kroki dla wpisu (łącznie z duplikatami i polami). Dla `budowa` – sekcja „Luźny wpis z Dziennika”.
   - Procedura = `ogólna` → zapisz według „Gdzie” i „Jak zapisać” z wiersza; najpierw szukaj duplikatu (2–3 słowa).
6. **Zamknij wpis:** przenieś go (z dialogiem) do „Przetworzone”, do **zwijanego bloku dzisiejszego dnia** (`<details>`,
   tytuł „📅 <dd.mm> <dzień> · <skrót linii 🤖>”; brak – utwórz na górze), jako `~~wpis~~ → <gdzie>: <link>`. Zdublowane
   / nieprzydatne / testowe → `~~wpis~~ → pominięte: <jedno zdanie>`. Nie usuwaj.
7. **Zapisy wsadowo** (`ja`, zasada 2): odczyty, potem jedno wywołanie na bazę docelową, na końcu **jedna** edycja strony
   Dziennik (przeniesienia do „❓”, do „Przetworzone”, linia „🤖”). Po niej **pierwszy poziom jest pusty** – poza „Jak używać”,
   trzema nagłówkami, podstroną „Przeglądy dzienne” i 1–2 pustymi liniami do pisania. Linia „🤖” idzie na górę bloku dnia:
   ```
   🤖 15.10 wieczór: dziennik – przetworzono 5 (budowa 2, emocje 1, zadania 2), czeka na Ciebie 1 · pomysły – 1 · jutro: 3
   ```
   Kolejny przebieg tego dnia (np. ręczny) – druga linia „🤖 … (ręczne)” w tym samym bloku. W rozmowie z inwestorem
   przy > 3 wpisach pokaż plan (tabela: wpis | obszar | gdzie trafi | pytanie?) i poproś o „ok”, chyba że powiedział
   „bez pytania”; w przeglądzie dnia – bez pytań.
8. **Podsumuj:** przetworzone (wpis → gdzie), do wyjaśnienia (wpis: pytanie), pominięte; Zmienione / Otwarte / Następny krok.
   „Przetworzone” czyści przegląd tygodnia (bloki dni starsze niż 14 dni, po zgodzie).

## Bez inwestora

Codziennie wieczorem Dziennik przerabia zaplanowany **przegląd dnia** (`przeglad-dnia`) – bez pytań w rozmowie, z wyjątkami
opisanymi tam.

## Zasady

- Nigdy nie zgaduj znaczenia skrótowego wpisu i nie zapisuj go „na wszelki wypadek” – lepiej jedno pytanie niż zagadka
  w bazie. Wyjątek: w docelowej bazie jest już wpis, który go wyjaśnia – wtedy dopisz uzupełnienie tam.
- Źródło (kto powiedział, skąd) przepisuj dosłownie, gdy procedura docelowa ma na nie pole.
- Zdjęcia we wpisie: budowa → `dziennik` (plugin dom-budowa); inne – zostaw w treści docelowej strony.
- Dziennik to skrzynka wejściowa, nie archiwum: wpis żyje w docelowym miejscu, „Przetworzone” to ślad na kilka dni.
- Inwestor woli pisać niż wypełniać pola – nie proponuj zamiany Dziennika na bazę.
