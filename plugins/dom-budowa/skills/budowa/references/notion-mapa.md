# Notion – co gdzie jest

Mapa dla asystenta: gdzie szukać, zanim odpowiesz. Same struktury i identyfikatory – treść jest w Notion.
Plik trafia też do przewodnika (`tools/dokumenty.py`) – strona Notion „📑 Przewodnik po dokumentach i Notion”, którą Claude Code
synchronizuje sam, więc asystent na claude.ai ma zawsze aktualną mapę.
Zmiana struktury Notion (nowa baza, widok, pole) → zaktualizuj ten plik (procedura `rozwoj-harnessu`).

Pulpit **DOM** `24af5982-09e7-806b-821a-e157ff33be42` – u góry dwa rozwijane nagłówki, pod nimi zakładki, na dole pomysły i sekcja dla AI:

```
DOM
├─ 📥 Inbox (toggle, wolny tekst) – na wierzchu tylko nowe wpisy inwestora (po przebiegu pusto);
│     „❓ Czeka na Twoją odpowiedź” (wpisy z pytaniem asystenta) i „Przetworzone” (zwijany blok na każdy dzień: linia „🤖” + ślad)
├─ ✅ Zadania (toggle) → TASKS (2) (baza)
├─ zakładki:
│  ├─ 🏗 Etap → baza Harmonogram (widok „📅 Oś czasu”), nagłówek „🔴 Do zamknięcia przed stanem zero” (checklista
│  │     bieżącego etapu), strony: Stan zero – punkty bez odwrotu (bramki), Plan przepustów i tras instalacji,
│  │     Etapy budowy – przewodnik; baza Zamówienia i dostawy
│  ├─ 📒 Notatnik → Notatnik budowy (baza): pytania, decyzje, ryzyka, „pamiętać” – bez daty zdarzenia
│  ├─ 📓 Dziennik → Dziennik budowy (baza): co się działo na budowie danego dnia
│  ├─ 📚 Wiedza → strona Baza wiedzy (Tematy, Informacje, Rozmowy i źródła, Rejestr sprzeczności)
│  ├─ 👷 Wykonawcy → „Wybór wykonawcy – stan zero” (rundy, zakres, wagi) + baza Porównanie wykonawców; baza Umowy i gwarancje
│  └─ 🗂 Więcej → Przeglądy dzienne, Przeglądy tygodniowe, Kontakty – kluczowe role (pełna lista w Excelu), zdjęcia i linki, Archiwum – stare notatki
├─ 💡 Pomysły na rozwój (toggle) → baza Pomysły na rozwój (widok „💡 Tablica”): pomysły inwestora na harness i setup + analizy
└─ 🤖 Dla asystenta (toggle) → 📑 Przewodnik po dokumentach i Notion, Asystent AI – harness (wersja + skrzynka
      Zmiany do harnessu), nagłówek „📐 Dane projektu (ściąga)” – JEDYNE źródło ściągi
```

