from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import addRegistroTiempo
from app.utils.helper import *
from app.controlador.sub_controlador.DAO_empleado_proyecto import asignarEmpleadoAProyecto, quitarEmpleadoDeProyecto
from app.controlador.sub_controlador.DAO_proyecto_departamento import verProyectosDeDepartamento
from app.controlador.sub_controlador.DAO_empleado_departamento import verEmpleadosDeDepartamento


def obtener_departamento_del_gerente():
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
1. Ver mi departamento
2. Ver empleados de mi departamento
3. Ver proyectos de mi departamento
4. Asignar empleado a un proyecto
5. Quitar empleado de un proyecto
6. Registrar horas trabajadas
7. Ver informes
8. Salir
""")

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            ver_mi_departamento()
        elif opc == "2":
            ver_empleados_mi_departamento()
        elif opc == "3":
            ver_proyectos_mi_departamento()
        elif opc == "4":
            asignarEmpleadoAProyecto_gerente()
        elif opc == "5":
            quitarEmpleadoDeProyecto_gerente()
        elif opc == "6":
            addRegistroTiempo()
        elif opc == "7":
            menu_informes()
        elif opc == "8":
            break
        else:
            print("Opcion invalida.")


def ver_mi_departamento():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No estas asignado como gerente de ningun departamento.")
        return
    
    print(f"Tu departamento es: {id_dep}")


def ver_empleados_mi_departamento():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No administras ningun departamento.")
        return

    empleados = verEmpleadosDeDepartamento(id_dep)
    print("\nEmpleados de tu departamento:")
    for e in empleados:
        print(e)


def ver_proyectos_mi_departamento():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No administras ningun departamento.")
        return
    
    proyectos = verProyectosDeDepartamento(id_dep)
    
    print("\n=== PROYECTOS DE TU DEPARTAMENTO ===")
    if not proyectos:
        print("No hay proyectos asignados a este departamento.")
    else:
        for p in proyectos:
            # Imprimimos cada proyecto de forma ordenada
            print(f"- {p}")
    print("====================================\n")


def asignarEmpleadoAProyecto_gerente():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No administras ningun departamento.")
        return

    print("\nEmpleados de tu departamento:")
    for e in verEmpleadosDeDepartamento(id_dep):
        print(e)

    print("\nProyectos de tu departamento:")
    for p in verProyectosDeDepartamento(id_dep):
        print(p)

    id_emp = input("ID del empleado a asignar: ")
    id_proj = input("ID del proyecto: ")

    asignarEmpleadoAProyecto(id_emp, id_proj)


def quitarEmpleadoDeProyecto_gerente():
    id_emp = input("ID del empleado: ")
    id_proj = input("ID del proyecto: ")
    quitarEmpleadoDeProyecto(id_emp, id_proj)
