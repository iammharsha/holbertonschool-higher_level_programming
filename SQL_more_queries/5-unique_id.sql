-- Create table unique_id with columns
-- id INT default value 1 and must be unique
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
