from config import app, db
from flask import render_template, jsonify
from sqlalchemy import text

@app.route("/")
def index():
    # Simplemente seleccionamos el primer proceso por ahora
    id_proceso = 1
    result_procesos = db.session.execute(text('EXEC ObtenerProcesos'))
    procesos = [{'ID': row.ID, 'Nombre': row.Nombre} for row in result_procesos]
       
    # Renderizamos la plantilla y pasamos los datos a la misma
    return render_template("index.html", procesos=procesos)