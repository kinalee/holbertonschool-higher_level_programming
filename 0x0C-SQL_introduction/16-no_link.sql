-- Lists all records of the table second_table
SELECT score, name from second_table
WHERE name IS NOT NULL ORDER BY score DESC;
