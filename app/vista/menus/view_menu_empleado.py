import app.sesion.sesion as sesion
from app.vista.view_registro_tiempo import addRegistroTiempo, verRegistrosEmpleado
from app.controlador.sub_controlador.DAO_empleado_proyecto import verProyectosDeEmpleado
from app.controlador.DAO_empleado import verEmpleadoPorID
from app.utils.helper import *

def menu_empleado():
    while True:

        saltar_pantalla()

        
        print("""
============================================
               MENÚ EMPLEADO
============================================
1. Ver mis datos
2. Ver mis proyectos
3. Registrar horas trabajadas
4. Ver mis registros de horas
5. Salir
""")

        opc = input("Seleccione una opción: ")

        # ---------------------------------------------
        #    Validación para seguridad
        # ---------------------------------------------
        if sesion.id_empleado_actual is None:
            print("ERROR: No hay un empleado asociado al usuario.")
            return  # vuelve al login

        if opc == "1":
            ver_mis_datos()

        elif opc == "2":
            ver_mis_proyectos()

        elif opc == "3":
            addRegistroTiempo()

        elif opc == "4":
            verRegistrosEmpleado()

        elif opc == "5":
            print("Cerrando menú empleado...")
            break

        else:
            print("Opción inválida.")


# ==========================================================
#   VER DATOS DEL EMPLEADO ACTUAL
# ==========================================================
from app.controlador.DAO_empleado import verEmpleado

def ver_mis_datos():
    try:
        datos = verEmpleadoPorID(sesion.id_empleado_actual)
        if not datos:
            print("No se pudo obtener la información del empleado.")
            return
        
        print("\n=== MIS DATOS ===")
        print(f"ID: {datos[0]}")
        print(f"Nombre: {datos[1]}")
        print(f"Apellido: {datos[2]}")
        print(f"Direccion: {datos[3]}")
        print(f"Email: {datos[4]}")
        print(f"Salario: {datos[5]}")
        print(f"Telefono: {datos[6]}")
        print(f"Gerente: {'Si' if datos[7] else 'No'}")
        print(f"Departamento: {datos[8]}")
        print("=================\n")

    except Exception as e:
        print("Error al obtener datos del empleado:", e)



# ==========================================================
#   VER PROYECTOS ASOCIADOS AL EMPLEADO ACTUAL
# ==========================================================
def ver_mis_proyectos():
    try:
        proyectos = verProyectosDeEmpleado(sesion.id_empleado_actual)

        print("\n=== MIS PROYECTOS ===")
        if not proyectos:
            print("No estás asignado a ningún proyecto.")
            return

        for p in proyectos:
            print(f"- {p}")

        print("=====================\n")

    except Exception as e:
        print("Error al obtener proyectos:", e)



