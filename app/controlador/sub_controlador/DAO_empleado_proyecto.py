from app.bbdd.conexion import getConexion
import mysql.connector


def asignarEmpleadoAProyecto(id_empleado, id_proyecto):
    try:
        sql = "INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES (%s, %s)"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado, id_proyecto))
        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        if ex.errno == 1062:
            print("El empleado ya estaba asignado a este proyecto.")
            return True
        print(f"Error asignando empleado a proyecto: {ex}")
        return False


def quitarEmpleadoDeProyecto(id_empleado, id_proyecto):
    try:
        sql = "DELETE FROM empleado_proyecto WHERE id_empleado=%s AND id_proyecto=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado, id_proyecto))
        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:
        print(f"Error quitando empleado de proyecto: {ex}")
        return False


def verEmpleadosDeProyecto(id_proyecto):
    try:
        sql = """SELECT empleado.* 
                 FROM empleado
                 INNER JOIN empleado_proyecto ON empleado.id_empleado = empleado_proyecto.id_empleado
                 WHERE empleado_proyecto.id_proyecto = %s"""

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_proyecto,))
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos

    except mysql.connector.Error as ex:
        print(f"Error listando empleados por proyecto: {ex}")
        return []


def verProyectosDeEmpleado(id_empleado):
    try:
        sql = """SELECT proyecto.* 
                 FROM proyecto
                 INNER JOIN empleado_proyecto ON proyecto.id_proyecto = empleado_proyecto.id_proyecto
                 WHERE empleado_proyecto.id_empleado = %s"""

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado,))
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos

    except mysql.connector.Error as ex:
        print(f"Error listando proyectos de empleado: {ex}")
        return []

