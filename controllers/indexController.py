from config import app, db
from flask import render_template
from sqlalchemy import text

# Ruta para la página de inicio
@app.route("/", methods=['GET'])
def index():
    # Ejecuta un procedimiento almacenado para obtener la lista de procesos
    result_procesos = db.session.execute(text('EXEC ObtenerProcesos'))

    # Convierte los resultados en una lista de diccionarios para facilitar su uso en la plantilla
    procesos = [{'ID': row.ID, 'Nombre': row.Nombre} for row in result_procesos]
    
    # Renderizamos la plantilla y pasamos los datos a la misma
    return render_template("index.html", procesos=procesos)