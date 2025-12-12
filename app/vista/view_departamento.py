from app.modelo.departamento import departamento
from app.controlador.DAO_departamento import *
from app.controlador.DAO_usuario import verUsuarioPorEmpleado
from app.utils.helper import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": 
            return dato
        intentos += 1
        print(f"Error: Este campo no puede estar vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operación cancelada.")
    return None


def addDepartamento():
    while True:
        saltar_pantalla()
        print("============================================")
        print("           AGREGAR DEPARTAMENTO             ")
        print("============================================")
        
        id_depart = input_no_vacio("Ingrese ID (ej: DPT001): ")
        if id_depart is None: break
        
        proposito_depart = input_no_vacio("Ingrese propósito: ")
        if proposito_depart is None: break
        
        nombre_depart = input_no_vacio("Ingrese nombre: ")
        if nombre_depart is None: break

        dep = departamento(id_depart, proposito_depart, nombre_depart, None)
        
        print("-" * 40)
        if agregarDepartamento(dep):
            print("¡Departamento agregado correctamente!")
        else:
            print("Error: No se pudo agregar el departamento (revise si el ID ya existe).")

        print("-" * 40)
        opcion = input("¿Desea agregar otro departamento? (s/n): ").strip().lower()
        if opcion != "s":
            break


def editDepartamento():
    saltar_pantalla()
    print("============================================")
    print("            EDITAR DEPARTAMENTO             ")
    print("============================================")
    
    departamentos_actuales = verDepartamento()
    
    if not departamentos_actuales:
        print("No hay departamentos registrados para editar.")
        input("Presiona Enter para continuar...")
        return

    print(f"{'ID':<12} {'Nombre':<20}")
    print("-" * 32)
    lista_ids = []
    for fila in departamentos_actuales:
        d_id = str(fila[0])
        lista_ids.append(d_id)
        print(f"{d_id:<12} {fila[2]:<20}")
    print("=" * 80)
    
    print("-" * 40)
    id_depart = input("Ingrese ID del departamento a editar: ").strip()
    
    if not id_depart:
        print("Error: El ID no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    if id_depart not in lista_ids:
        print(f"\nError: El departamento con ID '{id_depart}' NO existe.")
        print("Operación cancelada para evitar ingreso de datos innecesario.")
        input("Presiona Enter para continuar...")
        return
    # --------------------------

    print(f"\n--- Editando Departamento {id_depart} ---")
    proposito_depart = input_no_vacio("Nuevo propósito: ")
    if proposito_depart is None: return
    
    nombre_depart = input_no_vacio("Nuevo nombre: ")
    if nombre_depart is None: return

    dep = departamento(id_depart, proposito_depart, nombre_depart, None)
    
    print("-" * 40)
    if editarDepartamento(dep):
        print("Departamento actualizado correctamente.")
    else:
        print("Error: Ocurrió un problema al intentar actualizar en la base de datos.")

    input("Presiona Enter para continuar...")

def delDepartamento():
    saltar_pantalla()
    print("============================================")
    print("           ELIMINAR DEPARTAMENTO            ")
    print("============================================")
    
    readDepartamento(pausar=False)

    print("-" * 40)
    id_depart = input("Ingrese el ID a eliminar: ").strip()
    
    if not id_depart:
        print("Error: El ID no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar el departamento {id_depart}? (s/n): ").lower()
    if confirmacion == 's':
        if eliminarDepartamento(id_depart):
            print("Departamento eliminado correctamente.")
        else:
            print("Error: No se encontró un departamento con ese ID o no se pudo eliminar.")
    else:
        print("Operación cancelada.")
        
    input("Presiona Enter para continuar...")

def readDepartamento(pausar=True):
    if pausar:
        saltar_pantalla()
        print("============================================")
        print("           LISTA DE DEPARTAMENTOS           ")
        print("============================================")

    departamentos = verDepartamento()
    
    if not departamentos:
        print("\nNo hay departamentos registrados.\n")
    else:
        print(f"{'ID':<12} {'Nombre':<20} {'Gerente':<20} {'Propósito'}")
        print("="*80)

        for fila in departamentos:
            id_dep = str(fila[0])
            proposito = str(fila[1])
            nombre = str(fila[2])
            gerente = str(fila[3]) if fila[3] else "Sin Asignar"
            
            print(f"{id_dep:<12} {nombre:<20} {gerente:<20} {proposito}")
        print("="*80)
    
    if pausar:
        input("\nPresiona Enter para continuar...")


def asignarGerente_view():
    saltar_pantalla()
    print("============================================")
    print("      ASIGNAR GERENTE A DEPARTAMENTO        ")
    print("============================================")
    
    print("\n--- DEPARTAMENTOS ---")
    readDepartamento(pausar=False)

    id_depart = input("\nID del departamento: ").strip()
    if not id_depart:
        print("Error: ID vacío.")
        input("Presiona Enter...")
        return

    id_empleado = input("ID del empleado candidato: ").strip()
    if not id_empleado:
        print("Error: ID vacío.")
        input("Presiona Enter...")
        return

    usuario = verUsuarioPorEmpleado(id_empleado)
    if not usuario:
        print("ERROR: Este empleado no tiene un usuario asociado.")
        input("Presiona Enter...")
        return
    
    rol = usuario[2]
    if rol.lower() != "gerente":
        print(f"ERROR: El usuario tiene rol '{rol}'. Se requiere rol 'gerente'.")
        input("Presiona Enter...")
        return

    if asignarGerente(id_depart, id_empleado):
        print(f"Gerente asignado correctamente al departamento {id_depart}.")
    else:
        print("No se pudo asignar el gerente.")
        
    input("Presiona Enter para continuar...")