import re
import filetype

def validate_email(value):
    return "@" in value

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

