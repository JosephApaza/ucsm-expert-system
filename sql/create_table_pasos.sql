-- Este script crea la tabla de Pasos
USE GestionTramitesDB;

CREATE TABLE Pasos (
    ID INT PRIMARY KEY,
    ID_Proceso INT,
    Orden INT,
    Descripcion NVARCHAR(MAX),
    FOREIGN KEY (ID_Proceso) REFERENCES Procesos(ID)
);