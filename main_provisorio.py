from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *

# Nuevas vistas de relaciones
from app.controlador.sub_controlador.DAO_empleado_departamento import *
from app.controlador.sub_controlador.DAO_empleado_proyecto import *
from app.controlador.sub_controlador.DAO_proyecto_departamento import *


def menu_principal():
    while True:
        print("""
======================
      MENU ECOTECH
======================
1. Departamentos
2. Empleados
3. Proyectos
4. Usuarios
5. Salir
""")

        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: ingrese un numero.")
            continue

        if opc == 1:
            menu_departamentos()
        elif opc == 2:
            menu_empleados()
        elif opc == 3:
            menu_proyectos()
        elif opc == 4:
            menu_usuarios()
        elif opc == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida.")


# -----------------------------
#   MENU DEPARTAMENTOS
# -----------------------------
def menu_departamentos():
    while True:
        print("""
------ MENU DEPARTAMENTOS ------
1. Agregar Departamento
2. Editar Departamento
3. Eliminar Departamento
4. Ver Departamentos
5. Asignar empleado a departamento
6. Quitar empleado de departamento
7. Ver empleados por departamento
8. Asignar proyecto a departamento
9. Ver proyectos por departamento
10. Volver
""")

        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero.")
            continue

        if opc == 1:
            addDepartamento()
        elif opc == 2:
            editDepartamento()
        elif opc == 3:
            delDepartamento()
        elif opc == 4:
            readDepartamento()
        elif opc == 5:
            id_emp = input("ID empleado: ")
            id_dep = input("ID departamento: ")
            asignarEmpleadoADepartamento(id_emp, id_dep)
        elif opc == 6:
            id_emp = input("ID empleado: ")
            quitarEmpleadoDeDepartamento(id_emp)
        elif opc == 7:
            id_dep = input("ID departamento: ")
            print(verEmpleadosDeDepartamento(id_dep))
        elif opc == 8:
            id_proj = input("ID proyecto: ")
            id_dep = input("ID departamento: ")
            asignarProyectoADepartamento(id_proj, id_dep)
        elif opc == 9:
            id_dep = input("ID departamento: ")
            print(verProyectosDeDepartamento(id_dep))
        elif opc == 10:
            break
        else:
            print("Opcion invalida.")


# -----------------------------
#   MENU EMPLEADOS
# -----------------------------
def menu_empleados():
    while True:
        print("""
------ MENU EMPLEADOS ------
1. Agregar Empleado
2. Editar Empleado
3. Eliminar Empleado
4. Ver Empleados
5. Asignar empleado a proyecto
6. Quitar empleado de proyecto
7. Ver proyectos de un empleado
8. Volver
""")

        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero valido.")
            continue

        if opc == 1:
            addEmpleado()
        elif opc == 2:
            editEmpleado()
        elif opc == 3:
            delEmpleado()
        elif opc == 4:
            readEmpleado()
        elif opc == 5:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            asignarEmpleadoAProyecto(id_emp, id_proj)
        elif opc == 6:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            quitarEmpleadoDeProyecto(id_emp, id_proj)
        elif opc == 7:
            id_emp = input("ID empleado: ")
            print(verProyectosDeEmpleado(id_emp))
        elif opc == 8:
            break
        else:
            print("Opción inválida.")


# -----------------------------
#   MENU PROYECTOS
# -----------------------------
def menu_proyectos():
    while True:
        print("""
------ MENÚ PROYECTOS ------
1. Agregar Proyecto
2. Editar Proyecto
3. Eliminar Proyecto
4. Ver Proyectos
5. Asignar empleado a proyecto
6. Quitar empleado de proyecto
7. Ver empleados de un proyecto
8. Volver
""")

        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opc == 1:
            addProyecto()
        elif opc == 2:
            editProyecto()
        elif opc == 3:
            delProyecto()
        elif opc == 4:
            readProyecto()
        elif opc == 5:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            asignarEmpleadoAProyecto(id_emp, id_proj)
        elif opc == 6:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            quitarEmpleadoDeProyecto(id_emp, id_proj)
        elif opc == 7:
            id_proj = input("ID proyecto: ")
            print(verEmpleadosDeProyecto(id_proj))
        elif opc == 8:
            break
        else:
            print("Opción inválida.")


# -----------------------------
#   MENU USUARIOS
# -----------------------------
def menu_usuarios():
    while True:
        print("""
------ MENÚ USUARIOS ------
1. Registrar usuario
2. Ver usuarios
3. Editar usuario
4. Eliminar usuario
5. Volver
""")
        
        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue
        
        if opc == 1:
            addUsuario()
        elif opc == 2:
            readUsuario()
        elif opc == 3:
            editUsuario()
        elif opc == 4:
            delUsuario()
        elif opc == 5:
            break
        else:
            print("Opción inválida.")


# Ejecutar menú principal

