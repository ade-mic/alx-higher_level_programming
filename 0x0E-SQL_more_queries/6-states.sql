-- creates the database hbtn_0d_usa
-- table states on MYSQL server
CREATE DATABASE IF NOT EXISTS
hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
hbtn_0d_usa.states (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(256) NOT NULL);
