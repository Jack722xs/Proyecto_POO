from app.controlador.sub_controlador.DAO_proyecto_departamento import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato: return dato
        intentos += 1
        print(f"Campo vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos.")
    return None


# -------------------------
#   PROYECTO → DEPARTAMENTO
# -------------------------

def asignar_proyecto_departamento():
    print("\nASIGNAR PROYECTO A DEPARTAMENTO")
    id_proy = input_no_vacio("ID proyecto: ")
    if id_proy is None: return
    id_dep = input_no_vacio("ID departamento: ")
    if id_dep is None: return

    if asignarProyectoADepartamento(id_proy, id_dep):
        print("Proyecto asignado correctamente.")
    else:
        print("Error.")


def quitar_proyecto_departamento():
    print("\nQUITAR PROYECTO DE DEPARTAMENTO")
    id_proy = input_no_vacio("ID proyecto: ")
    if id_proy is None: return

    if quitarProyectoDeDepartamento(id_proy):
        print("Proyecto removido.")
    else:
        print("Error.")


def ver_proyectos_departamento():
    print("\nVER PROYECTOS POR DEPARTAMENTO")
    id_dep = input_no_vacio("ID departamento: ")
    if id_dep is None: return

    proyectos = verProyectosDeDepartamento(id_dep)
    if proyectos:
        print("\nListado de proyectos:")
        for p in proyectos:
            print(p)
    else:
        print("No hay proyectos asociados.")
