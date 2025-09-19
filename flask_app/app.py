from flask import Flask, request, render_template, redirect, url_for, session # pyright: ignore[reportMissingImports]
from utils.validations import validate_conf_img
from database import db
from werkzeug.utils import secure_filename # pyright: ignore[reportMissingImports]
from datetime import datetime
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

@app.route("/formulario_aviso", methods=["GET"])
def formulario_aviso(): 
    if request.method == "GET":
        regiones = db.get_all_regiones()
        comunas = db.get_all_comunas()
        return render_template("form/formulario_aviso.html", regiones=regiones, comunas=comunas)

@app.route("/post_aviso", methods=["POST"])
def post_aviso():       
    session = db.SessionLocal() 
    region_id = request.form.get("region")
    comuna_id = request.form.get("comuna")
    sector = request.form.get("sector")
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    celular = request.form.get("tel")
    tipo = request.form.get("mascota")
    cantidad = int(request.form.get("cantidad"))
    edad = int(request.form.get("edad"))
    unidad_medida = request.form.get("unidad")[0]  
    fecha_entrega = request.form.get("fecha-disponible")
    descripcion = request.form.get("descripcion")
    contactos = request.form.getlist("contacto-info[]")
    tipos_contacto = request.form.getlist("contacto-tipo[]")
    contactos_combinados = list(zip(tipos_contacto, contactos))
    error = ""

    dt = datetime.strptime(fecha_entrega, "%Y-%m-%dT%H:%M")
    fecha_entrega = dt.strftime("%Y-%m-%dT%H:%M")
    fotos = request.files.getlist("fotos[]")
    for f in fotos:
        if f and not validate_conf_img(f):
            session.close()
            error = "Una de las fotos no es válida. Solo se permiten imágenes (png, jpg, jpeg)."
            return render_template(
                "form/formulario_aviso.html",
                error=error,
                region_id=region_id,
                comuna_id=comuna_id,
                sector=sector,
                nombre=nombre,
                email=email,
                celular=celular,
                tipo=tipo,
                cantidad=cantidad,
                edad=edad,
                unidad_medida=unidad_medida,
                fecha_entrega=fecha_entrega,
                descripcion=descripcion,
                regiones=db.get_all_regiones(),
                comunas=db.get_all_comunas(),
                contactos_combinados=contactos_combinados
            )
        
    aviso = db.AvisoAdopcion(
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        tipo=tipo,
        cantidad=cantidad,
        edad=edad,
        unidad_medida=unidad_medida,
        fecha_entrega=fecha_entrega,
        descripcion=descripcion
    )
    session.add(aviso)
    session.commit()    
        
    fotos = request.files.getlist("fotos[]")  
    for f in fotos:
        if f.filename:
            filename = secure_filename(f.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            foto = db.Foto(ruta_archivo=filepath, nombre_archivo=filename, aviso=aviso)
            session.add(foto)
    session.commit()

    contactos = request.form.getlist("contacto-info[]")  
    tipos_contacto = request.form.getlist("contacto-tipo[]")  
    for tipo, ident in zip(tipos_contacto, contactos):
        if ident:
            contactar_por = db.ContactarPor(nombre=tipo, identificador=ident, aviso=aviso)
            session.add(contactar_por)
    session.commit()

    return redirect(url_for("index"))

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