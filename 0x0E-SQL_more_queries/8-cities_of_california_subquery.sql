-- lists all the cities of califonia that can be found in the databae hbtn_0d_usa
SELECT id, name FROM cities INNER JOIN states WHERE states.name='California' ORDER BY cities.id DESC;
