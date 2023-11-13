from config import app, db
from flask import render_template, jsonify
from sqlalchemy import text

@app.route("/")
def index():
    return render_template("index.html")