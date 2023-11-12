-- Este script crea la tabla de Pasos con ID como una columna de identidad
USE GestionTramitesDB;

CREATE TABLE Pasos (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    ID_Proceso INT,
    Orden INT,
    Descripcion NVARCHAR(MAX),
    FOREIGN KEY (ID_Proceso) REFERENCES Procesos(ID)
);
