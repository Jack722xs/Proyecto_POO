import time
from app.vista.view import *
from app.modelo.departamento import departamento 

print("""MENU
      ¡Seleccione una de las opciones!
      1. Departamentos
      2. Usuarios
      3. Proyectos
      4. Salir""")

while True:
    try:
        opc = int(input("selecione una opcion: "))
    except ValueError:
        print("Error, intentelo de nuevo")
        continue

    if opc == 1:
      
        filas = verDepartamento()
        if filas:
            print("Departamentos existentes:")
            for fila in filas:
                print(f"ID: {fila[0]}, Proposito: {fila[1]}, Nombre: {fila[2]}, Gerente: {fila[3]}")
        else:
            print("No hay departamentos registrados.")
        
      
        while True:
            print("""
            Menu Departamentos:
            1. Agregar departamento
            2. Editar departamento
            3. Eliminar departamento
            4. Volver al menu principal
            """)
            try:
                sub_opc = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Error, intentelo de nuevo")
                continue

            if sub_opc == 1:
               
                id_depart = input("Ingrese el ID del departamento: ")
                proposito_depart = input("Ingrese el proposito del departamento: ")
                nombre_depart = input("Ingrese el nombre del departamento: ")
                gerente_asociado = input("Ingrese el gerente asociado: ")
                dep = departamento(id_depart, proposito_depart, nombre_depart, gerente_asociado)
                if agregarDepartamento(dep):
                    print("Departamento agregado exitosamente.")
                else:
                    print("Error al agregar el departamento.")
            elif sub_opc == 2:
            
                id_depart = input("Ingrese el ID del departamento que desea editar: ")
                proposito_depart = input("Ingrese el nuevo proposito del departamento: ")
                nombre_depart = input("Ingrese el nuevo nombre del departamento: ")
                gerente_asociado = input("Ingrese el nuevo gerente asociado: ")
                dep = departamento(id_depart, proposito_depart, nombre_depart, gerente_asociado)
                
                if editarDepartamento(dep):
                    print("Departamento editado exitosamente.")
                else:
                    print("Error al editar el departamento.")
            elif sub_opc == 3:
                
                nombre_depart = input("Ingrese el nombre del departamento que desea eliminar: ")
                if eliminarDepartamento(nombre_depart):
                    print("Departamento eliminado exitosamente.")
                else:
                    print("Error al eliminar el departamento.")
            elif sub_opc == 4:
                break  
            else:
                print("Opcion no valida, intentelo de nuevo.")
   # elif opc == 2:
       
        
    #elif opc == 3:
       
        
    #elif opc == 4:
        print("Saliendo del programa...")
        break
    #else:
        print("Opcion no valida, intentelo de nuevo.")
