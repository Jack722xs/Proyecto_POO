from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import * 
from app.vista.sub_vista.view_usuario_empleado import *
from app.utils.helper import *


from app.controlador.DAO_empleado import verEmpleadoPorID
from app.controlador.DAO_proyecto import verProyecto

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
def menu_departamentos():
    # ... (El código de menu_departamentos se mantiene IGUAL que en la respuesta anterior) ...
    # (Por brevedad, asumo que ya lo tienes corregido. Si necesitas que lo repita, avísame)
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
            if not entrada: continue
            opc = int(entrada)
        except ValueError:
            print("Error: Ingrese un numero valido.")
            input("Presiona Enter para continuar...")
            continue

        if opc == 1: addDepartamento()
        elif opc == 2: editDepartamento()
        elif opc == 3: delDepartamento()
        elif opc == 4: readDepartamento()
        elif opc == 5:
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE EMPLEADO            ")
            print("============================================")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado a asignar: ").strip()
            
            if not id_emp:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue

            # Validación de existencia aquí también recomendada
            if not verEmpleadoPorID(id_emp):
                print(f"Error: Empleado {id_emp} no existe.")
                input("Presiona Enter...")
                continue

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
                    print(f"Se ha desvinculado al empleado {id_emp}.")
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
            id_dep = input("Ingrese ID del departamento: ").strip()
            if not id_dep:
                print("Error: ID vacío.")
            else:
                empleados = verEmpleadosDeDepartamento(id_dep)
                if empleados:
                    print(f"\n=== Empleados del Departamento {id_dep} ===")
                    for e in empleados: print(f"- {e}")
                else:
                    print("\nNo se encontraron empleados.")
            input("\nPresiona Enter para continuar...")
            
        elif opc == 8:
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE PROYECTO            ")
            print("============================================")
            readProyecto(pausar=False)
            id_proj = input("\nIngrese ID del proyecto: ").strip()
            if not id_proj:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue 
            saltar_pantalla()
            print("============================================")
            print("         SELECCIÓN DE DEPARTAMENTO          ")
            print("============================================")
            readDepartamento(pausar=False) 
            id_dep = input("\nIngrese ID del departamento: ").strip()
            print("-" * 40)
            if asignarProyectoADepartamento(id_proj, id_dep):
                print(f"Proyecto {id_proj} asignado correctamente.")
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
            id_dep = input("Ingrese ID del departamento: ").strip()
            if not id_dep:
                print("Error: ID vacío.")
            else:
                proyectos = verProyectosDeDepartamento(id_dep)
                if proyectos:
                    print(f"\n=== Proyectos del Departamento {id_dep} ===")
                    for p in proyectos: print(p)
                else:
                    print("\nNo hay proyectos asignados.")
            input("\nPresiona Enter para continuar...")
            
        elif opc == 10:
            asignarGerente_view()
        elif opc == 11:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")


