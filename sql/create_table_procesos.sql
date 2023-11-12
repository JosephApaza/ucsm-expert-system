-- Este script crea la tabla de Procesos
USE GestionTramitesDB;

CREATE TABLE Procesos (
    ID INT PRIMARY KEY,
    Nombre NVARCHAR(255) NOT NULL,
    Descripcion NVARCHAR(MAX),
    Url NVARCHAR(MAX)
);