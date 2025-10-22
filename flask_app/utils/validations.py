from datetime import datetime, timedelta
import os
import re
import filetype
from werkzeug.utils import secure_filename
from database import db

def validate_region_comuna(region_id, comuna_id):
    if not region_id or not comuna_id:
        return False, "Región y comuna son obligatorios."

    region = db.get_region_by_id(region_id)
    if not region:
        return False, "Región no válida."

    comuna = db.get_comuna_by_id(comuna_id)
    if not comuna:
        return False, "Comuna no válida."

    if comuna.region_id != region.id:
        return False, "La comuna no pertenece a la región."

    return True, ""

def validate_sector(sector):
    return len(sector) < 100

def validate_name(name):
    return name and len(name) >= 3 and len(name) < 200

def validate_email(mail):
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(regex, mail))

def validate_phone(tel):
    return not tel or (len(tel) <= 13 and re.match(r'^\+\d{3}\.\d{8}$', tel))

def validate_contactos(contactos_combinados):
    for contacto in contactos_combinados:
        info = contacto.get("info", "")
        if info and not (4 <= len(info) <= 50):
            return False
    return True

def validate_tipo_mascota(tipo):
    OPCIONES_VALIDAS = {"gato", "perro"}
    return tipo in OPCIONES_VALIDAS

def validate_amount(cant):
    return cant is not None and cant > 0

def validate_age(edad):
    return edad is not None and edad > 0

def validate_description(desc):
    if not desc:  
        return True
    return len(desc) <= 500

def validate_unidad_medida(unidad):
    OPCIONES_VALIDAS = {"m", "a"}
    return unidad in OPCIONES_VALIDAS

def validate_fecha_entrega(fecha_str):

    if not fecha_str:
        return False
    
    try:
        fecha_entrega = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M")
    except ValueError:
        return False

    ahora_mas_3 = datetime.now() + timedelta(hours=3)
    return fecha_entrega >= ahora_mas_3

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}
    MAX_FILE_SIZE = 5 * 1024 * 1024

    if conf_img is None:
        return False

    if conf_img.filename == "":
        return False
    
    filename = secure_filename(conf_img.filename)
    if filename == "":
        return False
    
    ftype_guess = filetype.guess(conf_img)

    if ftype_guess is None:   
        return False
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False

    conf_img.seek(0, os.SEEK_END)
    file_length = conf_img.tell()
    conf_img.seek(0)
    if file_length > MAX_FILE_SIZE:
        return False
    
    return True

def validate_photos(fotos):
    if not fotos or all(f.filename == '' for f in fotos):
        return False
    for f in fotos:
        if f and not validate_conf_img(f):
            return False
    return True

def validate_form(lista_form, error):

    val , error_region_comuna = validate_region_comuna(lista_form["region_id"], lista_form["comuna_id"])
    if not val:
        error += error_region_comuna
        lista_form["region_id"] = ""
        lista_form["comuna_id"] = ""

    if not validate_sector(lista_form["sector"]):
        error += "El sector debe tener un máximo de 100 caracteres."
        lista_form["sector"] = ""

    if not validate_name(lista_form["nombre"]):
        error += "El nombre es obligatorio y debe tener entre 3 y 200 caracteres."
        lista_form["nombre"] = ""

    if not validate_email(lista_form["email"]):
        error += "El email es obligatorio y debe ser válido."
        lista_form["email"] = ""

    if not validate_phone(lista_form["celular"]):
        error += "El teléfono es obligatorio y debe tener el formato +XXX.XXXXXXXX."
        lista_form["celular"] = ""
    if not validate_contactos(lista_form["contactos"]):
        error += "El contacto debe tener entre 4 y 50 caracteres."
        for contacto in lista_form["contactos"]:
            contacto["info"] = ""
            contacto["tipo"] = ""

    if not validate_tipo_mascota(lista_form["tipo"]):
        error += "Debe seleccionar un tipo de mascota válido."
        lista_form["tipo"] = ""

    if not validate_amount(lista_form["cantidad"]):
        error += "La cantidad es obligatoria y debe ser mayor a 0."
        lista_form["cantidad"] = ""

    if not validate_age(lista_form["edad"]):
        error += "La edad es obligatoria y debe ser mayor a 0."
        lista_form["edad"] = ""

    if not validate_unidad_medida(lista_form["unidad_medida"]):
        error += "Debe seleccionar una unidad de medida válida."
        lista_form["unidad_medida"] = ""

    if not validate_description(lista_form["descripcion"]):
        error += "La descripción debe tener un máximo de 500 caracteres."
        lista_form["descripcion"] = ""

    if not validate_fecha_entrega(lista_form["fecha_entrega"]):
        error += "La fecha de entrega debe ser al menos 3 horas en el futuro."
        lista_form["fecha_entrega"] = ""

    if not validate_photos(lista_form["fotos"]):
        error += "Una de las fotos no es válida o no se seleccionó ninguna. Solo se permiten imágenes (png, jpg, jpeg), y el tamaño máximo es 5MB."

    if error:
        return lista_form, error
    
    return lista_form, ""

def validar_comentario(nombre: str, texto: str):
    if not nombre or not texto:
        return {"status": "error", "msg": "Campos vacíos"}
    if not (3 <= len(nombre) <= 80):
        return {"status": "error", "msg": "Nombre inválido"}
    if len(texto) < 5 or len(texto) > 300:
        return {"status": "error", "msg": "Comentario inválido"}

    patron_sospechoso = re.compile(r"<\s*script|<\s*iframe|on\w+\s*=", re.IGNORECASE)
    if patron_sospechoso.search(texto) or patron_sospechoso.search(nombre):
        return {"status": "error", "msg": "Contenido no permitido"}

    return {"status": "ok", "msg": "Validación correcta"}