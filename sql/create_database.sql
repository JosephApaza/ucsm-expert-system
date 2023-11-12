-- Script para Crear la Base de Datos
IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = 'GestionTramitesDB')
BEGIN
    CREATE DATABASE GestionTramitesDB;
END;