| Czego szukasz | Gdzie (strona / baza → widok/sekcja) | ID | Najważniejsze pola |
|---|---|---|---|
| Luźne wpisy do przetworzenia; pytania asystenta do inwestora | DOM → „📥 Inbox” (toggle): bloki 1. poziomu = nowe wpisy; „❓ Czeka na Twoją odpowiedź” = wpisy z pytaniem (odpowiedź pod pytaniem); „Przetworzone” = ślad, zwijany blok na dzień | `24af5982-09e7-806b-821a-e157ff33be42` | – (wolny tekst) |
| Parametry projektu | DOM → „🤖 Dla asystenta” → „📐 Dane projektu (ściąga)” | `24af5982-09e7-806b-821a-e157ff33be42` | – |
| Jakie mamy dokumenty, co w którym jest, gdzie leżą | 📑 Przewodnik po dokumentach i Notion (generowany – nie edytuj) | `3f6f5982-09e7-81f5-bade-ec877d8d936a` | – |
| Co blokuje bieżący etap | DOM → zakładka 🏗 Etap → „🔴 Do zamknięcia przed …”; Notatnik → widok „🔴 Krytyczne i otwarte” | `view://3f3f5982-09e7-8125-a50b-000ce287ad48` | Status Otwarte/Do omówienia, Priorytet Krytyczne/Ważne |
| Otwarte pytania do konstruktora, architekta, kierownika… | Notatnik → „❓ Pytania do projektantów” (wg Do kogo) | `collection://7423414a-707b-415f-8751-c6ab7ebb6753`, `view://3f3f5982-09e7-81d2-a527-000caeaed4ea` | Typ Pytanie/Decyzja, Status otwarte, **Do kogo** |
| Co ustaliliśmy, decyzje | Notatnik → „✅ Ustalone i zrobione” | `view://3f3f5982-09e7-8172-a666-000cb0777dc1` | Status Ustalone/Zrobione/Odrzucone, Typ Decyzja |
| Notatki wg etapu / branży | Notatnik → „🏗 Wg etapu”, „🔧 Wg branży” | `view://3f3f5982-09e7-81f8-9782-000c7f49c705`, `view://3f3f5982-09e7-81e7-bfd0-000c9c2a8e8c` | Etap, Branża, Temat, Dziennik budowy |
| Kroki budowy w czasie, kto, zależności | Harmonogram → widok „📅 Oś czasu” | `collection://d7a479ab-1e23-453f-8f59-55f4097f7d04`, `view://3f7f5982-09e7-814f-bb28-000c12b8d4f1` | Krok, Nr etapu (= Excel Etapy), Termin, Kto, Status, Pewność terminu, Bez odwrotu, Zależy od/Blokuje, Zadania, Zamówienia, Umowa |
| Co inni mają zrobić i do kiedy („czekam na”) | TASKS → widok „⏳ Czekam na” (PLANNED = WAITING) | `view://3f7f5982-09e7-8126-9825-000cc472cb4d` | Kto, When, Desc, Harmonogram |
| Co zamówić i kiedy, dostawy | Zamówienia i dostawy → widok „🛒 Do zamówienia” | `collection://a9854c6c-43ec-4bc1-8ef0-273fb02261c7`, `view://3f7f5982-09e7-813b-8e74-000c6cb595e9` | Zamówić do, Dostawa, Status, Kto zamawia, Krok |
| Umowy, odbiory, gwarancje | Umowy i gwarancje → widok „🛡 Gwarancje” | `collection://60c06f30-7867-435d-8f2e-1e025a3daa5c`, `view://3f7f5982-09e7-81a0-9f52-000c2fddf3d0` | Rodzaj, Strona, Status, Odbiór, Gwarancja do, Rękojmia do, Zgłaszanie usterek, Kroki |
| Zadania z terminem | TASKS (2) → „Today”, „ToDo/Doing”, „📆 Kalendarz”; terminy także w Notatniku (Kiedy) | `collection://2a9f5982-09e7-81be-91e8-000b0e10a05e`, `view://2a9f5982-09e7-81b5-8a7d-000c3a8c8d35`, `view://2a9f5982-09e7-81ee-b1e2-000cb63e2408` | When, PLANNED (status), **Kto**, Priority, Kategoria, Harmonogram |
| Porównanie ofert wykonawców | Wybór wykonawcy – stan zero → tabela porównawcza (karta = wykonawca) | `3f3f5982-09e7-81e8-b361-c7bee2e3847d`, `collection://f7ca5f38-8fc3-46e7-8345-8a32cc8b5215` | Status (… Finał – spotkanie/Wybrany/Odpada), Knock-out OK, Zgodny z projektem, Ocena, Do dopytania |
| Co mówili wykonawcy, na kogo czekamy | Wybór wykonawcy → „🗒 Co już wiem z rozmów i ofert” | jw. | – |
| Kryteria wyboru ekipy, umowa | Wybór wykonawcy → Runda 1–3, 📄 Umowa, ⚖️ Kryteria i wagi | jw. | – |
| Co wiemy o temacie X | Baza wiedzy → Tematy | `3f4f5982-09e7-8193-a68e-fd35c9265012`, `collection://718422ca-ed6f-4269-a38f-4e508eff286c` | W skrócie, Stan wiedzy, Etap, Branża |
| Pojedyncze fakty ze źródeł | Baza wiedzy → Informacje; zakładki „🆕 Do przejrzenia”, „⭐ Kluczowe i ważne”, „💬 Z moim komentarzem”, „🎯 Na teraz – [bieżący etap]” (`view://3f7f5982-09e7-81bf-a377-000c19ce62cc`); niżej blok „🗂 Wiedza wg etapu” z zakładką na każdy etap | `collection://f78bb02d-6da5-46fb-bea9-c25e15f93117`, `view://3f4f5982-09e7-8124-95b3-000c5c02a4a2`, `view://3f7f5982-09e7-8141-80df-000c6d072a1e`, `view://3f7f5982-09e7-81cc-a5ff-000cd6d89601` | Status, **Istotność** (Kluczowe/Ważne/Ciekawostka), **Mój komentarz** (inwestora), Dotyczy nas, **Etap** (kiedy potrzebne), Pokazano, Potwierdzenia, Tematy, **Źródła** (ZRD) lub **Notatnik** (ustalenie) |
| Kto i kiedy coś powiedział | Baza wiedzy → Rozmowy i źródła | `collection://35453d82-e38d-4797-840c-d19677c71b54` | Data, Forma, Z kim, Typ autora, Wiarygodność |
| Sprzeczności do decyzji (SP-n) | Rejestr sprzeczności → „⏳ Czeka na Twoją decyzję” | `collection://7589d5f5-2d22-4b85-9138-72cd34d4a1f8`, `view://3f4f5982-09e7-8152-92b1-000c4785d478` | ID, Status, Priorytet, Tematy, Decyzja |
| Co się działo na budowie | Dziennik budowy → „📓 Ostatnie 7 dni”, „⚠️ Otwarte problemy” | `collection://cc113d57-3eaa-4f52-80f6-e4b39a4b4c92`, `view://3f5f5982-09e7-8192-847e-000c8ff6aba3`, `view://3f5f5982-09e7-8122-8524-000cb554728c` | Data, Etap, Krok, Problemy / usterki, Roboty dodatkowe, Przed zakryciem OK |
| Bramki „bez odwrotu” | Stan zero – punkty bez odwrotu (Bramki 0–6) | `3f4f5982-09e7-81d2-bcae-ee5500a80c20` | – |
| Przepusty, rury, trasy instalacji | Plan przepustów i tras instalacji | `3f4f5982-09e7-81fd-a382-dd14ab860ca2` | – |
| Kolejność prac, co ustalić przed etapem | Etapy budowy – przewodnik | `3f3f5982-09e7-8161-b30e-fdcf2284554b` | – |
| Ostatni przegląd tygodnia | Przeglądy tygodniowe | `3f4f5982-09e7-8144-af5e-f9521a52ea9d` | – |
| Przegląd dnia (dziś / jutro, „rozkminki”; ręczne przebiegi z dopiskiem „(ręczne)”) | 📆 Przeglądy dzienne | `3f8f5982-09e7-815e-8b03-eacaa74db190` | – |
| Zasady asystenta, wersja harnessu | Asystent AI – harness budowy | `3f4f5982-09e7-81f5-b7f9-d6cf5d79bb34` | – |
| Zgłoszone poprawki harnessu | Zmiany do harnessu | `collection://e217448a-60ec-4af6-8584-8f368315109c` | Status, Procedura, Rodzaj |
| Pomysły na rozwój harnessu i setupu (do analizy, nie wchodzą same) | DOM → „💡 Pomysły na rozwój” → „💡 Tablica” | `collection://fdee4f05-8f43-4be4-a0d5-2b88642fa6d3`, `view://3f7f5982-09e7-81f6-97bf-000cb7996ef0` | ID (POM-n), Status, Obszar, Nakład, Wymaga ode mnie; analiza w treści strony |
| Stare notatki sprzed systemu | Archiwum – stare notatki (tylko do wglądu; przydatne rzeczy są w Notatniku) | `3f3f5982-09e7-817c-bab8-f439d883e6ce` | – (nie zapisuj tam) |

**Słowniki.** Etap: Projekt i formalności / Stan zero / SSO / Deweloperski / Wykończenie / Teren i ogród / Cała budowa.
Notatnik – Typ: Pamiętać/Pytanie/Decyzja/Ryzyko/Doczytać/Pomysł; Status: Otwarte/Do omówienia/Ustalone/Zrobione/Odrzucone;
Priorytet: Krytyczne/Ważne/Zwykłe; Do kogo: Konstruktor/Architekt/Geotechnik/Kierownik budowy/Ekipa/Instalator/Dekarz/Ja.
Pełne schematy: `notatka/references/notion-schematy.md`, `wiedza/references/notion-wiedza.md`, `dziennik/references/notion-dziennik.md`.
Liczby (kosztorys, wydatki, oferty, kontakty wykonawców) – Excel; kwoty w Notion są pomocnicze, przy rozbieżności wygrywa Excel.
