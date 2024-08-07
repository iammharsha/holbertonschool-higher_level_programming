-- Create if not exists database hbtn_0d_usa
-- Create if not exists table cities (in the database hbtn_0d_usa) with columns
-- id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
