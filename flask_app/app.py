import html
import re
from flask import Flask, request, render_template, redirect, url_for, session, jsonify 
from utils.validations import validar_comentario, validate_conf_img, validate_form
from database import db
from werkzeug.utils import secure_filename 
from datetime import datetime
import hashlib
import filetype 
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
    cantidad_str = request.form.get("cantidad")
    if not cantidad_str:  
        cantidad = None 
    else:
        cantidad = int(cantidad_str)
    edad_str = request.form.get("edad")
    if not edad_str:  
        edad = None 
    else:
        edad = int(edad_str)
    unidad_medida = request.form.get("unidad") 
    if unidad_medida:
        unidad_medida = unidad_medida[0]
    else:
        unidad_medida = None
    fecha_entrega = request.form.get("fecha-disponible")
    descripcion = request.form.get("descripcion")
    contactos = request.form.getlist("contacto-info[]")
    tipos_contacto = request.form.getlist("contacto-tipo[]")
    contactos_combinados = list(zip(tipos_contacto, contactos))
    fotos = request.files.getlist("fotos[]")

    error = ""

    data = {
    "region_id": region_id,
    "comuna_id": comuna_id,
    "sector": sector,
    "nombre": nombre,
    "email": email,
    "celular": celular,
    "tipo": tipo,
    "cantidad": cantidad,
    "edad": edad,
    "unidad_medida": unidad_medida,
    "fecha_entrega": fecha_entrega,
    "descripcion": descripcion,
    "contactos": [
        {"tipo": tipo, "info": info}
        for tipo, info in contactos_combinados
    ],
    "fotos": fotos}    

    # Validaciones

    list_form, error = validate_form(data, error)

    if error:
            session.close()
            return render_template(
                "form/formulario_aviso.html",
                error=error,
                region_id=list_form["region_id"],
                comuna_id=list_form["comuna_id"],
                sector=list_form["sector"],
                nombre=list_form["nombre"],
                email=list_form["email"],
                celular=list_form["celular"],
                tipo=list_form["tipo"],
                cantidad=list_form["cantidad"],
                edad=list_form["edad"],
                unidad_medida=list_form["unidad_medida"],
                fecha_entrega=list_form["fecha_entrega"],
                descripcion=list_form["descripcion"],
                regiones=db.get_all_regiones(),
                comunas=db.get_all_comunas(),
                contactos_combinados=contactos_combinados,
            )
    
    # Paso todas las validaciones
      
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

    return redirect(url_for("index", confirmado=1))

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("adopcion/estadisticas.html")


@app.route("/listado", methods=["GET"])
def listado():
    page = int(request.args.get("page", 1))
    avisos, total_pages = db.get_all_avisos(page=page, per_page=5)

    return render_template( "adopcion/listado.html",avisos=avisos,page=page,total_pages=total_pages)

@app.route("/detalle",methods=["GET"])
def detalle():
    aviso_id = request.args.get("aviso_id")
    aviso = db.get_aviso_por_id(aviso_id)
    return render_template("adopcion/detalle.html", aviso=aviso)

@app.route("/get-avisos-tipo")
def get_avisos_tipo():
    data = db.get_avisos_por_tipo()
    return jsonify({"status": "ok", "data": data})

@app.route("/get-avisos-mes")
def get_avisos_mes():
    data = db.get_avisos_por_mes_y_tipo()
    return jsonify({"status": "ok", "data": data})

@app.route("/get-avisos-dia")
def get_avisos_dia_route():
    data = db.get_avisos_por_dia()
    return jsonify({"status": "ok", "data": data})

@app.route("/get-comentarios/<int:aviso_id>")
def get_comentarios(aviso_id):
    comentarios = db.get_comentarios_por_aviso(aviso_id)
    return jsonify({"status": "ok", "data": comentarios})

@app.route("/add-comentario/<int:aviso_id>", methods=["POST"])
def add_comentario(aviso_id):
    data = request.get_json()
    nombre = data.get("nombre", "").strip()
    texto = data.get("texto", "").strip()

    resultado = validar_comentario(nombre, texto)
    if resultado["status"] != "ok":
        return jsonify(resultado), 400
    
    nombre = html.escape(nombre)
    texto = html.escape(texto)

    db.agregar_comentario(aviso_id, nombre, texto)
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def index():
    avisos = db.get_last_5_avisos()
    return render_template("adopcion/index.html", avisos=avisos)

if __name__ == "__main__":
    app.run(debug=True)