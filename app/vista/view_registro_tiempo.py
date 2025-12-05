from datetime import date
from app.modelo.registro_tiempo import RegistroTiempo
from app.controlador.DAO_registro_tiempo import agregarRegistro, verRegistrosPorEmpleado, verRegistrosPorProyecto
from app.controlador.sub_controlador.DAO_empleado_proyecto import verProyectosDeEmpleado
import app.sesion.sesion as sesion
from app.utils.helper import *

def addRegistroTiempo():
    print("\n=== Registrar Horas Trabajadas ===")

    id_empleado = sesion.id_empleado_actual
    if id_empleado is None:
        print("ERROR: Tu usuario NO esta asociado a un empleado.")
        return

    # Obtener proyectos validos
    proyectos = verProyectosDeEmpleado(id_empleado)

    if not proyectos:
        print("No puedes registrar horas porque NO estas asignado a ningun proyecto.")
        return

    print("\nProyectos asignados:")
    for p in proyectos:
        print(f"- {p[0]} | {p[1]}")   

    id_proyecto = input("\nIngrese el ID del proyecto: ").strip()

    # Validar que el proyecto SI pertenece al empleado
    proyectos_validos = [str(p[0]) for p in proyectos]

    if id_proyecto not in proyectos_validos:
        print("ERROR: Ese proyecto NO está asignado a ti.")
        return

    # Validar horas
    try:
        horas = float(input("Horas trabajadas: "))
        if horas <= 0:
            print("Las horas deben ser mayor a cero.")
            return
    except:
        print("ERROR: Ingrese un numero valido.")
        return

    descripcion = input("Descripcion del trabajo: ").strip()
    fecha_hoy = date.today().strftime("%Y-%m-%d")

    rt = RegistroTiempo(
        id_registro=None,
        id_empleado=id_empleado,
        id_proyecto=id_proyecto,
        fecha=fecha_hoy,
        horas=horas,
        descripcion=descripcion
    )

    if agregarRegistro(rt):
        print("Registro agregado correctamente.")
    else:
        print("ERROR al guardar el registro en la BD.")

    input("Presiona enter para continuar")    


def verRegistrosEmpleado():
    id_emp = sesion.id_empleado_actual

    if id_emp is None:
        print("ERROR: No hay empleado asociado al usuario.")
        return
    
    registros = verRegistrosPorEmpleado(id_emp)
    
    print("\n=== MIS REGISTROS DE HORAS ===")
    if not registros:
        print("No hay registros.")
        return

    for r in registros:
        print(r)

    input("Presiona enter para continuar")    


def verRegistrosProyecto():
    id_proj = input("ID del proyecto: ").strip()
    
    registros = verRegistrosPorProyecto(id_proj)
    
    print("\n=== REGISTROS DEL PROYECTO ===")
    if not registros:
        print("No hay registros.")
        return
    
    for r in registros:
        print(r)
        
    input("Presiona enter para continuar")    
