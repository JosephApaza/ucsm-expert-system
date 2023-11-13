-- Procedimiento para obtener la información de todos los procesos
CREATE PROCEDURE ObtenerProcesos
AS
BEGIN
    SELECT ID, Nombre
    FROM Procesos;
END;
