-- lists all the cities of califonia that can be found in the databae hbtn_0d_usa
SELECT id, name FROM cities NATURAL JOIN states WHERE name='Califonia' ORDER BY cities.id DESC;
