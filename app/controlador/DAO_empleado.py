from app.bbdd.conexion import getConexion
from app.modelo.empleado import empleado
import mysql.connector


##=CRUD Empleado=========================================================================================================##
 
               
def agregarEmpleado(emp:empleado):
    try:
        sql = """INSERT INTO empleado (id_empleado, nombre, apellido, direccion, email, salario, telefono)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (emp.get_id_empleado(),
                             emp.get_nombre(),
                             emp.get_apellido(),
                             emp.get_direccion(),
                             emp.get_email(),
                             emp.get_salario(),
                             emp.get_telefono()
        ))
        cone.commit()
        cursor.close()
        cone.close()
        
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
    
def editarEmpleado(emp: empleado):
    try:
        sql = """UPDATE empleado SET nombre=%s, apellido=%s, direccion=%s, email=%s, salario=%s, telefono=%s WHERE id_empleado=%s"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (emp.get_nombre(), emp.get_apellido(), emp.get_direccion(), emp.get_email(), emp.get_salario(), emp.get_telefono(), emp.get_id_empleado()))
        cone.commit()
        
        filas = cursor.rowcount # CORRECCIÓN
        cursor.close()
        cone.close()
        return filas > 0

    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False

def eliminarEmpleado(id_empleado: str):
    try:
        sql = "DELETE FROM empleado WHERE id_empleado=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado,))
        cone.commit()
        
        filas = cursor.rowcount # CORRECCIÓN
        cursor.close()
        cone.close()
        return filas > 0

    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
    
def verEmpleado():
    try:
        sql = "SELECT * FROM empleado"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall() 
        cursor.close()
        cone.close()
        return filas
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")

def verEmpleadoPorID(id_empleado):
    try:
        sql = "SELECT * FROM empleado WHERE id_empleado=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        cursor.close()
        cone.close()
        return fila
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return None
