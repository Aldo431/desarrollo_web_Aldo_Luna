from flask import Flask, request, render_template, redirect, url_for, session # pyright: ignore[reportMissingImports]
from database import db
from werkzeug.utils import secure_filename # pyright: ignore[reportMissingImports]
import hashlib
import filetype # pyright: ignore[reportMissingImports]
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/formulario_aviso", methods=["GET"])
def formulario_aviso(): 
    return render_template("adopcion/formulario_aviso.html")

@app.route("/estadisticas")
def estadisticas():
    return render_template("adopcion/estadisticas.html")


@app.route("/listado")
def listado():
    return render_template("adopcion/listado.html")


@app.route("/", methods=["GET"])
def index():
    avisos = db.get_last_5_avisos()
    return render_template("adopcion/index.html", avisos=avisos)

if __name__ == "__main__":
    app.run(debug=True)