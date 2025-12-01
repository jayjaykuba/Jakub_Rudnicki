Projekt przedstawia praktyczną analizę danych z NASA Exoplanets Archive (dane z roku 2021), czyli największej publicznej bazy zawierającej potwierdzone egzoplanety oraz parametry ich gwiazd.
Celem projektu było:

- przećwiczenie zapytań SQL na realnym, dużym zestawie danych,

 - wyszukanie ciekawych rekordów i statystyk,

 - uporządkowanie plików i stworzenie repozytorium portfolio.

Dane zostały pobrane z NASA jako plik CSV, następnie oczyszczone tak, aby można je było bez błędów załadować do MySQL Workbench.

├── 📄 planets_raw.csv
│   – oryginalny plik z NASA Exoplanet Archive (nieedytowany)

├── 📄 planets_clean.csv
│   – plik oczyszczony: poprawione nagłówki, usunięte błędy formatowania, przygotowany do importu do MySQL

├── 📄 select_queries.sql
│   – główne zapytania SELECT użyte do wyszukiwania ciekawostek

├── 📄 practice_queries.sql
│   – zestaw ćwiczeń SQL modyfikujących tabelę (ALTER, UPDATE, DELETE itd.)
