-- Creates the database hbtn_0d_usa and the table states in hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY,
name VARCHAR(256) NOT NULL
)ENGINE=INNODB;
