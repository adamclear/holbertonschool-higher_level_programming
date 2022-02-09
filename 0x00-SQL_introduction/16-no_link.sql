-- lists all records of second_table with a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) <> ''
ORDER BY score
DESC;