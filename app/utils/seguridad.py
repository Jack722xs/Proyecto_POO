import bcrypt

def encriptar_password(password_texto_plano):
    if not password_texto_plano:
        return None
    hashed = bcrypt.hashpw(password_texto_plano.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def verificar_password(password_ingresada, hash_guardado):
    if not password_ingresada or not hash_guardado:
        return False
    try:
        return bcrypt.checkpw(
            password_ingresada.encode('utf-8'), 
            hash_guardado.encode('utf-8')
        )
    except Exception:
        return False