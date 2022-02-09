-- shows the max temp from each state, alphabetically by state code
SELECT state,
MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;