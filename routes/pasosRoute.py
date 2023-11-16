from config import app
from controllers.pasosController import mostrar_pasos

# Agrega una regla de URL para la vista de mostrar pasos en un proceso específico
# La variable dinámica <id_proceso> indica que se espera un parámetro en la URL
# que será pasado a la función del controlador.
app.add_url_rule("/proceso/<id_proceso>", view_func=mostrar_pasos)