from app.controlador.DAO_indicadores import obtener_indicador, guardar_consulta_indicador

def menu_indicadores():
    while True:
        print("""
============================================
      CONSULTA DE INDICADORES ECONÓMICOS
============================================
1. Unidad de Fomento (UF)
2. Índice de Valor Promedio (IVP)
3. Índice de Precio al Consumidor (IPC)
4. Unidad Tributaria Mensual (UTM)
5. Dólar Observado
6. Euro
============================================
7. Volver
""")
        opc = input("Seleccione indicador: ").strip()

        if opc == "7":
            break
        
        if opc not in ["1","2","3","4","5","6"]:
            print("Opción inválida.")
            continue

        print("\n¿Desea consultar el valor de hoy o una fecha histórica?")
        print("1. Hoy")
        print("2. Otra fecha (dd-mm-yyyy)")
        tipo_fecha = input("Selección: ").strip()

        fecha_str = None
        if tipo_fecha == "2":
            fecha_str = input("Ingrese fecha (ej: 04-11-2023): ").strip()

        print("Consultando API externa...")
        datos, mensaje = obtener_indicador(opc, fecha_str)

        if datos:
            print("\n" + "="*30)
            print(f" INDICADOR: {datos['indicador']}")
            print(f" VALOR:     ${datos['valor']}")
            print(f" FECHA:     {datos['fecha_valor']}")
            print(f" ORIGEN:    {datos['origen']}")
            print("="*30)

            # Opción de guardar en BD como pide la guía
            guardar = input("¿Guardar esta consulta en el historial? (s/n): ").lower()
            if guardar == "s":
                if guardar_consulta_indicador(datos):
                    print("Consulta registrada en Base de Datos exitosamente.")
                else:
                    print("Error al guardar en BD.")
        else:
            print(f"Error: {mensaje}")
        
        input("\nPresione ENTER para continuar...")