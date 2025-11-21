from app.bbdd.conexion import getConexion
from app.modelo.registro_tiempo import RegistroTiempo
import mysql.connector

def agregarRegistro(rt: RegistroTiempo):
    try:
        sql = """INSERT INTO registro_tiempo 
        (id_empleado, id_proyecto, fecha, horas, descripcion)
        VALUES (%s, %s, %s, %s, %s)"""

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            rt.get_id_empleado(),
            rt.get_id_proyecto(),
            rt.get_fecha(),
            rt.get_horas(),
            rt.get_descripcion()
        ))
        cone.commit()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        print("Error al insertar registro:", ex)
        return False


def verRegistrosPorEmpleado(id_emp):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM registro_tiempo WHERE id_empleado=%s", (id_emp,))
        data = cursor.fetchall()
        cone.close()
        return data
    except Exception as e:
        print("Error:", e)


def verRegistrosPorProyecto(id_proj):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM registro_tiempo WHERE id_proyecto=%s", (id_proj,))
        data = cursor.fetchall()
        cone.close()
        return data
    except Exception as e:
        print("Error:", e)
