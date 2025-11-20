
from app.bbdd.conexion import getConexion
import bcrypt
import getpass
from app.vista.menu import menu_principal 

def crear_usuario(nombre_usuario, email, pw):
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("""
        INSERT INTO usuario (nombre_usuario, email, password_hash)
        VALUES (%s, %s, %s)
    """, (nombre_usuario, email, pw_hash.decode()))
    cone.commit()
    cone.close()

def autentificacion(nombre_usuario, pw):
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("SELECT password_hash FROM usuario WHERE nombre_usuario=%s", (nombre_usuario,))
    row = cursor.fetchone()
    cone.close()
    if not row:
        return False
    return bcrypt.checkpw(pw.encode(), row[0].encode())

def login_terminal():
    print("=== LOGIN EMPRESA ===")
    intentos = 3
    while intentos > 0:
        usuario = input("Nombre de usuario: ")
        password = getpass.getpass("Contraseña: ")
        if autentificacion(usuario, password):
            print("Acceso concedido")
            menu_principal()  
            return
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    print("Demasiados intentos. Intente mas tarde.")

if __name__ == "__main__":
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    op = input("Selecciona: ")
    if op == "1":
        nombre_usuario = input("Nuevo nombre de usuario: ")
        email = input("Email: ")
        pw = getpass.getpass("Contraseña: ")
        crear_usuario(nombre_usuario, email, pw)
        print("Usuario creado.")
    elif op == "2":
        login_terminal()
    else:
        print("Opcion no valida.")
