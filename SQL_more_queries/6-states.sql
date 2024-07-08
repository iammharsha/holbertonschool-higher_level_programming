-- Create database if not exists hbtn_0d_usa
-- Create table if not exists states in db hbtn_0d_usa with columns
-- id INT unique, auto generating, can't be null and primary key
-- name VARCHAR(256)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256)
);
