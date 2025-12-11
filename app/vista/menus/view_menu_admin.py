from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import * 
from app.vista.sub_vista.view_usuario_empleado import *
from app.utils.helper import *

from app.controlador.sub_controlador.DAO_empleado_departamento import *
from app.controlador.sub_controlador.DAO_empleado_proyecto import *
from app.controlador.sub_controlador.DAO_proyecto_departamento import *
from app.vista.view_indicadores import menu_indicadores
from app.vista.view_roles import *
from app.vista.view_extras import menu_extras 


def menu_admin():
    while True:
        saltar_pantalla()
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
9. Extras (API 2 y JSON)                   = 
============================================
0. Salir
""")

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Error: ingrese un numero.")
            input("Presiona enter para continuar")
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
        elif opc == 9:
            menu_extras()
        elif opc == 0:
            print("Saliendo del sistema...")
            saltar_pantalla()
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")

# -----------------------------
#   MENU DEPARTAMENTOS
# -----------------------------

# ... (imports y otras funciones) ...

# ... (imports se mantienen igual)

# ... (imports se mantienen igual) ...

def menu_departamentos():
    while True:
        saltar_pantalla() 
        print("""
============================================
            MENU DEPARTAMENTOS
============================================
1. Agregar Departamento                    =
2. Editar Departamento                     =
3. Eliminar Departamento                   =
4. Ver Departamentos                       =
5. Asignar empleado a departamento         =
6. Quitar empleado de departamento         =
7. Ver empleados por departamento          =
8. Asignar proyecto a departamento         =
9. Ver proyectos por departamento          =
10. Asignar gerente a departamento         =
============================================              
11. Volver
""")

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Error: Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
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
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE EMPLEADO            ")
            print("============================================")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado a asignar: ").strip()

            saltar_pantalla()
            print("============================================")
            print("         SELECCIÓN DE DEPARTAMENTO          ")
            print("============================================")
            readDepartamento(pausar=False)
            id_dep = input("\nIngrese ID del departamento destino: ").strip()

            print("-" * 40)
            if asignarEmpleadoADepartamento(id_emp, id_dep):
                print(f"Empleado {id_emp} asignado correctamente al departamento {id_dep}.")
            else:
                print("No se pudo realizar la asignación.")
            input("Presiona Enter para continuar...")

        elif opc == 6:
            saltar_pantalla()
            print("============================================")
            print("      QUITAR EMPLEADO DE DEPARTAMENTO       ")
            print("============================================")
            print("\n--- LISTA DE EMPLEADOS ---")
            readEmpleado(pausar=False)
            print("-" * 40)
            id_emp = input("Ingrese ID del empleado a desvincular: ").strip()

            if not id_emp:
                print("Error: El ID no puede estar vacío.")
            else:
                if quitarEmpleadoDeDepartamento(id_emp):
                    print(f"Se ha desvinculado al empleado {id_emp} de su departamento.")
                else:
                    print("Error: No se pudo realizar la operación.")
            input("Presiona Enter para continuar...")

        elif opc == 7:
            saltar_pantalla()
            print("============================================")
            print("      VER EMPLEADOS POR DEPARTAMENTO        ")
            print("============================================")
            print("\n--- DEPARTAMENTOS DISPONIBLES ---")
            readDepartamento(pausar=False)
            print("-" * 40)
            id_dep = input("Ingrese ID del departamento a consultar: ").strip()

            if not id_dep:
                print("Error: El ID no puede estar vacío.")
            else:
                empleados = verEmpleadosDeDepartamento(id_dep)
                if empleados:
                    print(f"\n=== Empleados del Departamento {id_dep} ===")
                    for e in empleados:
                        print(f"- {e}")
                else:
                    print("\nNo se encontraron empleados en este departamento.")
            input("\nPresiona Enter para continuar...")

        elif opc == 8:
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE PROYECTO            ")
            print("============================================")
            readProyecto(pausar=False)
            id_proj = input("\nIngrese ID del proyecto a asignar: ").strip()

            if not id_proj:
                print("Error: El ID del proyecto no puede estar vacío.")
                input("Presiona Enter para continuar...")
                continue 

            saltar_pantalla()
            print("============================================")
            print("         SELECCIÓN DE DEPARTAMENTO          ")
            print("============================================")
            readDepartamento(pausar=False) 
            id_dep = input("\nIngrese ID del departamento destino: ").strip()

            if not id_dep:
                print("Error: El ID del departamento no puede estar vacío.")
                input("Presiona Enter para continuar...")
                continue

            print("-" * 40)
            if asignarProyectoADepartamento(id_proj, id_dep):
                print(f"Proyecto {id_proj} asignado correctamente al departamento {id_dep}.")
            else:
                print("No se pudo realizar la asignación.")
            input("Presiona Enter para continuar...")

        elif opc == 9:
            saltar_pantalla()
            print("============================================")
            print("      VER PROYECTOS POR DEPARTAMENTO        ")
            print("============================================")
            print("\n--- DEPARTAMENTOS DISPONIBLES ---")
            readDepartamento(pausar=False)
            print("-" * 40)
            id_dep = input("Ingrese ID del departamento a consultar: ").strip()

            if not id_dep:
                print("Error: El ID no puede estar vacío.")
            else:
                proyectos = verProyectosDeDepartamento(id_dep)
                if proyectos:
                    print(f"\n=== Proyectos del Departamento {id_dep} ===")
                    print(f"{'ID':<12} {'Nombre':<20} {'Estado':<15}")
                    print("-" * 50)
                    for p in proyectos:
                        p_id = str(p[0])
                        p_nom = str(p[1])
                        p_est = str(p[5]) if len(p) > 5 else "N/A"
                        print(f"{p_id:<12} {p_nom:<20} {p_est:<15}")
                    print("=" * 50)
                else:
                    print("\nNo hay proyectos asignados a este departamento.")
            input("\nPresiona Enter para continuar...")

        # --- OPCIÓN 10 CORREGIDA ---
        elif opc == 10:
            saltar_pantalla()
            print("============================================")
            print("      ASIGNAR GERENTE A DEPARTAMENTO        ")
            print("============================================")
            
            # 1. Mostrar Empleados
            print("\n--- LISTA DE EMPLEADOS ---")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado (candidato a gerente): ").strip()

            if not id_emp:
                print("Error: El ID del empleado no puede estar vacío.")
                input("Presiona Enter para continuar...")
                continue

            # 2. LIMPIAR PANTALLA Y MOSTRAR DEPARTAMENTOS (Corrección aquí)
            saltar_pantalla()
            print("============================================")
            print("         SELECCIÓN DE DEPARTAMENTO          ")
            print("============================================")
            readDepartamento(pausar=False)
            id_dep = input("\nIngrese ID del departamento: ").strip()

            if not id_dep:
                print("Error: El ID del departamento no puede estar vacío.")
                input("Presiona Enter para continuar...")
                continue

            print("-" * 40)
            usuario = verUsuarioPorEmpleado(id_emp)
            
            if not usuario:
                print("ERROR: Este empleado no tiene un usuario de sistema asociado.")
                print("Nota: Solo los usuarios con rol 'gerente' pueden ser asignados.")
            else:
                rol_actual = usuario[2]
                if rol_actual.lower() != "gerente":
                    print(f"ERROR: El usuario asociado tiene rol '{rol_actual}'.")
                    print("Se requiere rol 'gerente' para esta asignación.")
                else:
                    if asignarGerente(id_dep, id_emp):
                        print(f"¡ÉXITO! Empleado {id_emp} asignado como Gerente del Departamento {id_dep}.")
                    else:
                        print("Error: No se pudo asignar (verifique IDs).")

            input("\nPresiona Enter para continuar...")
        # ---------------------------

        elif opc == 11:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")

def menu_empleados():
    while True:
        saltar_pantalla()
        print("""
