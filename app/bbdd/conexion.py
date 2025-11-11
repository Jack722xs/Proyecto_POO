import mysql.connector

def getConexion():
    try:
        cone = mysql.connector.connect(
            host="",
            user="",
            pasword="",
            database=""
        )
        return cone
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
