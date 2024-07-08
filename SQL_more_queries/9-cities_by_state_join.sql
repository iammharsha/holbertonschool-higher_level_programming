-- List all cities in DB with name of state
-- List the cities in ascending order of cities.id
SELECT 
    cities.id, cities.name, states.name
FROM 
    cities, states
WHERE
    cities.state_id = states.id
ORDER BY cities.id ASC;
