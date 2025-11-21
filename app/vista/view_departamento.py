from app.modelo.departamento import departamento
from app.controlador.DAO_departamento import *
from app.controlador.DAO_departamento import *
from app.controlador.DAO_usuario import *


#Evitar inputs vacios
def input_no_vacio(mensaje, max_intentos = 5):
    intentos = 0

  
    while intentos < max_intentos:
        dato = input(mensaje).strip() #esta funcion remueve los caracteres del inicio y del final para que no hay espacios extras

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

        opcion = input("\n¿Desea agregar otro departamento? (s/n): ").lower() # esta funcion transofrma las letras en minuscula
        if opcion != "s":
            print("Saliendo del registro de departamentos...")
            break

def editDepartamento():
        print("EDITAR DEPARTAMENTO")
        id_depart = input_no_vacio("Ingrese ID: ")
        if id_depart is None:
            return
        proposito_depart = input_no_vacio("Ingrese nuevo proposito: ")
        if proposito_depart is None:
            return
        nombre_depart = input_no_vacio("Ingrese nuevo nombre: ")
        if nombre_depart is None:
            return
        gerente = input_no_vacio("Ingrese nuevo Gerente: ")
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
        print("No se encontro un departamento con ese ID.")



def asignarGerente_view():
    print("=== ASIGNAR GERENTE A DEPARTAMENTO ===")

    id_depart = input("ID del departamento: ")
    id_empleado = input("ID del empleado que sera gerente: ")

    usuario = verUsuarioPorEmpleado(id_empleado)

    if not usuario:
        print("ERROR: Este empleado no tiene un usuario asociado.")
        return

    rol = usuario[3]  # Nombre columna 'rol'

    if rol != "gerente":
        print("ERROR: Este usuario NO tiene el rol de GERENTE.")
        return

    if asignarGerente(id_depart, id_empleado):
        print("Gerente asignado correctamente.")
    else:
        print("No se pudo asignar el gerente.")
