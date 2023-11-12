from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@JOSEPH\\SQLSERVER2022/GestionTramitesDB?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes.indexRoute import index