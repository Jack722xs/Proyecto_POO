from app.modelo.usuario import Usuario
from app.controlador.DAO_usuario import *
import bcrypt
import getpass  #LIBRERIA PARA OCULTAR CONTRASEÑA

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

#FUNCION PARA PEDIR CONTRASEÑA OCULTA
def input_password(mensaje):
    while True:
        # getpass oculta lo que escribes en la terminal
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

        # --- ENCRIPTACIÓN ---
        hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
        password_hash = hashed.decode('utf-8') 
        # --------------------

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


def editUsuario():
    print("EDITAR USUARIO")
    nombre_usuario = input_no_vacio("Ingrese el nombre de usuario a editar: ")
    if nombre_usuario is None: return
    

    nueva_contraseña = input_password("Ingrese nueva contraseña: ")
    
    nuevo_email = input_no_vacio("Ingrese nuevo email: ")
    if nuevo_email is None: return

  
    hashed = bcrypt.hashpw(nueva_contraseña.encode('utf-8'), bcrypt.gensalt())
    password_hash = hashed.decode('utf-8') 

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

def readUsuario():
    usuarios = verUsuario()
    if usuarios:
        for u in usuarios:
            print(u)
    else:
        print("No hay usuarios registrados.")

def delUsuario():
    print("ELIMINAR USUARIO")
    nombre_usuario = input_no_vacio("Ingrese el nombre de usuario a eliminar: ")
    if nombre_usuario is None:
        return
    if eliminarUsuario(nombre_usuario):
        print("Usuario eliminado correctamente.")
    else:
        print("No se encontro un usuario con ese nombre.")