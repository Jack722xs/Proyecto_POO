from app.modelo.departamento import departamento
from app.controlador.DAO import *

#Evitar inputs vacios
def input_no_vacio(mensaje):
    dato = ""
    while dato.strip() == "":
        dato = input(mensaje).strip()
        if dato == "":
            print("Este campo no puede estar vacío.")
    return dato


def addDepartamento():
    while True:
        print("AGREGAR DEPARTAMENTO")
        id_depart = input_no_vacio("Ingrese ID: ")
        proposito_depart = input_no_vacio("Ingrese proposito: ")
        nombre_depart = input_no_vacio("Ingrese nombre: ")
        gerente = input_no_vacio("Ingrese Gerente: ")

        # Crear Objeto
        dep = departamento(
            id_depart,
            proposito_depart,
            nombre_depart,
            gerente
        )

        # Llamamos al DAO correcto
        if agregarDepartamento(dep):
            print("Departamento agregado correctamente.")
        else:
            print("No se pudo agregar el departamento.")

        opcion = input("\n¿Desea agregar otro departamento? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del registro de departamentos...")
            break
