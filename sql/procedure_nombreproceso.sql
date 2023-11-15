-- Procedimiento para consultar el nombre por ID
CREATE PROCEDURE ObtenerNombrePorID
    @ID INT
AS
BEGIN
    SELECT Nombre
    FROM Procesos
    WHERE ID = @ID;
END;
