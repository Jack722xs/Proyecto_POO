from app.utils.helper import *
from app.controlador.DAO_roles import obtenerRol, cambiarRol, listarRolesValidos
from app.controlador.DAO_usuario import verUsuario # Para validar existencia
from app.vista.view_usuario import readUsuario # Para mostrar la lista visualmente

def menu_roles():
    while True:
        saltar_pantalla()
        print("""
============================================
                 MENU ROLES
============================================
1. Ver rol de un usuario                   =
2. Cambiar rol de un usuario               =
3. Ver roles validos                       =
============================================
4. Volver
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
            ver_rol_usuario()
        elif opc == 2:
            cambiar_rol_usuario()
        elif opc == 3:
            ver_roles_validos()
        elif opc == 4:
            break
        else:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")

def ver_roles_validos():
    saltar_pantalla()
    print("============================================")
    print("              ROLES DISPONIBLES             ")
    print("============================================")
    roles = listarRolesValidos()
    for r in roles:
        print(f"- {r}")
    print("============================================")
    input("Presiona Enter para continuar...")

def ver_rol_usuario():
    saltar_pantalla()
    print("============================================")
    print("            VER ROL DE USUARIO              ")
    print("============================================")
    
    # 1. Mostrar lista de usuarios disponibles
    print("\n--- USUARIOS DISPONIBLES ---")
    readUsuario(pausar=False)
    
    nombre = input("\nIngrese nombre del usuario: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    # 2. Consultar Rol (DAO ya valida si existe en la consulta)
    rol = obtenerRol(nombre)

    print("-" * 40)
    if rol:
        print(f"El rol actual de '{nombre}' es: {rol}")
    else:
        print(f"Error: El usuario '{nombre}' no existe o no se encontró.")

    input("Presiona Enter para continuar...")

def cambiar_rol_usuario():
    saltar_pantalla()
    print("============================================")
    print("          CAMBIAR ROL DE USUARIO            ")
    print("============================================")

    # 1. Mostrar usuarios
    print("\n--- USUARIOS DISPONIBLES ---")
    readUsuario(pausar=False)

    nombre = input("\nIngrese nombre del usuario a modificar: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    # 2. Validar existencia REAL del usuario antes de pedir el rol
    usuarios = verUsuario() # Trae todos los usuarios de la BD
    # Buscamos si el nombre ingresado está en la lista (índice 1 es nombre_usuario)
    existe = False
    for u in usuarios:
        if u[1] == nombre:
            existe = True
            break
    
    if not existe:
        print(f"Error: El usuario '{nombre}' NO existe en la base de datos.")
        print("Operación cancelada.")
        input("Presiona Enter para continuar...")
        return

    # 3. Mostrar Roles y Pedir nuevo
    print("\n--- ROLES VÁLIDOS ---")
    roles = listarRolesValidos()
    print(", ".join(roles))

    nuevo_rol = input("\nIngrese el nuevo rol: ").strip().lower()

    print("-" * 40)
    # cambiarRol valida internamente si el rol es válido
    if cambiarRol(nombre, nuevo_rol):
        # El DAO suele imprimir el éxito, pero reforzamos por si acaso
        pass 
    else:
        print("No se pudo actualizar el rol (verifique que el rol sea válido).")

    # Corrección del error de tipeo "/n"
    input("Presiona Enter para continuar...")