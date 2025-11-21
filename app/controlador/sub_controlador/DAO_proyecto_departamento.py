from app.bbdd.conexion import getConexion
import mysql.connector


def asignarProyectoADepartamento(id_proyecto, id_depart):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        
        sql = "INSERT INTO proyecto_departamento (id_proyecto, id_depart) VALUES (%s, %s)"
        cursor.execute(sql, (id_proyecto, id_depart))
        
        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as ex:

        if ex.errno == 1062:
            print("⚠ Aviso: Este proyecto YA estaba asignado a ese departamento.")
            return False 

        
        print(f"Error asignando proyecto a departamento: {ex}")
        return False


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



def verProyectosDeDepartamento(id_depart):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        

        sql = """
            SELECT p.* FROM proyecto p
            INNER JOIN proyecto_departamento pd ON p.id_proyecto = pd.id_proyecto
            WHERE pd.id_depart = %s
        """
        
        cursor.execute(sql, (id_depart,))
        datos = cursor.fetchall()
        
        cursor.close()
        cone.close()
        return datos
        
    except mysql.connector.Error as ex:
        print(f"Error al listar proyectos de departamento: {ex}")
        return []