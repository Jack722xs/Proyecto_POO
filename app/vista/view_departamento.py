from app.modelo.departamento import departamento
from app.controlador.DAO_departamento import *
from app.controlador.DAO_usuario import verUsuarioPorEmpleado
from app.utils.helper import *

def input_no_vacio(mensaje, max_intentos=5):
    # (Mantener lógica)
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": return dato
        intentos += 1
        print(f"Este campo no puede estar vacio. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operacion cancelada.")
    return None

def addDepartamento():
    # (Mantener igual)
    while True:
        print("AGREGAR DEPARTAMENTO")
        id_depart = input_no_vacio("Ingrese ID: ")
        if id_depart is None: return
        proposito_depart = input_no_vacio("Ingrese proposito: ")
        if proposito_depart is None: return
        nombre_depart = input_no_vacio("Ingrese nombre: ")
        if nombre_depart is None: return

        dep = departamento(id_depart, proposito_depart, nombre_depart, None)
        if agregarDepartamento(dep):
            print("Departamento agregado correctamente.")
        else:
            print("No se pudo agregar el departamento.")

        opcion = input("\n¿Desea agregar otro departamento? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del registro de departamentos...")
            saltar_pantalla()
            break
        input("Presiona enter para continuar")

def editDepartamento():
    print("EDITAR DEPARTAMENTO")
    # MOSTRAR LISTA
    readDepartamento(pausar=False)

    id_depart = input_no_vacio("Ingrese ID del departamento a editar: ")
    if id_depart is None: return
    proposito_depart = input_no_vacio("Ingrese nuevo proposito: ")
    if proposito_depart is None: return
    nombre_depart = input_no_vacio("Ingrese nuevo nombre: ")
    if nombre_depart is None: return

    dep = departamento(id_depart, proposito_depart, nombre_depart, None)
    if editarDepartamento(dep):
        print("Departamento actualizado correctamente.")
    else:
        print("No se pudo actualizar el departamento (ID inexistente).")

    input("Presiona enter para continuar")    

def readDepartamento(pausar=True): # PARAMETRO NUEVO
    departamentos = verDepartamento()
    if not departamentos:
        print("\nNo hay departamentos registrados.\n")
        if pausar: input("Presiona enter para continuar")
        return
    print("\n" + "="*100)
    print(f"{'ID':<12} {'Nombre':<20} {'Gerente':<15} {'Propósito'}")
    print("="*100)

    for fila in departamentos:
        id_dep, proposito, nombre, gerente = fila
        id_str = str(id_dep)
        nombre_str = str(nombre)
        gerente_str = str(gerente) if gerente else "Sin Asignar"
        proposito_str = str(proposito)
        print(f"{id_str:<12} {nombre_str:<20} {gerente_str:<15} {proposito_str}")
    
    print("="*100 + "\n")
    if pausar:
        input("Presiona enter para continuar")


def delDepartamento():
    print("ELIMINAR DEPARTAMENTO")
    # MOSTRAR LISTA
    readDepartamento(pausar=False)

    id_depart = input_no_vacio("Ingrese el ID a eliminar: ")
    if id_depart is None: return

    if eliminarDepartamento(id_depart):
        print("Departamento eliminado correctamente.")
    else:
        print("No se encontro un departamento con ese ID.")
    input("Presiona enter para continuar")      

def asignarGerente_view():
    print("=== ASIGNAR GERENTE A DEPARTAMENTO ===")
    
    # OPCIONAL: Mostrar departamentos para ver IDs
    print("\n--- DEPARTAMENTOS ---")
    readDepartamento(pausar=False)

    id_depart = input("ID del departamento: ").strip()
    id_empleado = input("ID del empleado que sera gerente: ").strip()

    if not id_depart or not id_empleado:
        print("ID de departamento y empleado no pueden estar vacios.")
        return

    # Buscar usuario asociado a ese empleado
    usuario = verUsuarioPorEmpleado(id_empleado)
    if not usuario:
        print("ERROR: Este empleado no tiene un usuario asociado.")
        return
    
    nombre_usuario, email, rol, id_emp = usuario
    if rol != "gerente":
        print("ERROR: Este usuario NO tiene el rol de GERENTE.")
        return

    if asignarGerente(id_depart, id_empleado):
        print(f"Gerente (empleado {id_empleado}) asignado correctamente al departamento {id_depart}.")
    else:
        print("No se pudo asignar el gerente.")
        
    input("Presiona enter para continuar")