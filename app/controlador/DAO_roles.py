from app.bbdd.conexion import getConexion
import mysql.connector

# Lista de roles validos
ROLES_VALIDOS = ["admin", "gerente", "empleado"]


def obtenerRol(nombre_usuario):
    """Devuelve el rol actual del usuario."""
    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("""
            SELECT rol FROM usuario
            WHERE nombre_usuario = %s
        """, (nombre_usuario,))
        
        data = cursor.fetchone()
        cone.close()

        return data[0] if data else None

    except mysql.connector.Error as ex:
        print("Error obteniendo rol:", ex)
        return None


def cambiarRol(nombre_usuario, nuevo_rol):
    """Cambia el rol del usuario. Solo roles validos."""
    if nuevo_rol not in ROLES_VALIDOS:
        print("ROL NO VALIDO")
        return False

    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("""
            UPDATE usuario
            SET rol = %s
            WHERE nombre_usuario = %s
        """, (nuevo_rol, nombre_usuario))

        cone.commit()
        cone.close()
        print("Rol actualizado correctamente.")
        return True

    except mysql.connector.Error as ex:
        print("Error cambiando rol:", ex)
        return False


def listarRolesValidos():
    return ROLES_VALIDOS
