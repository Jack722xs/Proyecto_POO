import mysql.connector

def getConexion():
    try:
        cone = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ecotech"
        )
        return cone
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
