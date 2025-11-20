import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from app.modelo.informe import Informe
from app.controlador.generador_pdf import generador_informe
from app.controlador.DAO_empleado import verEmpleado
from app.controlador.DAO_departamento import verDepartamento
from app.controlador.DAO_proyecto import verProyectos


def convertir_a_diccionarios(datos, tipo):
    """Convierte tuplas de BD a diccionarios"""
    if not datos:
        return None
    
    resultado = []
    
    if tipo == "empleados":
        for row in datos:
            resultado.append({
                'id_empleado': row[0],
                'nombre': row[1],
                'apellido': row[2],
                'email': row[4],
                'salario': row[5]
            })
    
    elif tipo == "departamentos":
        for row in datos:
            resultado.append({
                'id_depart': row[0],
                'nombre_depart': row[2],
                'gerente_asociado': row[3],
                'proposito_depart': row[1]
            })
    
    elif tipo == "proyectos":
        for row in datos:
            resultado.append({
                'id_proyecto': row[0],
                'nombre': row[1],
                'descripcion': row[2],
                'fecha_inicio': row[3],
                'fecha_fin': row[4],
                'estado_proyecto': row[5]
            })
    
    return resultado if resultado else None


def menu_informes():
    """Menú interactivo - Generador de Informes PDF con datos de BD"""
    while True:
        print("=================================================================")
        print("GENERADOR DE INFORMES - ECOTECH")
        print("=================================================================")
        print("1. Informe de Empleados")
        print("2. Informe de Departamentos")
        print("3. Informe de Proyectos")
        print("4. Informe Completo")
        print("=================================================================")
        print("5. Volver")
        print("=================================================================")
        
        opcion = input("Selecciona opción: ").strip()
        
        if opcion == "1":
            try:
                datos_bd = verEmpleado()
                empleados = convertir_a_diccionarios(datos_bd, "empleados")
                
                if empleados:
                    generador_informe(empleados, None, None, "empleados")
                else:
                    print("No hay empleados registrados.")
            except Exception as e:
                print(f"Error: {str(e)}")
            
        elif opcion == "2":
            try:
                datos_bd = verDepartamento()
                departamentos = convertir_a_diccionarios(datos_bd, "departamentos")
                
                if departamentos:
                    generador_informe(None, departamentos, None, "departamentos")
                else:
                    print("No hay departamentos registrados.")
            except Exception as e:
                print(f"Error: {str(e)}")
            
        elif opcion == "3":
            try:
                datos_bd = verProyectos()
                proyectos = convertir_a_diccionarios(datos_bd, "proyectos")
                
                if proyectos:
                    generador_informe(None, None, proyectos, "proyectos")
                else:
                    print("No hay proyectos registrados.")
            except Exception as e:
                print(f"Error: {str(e)}")
            
        elif opcion == "4":
            try:
                datos_emp = verEmpleado()
                datos_dep = verDepartamento()
                datos_proy = verProyectos()
                
                empleados = convertir_a_diccionarios(datos_emp, "empleados")
                departamentos = convertir_a_diccionarios(datos_dep, "departamentos")
                proyectos = convertir_a_diccionarios(datos_proy, "proyectos")
                
                if empleados or departamentos or proyectos:
                    generador_informe(empleados, departamentos, proyectos, "completo")
                else:
                    print("No hay datos registrados.")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_informes()
