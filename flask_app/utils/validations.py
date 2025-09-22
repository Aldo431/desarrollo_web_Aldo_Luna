import re
import filetype

def validate_email(value):
    return "@" in value

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    if conf_img is None:
        return False

    if conf_img.filename == "":
        return False
    
    ftype_guess = filetype.guess(conf_img)

    if ftype_guess is None:   
        return False
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

