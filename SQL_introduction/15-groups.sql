-- Return list of number of records as number with same score in second_table
-- Sort the list based on number (top first)
SELECT COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;