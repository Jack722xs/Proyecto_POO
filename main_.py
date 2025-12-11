import sys
import getpass
import mysql.connector
from app.bbdd.init_db import crear_bd, borrar_base_datos
from app.utils.seguridad import verificar_password
from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion
from app.utils.helper import *
from app.vista.menus.view_menu_admin import menu_admin
from app.vista.menus.view_menu_gerente import menu_gerente
from app.vista.menus.view_menu_empleado import menu_empleado

def autentificacion(nombre_usuario, pw):
    cone = None
    try:
        cone = getConexion()
        cursor = cone.cursor()
        sql = "SELECT password_hash, id_empleado, rol FROM usuario WHERE nombre_usuario = %s"
        cursor.execute(sql, (nombre_usuario,))
        row = cursor.fetchone()

        if not row:
            return False

        hash_pw_str, id_empleado, rol = row

        if verificar_password(pw, hash_pw_str):
            sesion.nombre_usuario = nombre_usuario
            sesion.rol_actual = rol
            sesion.id_empleado_actual = id_empleado
            return True
        
        return False
    except Exception as e:
        print(e)
        return False

def login_terminal():
    intentos = 5  
    
    while intentos > 0:
        saltar_pantalla() 
        print("\n=== LOGIN ECOTECH ===")
        
        try:
            usuario = input("Nombre de usuario: ").strip()
            
            if not usuario:
                intentos -= 1 
                print("ERROR: El usuario no puede estar vacío.")
                print(f"Intentos restantes: {intentos}")
                input("Presione Enter para intentar de nuevo...") 
                continue 
                
            password = getpass.getpass("Contraseña: ")

            if autentificacion(usuario, password):
                print("\nAcceso concedido.")
                print(f"Bienvenido {sesion.nombre_usuario} | Rol: {sesion.rol_actual.upper()}")
                print("-" * 30)

                if sesion.rol_actual == "admin":
                    saltar_pantalla()
                    menu_admin()
                elif sesion.rol_actual == "gerente":
                    saltar_pantalla()
                    menu_gerente()
                elif sesion.rol_actual == "empleado":
                    saltar_pantalla()
                    menu_empleado()
                else:
                    print("Rol desconocido o sin permisos asignados.")
                    input("Presione Enter para continuar...")
                return 

            else:
                intentos -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
                input("Presione Enter para intentar de nuevo...") 

        except KeyboardInterrupt:
            print("\n\nOperacion cancelada por el usuario.")
            return

    print("Demasiados intentos fallidos. Acceso bloqueado temporalmente.")
    input("Presione Enter para volver al menú principal...")

def main():
    print("Verificando sistema de base de datos...")
    
    if not crear_bd():
        print("Error crítico: No se pudo conectar con la base de datos.")
        sys.exit()
    try:
        while True:

            saltar_pantalla() 
            
            print("\n" + "="*30)
            print("SISTEMA PRINCIPAL")
            print("="*30)
            print("1. Iniciar sesion")
            print("2. Salir")
            
            try:
                op = input("\nSelecciona una opcion: ").strip()

                if op == "1":
                    login_terminal()

                elif op == "2":
                    print("Cerrando sistema...")
                    break 

                else:
                    print("Opcion no valida, intente de nuevo.")
                    input("Presione Enter para continuar...") 
            
            except KeyboardInterrupt:
                print("\nInterrupción de teclado detectada...")
                break
            except Exception as e:
                print(f"Error en el menu principal: {e}")
                input("Presione Enter para continuar...")

    finally:
        borrar_base_datos()
        print("¡Hasta luego!")

if __name__ == "__main__":
    main()