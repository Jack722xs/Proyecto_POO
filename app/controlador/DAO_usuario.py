from app.bbdd.conexion import getConexion
from app.modelo.usuario import Usuario
import mysql.connector


# ==============================
#   AGREGAR USUARIO
# ==============================
def agregarUsuario(user: Usuario):
    try:
        sql = """
            INSERT INTO usuario (contraseña, email, nombre_usuario, password_hash, rol, id_empleado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cone = getConexion()
        cursor = cone.cursor()

        cursor.execute(sql, (
            user.get_contraseña(),
            user.get_email(),
            user.get_nombre_usuario(),
            user.get_password_hash(),
            user.get_rol(),
            user.get_id_empleado()
        ))

        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        print("Error agregando usuario:", ex)
        return False



# ==============================
#   VER TODOS LOS USUARIOS
# ==============================
def verUsuario():
    try:
        sql = "SELECT contraseña, email, nombre_usuario, password_hash, rol, id_empleado FROM usuario"

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        cone.close()

        return data

    except mysql.connector.Error as ex:
        print("Error:", ex)
        return []


# ==============================
#   EDITAR USUARIO
# ==============================
def editarUsuario(user: Usuario):
    try:
        sql = """
            UPDATE usuario
            SET contraseña=%s,
                email=%s,
                password_hash=%s,
                rol=%s
            WHERE nombre_usuario=%s
        """

        cone = getConexion()
        cursor = cone.cursor()

        cursor.execute(sql, (
            user.get_contraseña(),
            user.get_email(),
            user.get_password_hash(),
            user.get_rol(),
            user.get_nombre_usuario()
        ))

        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        print("Error actualizando usuario:", ex)
        return False



# ==============================
#   ELIMINAR USUARIO
# ==============================
def eliminarUsuario(nombre_usuario):
    try:
        sql = "DELETE FROM usuario WHERE nombre_usuario=%s"

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (nombre_usuario,))
        cone.commit()

        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        print("Error eliminando usuario:", ex)
        return False



# ==============================
#   BUSCAR USUARIO POR EMPLEADO
# ==============================
def verUsuarioPorEmpleado(id_empleado):
    try:
        cone = getConexion()
        cursor = cone.cursor()

        sql = """
            SELECT nombre_usuario, email, rol, id_empleado
            FROM usuario
            WHERE id_empleado = %s
        """

        cursor.execute(sql, (id_empleado,))
        data = cursor.fetchone()

        cursor.close()
        cone.close()
        return data

    except mysql.connector.Error as ex:
        print("Error buscando usuario por empleado:", ex)
        return None
