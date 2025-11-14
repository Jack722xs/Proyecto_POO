from app.modelo.departamento import departamento
from app.controlador.DAO import *

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
        print("No se encontró un departamento con ese ID.")

#----------- Empleado -------------

def addEmpleado():
    print("AGREGAR EMPLEADO")

    id_empleado = input_no_vacio("ID empleado: ")
    if id_empleado is None: return

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

    telefono = input("Telefono (opcional): ").strip() # esta funcion remueve los caracteres del inicio y del final para que no hay espacios extras
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

    direccion = input_no_vacio("Nueva dirección: ")
    if direccion is None: return

    email = input_no_vacio("Nuevo email: ")
    if email is None: return

    salario = input_no_vacio("Nuevo salario: ")
    if salario is None: return

    telefono = input("Nuevo teléfono (opcional): ").strip()
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
