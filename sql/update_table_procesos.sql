-- Este script actualiza la tabla de Procesos para incluir la nueva columna Url
USE GestionTramitesDB;

-- Verifica si la columna ya existe antes de agregarla
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Procesos' AND COLUMN_NAME = 'Url')
BEGIN
    ALTER TABLE Procesos
    ADD Url NVARCHAR(MAX);
END;