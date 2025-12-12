from app.modelo.usuario import Usuario
from app.controlador.DAO_usuario import *
from app.utils.helper import *
from app.utils.seguridad import encriptar_password
import getpass

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": return dato
        intentos += 1
        print(f"Error: Este campo no puede estar vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operación cancelada.")
    return None

def input_password_seguro(mensaje):
    """Pide contraseña ocultando caracteres y valida que no sea vacía."""
    while True:
        pw = getpass.getpass(mensaje).strip()
        if pw != "": 
            return pw
        print("Error: La contraseña no puede estar vacía.")


def addUsuario():
    while True:
        saltar_pantalla()
        print("============================================")
        print("             REGISTRAR USUARIO              ")
        print("============================================")
        
        nombre_usuario = input_no_vacio("Nombre de usuario: ")
        if nombre_usuario is None: break
        
        email = input_no_vacio("Email corporativo: ")
        if email is None: break
        
        contraseña = input_password_seguro("Ingrese Contraseña: ")
        
        print("\n(Opcional) Asociar a un empleado existente.")
        id_empleado_str = input("ID Empleado (Enter para omitir): ").strip()
        
        id_empleado = None
        if id_empleado_str:
            if id_empleado_str.isdigit():
                id_empleado = int(id_empleado_str)
            else:
                print("Aviso: ID no válido, se dejará sin empleado asociado.")

        print("\nRoles disponibles: admin, gerente, empleado")
        rol = input("Ingrese rol (Enter para 'empleado'): ").strip().lower()
        if rol not in ['admin', 'gerente', 'empleado']:
            rol = 'empleado'

        password_hash = encriptar_password(contraseña)
        nuevo_usuario = Usuario(nombre_usuario, email, password_hash, id_empleado, rol)
        
        print("-" * 40)
        if agregarUsuario(nuevo_usuario):
            print(f"¡Usuario '{nombre_usuario}' registrado exitosamente!")
        else:
            print("Error: No se pudo registrar (posible nombre de usuario duplicado).")

        print("-" * 40)
        opcion = input("¿Desea registrar otro usuario? (s/n): ").strip().lower()
        if opcion != "s":
            break

def readUsuario(pausar=True):
    if pausar:
        saltar_pantalla()
        print("============================================")
        print("              LISTA DE USUARIOS             ")
        print("============================================")

    usuarios = verUsuario()
    
    if not usuarios:
        print("\nNo hay usuarios registrados.\n")
    else:
        print(f"{'Usuario':<15} {'Rol':<10} {'ID Emp.':<10} {'Email'}")
        print("="*80)
        for u in usuarios:
            nombre = str(u[1])
            rol = str(u[3]) if u[3] else "N/A"
            id_emp = str(u[4]) if u[4] else "---"
            email = str(u[0])
            print(f"{nombre:<15} {rol:<10} {id_emp:<10} {email}")
        print("="*80)
    
    if pausar:
        input("\nPresiona Enter para continuar...")

def editUsuario():
    saltar_pantalla()
    print("============================================")
    print("               EDITAR USUARIO               ")
    print("============================================")
    
    usuarios_existentes = verUsuario()
    if not usuarios_existentes:
        print("No hay usuarios para editar.")
        input("Presiona Enter...")
        return

    print(f"{'Usuario':<15} {'Email'}")
    print("-" * 40)
    lista_nombres = []
    for u in usuarios_existentes:
        lista_nombres.append(str(u[1])) 
        print(f"{u[1]:<15} {u[0]}")
    print("=" * 40)

    print("-" * 40)
    nombre_usuario = input("Ingrese nombre de usuario a editar: ").strip()
    
    if not nombre_usuario:
        print("Error: Debe ingresar un nombre.")
        input("Presiona Enter...")
        return

    if nombre_usuario not in lista_nombres:
        print(f"\nError: El usuario '{nombre_usuario}' NO existe.")
        input("Presiona Enter para continuar...")
        return

    print(f"\n--- Editando a {nombre_usuario} ---")
    print("Deje vacío si no desea cambiar el valor.")
    
    nuevo_email = input("Nuevo Email: ").strip()
    if nuevo_email == "":
        print("Error: El email es obligatorio (o ingrese el mismo).")
        input("Presiona Enter...")
        return

    nuevo_rol = input("Nuevo Rol (admin/gerente/empleado): ").strip().lower()
    
    cambiar_pass = input("¿Desea cambiar la contraseña? (s/n): ").lower()
    nuevo_hash = None 
    
    if cambiar_pass == 's':
        nueva_pass = input_password_seguro("Nueva Contraseña: ")
        nuevo_hash = encriptar_password(nueva_pass)
    else:
        pass 

    if nuevo_rol not in ['admin', 'gerente', 'empleado', '']:
        nuevo_rol = 'empleado'
    if nuevo_rol == "": nuevo_rol = 'empleado'

    usu_edit = Usuario(nombre_usuario, nuevo_email, nuevo_hash, None, nuevo_rol)

    if editarUsuario(usu_edit):
        print("Usuario actualizado (Si la contraseña se dejó vacía, verifique su DAO).")
    else:
        print("No se pudo actualizar.")
    input("Presiona Enter para continuar...")

def delUsuario():
    saltar_pantalla()
    print("============================================")
    print("              ELIMINAR USUARIO              ")
    print("============================================")
    
    readUsuario(pausar=False)

    print("-" * 40)
    nombre_usuario = input("Ingrese nombre de usuario a eliminar: ").strip()
    
    if not nombre_usuario:
        print("Error: Campo vacío.")
        input("Presiona Enter...")
        return

    confirmar = input(f"¿Seguro de eliminar a '{nombre_usuario}'? (s/n): ").lower()
    if confirmar == 's':
        if eliminarUsuario(nombre_usuario):
            print("Usuario eliminado correctamente.")
        else:
            print("No se encontró el usuario.")
    
    input("Presiona Enter para continuar...")