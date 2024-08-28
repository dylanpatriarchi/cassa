CREATE DATABASE cassa_db;

USE cassa_db;

CREATE TABLE prodotti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    codice_barre VARCHAR(50) UNIQUE,
    prezzo DECIMAL(10, 2)
);
