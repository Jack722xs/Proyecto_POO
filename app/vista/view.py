from app.modelo.departamento import departamento
from app.controlador.DAO import *

#Evitar inputs vacios
def input_no_vacio(mensaje, max_intentos = 5):
    intentos = 0

  
    while intentos < max_intentos:
        dato = input(mensaje).strip()

        if dato != "":          
            return dato

        intentos += 1
        print(f"Este campo no puede estar vacio. Intento {intentos}/{max_intentos}")

    print("Demasiados intentos fallidos. Operacion cancelada.")
    return None

# ADD DEPARTAMENTO
def addDepartamento():
    while True:
        print("AGREGAR DEPARTAMENTO")
        id_depart = input_no_vacio("Ingrese ID: ")
        if id_depart is None:
            return
        proposito_depart = input_no_vacio("Ingrese proposito: ")
        if proposito_depart is None:
            return
        nombre_depart = input_no_vacio("Ingrese nombre: ")
        if nombre_depart is None:
            return
        gerente = input_no_vacio("Ingrese Gerente: ")
        if gerente is None:
            return

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

def editDepartamento():
        print("EDITAR DEPARTAMENTO")
        id_depart = input_no_vacio("Ingrese ID: ")
        if id_depart is None:
            return
        proposito_depart = input_no_vacio("Ingrese proposito: ")
        if proposito_depart is None:
            return
        nombre_depart = input_no_vacio("Ingrese nombre: ")
        if nombre_depart is None:
            return
        gerente = input_no_vacio("Ingrese Gerente: ")
        if gerente is None:
            return
        
        dep = departamento(
            id_depart,
            proposito_depart,
            nombre_depart,
            gerente
        )

        if editarDepartamento(dep):
            print("Departamento actualizado correctamente.")
        else:
            print("No se pudo agregar el departamento (ID inexistente)")

def readDepartamento():
    
    departamentos = verDepartamento()
    print(departamentos)


def delDepartamento():
    print("ELIMINAR DEPARTAMENTO")

    id_depart = input_no_vacio("Ingrese el ID a eliminar: ")
    if id_depart is None:
        return  

    if eliminarDepartamento(id_depart):
        print("Departamento eliminado correctamente.")
    else:
        print("No se encontró un departamento con ese ID.")
