from app.bbdd.conexion import getConexion
import mysql.connector


# ASIGNAR EMPLEADO A DEPARTAMENTO
def asignarEmpleadoADepartamento(id_empleado, id_depart):
    try:
        sql = "UPDATE empleado SET id_depart=%s WHERE id_empleado=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart, id_empleado))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error asignando empleado a departamento: {ex}")
        return False


# QUITAR EMPLEADO DE DEPARTAMENTO
def quitarEmpleadoDeDepartamento(id_empleado):
    try:
        sql = "UPDATE empleado SET id_depart=NULL WHERE id_empleado=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error quitando empleado de departamento: {ex}")
        return False


# LISTAR EMPLEADOS DE UN DEPARTAMENTO
def verEmpleadosDeDepartamento(id_depart):
    try:
        sql = "SELECT * FROM empleado WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart,))
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos
    except mysql.connector.Error as ex:
        print(f"Error al listar empleados del departamento: {ex}")
        return []
