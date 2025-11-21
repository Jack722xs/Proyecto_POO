from datetime import date
from app.modelo.registro_tiempo import RegistroTiempo
from app.controlador.DAO_registro_tiempo import agregarRegistro, verRegistrosPorEmpleado, verRegistrosPorProyecto
import app.sesion.sesion as sesion


def addRegistroTiempo():
    
    # Tomar usuario desde sesion real

    id_empleado = sesion.usuario_actual

    if id_empleado is None:
        print("ERROR: No hay usuario logeado.")
        return

    print("\n=== Registrar Horas Trabajadas ===")

    id_proyecto = input("Ingrese ID del proyecto: ").strip()
    if id_proyecto == "":
        print("El ID del proyecto no puede estar vacio.")
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

    # Crear el registro (id_registro no se usa)
    rt = RegistroTiempo(
        id_empleado=id_empleado,
        id_proyecto=id_proyecto,
        fecha=fecha_hoy,
        horas=horas,
        descripcion=descripcion
    )

    if agregarRegistro(rt):
        print("Registro agregado correctamente.")
    else:
        print("ERROR al guardar el registro.")


def verRegistrosEmpleado():
    id_emp = sesion.usuario_actual

    if id_emp is None:
        print("ERROR: No hay usuario en sesion.")
        return
    
    registros = verRegistrosPorEmpleado(id_emp)
    print("\n=== MIS REGISTROS DE HORAS ===")
    for r in registros:
        print(r)


def verRegistrosProyecto():
    id_proj = input("ID del proyecto: ")
    registros = verRegistrosPorProyecto(id_proj)
    print("\n=== REGISTROS DEL PROYECTO ===")
    for r in registros:
        print(r)
