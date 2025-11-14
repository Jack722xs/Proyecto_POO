from app.bbdd.conexion import getConexion
from app.modelo.departamento import departamento
import mysql.connector

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
##
#def editarDepartamento(departamento:departamento):
    #try:
        #sql = "UPDATE Departamento SET id_depart=%s, proposito_"



                

