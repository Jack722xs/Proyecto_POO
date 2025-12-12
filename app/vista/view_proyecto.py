from app.modelo.proyecto import proyecto
from app.controlador.DAO_proyecto import *
from app.utils.helper import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": return dato
        intentos += 1
        print(f"Error: Este campo no puede estar vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operación cancelada.")
    return None

def addProyecto():
    while True:
        saltar_pantalla()
        print("============================================")
        print("             AGREGAR PROYECTO               ")
        print("============================================")
        
        id_proyecto = input_no_vacio("ID Proyecto (ej: PRJ001): ")
        if id_proyecto is None: break
        
        if verProyecto(id_proyecto):
             print(f"Error: El ID '{id_proyecto}' ya existe.")
             input("Presiona Enter para continuar...")
             break

        nombre = input_no_vacio("Nombre del Proyecto: ")
        if nombre is None: break
        
        descripcion = input_no_vacio("Descripción: ")
        if descripcion is None: break
        
        fecha_inicio = input_no_vacio("Fecha Inicio (YYYY-MM-DD): ")
        if fecha_inicio is None: break
        
        fecha_fin = input_no_vacio("Fecha Fin (YYYY-MM-DD): ")
        if fecha_fin is None: break
        
        estado = input_no_vacio("Estado (Activo/Planificado/Terminado): ")
        if estado is None: break

        proy = proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado, None)
        
        print("-" * 40)
        if agregarProyecto(proy):
            print("¡Proyecto creado exitosamente!")
        else:
            print("Error: No se pudo guardar el proyecto.")

        print("-" * 40)
        opcion = input("¿Desea agregar otro proyecto? (s/n): ").strip().lower()
        if opcion != "s":
            break


def editProyecto():
    saltar_pantalla()
    print("============================================")
    print("              EDITAR PROYECTO               ")
    print("============================================")
    
    proyectos_actuales = verProyectos()
    
    if not proyectos_actuales:
        print("No hay proyectos registrados para editar.")
        input("Presiona Enter para continuar...")
        return

    print(f"{'ID':<12} {'Nombre':<20} {'Estado'}")
    print("-" * 45)
    lista_ids = []
    for p in proyectos_actuales:
        p_id = str(p[0])
        lista_ids.append(p_id)
        estado = str(p[5]) if len(p) > 5 else "N/A"
        print(f"{p_id:<12} {p[1]:<20} {estado}")
    print("=" * 80)

    id_proyecto = input("\nIngrese ID del proyecto a editar: ").strip()
    
    if not id_proyecto:
        print("Error: ID vacío.")
        input("Presiona Enter para continuar...")
        return

    if id_proyecto not in lista_ids:
        print(f"\nError: El proyecto con ID '{id_proyecto}' NO existe.")
        print("Operación cancelada.")
        input("Presiona Enter para continuar...")
        return

    print(f"\n--- Editando datos de {id_proyecto} ---")
    
    nombre = input_no_vacio("Nuevo Nombre: ")
    if nombre is None: return
    
    descripcion = input_no_vacio("Nueva Descripción: ")
    if descripcion is None: return
    
    fecha_inicio = input_no_vacio("Nueva Fecha Inicio: ")
    if fecha_inicio is None: return
    
    fecha_fin = input_no_vacio("Nueva Fecha Fin: ")
    if fecha_fin is None: return
    
    estado = input_no_vacio("Nuevo Estado: ")
    if estado is None: return

    proy = proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado, None)

    print("-" * 40)
    if editarProyecto(proy):
        print("Proyecto actualizado correctamente.")
    else:
        print("Error: No se pudo actualizar en la base de datos.")

    input("Presiona Enter para continuar...")

def delProyecto():
    saltar_pantalla()
    print("============================================")
    print("             ELIMINAR PROYECTO              ")
    print("============================================")
    
    readProyecto(pausar=False)

    print("-" * 40)
    id_proyecto = input("Ingrese ID del proyecto a eliminar: ").strip()
    
    if not id_proyecto:
        print("Error: ID vacío.")
        input("Presiona Enter...")
        return

    confirmacion = input(f"¿Seguro que desea eliminar el proyecto {id_proyecto}? (s/n): ").lower()
    if confirmacion == 's':
        if eliminarProyecto(id_proyecto):
            print("Proyecto eliminado correctamente.")
        else:
            print("Error: No se encontró el ID o hubo un fallo en la BD.")
    else:
        print("Operación cancelada.")
        
    input("Presiona Enter para continuar...")


def readProyecto(pausar=True):
    if pausar:
        saltar_pantalla()
        print("============================================")
        print("             LISTA DE PROYECTOS             ")
        print("============================================")

    proyectos = verProyectos()
    
    if not proyectos:
        print("\nNo hay proyectos registrados.\n")
    else:
        print(f"{'ID':<10} {'Nombre':<18} {'Descripción':<25} {'Inicio':<12} {'Fin':<12} {'Estado'}")
        print("="*90)

        for p in proyectos:
            p_id = str(p[0])
            nom = str(p[1])
            desc = str(p[2])
            if len(desc) > 22: desc = desc[:20] + "..."
            ini = str(p[3])
            fin = str(p[4])
            est = str(p[5])
            
            print(f"{p_id:<10} {nom:<18} {desc:<25} {ini:<12} {fin:<12} {est}")
        print("="*90)
    
    if pausar:
        input("\nPresiona Enter para continuar...")