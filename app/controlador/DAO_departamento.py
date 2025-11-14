from app.bbdd.conexion import getConexion
from app.modelo.departamento import departamento
import mysql.connector


##=CRUD DEPARTAMENTO=========================================================================================================##

def agregarDepartamento(departamento:departamento):
    try:
        sql = """INSERT INTO departamento (id_depart, proposito_depart, nombre_depart, gerente_asociado)
                 VALUES (%s, %s, %s, %s)"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql,(departamento.get_id_depart(),
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
##_________________________________________________________##  
    
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

