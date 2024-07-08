-- List all cities in of California
-- List in ascending order of cities.id
SELECT id, name
FROM 
    cities
WHERE
    state_id IN (
	SELECT id FROM states WHERE name = 'California'
    )
ORDER BY id ASC;
