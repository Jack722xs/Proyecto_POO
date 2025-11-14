from app.bbdd.conexion import getConexion
from app.modelo.usuario import usuario
import mysql.connector

##=CRUD USUARIO=========================================================================================================##

def agregarUsuario(user: usuario):
    try:
        sql = """INSERT INTO usuario (contraseña, email, nombre_usuario)
                 VALUES (%s, %s, %s)"""
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            user.get_contraseña(),
            user.get_email(),
            user.get_nombre_usuario()
        ))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False

##_________________________________________________________##

def verUsuario():
    try:
        sql = "SELECT * FROM usuario"
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

def editarUsuario(user: usuario):
    try:
        sql = "UPDATE usuario SET contraseña=%s, email=%s WHERE nombre_usuario=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (
            user.get_contraseña(),
            user.get_email(),
            user.get_nombre_usuario()
        ))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False

##_________________________________________________________##

def eliminarUsuario(nombre_usuario: int):
    try:
        sql = "DELETE FROM usuario WHERE nombre_usuario=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (nombre_usuario,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
        return False
##_________________________________________________________##
