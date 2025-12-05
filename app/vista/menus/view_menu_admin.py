from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import * 
from app.vista.sub_vista.view_usuario_empleado import *

# Nuevas vistas de relaciones
from app.controlador.sub_controlador.DAO_empleado_departamento import *
from app.controlador.sub_controlador.DAO_empleado_proyecto import *
from app.controlador.sub_controlador.DAO_proyecto_departamento import *
from app.vista.view_indicadores import menu_indicadores
from app.vista.view_roles import *

# === IMPORTANTE: AGREGAR ESTA LÍNEA PARA QUE FUNCIONE LA OPCIÓN 9 ===
from app.vista.view_extras import menu_extras 
# ====================================================================

def menu_admin():
    while True:
        print("""
============================================
                MENU ADMIN                   
============================================
1. Departamentos                           =
2. Empleados                               =
3. Proyectos                               =
4. Usuarios                                =
5. Generar Informes PDF                    =
6. Registro Horas Trabajadas               =
7. Roles                                   =
8. Indicadores Economicos (API)            =
9. Extras (API 2 y JSON)                   =  <-- NUEVA OPCION
============================================
0. Salir
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
            menu_informes()  
        elif opc == 6:
            menu_registro_tiempo()
        elif opc == 7:
            menu_roles()
        elif opc == 8:
            menu_indicadores()
        
        # === AGREGAR ESTE BLOQUE ===
        elif opc == 9:
            menu_extras()
        # ===========================

        elif opc == 0:
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
10. Asignar gerente a departamento
11. Volver
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
            asignarGerente_view()
        elif opc == 11:
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
            print("Opcion invalida.")



# -----------------------------
#   MENU PROYECTOS
# -----------------------------

def menu_proyectos():
    while True:
        print("""
------ MENU PROYECTOS ------
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
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero valido.")
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
            print("Opcion invalida.")




#   MENU USUARIOS

def menu_usuarios():
    while True:
        print("""
------ MENU USUARIOS ------
1. Registrar usuario
2. Ver usuarios
3. Editar usuario
4. Eliminar usuario
5. Asignar usuario a empleado
6. Quitar usuario de empleado
7. Ver empleado asociado a usuario

8. Volver
""")
        
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero valido.")
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
            addUsuarioAEmpleado()
        elif opc == 6:
            delUsuarioDeEmpleado()
        elif opc == 7:
            readEmpleadoDeUsuario()
        elif opc == 8:
            break
        else:
            print("Opcion invalida.")

# -----------------------------
#   MENU REGISTRO TIEMPO
# -----------------------------

def menu_registro_tiempo():
    while True:
        print("""
------ MENU REGISTRO DE HORAS ------
1. Registrar horas trabajadas
2. Ver registros por empleado
3. Ver registros por proyecto
4. Volver
""")
        
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero valido.")
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


if __name__ == "__main__":
    menu_admin()

