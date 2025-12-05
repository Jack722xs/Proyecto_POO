from app.modelo.usuario import Usuario
from app.controlador.DAO_usuario import *
from app.utils.helper import *
import getpass

from app.utils.seguridad import encriptar_password 


def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        intentos += 1
        print(f"Este campo no puede estar vacio. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operacion cancelada.")
    return None

def input_password(mensaje):
    while True:
        pw = getpass.getpass(mensaje).strip()
        if pw != "":
            return pw
        print("Error: La contraseña no puede estar vacia.")

def addUsuario():
    while True:

        print("AGREGAR USUARIO")

        nombre_usuario = input_no_vacio("Ingrese el nombre de usuario: ")
        if nombre_usuario is None: return

        contraseña = input_password("Ingrese la contraseña: ")
        
        email = input_no_vacio("Ingrese el email: ")
        if email is None: return

        password_hash = encriptar_password(contraseña)

        usu = Usuario(
            nombre_usuario=nombre_usuario,
            email=email,
            password_hash=password_hash, 
            contraseña=contraseña        
        )

        if agregarUsuario(usu):
            print("Usuario agregado correctamente.")
        else:
            print("No se pudo agregar el usuario.")

        opcion = input("\n¿Desea agregar otro usuario? (s/n): ").lower()
        if opcion != "s":
            print("Saliendo del registro de usuarios...")
            break
        input("Presiona enter para continuar")


def editUsuario():
    print("EDITAR USUARIO")
    nombre_usuario = input_no_vacio("Ingrese el nombre de usuario a editar: ")
    if nombre_usuario is None: return
    
    nueva_contraseña = input_password("Ingrese nueva contraseña: ")
    
    nuevo_email = input_no_vacio("Ingrese nuevo email: ")
    if nuevo_email is None: return

    
    password_hash = encriptar_password(nueva_contraseña)

    usu = Usuario(
        nombre_usuario=nombre_usuario,
        email=nuevo_email,
        password_hash=password_hash,
        contraseña=nueva_contraseña
    )

    if editarUsuario(usu):
        print("Usuario actualizado correctamente.")
    else:
        print("No se pudo actualizar el usuario (nombre de usuario inexistente)")
    input("Presiona enter para continuar")    

def readUsuario():
    usuarios = verUsuario()
    
    if not usuarios:
        print("\nNo hay usuarios registrados.\n")
        return

    print("\n" + "="*90)
    print(f"{'Usuario':<20} {'Email':<30} {'Rol':<15} {'ID Empleado'}")
    print("="*90)

    for u in usuarios:       
        email = str(u[1])
        usuario = str(u[2])
        rol = str(u[4])
        id_emp = str(u[5]) if u[5] else "N/A"

        print(f"{usuario:<20} {email:<30} {rol:<15} {id_emp}")

    print("="*90 + "\n")

    input("Presiona enter para continuar")




def delUsuario():
    print("ELIMINAR USUARIO")
    nombre_usuario = input_no_vacio("Ingrese el nombre de usuario a eliminar: ")
    if nombre_usuario is None:
        return
    if eliminarUsuario(nombre_usuario):
        print("Usuario eliminado correctamente.")
    else:
        print("No se encontro un usuario con ese nombre.")
    input("Presiona enter para continuar")    