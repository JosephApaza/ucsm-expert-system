-- Este script inserta un proceso de solicitud de descuento y sus pasos asociados
USE GestionTramitesDB;

-- Insertar el proceso de solicitud de descuento
INSERT INTO Procesos (ID, Nombre, Descripcion, Url)
VALUES (2, 'Solicitud de Descuento 8%', 'Proceso de solicitud de beneficio de descuento del 8%', 'https://apps.ucsm.edu.pe/UCSMERP/tramites.php');

-- Insertar los pasos asociados al proceso de solicitud de descuento
INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 1, 'Seleccionar Alumno.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 2, 'Ingresar datos (usuario y contraseña es el DNI si es la primera vez que ingresa).');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 3, 'Resolver el captcha e iniciar sesión.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 4, 'En el menú de opciones, buscar Beneficio de 8% de descuento.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 5, 'Seleccionar Registrar solicitud.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 6, 'Aceptar los términos y condiciones.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (2, 7, 'Siguiente.');
