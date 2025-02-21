DROP DATABASE IF EXISTS flask_examen;
CREATE DATABASE flask_examen;

USE flask_examen;

CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(35),
    email VARCHAR(20),
    password VARCHAR(255)
);

CREATE TABLE contacts(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    img VARCHAR(255),
    descripcion VARCHAR(255),
    users_id INT UNSIGNED,
    FOREIGN KEY (users_id) REFERENCES users_id(id) 
);
