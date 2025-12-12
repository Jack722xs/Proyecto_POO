from app.bbdd.conexion import getConexion
from app.modelo.departamento import departamento
import mysql.connector


## = CRUD DEPARTAMENTO =================================================================== ##

def agregarDepartamento(dep: departamento):
    try:
        sql = """INSERT INTO departamento (id_depart, proposito_depart, nombre_depart, gerente_asociado)
                 VALUES (%s, %s, %s, %s)"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            dep.get_id_depart(),
            dep.get_proposito_depart(),
            dep.get_nombre_depart(),
            dep.get_gerente_asociado() 
        ))
        cone.commit()
        cursor.close()
        cone.close()

        return True

    except mysql.connector.Error as ex:
        print(f"Error al agregar departamento: {ex}")
        return False


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
        print(f"Error al listar departamentos: {ex}")
        return []

def editarDepartamento(dep: departamento):
    try:
        sql = "UPDATE departamento SET proposito_depart=%s, nombre_depart=%s WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (dep.get_proposito_depart(), dep.get_nombre_depart(), dep.get_id_depart()))
        cone.commit()
        
        filas = cursor.rowcount 
        cursor.close()
        cone.close()
        return filas > 0
    except mysql.connector.Error as ex:
        print(f"Error al editar departamento: {ex}")
        return False

def eliminarDepartamento(id_depart: str):
    try:
        sql = "DELETE FROM departamento WHERE id_depart=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (id_depart,))
        cone.commit()
        
        filas = cursor.rowcount
        cursor.close()
        cone.close()
        return filas > 0
    except mysql.connector.Error as ex:
        print(f"Error al eliminar departamento: {ex}")
        return False

## = ASIGNAR GERENTE ===================================================================== ##

def asignarGerente(id_depart, id_empleado):
    """
    Guarda el id_empleado como gerente_asociado del departamento.
    """
    try:
        cone = getConexion()
        cursor = cone.cursor()

        sql = """
            UPDATE departamento
            SET gerente_asociado = %s
            WHERE id_depart = %s
        """

        cursor.execute(sql, (id_empleado, id_depart))
        cone.commit()

        cursor.close()
        cone.close()

        print("Gerente asignado correctamente al departamento.")
        return True

    except mysql.connector.Error as ex:
        print(f"Error asignando gerente: {ex}")
        return False
