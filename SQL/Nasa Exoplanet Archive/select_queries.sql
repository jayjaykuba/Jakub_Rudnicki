CREATE DATABASE exoplanets;
USE exoplanets;
CREATE TABLE planets (
    pl_hostname VARCHAR(255),
    pl_letter VARCHAR(10),
    pl_discmethod VARCHAR(100),
    pl_orbper DOUBLE,
    pl_rade DOUBLE,
    pl_bmasse DOUBLE,
    pl_facility VARCHAR(255)
);
LOAD DATA LOCAL INFILE 'C:\\Users\\Erazer\\Desktop\\sql\\NASA exoplanet\\planets_clean.csv'
INTO TABLE planets
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
-- table data import wizard niestety zaimportował tylko część danych z pliku csv, stąd import danych za pomocą komendy. 
SELECT*FROM planets;
SELECT pl_hostname AS Gwiazda, COUNT(*) AS Liczba_planet FROM planets group by pl_hostname order by liczba_planet DESC;
SELECT COUNT(*) AS Liczba_gwiazd_z_jedną_planetą FROM (SELECT pl_hostname FROM planets GROUP BY pl_hostname HAVING COUNT(*) = 1) AS jednoplanetowe;
SELECT COUNT(*) AS Gwiazdy_z_8_planetami FROM (SELECT pl_hostname FROM planets GROUP BY pl_hostname HAVING COUNT(*) = 8) AS ośmioplanetowe;
SELECT COUNT(*) AS Liczba_gwiazd, Liczba_planet
FROM (
    SELECT pl_hostname, COUNT(*) AS Liczba_planet
    FROM planets
    GROUP BY pl_hostname
) AS zliczone_planety
GROUP BY Liczba_planet
ORDER BY Liczba_planet;
-- zestawienie liczby gwiazd pojadiających poszególną liczbę planet (od 1 do 8)
SELECT pl_discmethod AS Metoda_wykrycia_gwiazdy, COUNT(*) AS Ilość_wykryć FROM planets group by pl_discmethod order by Ilość_wykryć DESC;
-- egzoplanety według metody wykrycia
select pl_facility AS instytucja_lub_teleskop, COUNT(*) AS Liczba_odkryć FROM planets group by pl_facility order by Liczba_odkryć DESC;
-- egzoplanety według odkrywcy
select pl_name AS Planeta, pl_orbper AS Okres_orbitalny_planety_w_dniach FROM planets order by Okres_orbitalny_planety_w_dniach DESC LIMIT 5;
select pl_name AS Planeta, pl_orbper AS Okres_orbitalny_planety_w_dniach FROM planets order by Okres_orbitalny_planety_w_dniach LIMIT 5;
select pl_hostname AS Gwiazda, st_massn AS masa_gwiazdy_w_jednostkach_masy_Słońca FROM planets order by masa_gwiazdy_w_jednostkach_masy_Słońca DESC; -- najcięższe gwiazdy z egzoplanetami
select pl_hostname AS Gwiazda, st_rad AS promień_gwiazdy FROM Planets WHERE st_rad > 50 order by promień_gwiazdy DESC; -- największe gwiazdy, wielkość wyrażona w jednostkach promienia Słońca
SELECT LEFT (TRIM(UPPER(pl_hostname)), 1) AS Pierwszy_znak_gwiazdy, COUNT(DISTINCT pl_hostname) AS liczba_gwiazd FROM planets group by Pierwszy_znak_gwiazdy Order by liczba_gwiazd DESC;
select COUNT(distinct(pl_hostname)) AS Libcza_unikalnych_gwiazd FROM planets;
select pl_name AS Planeta, CASE 
WHEN pl_pnum = 6 THEN 'największa planeta' 
WHEN pl_pnum = 1 THEN 'najmniejsza planeta' 
ELSE 'średnia planeta' 
END AS Rozmiar_planety FROM planets;
-- planety o rozmiarze 6 przedstwione jako największe o rozmiarze 1 jako najmniejsze reszta planet średnia
SELECT Distinct pl_hostname AS Gwiazda, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets ORDER BY st_teff;
SELECT Distinct pl_hostname AS Gwiazda, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets ORDER BY st_teff DESC;
SELECT Distinct pl_hostname AS Gwiazda, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets ORDER BY st_teff LIMIT 5;
SELECT Distinct pl_hostname AS Gwiazda, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets ORDER BY st_teff DESC LIMIT 5;
SELECT distinct pl_hostname AS Gwiazda, st_teff, CASE WHEN st_teff > 6500 THEN 'Najgorętsze gwiazdy'
WHEN st_teff < 3500 THEN 'Najchłodniejsze gwiazdy'
ELSE "Gwiazdy pośrednie"
END AS Grupa_gwiazdy_wg_temperatury FROM planets
ORDER BY CASE
WHEN st_teff > 6500 THEN 1
WHEN st_teff BETWEEN 3500 AND 6500 THEN 2
ELSE 3
END;
/* Gwiazdy podzielone na grupy według temperatury powierzhni powyżej 6500 stopni kelwina jako najgorętsze gwiazdy poniżej 3500 stopni jako najchłodniejsze reszta jako pośrednie.
Następnie posortowano gwiazdy w kolejności od grup: najgorętszych, pośrednich i najchłodniejszych. */
SELECT pl_name AS Planeta, pl_controvflag AS Flaga_kontrowersyjności FROM planets ORDER BY pl_controvflag;
SELECT pl_name AS Planeta, pl_controvflag AS Flaga_kontrowersyjności FROM planets WHERE pl_controvflag = 1;
SELECT pl_name AS Planeta, CASE WHEN pl_controvflag = 1 THEN "TAK"
ELSE "NIE"
END AS Czy_planeta_jest_kontorwersyjna FROM planets
ORDER BY pl_controvflag DESC;
-- Planety zostały podzielone na grupy czy sposób ich wykyrcia jest konrowersyjny i budzi wątpliwości (tak/nie). Posortowano wyniki tak, że najpierw pokazują się planety kontrowersyjne
SELECT pl_name AS Planety_kontorwersyjne FROM planets WHERE pl_controvflag = 1;
-- Pokazanie tylko planet kontrowersyjnych
select DISTINCT pl_hostname AS Gwiazda, st_massn AS masa_gwiazdy_w_jednostkach_masy_Słońca, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets WHERE st_massn = 6 AND st_teff < 3500;
-- pokzanie planet o największej masie i temperaturze poniżej 3500 stopni kelwina
select DISTINCT pl_hostname AS Gwiazda, st_massn AS masa_gwiazdy_w_jednostkach_masy_Słońca, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets WHERE st_massn = 6 AND st_teff > 6000;
-- pokazanie planet o największej masie i temperaturze powyżej 6000 stopni kelwina
select DISTINCT pl_hostname AS Gwiazda, st_massn AS masa_gwiazdy_w_jednostkach_masy_Słońca, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets WHERE st_massn = 1 AND st_teff < 3500;
-- pokzanie planet o najmniejszej masie i temperaturze poniżej 3500 stopni kelwina
select DISTINCT pl_hostname AS Gwiazda, st_massn AS masa_gwiazdy_w_jednostkach_masy_Słońca, st_teff AS Temperatura_powierzchni_gwiazdy FROM planets WHERE st_massn = 1 AND st_teff > 6500;
-- pokazanie planet o najmniejszej masie i temperaturze powyżej 6000 stopni kelwina
select  COUNT(pl_hostname) AS Liczba_gwiazd, AVG(st_massn) AS masa_gwiazdy_w_jednostkach_masy_Słońca from planets;
-- średnia masa wszystkich gwiazd posiadających egzoplanety
select COUNT(pl_hostname) AS Liczba_gwiazd, AVG(st_massn) AS masa_gwiazdy_w_jednostkach_masy_Słońca, AVG(st_teff) AS Temperatura_powierzchni_gwiazdy FROM planets;
-- średnia masa oraz temperatura wszystkich gwiazd posiadających egzoplanety
select distinct pl_hostname AS Gwiazda, st_dist AS odległość_od_Ziemii FROM planets ORDER BY st_dist LIMIT 3;
-- 3 najbliżej znajdujące się od Ziemii gwiazdy posiadające egzoplanety. Odległość w parsekach (1 parsek = 3,26 lat świetlnych).
select distinct pl_hostname AS Gwiazda, st_dist AS odległość_od_Ziemii FROM planets ORDER BY st_dist DESC LIMIT 3;
-- 3 najdalej znajdujące się od Ziemii gwiazdy posiadające egzoplanety. Odległość w parsekach (1 parsek = 3,26 lat świetlnych).
select pl_name AS Planeta, pl_orbsmax AS średnia_odległość_planety_od_gwiazdy from planets ORDER by pl_orbsmax;
select pl_name AS Planeta, pl_orbsmax AS średnia_odległość_planety_od_gwiazdy from planets ORDER by pl_orbsmax LIMIT 3;
/* Średnia odległość planety od gwiazdy – określa jak daleko egzoplaneta krąży od swojej gwiazdy, podane w jednostkach astronomicznych (AU). 
1 AU to średnia odległość Ziemi od Słońca (~150 mln km). W zapytaniu wybrano 3 najbliżej krążące swojej gwiazdy egzoplanety */
select SUM(st_dist) AS suma_odległości_gwiazd_od_Ziemii from planets;
select pl_name AS Planeta, pl_orbsmax AS średnia_odległość_planety_od_gwiazdy from planets ORDER by pl_orbsmax DESC LIMIT 3;
-- 3 nadalej krążące od swoich gwiazd egzoplanety
select AVG(pl_orbsmax) AS średnia_odległość_planety_od_gwiazdy from planets;
-- wyliczenie średniej odległości wszystkich egzoplanet od gwiazd
select COUNT(pl_name) AS liczba_egzoplanet, AVG(pl_orbsmax) AS średnia_odległość_planety_od_gwiazdy from planets;
-- wyliczenie średniej odległości wszystkich egzoplanet od gwiazd i liczba wszystkich egzoplanet
select SUM(st_dist) AS Suma_odległości_gwiazd_od_Ziemii, COUNT(distinct pl_hostname) AS Liczba_gwiazd from planets;
-- suma odległości gwiazd z egzoplanetami od Ziemii
select AVG (length(pl_hostname)) from planets;
-- wskazuje średnią długość znaków w nazwie gwiazd, powstaje jednak problem, bo niektóre planety się powtarzają (mają więcej niż 1 egzoplanetę)
select AVG (length(pl_hostname)) AS średnia_ilość_znaków_nazwy_gwiazd from (select distinct pl_hostname from planets) AS unikalne_gwiazdy;
--  wskazuje średnią długość znaków w nazwie gwiazd, gwiazdy się nie powtarzają
select MIN(length(pl_hostname)) AS długość_znaków_nazwy_gwiazdy from planets;
select MAX(length(pl_hostname)) AS długość_znaków_nazwy_gwiazdy from planets;
SELECT COUNT(*) FROM planets;
SELECT DISTINCT COUNT(*) FROM planets;
SELECT COUNT(DISTINCT pl_name) FROM planets;
