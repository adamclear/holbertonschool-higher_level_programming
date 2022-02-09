-- displays the average temperatures for cities from db, temperatures
SELECT city,
AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp
DESC;