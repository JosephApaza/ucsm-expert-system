-- Este script inserta un proceso de matrícula y sus pasos asociados
USE GestionTramitesDB;

-- Insertar el proceso de matrícula
INSERT INTO Procesos (ID, Nombre, Descripcion, Url)
VALUES (1, 'Matrícula', 'Proceso de matrícula', 'https://webapp.ucsm.edu.pe/sm/Views/login.php');

-- Insertar los pasos asociados al proceso de matrícula
INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 1, 'Verificar el horario  para confirmar que el día y la hora corresponden a la carrera.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 2, 'Iniciar sesión.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 3, 'Ir a la sección de Matrículas.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 4, 'Ir a Registrar matrícula.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 5, 'Seleccionar escuela profesional.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 6, 'Aceptar la Declaración y Compromiso de matrícula.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 7, 'Seleccionar los cursos.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 8, 'Seleccionar horarios (no se permiten cruces de más de 45 minutos).');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 9, 'Clic en botón matricularse.');

INSERT INTO Pasos (ID_Proceso, Orden, Descripcion)
VALUES (1, 10, 'Confirmar matrícula.');
