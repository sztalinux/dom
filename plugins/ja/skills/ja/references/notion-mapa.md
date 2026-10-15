# Notion – sprawy osobiste (mapa)

Mapa dla asystenta: gdzie szukać i dokąd zapisywać sprawy pozabudowlane. Same struktury i identyfikatory – treść jest w Notion.
Plik trafia do przewodnika (`tools/dokumenty.py`) – strona Notion „📑 Przewodnik po dokumentach i Notion”.
Zmiana struktury (nowa baza, widok, pole, sekcja) → zaktualizuj ten plik (procedura `rozwoj-harnessu`).

Strona **📓 Dziennik** `3f8f5982-09e7-80c8-a154-c59aeb844e8f` (najwyższy poziom) – jedno wejście na wszystko:

```
📓 Dziennik
├─ Jak używać (toggle)
├─ nowe wpisy inwestora – bloki 1. poziomu i podstrony (po przebiegu pusto)
├─ ### ❓ Czeka na Twoją odpowiedź (toggle) – wpisy z pytaniem asystenta, odpowiedź pod pytaniem
├─ ### Przetworzone (toggle) – zwijany blok na każdy dzień: linia „🤖” + ślad „~~wpis~~ → gdzie”
├─ ### 🧭 Dla asystenta (toggle) – baza 🧭 Obszary Dziennika, wzmianka przewodnika
└─ 📆 Przeglądy dzienne (podstrona)
```

| Czego szukasz | Gdzie | ID | Najważniejsze pola |
|---|---|---|---|
| Nowe wpisy, pytania asystenta | 📓 Dziennik (schemat wyżej) | `3f8f5982-09e7-80c8-a154-c59aeb844e8f` | – (wolny tekst) |
| Podział wpisów na obszary (dokąd co idzie) | 🧭 Obszary Dziennika | `collection://253b7564-00ac-45b2-a3f4-956275e3a7e0` | Obszar, Rozpoznawanie, Gdzie, Jak zapisać, Procedura, Aktywny, Kolejność, Przykład |
| Przegląd dnia (dziś / jutro; ręczne przebiegi „(ręczne)”) | 📆 Przeglądy dzienne (pod Dziennikiem) | `3f8f5982-09e7-815e-8b03-eacaa74db190` | – |
| Wszystkie zadania (dom i prywatne) | TASKS (fizycznie na stronie DOM) | `collection://2a9f5982-09e7-81be-91e8-000b0e10a05e` | Name, **Obszar** (Dom / Prywatne / Dziecko / Praca; puste = Dom), PLANNED, When, Priority, Kategoria, Kto, Desc |
| Zadania prywatne / dziecka / jutro | TASKS → „🏠 Prywatne”, „👪 Dziecko”, „📅 Jutro – wszystko” | `view://3faf5982-09e7-81f9-9832-000c4e6b8e97`, `view://3faf5982-09e7-81aa-8e09-000c3fb8e29f`, `view://3faf5982-09e7-818a-9939-000cb6095c9c` | – |
| Emocje (jeden wiersz = jedna emocja) | Dziennik emocji → Wpisy emocji | `collection://41556944-46fa-4155-ae95-5b74b983d7aa` | Wpis (nazwa emocji), Kiedy, Intensywność, Trigger / co się stało, Ciało, Myśl, Potrzeba, Reakcja, Emocja wtórna, Czynniki podatności |
| Podsumowania dni emocji (tylko na prośbę) | Dziennik emocji → Dni (dziennik emocji) | `collection://15f206a7-3832-472f-9ed6-b01a515193e1` | Dzień, Data, Podsumowanie (opcjonalnie) |
| Dzień pracy | Dziennik emocji → Dziennik produktywności (praca) | `collection://4b0ef0a5-859e-42e0-98fa-673510b4629c` | Data (tytuł), Początek pracy, Koniec pracy, Ocena produktywności (1–10), Opis pracy, Przerwy i przeszkadzajki, Multitasking |
| Notatki o dziecku | Strona dziecka (nazwa = imię) | `241f5982-09e7-8023-9793-fa12d36bdb2e` | sekcje: 💬 Do przegadania, 🎁 Prezenty, 📝 Obserwacje i informacje, 💡 Pomysły (zabawy, wyjazdy, książki), 🩺 Zalecenia (fizjoterapia, przedszkole), 🗄 Archiwum |
| Książki dla dziecka | strona dziecka → 💡 Pomysły → baza Ksiazki | `collection://32ff5982-09e7-809c-b4ac-000b8a8bf9ac` | Name |
| Suplementy | Suple | `collection://0771d295-5bc0-46e3-b0cb-def13bccab8d` | Name, Status (TAKING / BREAK / TO START / SUSPENDED), **Buy**, Who, When, Last break, Type |
| Książki do przeczytania | Books → All | `collection://5b028761-478a-4d72-acfd-6082043487c2` | Name, Author, Status (To read…), Priority (Must/Should/May), Area |
| Poprawki sposobu pracy asystenta | Zmiany do harnessu | `collection://e217448a-60ec-4af6-8584-8f368315109c` | Zmiana, Status, **Plugin**, Procedura, Rodzaj, Treść do wdrożenia, Dlaczego |
| Pomysły na rozwój harnessu | Pomysły na rozwój (na stronie DOM) | `collection://fdee4f05-8f43-4be4-a0d5-2b88642fa6d3` | ID (POM-n), Status, Obszar, Nakład, Wymaga ode mnie |
| Wersja harnessu | Asystent AI – harness | `3f4f5982-09e7-81f5-b7f9-d6cf5d79bb34` | – |

**Archiwa (tylko do wglądu, nie zapisuj):** ALL TODOS (stara lista zadań, wszystko ARCHIVED 15.10.2026), lista „TO DO”
na stronie Quick notes (przeniesiona do TASKS). Strona WORK ma własną bazę zadań z pracy – nie zapisuj tam; zadania z pracy
wpisane do Dziennika idą do TASKS z Obszar = Praca.
