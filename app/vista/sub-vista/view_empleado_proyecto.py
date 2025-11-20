from app.controlador.sub_controlador.DAO_empleado_proyecto import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato: return dato
        intentos += 1
        print(f"Campo vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos.")
    return None


# ----------------------------------
#   EMPLEADO ↔ PROYECTO (N a N)
# ----------------------------------

#def asignar_empleado_proyecto():
#        print("\nASIGNAR EMPLEADO A PROYECTO")    
#        id_emp = input_no_vacio("ID empleado: ")
#        if id_emp is None: return
#        id_proy = input_no_vacio("ID proyecto: ")
#        if id_proy is None: return
#
#        if asignarEmpleadoAProyecto(id_emp, id_proy):
#            print("Empleado asignado al proyecto.")
#        else:
#            print("Error al asignar.")




def quitar_empleado_proyecto():
    print("\nQUITAR EMPLEADO DE PROYECTO")
    id_emp = input_no_vacio("ID empleado: ")
    if id_emp is None: return
    id_proy = input_no_vacio("ID proyecto: ")
    if id_proy is None: return

    if quitarEmpleadoDeProyecto(id_emp, id_proy):
        print("Empleado eliminado del proyecto.")
    else:
        print("Error al eliminar.")


def ver_empleados_proyecto():
    print("\nVER EMPLEADOS DE UN PROYECTO")
    id_proy = input_no_vacio("ID proyecto: ")
    if id_proy is None: return

    empleados = verEmpleadosDeProyecto(id_proy)
    if empleados:
        print("\nListado:")
        for e in empleados:
            print(e)
    else:
        print("No hay empleados asignados.")


def ver_proyectos_empleado():
    print("\nVER PROYECTOS DE UN EMPLEADO")
    id_emp = input_no_vacio("ID empleado: ")
    if id_emp is None: return

    proyectos = verProyectosDeEmpleado(id_emp)
    if proyectos:
        print("\nProyectos:")
        for p in proyectos:
            print(p)
    else:
        print("El empleado no tiene proyectos asignados.")