# -----------------------------
#   MENU EMPLEADOS (CORREGIDO)
# -----------------------------

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
            print("Error: Ingrese un numero valido.")
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

        # --- OPCIÓN 5 CORREGIDA (Tu petición actual) ---
        elif opc == 5:
            # 1. Seleccionar Empleado
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE EMPLEADO            ")
            print("============================================")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado a asignar: ").strip()

            if not id_emp:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue

            # VALIDACIÓN DE EXISTENCIA (Para no saltar a proyectos si falla)
            if not verEmpleadoPorID(id_emp):
                print(f"ERROR: El empleado con ID '{id_emp}' NO existe.")
                input("Presiona Enter para volver...")
                continue

            # 2. Seleccionar Proyecto (Ahora con indicador claro)
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE PROYECTO            ")
            print("============================================")
            
            # --- INDICADOR NUEVO ---
            print("\n--- PROYECTOS DISPONIBLES ---") 
            readProyecto(pausar=False)
            
            id_proj = input("\nIngrese ID del proyecto destino: ").strip()

            if not id_proj:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue

            # VALIDACIÓN DE PROYECTO
            if not verProyecto(id_proj):
                print(f"ERROR: El proyecto con ID '{id_proj}' NO existe.")
                input("Presiona Enter para volver...")
                continue

            # 3. Asignar
            print("-" * 40)
            if asignarEmpleadoAProyecto(id_emp, id_proj):
                print(f"¡ÉXITO! Empleado {id_emp} asignado correctamente al proyecto {id_proj}.")
            else:
                print("No se pudo realizar la asignación (posible duplicado).")
            
            input("Presiona Enter para continuar...")
        # -----------------------------------------------

        elif opc == 6:
            saltar_pantalla()
            print("============================================")
            print("        QUITAR EMPLEADO DE PROYECTO         ")
            print("============================================")
            
            print("\n--- LISTA DE EMPLEADOS ---")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado: ").strip()
            
            if not id_emp:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue
            
            saltar_pantalla()
            print(f"============================================")
            print(f"   PROYECTOS DEL EMPLEADO {id_emp}         ")
            print(f"============================================")
            
            proyectos = verProyectosDeEmpleado(id_emp)
            
            if not proyectos:
                print("Este empleado no tiene proyectos asignados.")
                input("Presiona Enter para continuar...")
                continue

            print(f"{'ID Proyecto':<15} {'Nombre Proyecto'}")
            print("-" * 40)
            lista_proy_ids = []
            for p in proyectos:
                p_id = str(p[0])
                lista_proy_ids.append(p_id)
                print(f"{p_id:<15} {p[1]}")
            print("=" * 40)

            id_proj = input("\nIngrese ID del proyecto a desvincular: ").strip()
            
            if id_proj not in lista_proy_ids:
                print("Error: El empleado no está asignado a ese proyecto o ID incorrecto.")
            else:
                if quitarEmpleadoDeProyecto(id_emp, id_proj):
                    print("Asignación eliminada correctamente.")
                else:
                    print("Error al intentar eliminar la asignación.")
            
            input("Presiona Enter para continuar...")

        elif opc == 7:
            saltar_pantalla()
            print("============================================")
            print("       VER PROYECTOS DE UN EMPLEADO         ")
            print("============================================")
            
            print("\n--- LISTA DE EMPLEADOS ---")
            readEmpleado(pausar=False)
            print("-" * 40)
            id_emp = input("Ingrese ID del empleado a consultar: ").strip()

            if not id_emp:
                print("Error: ID vacío.")
            else:
                proyectos = verProyectosDeEmpleado(id_emp)
                if proyectos:
                    print(f"\n=== Proyectos Asignados al Empleado {id_emp} ===")
                    print(f"{'ID':<12} {'Nombre':<20} {'Estado':<15}")
                    print("-" * 50)
                    for p in proyectos:
                        p_id = str(p[0])
                        p_nom = str(p[1])
                        p_est = str(p[5]) if len(p) > 5 else "N/A"
                        print(f"{p_id:<12} {p_nom:<20} {p_est:<15}")
                    print("=" * 50)
                else:
                    print("\nEste empleado no tiene proyectos asignados.")
            
            input("\nPresiona Enter para continuar...")

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
            print("Error: Ingrese un numero valido.")
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
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE EMPLEADO            ")
            print("============================================")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del empleado a asignar: ").strip()

            if not id_emp:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue

            if not verEmpleadoPorID(id_emp):
                print(f"ERROR: El empleado con ID '{id_emp}' NO existe en el sistema.")
                input("Presiona Enter para volver...")
                continue

            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE PROYECTO            ")
            print("============================================")
            print("\n--- PROYECTOS DISPONIBLES ---")
            readProyecto(pausar=False)
            id_proj = input("\nIngrese ID del proyecto destino: ").strip()

            if not id_proj:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue

            if not verProyecto(id_proj):
                print(f"ERROR: El proyecto con ID '{id_proj}' NO existe.")
                input("Presiona Enter para volver...")
                continue

            print("-" * 40)
            if asignarEmpleadoAProyecto(id_emp, id_proj):
                print(f"¡ÉXITO! Empleado {id_emp} asignado al proyecto {id_proj}.")
            else:
                print("No se pudo asignar.")
            input("Presiona Enter para continuar...")

        elif opc == 6:
            saltar_pantalla()
            print("============================================")
            print("       QUITAR EMPLEADO DE PROYECTO          ")
            print("============================================")
            print("\n--- LISTA DE PROYECTOS ---")
            readProyecto(pausar=False)
            id_proj = input("\nIngrese ID del proyecto: ").strip()

            if not id_proj or not verProyecto(id_proj):
                print("Error: Proyecto no válido.")
                input("Presiona Enter...")
                continue
            
            saltar_pantalla()
            print(f"============================================")
            print(f"   EMPLEADOS DEL PROYECTO {id_proj}        ")
            print(f"============================================")
            
            empleados_asignados = verEmpleadosDeProyecto(id_proj)
            
            if not empleados_asignados:
                print("Este proyecto no tiene empleados asignados.")
                input("Presiona Enter para continuar...")
                continue

            print(f"{'ID':<12} {'Nombre':<15} {'Apellido'}")
            print("-" * 40)
            lista_ids_validos = []
            for e in empleados_asignados:
                e_id = str(e[0])
                lista_ids_validos.append(e_id)
                print(f"{e_id:<12} {e[1]:<15} {e[2]}")
            print("=" * 40)

            id_emp = input("\nIngrese ID del empleado a quitar: ").strip()

            if id_emp not in lista_ids_validos:
                print("Error: Empleado no válido.")
            else:
                if quitarEmpleadoDeProyecto(id_emp, id_proj):
                    print("Asignación eliminada correctamente.")
                else:
                    print("Error al eliminar.")
            input("Presiona Enter para continuar...")

        elif opc == 7:
            saltar_pantalla()
            print("============================================")
            print("       VER EMPLEADOS DE UN PROYECTO         ")
            print("============================================")
            readProyecto(pausar=False)
            print("-" * 40)
            id_proj = input("Ingrese ID del proyecto a consultar: ").strip()

            if not id_proj:
                print("Error: ID vacío.")
            elif not verProyecto(id_proj):
                print("Error: El proyecto no existe.")
            else:
                empleados = verEmpleadosDeProyecto(id_proj)
                if empleados:
                    print(f"\n=== Equipo del Proyecto {id_proj} ===")
                    for e in empleados:
                        print(f"{str(e[0])} - {e[1]} {e[2]}")
                else:
                    print("\nEste proyecto no tiene empleados asignados.")
            input("\nPresiona Enter para continuar...")

        elif opc == 8:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")


