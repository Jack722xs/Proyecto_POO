from datetime import date
from app.modelo.registro_tiempo import RegistroTiempo
from app.controlador.DAO_registro_tiempo import *

# IMPORTANTE:
# DEBES reemplazar esto con el usuario real del login
usuario_actual = None   # Se debe actualizar desde login

def addRegistroTiempo():
    global usuario_actual

    if usuario_actual is None:
        print("ERROR: No hay usuario logeado.")
        return

    print("=== Registrar Horas Trabajadas ===")

    id_empleado = usuario_actual   # tomado del login
    id_proyecto = input("Ingrese ID del proyecto: ")
    
    horas = float(input("Horas trabajadas: "))
    descripcion = input("Descripcion: ")

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
        print("Registro añadido exitosamente.")
    else:
        print("Error al guardar el registro.")


def verRegistrosEmpleado():
    global usuario_actual
    id_emp = usuario_actual
    print(verRegistrosPorEmpleado(id_emp))


def verRegistrosProyecto():
    id_proj = input("ID proyecto: ")
    print(verRegistrosPorProyecto(id_proj))
