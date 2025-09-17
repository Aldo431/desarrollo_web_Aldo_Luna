from flask import Flask, request, render_template, redirect, url_for, session # pyright: ignore[reportMissingImports]
from database import db
from werkzeug.utils import secure_filename # pyright: ignore[reportMissingImports]
import hashlib
import filetype  # pyright: ignore[reportMissingImports]
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/confirmacion", methods=["GET"])
def confirmacion():
    return render_template("form/confirmacion.html")

@app.route("/formulario_aviso", methods=["GET", "POST"])
def formulario_aviso(): 
    if request.method == "GET":
        regiones = db.get_all_regiones()
        comunas = db.get_all_comunas()
        return render_template("form/formulario_aviso.html", regiones=regiones, comunas=comunas)

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("adopcion/estadisticas.html")


@app.route("/listado", methods=["GET"])
def listado():
    return render_template("adopcion/listado.html")


@app.route("/", methods=["GET"])
def index():
    avisos = db.get_last_5_avisos()
    return render_template("adopcion/index.html", avisos=avisos)

if __name__ == "__main__":
    app.run(debug=True)