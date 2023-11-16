import sys
from config import app, db
from flask import render_template, redirect, url_for
from sqlalchemy import text

# Obtener la lista de procesos desde la base de datos
def obtener_lista_procesos():
    procesos = db.session.execute(text('EXEC ObtenerProcesos')).fetchall()
    return [proceso.ID for proceso in procesos]

@app.route("/proceso/<id_proceso>", methods=['POST', 'GET'])
def mostrar_pasos(id_proceso):
    # Obtener la lista de procesos
    lista_procesos = obtener_lista_procesos()

    try:
        # Intentar convertir id_proceso a un entero
        id_proceso = int(id_proceso)

        # Verificar si el id_proceso es mayor que el valor máximo permitido
        if id_proceso > sys.maxsize:
            # Redireccionar a la página de error 400
            return redirect(url_for('error_400'))

        # Verificar si el id_proceso está en la lista de procesos
        if id_proceso not in lista_procesos:
            # Redireccionar a la página de error 404
            return redirect(url_for('error_404'))

    except ValueError:
        # Si la conversión falla, redireccionar a la página de error 400
        return redirect(url_for('error_400'))
    
    # Obtener la lista de pasos del proceso desde la base de datos
    pasos_proceso = db.session.execute(
        text('EXEC ObtenerPasosDelProceso :id_proceso'), {'id_proceso': id_proceso}
    )

    # Obtener los pasos del resultado de la consulta
    pasos = [{'Orden': row.Orden, 'Descripcion': row.Descripcion} for row in pasos_proceso]

    # Obtener el nombre del proceso
    nombre_proceso = db.session.execute(
        text('EXEC ObtenerNombrePorID :id_proceso'), {'id_proceso': id_proceso}
    )
    nombre = [{'Nombre': row.Nombre} for row in nombre_proceso]

    # Renderizar la plantilla y pasar los datos
    return render_template("pasos.html", pasos=pasos, nombre=nombre)
