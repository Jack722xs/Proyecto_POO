from app.bbdd.conexion import getConexion
import mysql.connector


def asignarEmpleadoADepartamento(id_empleado, id_depart):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        sql = "INSERT INTO empleado_departamento (id_empleado, id_depart) VALUES (%s, %s)"
        cursor.execute(sql, (id_empleado, id_depart))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
    
def quitarEmpleadoDeDepartamento(id_empleado):
    try:
        sql = "DELETE FROM empleado_departamento WHERE id_empleado=%s"
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


def verEmpleadosDeDepartamento(id_depart):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        
        sql = """
            SELECT e.* FROM empleado e
            INNER JOIN empleado_departamento ed ON e.id_empleado = ed.id_empleado
            WHERE ed.id_depart = %s
        """
        
        cursor.execute(sql, (id_depart,))
        datos = cursor.fetchall()
        
        cursor.close()
        cone.close()
        return datos

    except mysql.connector.Error as ex:
        print(f"Error al listar empleados del departamento: {ex}")
        return []