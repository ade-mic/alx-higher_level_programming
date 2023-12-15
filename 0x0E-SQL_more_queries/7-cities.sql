-- create the databse hbtn_0d_usa and
-- the table cities in a MYSQL server
CREATE DATABASE IF NOT EXISTS
hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
hbtn_0d_usa.cities (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
state_id NOT NULL FOREIGN KEY REFERENCES states (id),
name VARCHAR(256) NOT NULL
);
