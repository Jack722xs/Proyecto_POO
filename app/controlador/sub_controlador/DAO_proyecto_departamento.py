from app.bbdd.conexion import getConexion
import mysql.connector


# ASIGNAR PROYECTO A DEPARTAMENTO
def asignarProyectoADepartamento(id_proyecto, id_depart):
    try:
        sql = "UPDATE proyecto SET id_depart=%s WHERE id_proyecto=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart, id_proyecto))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error asignando proyecto a departamento: {ex}")
        return False


# QUITAR PROYECTO DE DEPARTAMENTO
def quitarProyectoDeDepartamento(id_proyecto):
    try:
        sql = "UPDATE proyecto SET id_depart=NULL WHERE id_proyecto=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_proyecto,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error quitando proyecto de departamento: {ex}")
        return False


# VER PROYECTOS DE UN DEPARTAMENTO
def verProyectosDeDepartamento(id_depart):
    try:
        sql = "SELECT * FROM proyecto WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart,))
        datos = cursor.fetchall()
        cursor.close()
        cone.close()
        return datos
    except mysql.connector.Error as ex:
        print(f"Error al listar proyectos de departamento: {ex}")
        return []
