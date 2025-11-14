from app.bbdd.conexion import getConexion
from app.modelo.departamento import departamento
from app.modelo.empleado import empleado
import mysql.connector


##=CRUD DEPARTAMENTO=========================================================================================================##

def agregarDepartamento(departamento:departamento):
    try:
        sql = """INSERT INTO departamento (id_depart, proposito_depart, nombre_depart, gerente_asociado)
                 VALUES (%s, %s, %s, %s)"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql,(
            departamento.get_id_depart(),
            departamento.get_proposito_depart(),
            departamento.get_nombre_depart(),
            departamento.get_gerente_asociado()
        ))
        cone.commit()
        cursor.close()
        cone.close()

        return True
    
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
    
        return False
##_________________________________________________________## 
#    
def verDepartamento():
    try:
        sql = "SELECT * FROM departamento"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        cone.close()
        return filas
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")

##_________________________________________________________##    
##_________________________________________________________## 

def editarDepartamento(departamento:departamento):
    try:
        sql = "UPDATE departamento SET proposito_depart=%s, nombre_depart=%s, gerente_asociado=%s WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (departamento.get_proposito_depart(),
                             departamento.get_nombre_depart(),
                             departamento.get_gerente_asociado(),
                             departamento.get_id_depart()))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error:{ex}")

##_________________________________________________________## 

def eliminarDepartamento(id_depart: str):
    try:
        sql = "DELETE FROM departamento WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
##_________________________________________________________## 

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

        cursor.execute(sql, (emp.get_nombre(),
                             emp.get_apellido(),
                             emp.get_direccion(),
                             emp.get_email(),
                             emp.get_salario(),
                             emp.get_telefono(),
                             emp.get_id_empleado()
        ))

        cone.commit()
        cursor.close()
        cone.close()

        return True

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
        cursor.close()
        cone.close()

        return True

    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
    
def verEmpleado():
    try:
        sql = "SELECT * FROM empleado"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall() #este codigo es para recuperar todas las filas
        cursor.close()
        cone.close()
        return filas
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