# (Mantener menu_usuarios y menu_registro_tiempo como estaban...)
# ... (Resto de funciones) ...
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
            if not entrada: continue
            opc = int(entrada)
        except ValueError:
            print("Error: Ingrese un numero valido.")
            input("Presiona Enter...")
            continue
        
        if opc == 1: addUsuario()
        elif opc == 2: readUsuario()
        elif opc == 3: editUsuario() # Ahora usa la versión corregida de view_usuario.py
        elif opc == 4: delUsuario()
        
        # --- OPCIÓN 5: ASIGNAR USUARIO A EMPLEADO ---
        elif opc == 5:
            saltar_pantalla()
            print("============================================")
            print("         ASIGNAR USUARIO A EMPLEADO         ")
            print("============================================")
            
            # 1. Seleccionar Usuario
            print("\n--- LISTA DE USUARIOS ---")
            readUsuario(pausar=False)
            nombre_usuario = input("\nIngrese Nombre de Usuario: ").strip()

            if not nombre_usuario:
                print("Error: Usuario vacío.")
                input("Presiona Enter...")
                continue
            
            # (Validación simple: verificamos si existe en la lista recuperada o confiamos en el DAO)
            # Para mejor UX, validamos antes de seguir:
            usuarios = verUsuario()
            if not any(u[1] == nombre_usuario for u in usuarios):
                print(f"Error: El usuario '{nombre_usuario}' no existe.")
                input("Presiona Enter...")
                continue

            # 2. Seleccionar Empleado
            saltar_pantalla()
            print("============================================")
            print("           SELECCIÓN DE EMPLEADO            ")
            print("============================================")
            readEmpleado(pausar=False)
            id_emp = input("\nIngrese ID del Empleado a vincular: ").strip()

            if not id_emp:
                print("Error: ID vacío.")
                input("Presiona Enter...")
                continue
            
            if not verEmpleadoPorID(id_emp):
                print(f"Error: El empleado {id_emp} no existe.")
                input("Presiona Enter...")
                continue

            # 3. Vincular (Actualizamos el usuario poniéndole el ID empleado)
            # Como editarUsuario pide todo el objeto, necesitamos los datos actuales del usuario.
            # Buscamos el usuario específico
            usuario_actual = next((u for u in usuarios if u[1] == nombre_usuario), None)
            
            if usuario_actual:
                # usuario_actual: (email, nombre, hash, rol, id_emp_actual)
                # Creamos objeto con el NUEVO id_empleado
                # Nota: usuario_actual[2] es el hash, lo pasamos tal cual para no cambiar la clave
                usu_obj = Usuario(nombre_usuario, usuario_actual[0], usuario_actual[2], id_emp, usuario_actual[3])
                
                print("-" * 40)
                if editarUsuario(usu_obj):
                    print(f"¡ÉXITO! Usuario '{nombre_usuario}' vinculado al empleado {id_emp}.")
                else:
                    print("Error al actualizar la vinculación.")
            else:
                print("Error inesperado recuperando datos del usuario.")

            input("Presiona Enter para continuar...")

        # --- OPCIÓN 6: QUITAR USUARIO DE EMPLEADO ---
        elif opc == 6:
            saltar_pantalla()
            print("============================================")
            print("         DESVINCULAR USUARIO DE EMPLEADO    ")
            print("============================================")
            
            # Mostramos usuarios que TIENEN empleado asignado
            usuarios = verUsuario()
            usuarios_vinculados = [u for u in usuarios if u[4] is not None]

            if not usuarios_vinculados:
                print("\nNo hay usuarios vinculados a empleados actualmente.")
                input("Presiona Enter...")
                continue

            print(f"{'Usuario':<15} {'ID Empleado Asignado'}")
            print("-" * 40)
            lista_nombres_validos = []
            for u in usuarios_vinculados:
                lista_nombres_validos.append(u[1])
                print(f"{u[1]:<15} {u[4]}")
            print("=" * 40)

            nombre_usuario = input("\nIngrese Nombre de Usuario a desvincular: ").strip()

            if nombre_usuario not in lista_nombres_validos:
                print("Error: Usuario no válido o no tiene vinculación.")
            else:
                # Recuperamos datos para update
                usuario_actual = next((u for u in usuarios if u[1] == nombre_usuario), None)
                if usuario_actual:
                    # Pasamos None como id_empleado
                    usu_obj = Usuario(nombre_usuario, usuario_actual[0], usuario_actual[2], None, usuario_actual[3])
                    if editarUsuario(usu_obj):
                        print(f"Vinculación eliminada para '{nombre_usuario}'.")
                    else:
                        print("Error al actualizar.")
            
            input("Presiona Enter para continuar...")

        # --- OPCIÓN 7: VER EMPLEADO ASOCIADO ---
        elif opc == 7:
            saltar_pantalla()
            print("============================================")
            print("       VER EMPLEADO ASOCIADO A USUARIO      ")
            print("============================================")
            
            readUsuario(pausar=False)
            nombre_usuario = input("\nIngrese Nombre de Usuario: ").strip()

            if not nombre_usuario:
                print("Error: Vacío.")
            else:
                # Buscamos en la lista
                usuarios = verUsuario()
                usuario_target = next((u for u in usuarios if u[1] == nombre_usuario), None)
                
                if not usuario_target:
                    print(f"El usuario '{nombre_usuario}' no existe.")
                else:
                    id_emp = usuario_target[4]
                    if not id_emp:
                        print(f"El usuario '{nombre_usuario}' NO tiene empleado asociado.")
                    else:
                        # Buscamos datos del empleado para mostrar detalle
                        emp = verEmpleadoPorID(id_emp)
                        print("-" * 40)
                        if emp:
                            print(f"Empleado Asociado: {emp[1]} {emp[2]} (ID: {emp[0]})")
                            print(f"Cargo: {'Gerente' if emp[7] else 'Empleado'}")
                        else:
                            print(f"ID asociado: {id_emp} (Pero el empleado ya no existe en BD).")
            
            input("\nPresiona Enter para continuar...")

        elif opc == 8:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter...")