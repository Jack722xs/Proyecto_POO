from app.controlador.sub_controlador.DAO_empleado_departamento import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato:
            return dato
        intentos += 1
        print(f"Campo vacio. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos.")
    return None


# ========================================================
#               EMPLEADO  DEPARTAMENTO
# ========================================================

def asignar_empleado_departamento():
    print("\n--- ASIGNAR EMPLEADO A DEPARTAMENTO ---")

    id_emp = input_no_vacio("ID empleado: ")
    if id_emp is None: return

    id_dep = input_no_vacio("ID departamento: ")
    if id_dep is None: return

    try:
        if asignarEmpleadoADepartamento(id_emp, id_dep):
            print("Empleado asignado correctamente.")
        else:
            print("No se pudo asignar el empleado.")
    except Exception as ex:
        print("Error al asignar empleado al departamento.")
        print(ex)


def quitar_empleado_departamento():
    print("\n--- QUITAR EMPLEADO DE DEPARTAMENTO ---")

    id_emp = input_no_vacio("ID empleado: ")
    if id_emp is None: return

    try:
        if quitarEmpleadoDeDepartamento(id_emp):
            print("Empleado removido del departamento.")
        else:
            print("No se pudo quitar al empleado.")
    except Exception as ex:
        print("Error al quitar empleado del departamento.")
        print(ex)


def ver_empleados_departamento():
    print("\n--- VER EMPLEADOS POR DEPARTAMENTO ---")

    id_dep = input_no_vacio("ID departamento: ")
    if id_dep is None: return

    try:
        empleados = verEmpleadosDeDepartamento(id_dep)
        if empleados:
            print("\nEmpleados encontrados:")
            for e in empleados:
                print(" -", e)
        else:
            print("No hay empleados o el departamento no existe.")
    except Exception as ex:
        print("Error al obtener empleados del departamento.")
        print(ex)
