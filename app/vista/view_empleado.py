from app.modelo.empleado import empleado
from app.controlador.DAO_empleado import *
from app.utils.helper import *

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
    # ...
    try:
        val_id = input_no_vacio("ID empleado: ")
        if val_id is None: return
        id_empleado = int(val_id) # Conversión explícita
    except ValueError:
        print("Error: El ID debe ser un número.")
        return
    
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
        
    input("Presiona enter para continuar")    
 

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
    input("Presiona enter para continuar")

def delEmpleado():
    print("ELIMINAR EMPLEADO")

    id_empleado = input_no_vacio("ID empleado a eliminar: ")
    if id_empleado is None: return

    if eliminarEmpleado(id_empleado):
        print("Empleado eliminado.")
    else:
        print("No existe un empleado con ese ID.")
    input("Presiona enter para continuar")    
    

def readEmpleado():
    empleados = verEmpleado()
    
    if not empleados:
        print("\nNo hay empleados registrados.\n")
        return

    print("\n" + "="*110)
    print(f"{'ID':<12} {'Nombre':<12} {'Apellido':<12} {'Email':<30} {'Teléfono':<12} {'Salario':<12} {'Dirección'}")
    print("="*110)

    for emp in empleados:
        id_emp = str(emp[0])
        nombre = str(emp[1])
        apellido = str(emp[2])
        telefono = str(emp[3])  
        email = str(emp[4])
        salario = str(emp[5])
        direccion = str(emp[6])

        print(f"{id_emp:<12} {nombre:<12} {apellido:<12} {email:<30} {telefono:<12} ${salario:<11} {direccion}")
    
    print("="*110 + "\n")
    input("Presiona enter para continuar")

