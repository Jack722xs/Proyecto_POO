from datetime import date
from app.modelo.registro_tiempo import RegistroTiempo
from app.controlador.DAO_registro_tiempo import agregarRegistro, verRegistrosPorEmpleado, verRegistrosPorProyecto
from app.controlador.sub_controlador.DAO_empleado_proyecto import verProyectosDeEmpleado
from app.vista.view_proyecto import readProyecto 
import app.sesion.sesion as sesion
from app.utils.helper import *

def addRegistroTiempo():
    saltar_pantalla()
    print("============================================")
    print("        REGISTRAR HORAS TRABAJADAS          ")
    print("============================================")

    id_empleado = sesion.id_empleado_actual
    if id_empleado is None:
        print("ERROR: Tu usuario NO está asociado a un empleado.")
        print("(Los administradores puros no pueden registrar horas propias).")
        input("Presiona enter para continuar")
        return

    proyectos = verProyectosDeEmpleado(id_empleado)

    if not proyectos:
        print("No puedes registrar horas porque NO estás asignado a ningún proyecto.")
        input("Presiona enter para continuar")
        return

    print("\n--- TUS PROYECTOS ASIGNADOS ---")
    print(f"{'ID':<12} {'Nombre del Proyecto'}")
    print("-" * 40)
    for p in proyectos:
        print(f"{str(p[0]):<12} {p[1]}")
    print("=" * 40)

    id_proyecto = input("\nIngrese el ID del proyecto: ").strip()
    proyectos_validos = [str(p[0]) for p in proyectos]

    if id_proyecto not in proyectos_validos:
        print("ERROR: Ese proyecto NO está asignado a ti (o no existe).")
        input("Presiona enter para continuar")
        return
    try:
        entrada_horas = input("Horas trabajadas: ").strip()
        if not entrada_horas: return
        horas = float(entrada_horas)
        if horas <= 0:
            print("Las horas deben ser mayor a cero.")
            return
    except ValueError:
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
    saltar_pantalla()
    print("============================================")
    print("          MIS REGISTROS DE HORAS            ")
    print("============================================")

    id_emp = sesion.id_empleado_actual

    if id_emp is None:
        print("ERROR: No hay empleado asociado al usuario.")
        input("Presiona enter para continuar")
        return
    
    registros = verRegistrosPorEmpleado(id_emp)
    
    if not registros:
        print("No tienes registros de horas.")
    else:
        print(f"{'Fecha':<12} {'Horas':<8} {'Descripción'}")
        print("-" * 60)
        for r in registros:
            fecha = str(r[3])
            horas = str(r[4])
            desc = str(r[5])
            print(f"{fecha:<12} {horas:<8} {desc}")
            
    print("=" * 60)
    input("Presiona enter para continuar")    


def verRegistrosProyecto():
    saltar_pantalla()
    print("============================================")
    print("        VER REGISTROS POR PROYECTO          ")
    print("============================================")
    
    print("\n--- PROYECTOS DISPONIBLES ---")
    readProyecto(pausar=False) 
    
    id_proj = input("\nIngrese ID del proyecto a consultar: ").strip()
    if not id_proj: 
        input("Presiona Enter...")
        return
    
    registros = verRegistrosPorProyecto(id_proj)
    
    print(f"\n=== REGISTROS DEL PROYECTO {id_proj} ===")
    if not registros:
        print("No hay registros de horas para este proyecto.")
    else:
        print(f"{'Empleado':<10} {'Fecha':<12} {'Horas':<8} {'Descripción'}")
        print("-" * 70)
        for r in registros:
            emp = str(r[1])
            fecha = str(r[3])
            horas = str(r[4])
            desc = str(r[5])
            print(f"{emp:<10} {fecha:<12} {horas:<8} {desc}")
    print("=" * 70)
        
    input("Presiona enter para continuar")

def menu_registro_tiempo():
    while True:
        saltar_pantalla()
        print("""
============================================
          MENU REGISTRO DE HORAS
============================================
1. Registrar horas trabajadas              =
2. Ver mis registros (Empleado)            =
3. Ver registros por proyecto              =
============================================
4. Volver
""")
        
        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada: continue
            opc = int(entrada)
        except ValueError:
            print("Ingrese un numero valido.")
            input("Presiona Enter...")
            continue

        if opc == 1:
            addRegistroTiempo()
        elif opc == 2:
            verRegistrosEmpleado()
        elif opc == 3:
            verRegistrosProyecto()
        elif opc == 4:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar..")