import mysql.connector

def getConexion():
    try:
        cone = mysql.connector.connect(
            host="localhost",
            #port=54000,
            user="root",
            password="",
            database="ecotech"
        )
        return cone
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")


