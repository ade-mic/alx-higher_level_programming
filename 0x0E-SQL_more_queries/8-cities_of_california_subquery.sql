-- lists all the cities of califonia that can be found in the databae hbtn_0d_usa
SELECT id, name FROM cities
NATURAL JOIN states ON cities.state_id = states.id
WHERE states.name='California' ORDER BY cities.id DESC;
