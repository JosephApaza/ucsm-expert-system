import sys
from config import app, db
from flask import render_template, abort
from sqlalchemy import text

@app.route("/proceso/<id_proceso>", methods=['POST', 'GET'])
def mostrar_pasos(id_proceso):
    try:
        # Intentar convertir id_proceso a un entero
        id_proceso = int(id_proceso)

        # Verificar si el id_proceso es mayor que el valor máximo permitido
        if id_proceso > sys.maxsize:
            abort(400, "ID de proceso demasiado grande. Debe ser un número entero válido.")

    except ValueError:
        # Si la conversión falla, retornar un error 400 (Bad Request)
        abort(400, "ID de proceso no válido. Debe ser un número entero.")

    # Obtener la lista de pasos del proceso desde la base de datos
    pasos_proceso = db.session.execute(
        text('EXEC ObtenerPasosDelProceso :id_proceso'), {'id_proceso': id_proceso}
    )

    # Verificar si el resultado está vacío, lo que indica que el proceso no existe
    if not pasos_proceso.rowcount:
        # Si el proceso no existe, retornar un error 404 (Not Found)
        abort(404, f"No se encontró el proceso con ID {id_proceso}.")

    # Obtener los pasos del resultado de la consulta
    pasos = [{'Orden': row.Orden, 'Descripcion': row.Descripcion} for row in pasos_proceso]

    # Obtener el nombre del proceso
    nombre_proceso = db.session.execute(
        text('EXEC ObtenerNombrePorID :id_proceso'), {'id_proceso': id_proceso}
    )
    nombre = [{'Nombre': row.Nombre} for row in nombre_proceso]

    # Renderizar la plantilla y pasar los datos
    return render_template("pasos.html", pasos=pasos, nombre=nombre)
