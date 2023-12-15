-- lists all the cities of califonia that can be found in the databae hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