============================================
              MENU EMPLEADOS
============================================
1. Agregar Empleado                        =
2. Editar Empleado                         =
3. Eliminar Empleado                       =
4. Ver Empleados                           =
5. Asignar empleado a proyecto             =
6. Quitar empleado de proyecto             =
7. Ver proyectos de un empleado            =
============================================
8. Volver
""")

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
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
            input("Presiona Enter para continuar...")
        elif opc == 6:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            quitarEmpleadoDeProyecto(id_emp, id_proj)
            input("Presiona Enter para continuar...")
        elif opc == 7:
            id_emp = input("ID empleado: ")
            print(verProyectosDeEmpleado(id_emp))
            input("Presiona Enter para continuar...")
        elif opc == 8:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")


# -----------------------------
#   MENU PROYECTOS
# -----------------------------

def menu_proyectos():
    while True:
        saltar_pantalla()
        print("""
============================================
              MENU PROYECTOS
============================================
1. Agregar Proyecto                        =
2. Editar Proyecto                         =
3. Eliminar Proyecto                       =
4. Ver Proyectos                           =
5. Asignar empleado a proyecto             =
6. Quitar empleado de proyecto             =
7. Ver empleados de un proyecto            =
============================================
8. Volver
""")

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
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
            input("Presiona Enter para continuar...")
        elif opc == 6:
            id_emp = input("ID empleado: ")
            id_proj = input("ID proyecto: ")
            quitarEmpleadoDeProyecto(id_emp, id_proj)
            input("Presiona Enter para continuar...")
        elif opc == 7:
            id_proj = input("ID proyecto: ")
            print(verEmpleadosDeProyecto(id_proj))
            input("Presiona Enter para continuar...")
        elif opc == 8:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")


#   MENU USUARIOS

def menu_usuarios():
    while True:
        saltar_pantalla()
        print("""
============================================
               MENU USUARIOS
============================================
1. Registrar usuario                       =
2. Ver usuarios                            =
3. Editar usuario                          =
4. Eliminar usuario                        =
5. Asignar usuario a empleado              =
6. Quitar usuario de empleado              =
7. Ver empleado asociado a usuario         =
============================================
8. Volver
""")
        
        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
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
            input("Presiona Enter para continuar...")

# -----------------------------
#   MENU REGISTRO TIEMPO
# -----------------------------

def menu_registro_tiempo():
    while True:
        saltar_pantalla()
        print("""
============================================
          MENU REGISTRO DE HORAS
============================================
1. Registrar horas trabajadas              =
2. Ver registros por empleado              =
3. Ver registros por proyecto              =
============================================
4. Volver
""")
        
        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
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

if __name__ == "__main__":
    menu_admin()