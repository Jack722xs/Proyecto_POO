from app.modelo.empleado import empleado
from app.controlador.DAO_empleado import *
import time

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

def addEmpleado():
    print("AGREGAR EMPLEADO")


    print("¿Como desea ingresar el ID?")
    print("1. Generar automaticamente")
    print("2. Ingresar manualmente")
    op_id = input("Seleccione (1/2): ").strip()

    if op_id == "1":

        id_empleado = int(time.time())
        print(f"ID generado: {id_empleado}")
    else:
        try:
            val = input_no_vacio("ID empleado: ")
            if val is None: return
            id_empleado = int(val)
        except ValueError:
            print("Error: El ID debe ser numerico.")
            return

    nombre = input_no_vacio("Nombre: ")
    if nombre is None: return

    apellido = input_no_vacio("Apellido: ")
    if apellido is None: return

    direccion = input_no_vacio("Direccion: ")
    if direccion is None: return

    email = input_no_vacio("Email: ")
    if email is None: return

    salario = input_no_vacio("Salario: ")
    if salario is None: return

    telefono = input("Telefono (opcional): ").strip()
    if telefono == "":
        telefono = None

    emp = empleado(id_empleado, nombre, apellido, direccion, email, salario, telefono)

    if agregarEmpleado(emp):
        print("Empleado agregado correctamente.")
    else:
        print("No se pudo agregar el empleado.")


def editEmpleado():
    print("EDITAR EMPLEADO")

    id_empleado = input_no_vacio("ID empleado a editar: ")
    if id_empleado is None: return

    nombre = input_no_vacio("Nuevo nombre: ")
    if nombre is None: return

    apellido = input_no_vacio("Nuevo apellido: ")
    if apellido is None: return

    direccion = input_no_vacio("Nueva direccion: ")
    if direccion is None: return

    email = input_no_vacio("Nuevo email: ")
    if email is None: return

    salario = input_no_vacio("Nuevo salario: ")
    if salario is None: return

    telefono = input("Nuevo telefono (opcional): ").strip()
    if telefono == "":
        telefono = None

    emp = empleado(id_empleado, nombre, apellido, direccion, email, salario, telefono)

    if editarEmpleado(emp):
        print("Empleado actualizado correctamente.")
    else:
        print("No se pudo actualizar (ID inexistente).")


def delEmpleado():
    print("ELIMINAR EMPLEADO")

    id_empleado = input_no_vacio("ID empleado a eliminar: ")
    if id_empleado is None: return

    if eliminarEmpleado(id_empleado):
        print("Empleado eliminado.")
    else:
        print("No existe un empleado con ese ID.")



def readEmpleado():
    
    empleado = verEmpleado()
    print(empleado)
