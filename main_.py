import sys
import bcrypt
import getpass
import mysql.connector
from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion

# Importación de menús por rol
from app.vista.menus.view_menu_admin import menu_admin
from app.vista.menus.view_menu_gerente import menu_gerente
from app.vista.menus.view_menu_empleado import menu_empleado


def autentificacion(nombre_usuario, pw):
    """
    Valida credenciales y almacena datos en sesion.
    Retorna True si es valido, False en caso contrario.
    """
    cone = None
    cursor = None
    try:
        cone = getConexion()
        if cone is None:
            print("Error: No hay conexion.")
            return False

        cursor = cone.cursor()
        sql = "SELECT password_hash, id_empleado, rol FROM usuario WHERE nombre_usuario = %s"
        cursor.execute(sql, (nombre_usuario,))
        row = cursor.fetchone()

        if not row:
            return False

        hash_pw_str, id_empleado, rol = row

        # Verificar contraseña con bcrypt
        if bcrypt.checkpw(pw.encode('utf-8'), hash_pw_str.encode('utf-8')):
            # Guardar en sesion global
            sesion.nombre_usuario = nombre_usuario
            sesion.rol_actual = rol
            sesion.id_empleado_actual = id_empleado
            return True
        
        return False

    except mysql.connector.Error as e:
        print(f"Error de conexión al autenticar: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if cone: cone.close()


def login_terminal():
    print("\n=== LOGIN ECOTECH ===")
    intentos = 3

    while intentos > 0:
        try:
            usuario = input("Nombre de usuario: ").strip()
            if not usuario:
                print("El usuario no puede estar vacío.")
                continue
                
            password = getpass.getpass("Contraseña: ")

            if autentificacion(usuario, password):
                print("\nAcceso concedido.")
                print(f"Bienvenido {sesion.nombre_usuario} | Rol: {sesion.rol_actual.upper()}")
                print("-" * 30)

                # Redirección según rol
                if sesion.rol_actual == "admin":
                    menu_admin()
                elif sesion.rol_actual == "gerente":
                    menu_gerente()
                elif sesion.rol_actual == "empleado":
                    menu_empleado()
                else:
                    print("Rol desconocido o sin permisos asignados.")
                return 

            else:
                intentos -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

        except KeyboardInterrupt:
            print("\n\nOperacion cancelada por el usuario.")
            return

    print("Demasiados intentos fallidos. Acceso bloqueado temporalmente.")


def main():
    while True:
        print("\n" + "="*30)
        print("      SISTEMA PRINCIPAL")
        print("="*30)
        # Menú simplificado: Solo Login y Salir
        print("1. Iniciar sesion")
        print("2. Salir")
        
        try:
            op = input("\nSelecciona una opcion: ").strip()

            if op == "1":
                login_terminal()

            elif op == "2":
                print("Saliendo del sistema... ¡Hasta luego!")
                break

            else:
                print("Opcion no valida, intente de nuevo.")
        
        except KeyboardInterrupt:
            print("\nSaliendo...")
            sys.exit()
        except Exception as e:
            print(f"Error en el menu principal: {e}")

if __name__ == "__main__":
    main()