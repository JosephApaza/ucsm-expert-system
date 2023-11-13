--Procedimiento para obtener los pasos del proceso
CREATE PROCEDURE ObtenerPasosDelProceso
    @ID_Proceso INT
AS
BEGIN
    SELECT Orden, Descripcion
    FROM Pasos
    WHERE ID_Proceso = @ID_Proceso
    ORDER BY Orden;
END;

