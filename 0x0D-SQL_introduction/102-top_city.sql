-- displays the average temperature of top 3 city during july and august
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3; 
