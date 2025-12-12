import bcrypt

def encriptar_password(password):
    """Encripta una contraseña en texto plano y devuelve el hash en string."""
    if not password:
        return None
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_password(password_plano, password_hash):
    """Verifica si la contraseña coincide con el hash guardado."""
    try:
        if isinstance(password_plano, str):
            password_bytes = password_plano.encode('utf-8')
        else:
            password_bytes = password_plano

        if isinstance(password_hash, str):
            hash_bytes = password_hash.encode('utf-8')
        else:
            hash_bytes = password_hash

        return bcrypt.checkpw(password_bytes, hash_bytes)
    
    except Exception as e:
        print(f"Error verificando password: {e}")
        return False