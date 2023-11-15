from config import app
from controllers.pasosController import mostrar_pasos

app.add_url_rule("/proceso/<id_proceso>", view_func=mostrar_pasos)