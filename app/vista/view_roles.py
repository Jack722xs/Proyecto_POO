from app.utils.helper import *
from app.controlador.DAO_roles import (
    obtenerRol,
    cambiarRol,
    listarRolesValidos
)


def menu_roles():
    while True:

        saltar_pantalla()

        print("""
======== MENU ROLES ========
1. Ver rol de un usuario
2. Cambiar rol de un usuario
3. Ver roles validos
4. Volver
============================""")

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            ver_rol_usuario()
            input("Presiona enter para continuar")
        elif opc == "2":
            cambiar_rol_usuario()
        elif opc == "3":
            print("Roles disponibles:", listarRolesValidos())
        elif opc == "4":
            saltar_pantalla()
            break
        else:
            print("Opcion invalida.")


def ver_rol_usuario():
    nombre = input("Nombre del usuario: ")
    rol = obtenerRol(nombre)

    if rol:
        print(f"El rol actual de {nombre} es: {rol}")
    else:
        print("Usuario no existe.")

    input("Presiona enter para continuar")    

def cambiar_rol_usuario():
    nombre = input("Nombre del usuario: ")

    print("Roles validos:", listarRolesValidos())
    nuevo_rol = input("Nuevo rol: ").lower()

    cambiarRol(nombre, nuevo_rol)

    input("/nPresiona enter para continuar")
