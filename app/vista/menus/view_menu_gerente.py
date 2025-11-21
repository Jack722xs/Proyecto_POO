from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion
from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import * 
from app.vista.sub_vista.view_usuario_empleado import *

from app.controlador.sub_controlador.DAO_empleado_proyecto import asignarEmpleadoAProyecto
from app.controlador.sub_controlador.DAO_proyecto_departamento import verProyectosDeDepartamento
from app.controlador.sub_controlador.DAO_empleado_departamento import verEmpleadosDeDepartamento
from app.controlador.sub_controlador.DAO_empleado_proyecto import quitarEmpleadoDeProyecto


def obtener_departamento_del_gerente():
    """Devuelve el id_depart del departamento donde el gerente_actual es responsable."""
    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("""
            SELECT id_depart 
            FROM departamento
            WHERE gerente_asociado = %s
        """, (sesion.usuario_actual,))
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
    print("Empleados de tu departamento:")
    print(empleados)



def ver_proyectos_mi_departamento():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No administras ningun departamento.")
        return
    
    proyectos = verProyectosDeDepartamento(id_dep)
    print("Proyectos de tu departamento:")
    print(proyectos)


def asignarEmpleadoAProyecto_gerente():
    id_dep = obtener_departamento_del_gerente()
    if not id_dep:
        print("No administras ningun departamento.")
        return

    print("Empleados de tu departamento:")
    print(verEmpleadosDeDepartamento(id_dep))

    print("Proyectos de tu departamento:")
    print(verProyectosDeDepartamento(id_dep))

    id_emp = input("ID del empleado a asignar: ")
    id_proj = input("ID del proyecto: ")

    asignarEmpleadoAProyecto(id_emp, id_proj)



def quitarEmpleadoDeProyecto_gerente():
    id_emp = input("ID del empleado: ")
    id_proj = input("ID del proyecto: ")
    quitarEmpleadoDeProyecto(id_emp, id_proj)
