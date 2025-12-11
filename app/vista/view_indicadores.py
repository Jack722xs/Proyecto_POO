from app.controlador.DAO_indicadores import obtener_indicador, guardar_consulta_indicador
from app.utils.helper import *

def menu_indicadores():
    while True:
        saltar_pantalla()
        print("""
============================================
      CONSULTA DE INDICADORES ECONÓMICOS
============================================
1. Unidad de Fomento (UF)                  =
2. Índice de Valor Promedio (IVP)          =
3. Índice de Precio al Consumidor (IPC)    =
4. Unidad Tributaria Mensual (UTM)         =
5. Dólar Observado                         =
6. Euro                                    =
============================================
7. Volver
""")
        
        opc = input("Seleccione indicador: ").strip()

        if opc == "7":
            break
        
        if opc not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Opción inválida.")
            input("Presiona Enter para continuar...")
            continue

        # --- LOGICA COMÚN PARA TODAS LAS OPCIONES (1-6) ---
        procesar_consulta(opc)


def procesar_consulta(opc):
    """Maneja el flujo de consulta de fecha, API y guardado."""
    
    # 1. Selección de Fecha
    fecha_str = None
    while True:
        saltar_pantalla()
        print("============================================")
        print("            SELECCIÓN DE FECHA              ")
        print("============================================")
        print("1. Valor de Hoy")
        print("2. Otra fecha histórica (dd-mm-yyyy)")
        print("============================================")
        print("3. Cancelar")
        
        tipo_fecha = input("\nSelección: ").strip()

        if tipo_fecha == "1":
            fecha_str = None # Hoy
            break
        elif tipo_fecha == "2":
            while True:
                fecha_input = input("Ingrese fecha (ej: 04-11-2023): ").strip()
                if fecha_input:
                    fecha_str = fecha_input
                    break
                print("Error: La fecha no puede estar vacía.")
            break
        elif tipo_fecha == "3":
            return # Volver al menú anterior
        else:
            print("Error: Opción no válida.")
            input("Presiona Enter para reintentar...")

    # 2. Consultar API
    saltar_pantalla()
    print("Consultando API externa, por favor espere...")
    
    datos, mensaje = obtener_indicador(opc, fecha_str)

    # 3. Mostrar Resultados
    saltar_pantalla()
    if datos:
        print("============================================")
        print("           RESULTADO DE LA CONSULTA         ")
        print("============================================")
        print(f" INDICADOR: {datos['indicador']}")
        print(f" VALOR:     ${datos['valor']}")
        print(f" FECHA:     {datos['fecha_valor']}")
        print(f" ORIGEN:    {datos['origen']}")
        print("============================================")

        # 4. Guardar en Historial
        while True:
            guardar = input("\n¿Guardar esta consulta en el historial? (s/n): ").strip().lower()
            
            if guardar == "s":
                if guardar_consulta_indicador(datos):
                    print("\n>> Consulta registrada en Base de Datos exitosamente.")
                else:
                    print("\n>> Error al guardar en BD.")
                break
            elif guardar == "n":
                print("\n>> No se guardó la consulta.")
                break
            else:
                print("Error: Ingrese 's' para sí o 'n' para no.")
    else:
        print("============================================")
        print("                 ERROR                      ")
        print("============================================")
        print(f"Detalle: {mensaje}")
    
    # Pausa final para leer antes de volver al menú principal
    print("-" * 44)
    input("Presiona Enter para continuar...")