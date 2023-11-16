from config import app
from controllers.errorController import *

app.add_url_rule("/error_400", view_func=error_400)
app.add_url_rule("/error_404", view_func=error_404)