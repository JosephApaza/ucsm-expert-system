--Procedimiento para obtener la información del proceso
CREATE PROCEDURE ObtenerInfoProceso
    @ID_Proceso INT
AS
BEGIN
    SELECT Nombre, Descripcion, Url
    FROM Procesos
    WHERE ID = @ID_Proceso;
END;
