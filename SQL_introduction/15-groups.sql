-- Return list of number of records as number with same score in second_table
-- Display score, count of score as number in this order
-- Sort the list based on number (top first)
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;