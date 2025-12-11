from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import addRegistroTiempo
from app.utils.helper import *

# Importamos DAOs necesarios
from app.controlador.sub_controlador.DAO_empleado_proyecto import asignarEmpleadoAProyecto, quitarEmpleadoDeProyecto, verProyectosDeEmpleado
from app.controlador.sub_controlador.DAO_proyecto_departamento import verProyectosDeDepartamento
from app.controlador.sub_controlador.DAO_empleado_departamento import verEmpleadosDeDepartamento


def obtener_departamento_del_gerente():
    """Retorna el ID del departamento que administra el usuario actual."""
    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("""
            SELECT id_depart 
            FROM departamento
            WHERE gerente_asociado = %s
        """, (sesion.id_empleado_actual,))   
        result = cursor.fetchone()
        cone.close()

        if result:
            return result[0]
        return None

    except Exception as ex:
        print("Error obteniendo departamento del gerente:", ex)
        return None


def menu_gerente():
    while True:
        saltar_pantalla()
        print("""
============================================
              MENU GERENTE                  
============================================
1. Ver mi departamento                     =
2. Ver empleados de mi departamento        =
3. Ver proyectos de mi departamento        =
4. Asignar empleado a un proyecto          =
5. Quitar empleado de un proyecto          =
6. Registrar horas trabajadas              =
7. Ver informes                            =
============================================
8. Salir
""")

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presiona Enter...")
            continue

        if opc == 1:
            ver_mi_departamento()
        elif opc == 2:
            ver_empleados_mi_departamento()
        elif opc == 3:
            ver_proyectos_mi_departamento()
        elif opc == 4:
            asignarEmpleadoAProyecto_gerente()
        elif opc == 5:
            quitarEmpleadoDeProyecto_gerente()
        elif opc == 6:
            addRegistroTiempo()
        elif opc == 7:
            menu_informes()
        elif opc == 8:
            print("Cerrando sesión...")
            saltar_pantalla()
            break
        else:
            print("Opción inválida.")
            input("Presiona Enter para continuar...")


def ver_mi_departamento():
    saltar_pantalla()
    print("============================================")
    print("            MI DEPARTAMENTO                 ")
    print("============================================")
    
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No estás asignado como gerente de ningún departamento.")
    else:
        print(f"\nEstás administrando el departamento con ID: {id_dep}")
        # Aquí podrías buscar el nombre del departamento si quisieras hacerlo más completo
    
    input("\nPresiona Enter para continuar...")


def ver_empleados_mi_departamento():
    saltar_pantalla()
    print("============================================")
    print("      EMPLEADOS DE MI DEPARTAMENTO          ")
    print("============================================")

    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("Error: No tienes un departamento asignado.")
        input("Presiona Enter...")
        return

    empleados = verEmpleadosDeDepartamento(id_dep)
    
    if not empleados:
        print("\nNo hay empleados en tu departamento.")
    else:
        print(f"\n{'ID':<12} {'Nombre':<15} {'Apellido':<15}")
        print("-" * 45)
        for e in empleados:
            # e[0]=id, e[1]=nombre, e[2]=apellido
            print(f"{str(e[0]):<12} {e[1]:<15} {e[2]:<15}")
        print("-" * 45)

    input("\nPresiona Enter para continuar...")


def ver_proyectos_mi_departamento():
    saltar_pantalla()
    print("============================================")
    print("      PROYECTOS DE MI DEPARTAMENTO          ")
    print("============================================")

    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("Error: No tienes un departamento asignado.")
        input("Presiona Enter...")
        return
    
    proyectos = verProyectosDeDepartamento(id_dep)
    
    if not proyectos:
        print("\nNo hay proyectos asignados a tu departamento.")
    else:
        print(f"\n{'ID':<12} {'Nombre':<20} {'Estado'}")
        print("-" * 50)
        for p in proyectos:
            p_id = str(p[0])
            p_nom = str(p[1])
            p_est = str(p[5]) if len(p) > 5 else "N/A"
            print(f"{p_id:<12} {p_nom:<20} {p_est}")
        print("-" * 50)

    input("\nPresiona Enter para continuar...")


