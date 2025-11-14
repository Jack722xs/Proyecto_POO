from app.bbdd.conexion import getConexion
from app.modelo.proyecto import proyecto 
import mysql.connector


##=CRUD DEPARTAMENTO=========================================================================================================##

def agregarProyecto(proy:proyecto):
    try:
        sql = """INSERT INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado_proyecto)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            proy.get_id_proyecto(),
            proy.get_nombre(),
            proy.get_descripcion(),
            proy.get_fecha_inicio(),
            proy.get_fecha_fin(),
            proy.get_estado_proyecto()
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
    
def verProyectos():
    try:
        sql = "SELECT * FROM proyecto"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return []

##_________________________________________________________## 
##_________________________________________________________##  
    
def verProyecto():
    try:
        sql = "SELECT * FROM proyecto WHERE id_proyecto=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return []

##_________________________________________________________##      
##_________________________________________________________## 

def editarProyecto(proy:proyecto):
    try:
        sql = """UPDATE proyecto 
                 SET nombre=%s, descripcion=%s, fecha_inicio=%s, fecha_fin=%s, estado_proyecto=%s
                 WHERE id_proyecto=%s"""

        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            proy.get_nombre(),
            proy.get_descripcion(),
            proy.get_fecha_inicio(),
            proy.get_fecha_fin(),
            proy.get_estado_proyecto(),
            proy.get_id_proyecto()
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

def eliminarProyecto(id_proyecto: str):
    try:
        sql = "DELETE FROM proyecto WHERE id_proyecto=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_proyecto,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
##_________________________________________________________## 

