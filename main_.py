from app.bbdd.conexion import getConexion
import bcrypt
import getpass
from app.vista.menus.view_menu_admin import menu_admin
from app.vista.menus.view_menu_gerente import menu_gerente
from app.vista.menus.view_menu_empleado import menu_empleado
from app.controlador.DAO_usuario import *
from app.controlador.sub_controlador.DAO_usuario_empleado import *

import app.sesion.sesion as sesion   # Manejo de usuario logueado


def crear_usuario(nombre_usuario, email, pw):
    """
    Crea el usuario con rol EMPLEADO por defecto y SIN id_empleado,
    porque eso sera asignado despues desde el menu.
    """
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("""
    INSERT INTO usuario (nombre_usuario, email, password_hash, rol, id_empleado)
    VALUES (%s, %s, %s, %s, NULL)
    """, (nombre_usuario, email, pw_hash.decode(), "empleado"))
    cone.commit()
    cone.close()


def autentificacion(nombre_usuario, pw):
    """
    Valida credenciales y almacena datos en sesion.
    Retorna True si es valido, False en caso contrario.
    """
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("""
        SELECT password_hash, id_empleado, rol
        FROM usuario
        WHERE nombre_usuario=%s
    """, (nombre_usuario,))
    row = cursor.fetchone()
    cone.close()

    if not row:
        return False

    hash_pw, id_empleado, rol = row

    if not bcrypt.checkpw(pw.encode(), hash_pw.encode()):
        return False

    # Guardar en sesion **correctamente**
    sesion.nombre_usuario = nombre_usuario
    sesion.rol_actual = rol
    sesion.id_empleado_actual = id_empleado  # antes ESTO NO EXISTÍA

    return True



def login_terminal():
    print("=== LOGIN EMPRESA ===")
    intentos = 3

    while intentos > 0:
        usuario = input("Nombre de usuario: ")
        password = getpass.getpass("Contraseña: ")

        if autentificacion(usuario, password):
            print("Acceso concedido.")
            print(f"Usuario: {sesion.nombre_usuario} | Rol: {sesion.rol_actual}")

            if sesion.rol_actual == "admin":
                menu_admin()
            elif sesion.rol_actual == "gerente":
                menu_gerente()
            elif sesion.rol_actual == "empleado":
                menu_empleado()
            else:
                print("Rol desconocido.")

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
        print("Usuario creado con rol EMPLEADO.")
    elif op == "2":
        login_terminal()
    else:
        print("Opcion no valida.")
