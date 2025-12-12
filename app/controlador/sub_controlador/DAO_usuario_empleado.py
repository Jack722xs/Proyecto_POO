from app.bbdd.conexion import getConexion
import mysql.connector


def asignarUsuarioAEmpleado(nombre_usuario, id_empleado):
    try:
        cone = getConexion()
        cursor = cone.cursor()


        cursor.execute("SELECT rol FROM usuario WHERE nombre_usuario=%s", (nombre_usuario,))
        row = cursor.fetchone()

        if not row:
            print("El usuario no existe.")
            return False

        rol_usuario = row[0].lower()


        cursor.execute("""
            UPDATE usuario 
            SET id_empleado = %s
            WHERE nombre_usuario = %s
        """, (id_empleado, nombre_usuario))

 
        es_gerente = (rol_usuario == "gerente")

        cursor.execute("""
            UPDATE empleado
            SET es_gerente = %s
            WHERE id_empleado = %s
        """, (es_gerente, id_empleado))

        cone.commit()
        cursor.close()
        cone.close()

        print("Usuario asignado y empleado sincronizado correctamente.")
        return True

    except mysql.connector.Error as ex:
        print(f"Error asignando usuario a empleado: {ex}")
        return False


def quitarUsuarioDeEmpleado(nombre_usuario):
    try:
        cone = getConexion()
        cursor = cone.cursor()

        cursor.execute("SELECT id_empleado FROM usuario WHERE nombre_usuario=%s", (nombre_usuario,))
        row = cursor.fetchone()

        if row and row[0] is not None:
            id_empleado = row[0]

            cursor.execute("""
                UPDATE empleado
                SET es_gerente = False
                WHERE id_empleado = %s
            """, (id_empleado,))

        cursor.execute("""
            UPDATE usuario 
            SET id_empleado = NULL
            WHERE nombre_usuario = %s
        """, (nombre_usuario,))

        cone.commit()
        cursor.close()
        cone.close()

        print("Usuario desvinculado del empleado y rol limpiado.")
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
