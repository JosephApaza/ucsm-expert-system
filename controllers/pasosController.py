from config import app, db
from flask import render_template
from sqlalchemy import text

@app.route("/proceso/<id_proceso>", methods=['POST', 'GET'])
def mostrar_pasos(id_proceso):
    # Simplemente seleccionamos el primer proceso por ahora
    pasos_proceso = db.session.execute(text('EXEC ObtenerPasosDelProceso :id_proceso'), {'id_proceso': id_proceso})
    pasos = [{'Orden': row.Orden, 'Descripcion': row.Descripcion} for row in pasos_proceso]
    
    nombre_proceso = db.session.execute(text('EXEC ObtenerNombrePorID :id_proceso'), {'id_proceso': id_proceso})
    nombre = [{'Nombre': row.Nombre} for row in nombre_proceso]

    
    # Renderizamos la plantilla y pasamos los datos a la misma
    return render_template("pasos.html", pasos=pasos, nombre=nombre)