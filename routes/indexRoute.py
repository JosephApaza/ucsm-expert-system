from config import app
from controllers.indexController import index

app.add_url_rule("/", view_func=index)
