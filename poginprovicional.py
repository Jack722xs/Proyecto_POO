from app.bbdd.conexion import getConexion
import bcrypt
import getpass


def crear_usuario(id_emp, nombre, pw):
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("INSERT INTO empleados VALUES (%s, %s, %s)", (id_emp, nombre, pw_hash))
    cone.commit()
    cone.close()


def autenticar(id_emp, pw):
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("SELECT password_hash FROM empleados WHERE id=%s", (id_emp,))
    row = cursor.fetchone()
    cone.close()
    if not row:
        return False
    return bcrypt.checkpw(pw.encode(), row[0])


# LOGIN POR TERMINAL

def login_terminal():
    print(""" LOGIN EMPRESA """)
    usuario = input("ID empleado: ")
    password = getpass.getpass("Contrasenia: ")

    if autenticar(usuario, password):
        print("Acceso concedido")
        menu_principal()
    else:
        print("Credenciales incorrectas")


def menu_principal():
    print("===== MENU PRINCIPAL =====")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    input("Presiona ENTER para continuar...")


# MAIN

if __name__ == "__main__":
    init_db()

    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    op = input("Selecciona: ")

    if op == "1":
        id_emp = input("ID nuevo empleado: ")
        nom = input("Nombre: ")
        pw = getpass.getpass("Contrasenia: ")
        crear_usuario(id_emp, nom, pw)
        print(" Usuario creado")
    else:
        login_terminal()