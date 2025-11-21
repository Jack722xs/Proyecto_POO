import sys
import bcrypt
import getpass
import mysql.connector
from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion


from app.vista.menus.view_menu_admin import menu_admin
from app.vista.menus.view_menu_gerente import menu_gerente
from app.vista.menus.view_menu_empleado import menu_empleado


def crear_usuario(nombre_usuario, email, pw):
    """
    Crea el usuario con rol EMPLEADO por defecto.
    Retorna True si se creó correctamente, False si hubo error.
    """
    cone = None
    cursor = None
    try:
        
        pw_hash = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

        cone = getConexion()
        if cone is None:
            print("Error: No se pudo conectar a la base de datos.")
            return False

        cursor = cone.cursor()
        sql = """
            INSERT INTO usuario (nombre_usuario, email, password_hash, rol, id_empleado)
            VALUES (%s, %s, %s, %s, NULL)
        """
        #Guardamos el hash decodificado como string en la BD
        cursor.execute(sql, (nombre_usuario, email, pw_hash.decode('utf-8'), "empleado"))
        cone.commit()
        print("Usuario creado con rol EMPLEADO exitosamente.")
        return True

    except mysql.connector.IntegrityError:
        print("Error: El nombre de usuario o email ya existe.")
        return False
    except mysql.connector.Error as e:
        print(f"Error de Base de Datos: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if cone: cone.close()


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


        # hash_pw_str viene de la BD como string, lo codificamos a bytes para bcrypt
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
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        
        try:
            op = input("\nSelecciona una opcion: ").strip()

            if op == "1":
                print("\n--- Nuevo Registro ---")
                nombre = input("Nuevo nombre de usuario: ").strip()
                email = input("Email: ").strip()
                if not nombre or not email:
                    print("Todos los campos son obligatorios.")
                    continue
                
                pw = getpass.getpass("Nueva contraseña: ")
                crear_usuario(nombre, email, pw)

            elif op == "2":
                login_terminal()

            elif op == "3":
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