def asignarEmpleadoAProyecto_gerente():
    # 1. Obtener Depto
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        saltar_pantalla()
        print("Error: No tienes un departamento asignado.")
        input("Presiona Enter...")
        return

    # 2. Seleccionar Empleado (del departamento)
    saltar_pantalla()
    print("============================================")
    print("           SELECCIÓN DE EMPLEADO            ")
    print("============================================")
    print(f"(Mostrando solo empleados de tu departamento {id_dep})")
    
    empleados = verEmpleadosDeDepartamento(id_dep)
    if not empleados:
        print("\nNo hay empleados disponibles en tu departamento.")
        input("Presiona Enter...")
        return

    print(f"\n{'ID':<12} {'Nombre':<15}")
    print("-" * 30)
    lista_emp_ids = []
    for e in empleados:
        print(f"{str(e[0]):<12} {e[1]:<15}")
        lista_emp_ids.append(str(e[0]))
    print("-" * 30)

    id_emp = input("\nIngrese ID del empleado a asignar: ").strip()
    if id_emp not in lista_emp_ids:
        print("Error: ID inválido o no pertenece a tu departamento.")
        input("Presiona Enter...")
        return

    # 3. Seleccionar Proyecto (del departamento)
    saltar_pantalla()
    print("============================================")
    print("           SELECCIÓN DE PROYECTO            ")
    print("============================================")
    print(f"(Mostrando solo proyectos de tu departamento {id_dep})")

    proyectos = verProyectosDeDepartamento(id_dep)
    if not proyectos:
        print("\nNo hay proyectos disponibles en tu departamento.")
        input("Presiona Enter...")
        return

    print(f"\n{'ID':<12} {'Nombre':<20}")
    print("-" * 35)
    lista_proy_ids = []
    for p in proyectos:
        print(f"{str(p[0]):<12} {p[1]:<20}")
        lista_proy_ids.append(str(p[0]))
    print("-" * 35)

    id_proj = input("\nIngrese ID del proyecto: ").strip()
    if id_proj not in lista_proy_ids:
        print("Error: ID inválido o no pertenece a tu departamento.")
        input("Presiona Enter...")
        return

    # 4. Asignar
    print("-" * 40)
    if asignarEmpleadoAProyecto(id_emp, id_proj):
        print(f"¡ÉXITO! Empleado {id_emp} asignado al proyecto {id_proj}.")
    else:
        print("No se pudo realizar la asignación.")
    
    input("Presiona Enter para continuar...")


def quitarEmpleadoDeProyecto_gerente():
    # 1. Obtener Depto
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        saltar_pantalla()
        print("Error: No tienes un departamento asignado.")
        input("Presiona Enter...")
        return

    # 2. Seleccionar Empleado (del departamento)
    saltar_pantalla()
    print("============================================")
    print("      QUITAR EMPLEADO DE UN PROYECTO        ")
    print("============================================")
    
    empleados = verEmpleadosDeDepartamento(id_dep)
    if not empleados:
        print("No hay empleados en tu departamento.")
        input("Presiona Enter...")
        return

    print("\n--- TUS EMPLEADOS ---")
    print(f"{'ID':<12} {'Nombre':<15}")
    for e in empleados:
        print(f"{str(e[0]):<12} {e[1]:<15}")
    
    id_emp = input("\nIngrese ID del empleado: ").strip()
    
    # Validar que sea de su equipo
    ids_validos = [str(e[0]) for e in empleados]
    if id_emp not in ids_validos:
        print("Error: Ese empleado no pertenece a tu departamento.")
        input("Presiona Enter...")
        return

    # 3. Mostrar proyectos de ESE empleado
    saltar_pantalla()
    print(f"============================================")
    print(f"   PROYECTOS DEL EMPLEADO {id_emp}         ")
    print(f"============================================")

    proyectos_asignados = verProyectosDeEmpleado(id_emp)
    
    if not proyectos_asignados:
        print("Este empleado no tiene proyectos asignados.")
        input("Presiona Enter...")
        return

    print(f"\n{'ID':<12} {'Nombre':<20}")
    print("-" * 35)
    lista_proy_ids = []
    for p in proyectos_asignados:
        print(f"{str(p[0]):<12} {p[1]:<20}")
        lista_proy_ids.append(str(p[0]))
    print("-" * 35)

    id_proj = input("\nIngrese ID del proyecto a quitar: ").strip()

    if id_proj not in lista_proy_ids:
        print("Error: El empleado no está en ese proyecto o ID incorrecto.")
    else:
        if quitarEmpleadoDeProyecto(id_emp, id_proj):
            print("Asignación eliminada correctamente.")
        else:
            print("Error al eliminar.")

    input("Presiona Enter para continuar...")