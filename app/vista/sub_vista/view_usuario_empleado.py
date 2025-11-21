from app.controlador.sub_controlador.DAO_usuario_empleado import *


def addUsuarioAEmpleado():
    nombre_usuario = input("Nombre de usuario: ")
    id_empleado = input("ID empleado: ")

    asignarUsuarioAEmpleado(nombre_usuario, id_empleado)


def delUsuarioDeEmpleado():
    nombre_usuario = input("Nombre de usuario: ")

    quitarUsuarioDeEmpleado(nombre_usuario)


def readEmpleadoDeUsuario():
    nombre_usuario = input("Nombre de usuario: ")
    datos = verEmpleadoDeUsuario(nombre_usuario)

    if datos is None:
        print("No se encontro informacion.")
        return

    print("\n=== Usuario - Empleado ===")
    print(f"Usuario: {datos[0]}")
    if datos[1] is None:
        print("No tiene empleado asociado.")
    else:
        print(f"Empleado: {datos[1]} - {datos[2]} {datos[3]} ({datos[4]})")
