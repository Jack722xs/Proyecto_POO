from app.bbdd.conexion import getConexion
import mysql.connector


# ==============================
#   ASIGNAR USUARIO A EMPLEADO
# ==============================
def asignarUsuarioAEmpleado(nombre_usuario, id_empleado):
    try:
        cone = getConexion()
        cursor = cone.cursor()

        sql = """
            UPDATE usuario 
            SET id_empleado = %s
            WHERE nombre_usuario = %s
        """

        cursor.execute(sql, (id_empleado, nombre_usuario))
        cone.commit()

        cursor.close()
        cone.close()

        print("Usuario asignado al empleado correctamente.")
        return True

    except mysql.connector.Error as ex:
        print(f"Error asignando usuario a empleado: {ex}")
        return False


# ==============================
#   QUITAR ASOCIACION
# ==============================
def quitarUsuarioDeEmpleado(nombre_usuario):
    try:
        cone = getConexion()
        cursor = cone.cursor()

        sql = """
            UPDATE usuario 
            SET id_empleado = NULL
            WHERE nombre_usuario = %s
        """

        cursor.execute(sql, (nombre_usuario,))
        cone.commit()

        cursor.close()
        cone.close()

        print("Usuario desvinculado del empleado.")
        return True

    except mysql.connector.Error as ex:
        print(f"Error al desvincular: {ex}")
        return False


# ==============================
#   VER EMPLEADO ASOCIADO
# ==============================
def verEmpleadoDeUsuario(nombre_usuario):
    try:
        cone = getConexion()
        cursor = cone.cursor()

        sql = """
            SELECT u.nombre_usuario, e.id_empleado, e.nombre, e.apellido, e.email
            FROM usuario u
            LEFT JOIN empleado e 
            ON u.id_empleado = e.id_empleado
            WHERE u.nombre_usuario = %s
        """

        cursor.execute(sql, (nombre_usuario,))
        datos = cursor.fetchone()

        cursor.close()
        cone.close()

        return datos

    except mysql.connector.Error as ex:
        print(f"Error consultando datos: {ex}")
        return None
