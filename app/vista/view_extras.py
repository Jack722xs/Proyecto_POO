from app.utils.api_helper import obtener_socios_externos_api
from app.utils.serializacion import exportar_datos_a_json
from app.controlador.DAO_empleado import verEmpleado
from app.controlador.DAO_proyecto import verProyectos
from app.utils.helper import *

def menu_extras():
    while True:
        saltar_pantalla()
        print("""
===================================
===================================
1. Consultar API Externa (Socios)
2. Exportar Empleados a JSON
3. Exportar Proyectos a JSON
4. Volver
===================================""")
        opc = input("Seleccione: ")

        if opc == "1":
            print("\n--- API 2: JSONPlaceholder ---")
            socios = obtener_socios_externos_api()
            if socios:
                for s in socios:
                    print(f"- {s['name']} | {s['email']} | {s['company']['name']}")
            else:
                print("No se pudo conectar a la API.")

        elif opc == "2":
            datos = verEmpleado()
            lista = []
            if datos:
                for fila in datos:
                    lista.append({
                        "id": fila[0], "nombre": fila[1], 
                        "apellido": fila[2], "email": fila[4]
                    })
                exito, msg = exportar_datos_a_json(lista, "empleados_backup")
                print(msg)
            else:
                print("No hay empleados para exportar.")

        elif opc == "3":
            datos = verProyectos()
            lista = []
            if datos:
                for fila in datos:
                    lista.append({
                        "id": fila[0], "nombre": fila[1], 
                        "estado": fila[5]
                    })
                exito, msg = exportar_datos_a_json(lista, "proyectos_backup")
                print(msg)
            else:
                print("No hay proyectos para exportar.")

        elif opc == "4":
            break
        input("Presiona enter para continuar")
