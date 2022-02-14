-- lists all the cities of CA that can be found in DB hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name
    LIKE 'California'
)
ORDER BY id ASC;
