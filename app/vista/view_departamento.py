from app.modelo.departamento import departamento
from app.controlador.DAO_departamento import *
from app.controlador.DAO_usuario import verUsuarioPorEmpleado


# Evitar inputs vacios
def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0

    while intentos < max_intentos:
        dato = input(mensaje).strip()  # elimina espacios extra

        if dato != "":
            return dato

        intentos += 1
        print(f"Este campo no puede estar vacio. Intento {intentos}/{max_intentos}")

    print("Demasiados intentos fallidos. Operacion cancelada.")
    return None


# ================================
#   AGREGAR DEPARTAMENTO
# ================================

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

        dep = departamento(
            id_depart,
            proposito_depart,
            nombre_depart,
            None  # gerente_asociado
        )

        if agregarDepartamento(dep):
            print("Departamento agregado correctamente.")
        else:
            print("No se pudo agregar el departamento.")

        opcion = input("\n¿Desea agregar otro departamento? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del registro de departamentos...")
            break


# ================================
#   EDITAR DEPARTAMENTO
# ================================

def editDepartamento():
    print("EDITAR DEPARTAMENTO")

    id_depart = input_no_vacio("Ingrese ID del departamento a editar: ")
    if id_depart is None:
        return

    proposito_depart = input_no_vacio("Ingrese nuevo proposito: ")
    if proposito_depart is None:
        return

    nombre_depart = input_no_vacio("Ingrese nuevo nombre: ")
    if nombre_depart is None:
        return

    
    dep = departamento(
        id_depart,
        proposito_depart,
        nombre_depart,
        None
    )

    if editarDepartamento(dep):
        print("Departamento actualizado correctamente.")
    else:
        print("No se pudo actualizar el departamento (ID inexistente).")


# ================================
#   LISTAR DEPARTAMENTOS
# ================================

def readDepartamento():
    departamentos = verDepartamento()
    if not departamentos:
        print("No hay departamentos registrados.")
        return

    print("\n=== LISTA DE DEPARTAMENTOS ===")
    for fila in departamentos:
        id_dep, proposito, nombre, gerente = fila
        print(f"ID: {id_dep} | Nombre: {nombre} | Proposito: {proposito} | Gerente (id_empleado): {gerente}")
    print("================================\n")


# ================================
#   ELIMINAR DEPARTAMENTO
# ================================

def delDepartamento():
    print("ELIMINAR DEPARTAMENTO")

    id_depart = input_no_vacio("Ingrese el ID a eliminar: ")
    if id_depart is None:
        return

    if eliminarDepartamento(id_depart):
        print("Departamento eliminado correctamente.")
    else:
        print("No se encontro un departamento con ese ID.")


# ================================
#   ASIGNAR GERENTE A DEPARTAMENTO
# ================================

def asignarGerente_view():
    print("=== ASIGNAR GERENTE A DEPARTAMENTO ===")

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
