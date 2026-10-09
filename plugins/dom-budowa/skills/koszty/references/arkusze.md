# Excel „Kosztorys_stan_zero.xlsx” – układ (stan: 2026-10-09)

Plik prowadzi inwestor ręcznie; poniższy opis może się zdezaktualizować – jeśli plik wygląda inaczej,
pracuj na faktycznym układzie i zaproponuj aktualizację tego pliku (procedura `rozwoj-harnessu`).

## Arkusze (kolejność)
Instrukcja · Podsumowanie · Realizacja · Wydatki · Wykonawcy · Oferty · Porównanie ofert · Etapy · Kosztorys ·
Parametry · Cennik · Porównanie · Zestawienie.

## Kolumny wejściowe (wpisywane ręcznie)
- **Wydatki!A:K** – Data, Status (Zrealizowane/Planowane), Kwota, Etap (lista z Etapy!A), Kod (opcj.), Typ
  (Materiał/Robocizna/Sprzęt/Usługa), Sposób (Gotówka/Przelew/Karta/BLIK), Kto płacił, Opis, Dostawca / nr FV, Notatki.
  L:N liczą się same (Stan, Miesiąc, Nazwa z cennika).
- **Oferty!A:H + J:O** – Wykonawca (lista z Wykonawcy!A), Nr/data, Etap/Stan (główny), Obejmuje etapy („02,05,07”),
  Kod, Zakres, Kwota netto, VAT (0%/8%/23%) | Materiał w cenie? (Tak/Nie/Częściowo/Tylko materiał), Zgodna z projektem?
  (Tak/Nie/Do sprawdzenia), Termin, Status (Otrzymana/Negocjacje/Wybrana/Odrzucona), Ocena 1–5, Uwagi.
  I (brutto), P–R (stan, plan dla zakresu, różnica) liczą się same. Robocizna i materiał tej samej firmy = osobne wiersze.
- **Wykonawcy!A:K** – Wykonawca, Branża, Telefon, E-mail, Dzwonione (T/N), E-mail wysłany (T/N), Status, Dostępność,
  Ocena, Notatki, Etap domyślny. L:N (liczba i suma ofert, wybrany) liczą się same.
- **Cennik!H** – cena z oferty (nadpisuje średnią min–max).
- **Kosztorys!G / P** – ilość (nadpisanie formuły) / wykonawca pozycji (Sam/Ekipa).
- **Etapy!C / D** – Wykonawca etapu (Ekipa/Sam), Uwzględnij (1/0).
- **Parametry!B** – wymiary i założenia.
- **Realizacja!J** – etap zakończony (1/0).
- **„Porównanie ofert”!G4:P4** – nazwy porównywanych wykonawców.

## Trzy warstwy liczb
PLAN = Kosztorys/Etapy; UMÓWIONE = Oferty „Wybrana”; WYDANE = Wydatki „Zrealizowane” („Planowane” = zobowiązania).
