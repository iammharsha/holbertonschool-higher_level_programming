-- List all records of table second_table in db hbtn_0c_0
-- Don't list record is name doesn't have a value
-- Display column score, name in this order
-- Order is based on score in descending order
SELECT 
    score, name 
FROM 
    second_table
WHERE
    name IS NOT NULL 
    AND name != ''
ORDER BY score DESC;