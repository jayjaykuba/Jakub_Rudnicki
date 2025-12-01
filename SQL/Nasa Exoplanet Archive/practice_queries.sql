
ALTER TABLE planets RENAME COLUMN pl_hostname TO gwiazda;
ALTER TABLE planets RENAME COLUMN pl_name TO planeta;
ALTER TABLE planets DROP COLUMN st_tefflim;
ALTER TABLE planets DROP column pl_orbeccenlim;
ALTER TABLE planets ADD COLUMN testowa INT;
ALTER TABLE planets DROP COLUMN testowa;
ALTER TABLE planets ADD COLUMN test varchar(30);
update planets SET test='brak_danych' WHERE test IS NULL;
/* trzeba było wyłączyc safe updates aby wykonać to zapytanie modyfukujące całą kolumnę. Kroki niezbędnego do tego 
Przejdź do Edit → Preferences → SQL Editor
Odznacz opcję "Safe Updates" (Require WHERE clause on UPDATE and DELETE statements)
Zrestartuj połączenie z bazą danych */
ALTER TABLE planets DROP COLUMN test;
ALTER TABLE planets ADD COLUMN nowa varchar(55) default 'Brak_danych';
SET SQL_SAFE_UPDATES = 0;
UPDATE planets 
SET nowa = NULL 
WHERE nowa = 'Brak_danych';
SET SQL_SAFE_UPDATES = 1;
-- problem z zapytaniem 17 do 22 nie chce zamieniać w kolumnie nowa Brak_danych na cokolwiek innego
ALTER TABLE planets ADD COLUMN liczby INT default 1;
SET SQL_SAFE_UPDATES = 0;
UPDATE planets 
SET liczby = 2 
WHERE liczby = 1;
SET SQL_SAFE_UPDATES = 1;
INSERT INTO planets (gwiazda, planeta) VALUES ('testowa', 'testowa_a');
INSERT INTO planets (gwiazda) VALUES ('Ziemia2');
UPDATE planets SET gwiazda = 'brak_danych' WHERE gwiazda = 'Ziemia2';
UPDATE planets SET pl_letter = 'a' WHERE gwiazda = 'testowa';
UPDATE planets SET pl_discmethod = 'mój_wymysł', pl_controvflag = 1 WHERE gwiazda ='brak_danych';
DELETE FROM planets where gwiazda = "brak_danych" limit 1;
UPDATE planets SET pl_pnum = 1, pl_discmethod = 'wymyśliłem', pl_controvflag = 1 WHERE gwiazda='testowa';
DELETE FROM planets where gwiazda ='testowa' limit 1;
DELETE FROM planets where gwiazda ='Ziemia2' limit 1;
update planets SET planeta = 'Ziemia2a', pl_discmethod = 'wymyślona' where gwiazda = 'Ziemia2';
CREATE TABLE stars AS
SELECT DISTINCT
  gwiazda AS star_name,
  st_teff,
  st_mass
FROM planets;
CREATE TABLE exoplanets AS
SELECT planeta,
gwiazda AS star_name,
pl_orbper,
pl_orbsmax
FROM planets;
ALTER TABLE stars MODIFY COLUMN star_name VARCHAR(100);
ALTER TABLE stars ADD PRIMARY KEY (star_name);
ALTER TABLE exoplanets MODIFY COLUMN star_name VARCHAR(100);
ALTER TABLE exoplanets
ADD CONSTRAINT fk_star
FOREIGN KEY (star_name) REFERENCES stars(star_name);
describe exoplanets;
describe stars;
-- sposób na szybkie podejrzenie właściowości kolum
select*from stars s inner join exoplanets e ON s.star_name = e.star_name;
select*from stars s left join exoplanets e ON s.star_name = e.star_name;
select*from stars s right join exoplanets e ON s.star_name = e.star_name;
select*from stars s full join exoplanets e ON s.star_name = e.star_name;
-- okazało się, że mySQL nie obsłguje full join trzeba zrobić union z left join i right join
SELECT * FROM stars s LEFT JOIN exoplanets e ON s.star_name = e.star_name
UNION
SELECT * FROM stars s RIGHT JOIN exoplanets e ON s.star_name = e.star_name;
SELECT * FROM stars s CROSS JOIN exoplanets e;
-- tworzony jest iloczyn kartezjański czyli każdy wiersz z pierwszej tabeli jest łączony z każdym wierszem drugiej tabeli




