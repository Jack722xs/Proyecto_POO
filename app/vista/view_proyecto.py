from app.modelo.proyecto import proyecto
from app.controlador.DAO_proyecto import *



#Evitar inputs vacios
def input_no_vacio(mensaje, max_intentos = 5):
    intentos = 0

  
    while intentos < max_intentos:
        dato = input(mensaje).strip() #esta funcion remueve los caracteres del inicio y del final para que no hay espacios extras

        if dato != "":          
            return dato

        intentos += 1
        print(f"Este campo no puede estar vacio. Intento {intentos}/{max_intentos}")

    print("Demasiados intentos fallidos. Operacion cancelada.")
    return None


def addProyecto():
    print("AGREGAR PROYECTO")

    id_proyecto = input_no_vacio("ID proyecto: ")
    if id_proyecto is None: return

    descripcion = input_no_vacio("Descripcion: ")
    if descripcion is None: return

    estado_proyecto = input_no_vacio("Estado del Proyecto: ")
    if estado_proyecto is None: return

    
    fecha_inicio = input_no_vacio("Fecha inicial (YYYY-MM-DD): ")
    if fecha_inicio is None: return

    
    fecha_fin = input_no_vacio("Fecha final (YYYY-MM-DD): ")
    if fecha_fin is None: return

    nombre = input_no_vacio("Nombre del proyecto: ")
    if nombre is None: return

    proy = proyecto(id_proyecto, descripcion, estado_proyecto, fecha_fin, fecha_inicio, nombre)

    if agregarProyecto(proy):
        print("Proyecto agregado correctamente.")
    else:
        print("No se pudo agregar el proyecto.")


def editProyecto():
    print("EDITAR PROYECTO")

    id_proyecto = input_no_vacio("ID proyecto a editar: ")
    if id_proyecto is None: return

    descripcion = input_no_vacio("Nueva descripcion: ")
    if descripcion is None: return

    estado_proyecto = input_no_vacio("Nuevo estado de proyecto: ")
    if estado_proyecto is None: return

    fecha_fin = input_no_vacio("Nueva fecha final (YYYY-MM-DD): ")
    if fecha_fin is None: return

    fecha_inicio = input_no_vacio("Nueva fecha inicial (YYYY-MM-DD): ")
    if fecha_inicio is None: return

    nombre = input_no_vacio("Nuevo nombre: ")
    if nombre is None: return

    proy = proyecto(id_proyecto, descripcion, estado_proyecto, fecha_fin, fecha_inicio, nombre)

    if editarProyecto(proy):
        print("Proyecto actualizado correctamente.")
    else:
        print("No se pudo actualizar (ID inexistente).")



def delProyecto():
    print("ELIMINAR PROYECTO")

    id_proyecto = input_no_vacio("ID empleado a eliminar: ")
    if id_proyecto is None: return

    if eliminarProyecto(id_proyecto):
        print("Proyecto eliminado.")
    else:
        print("No existe un Proyecto con ese ID.")



def readProyecto():
    
    proyecto = verProyectos()
    print(proyecto)
