import json
import requests
import datetime
from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion # Para saber quién hace la consulta

# Diccionario para mapear nombres de la guía a los códigos de la API
TIPOS_INDICADORES = {
    "1": "uf",
    "2": "ivp",
    "3": "ipc",
    "4": "utm",
    "5": "dolar",
    "6": "euro"
}

def obtener_indicador(opcion, fecha_consulta=None):
    """
    Consume la API de mindicador.cl
    Si fecha_consulta es None, trae el valor del día.
    Formato fecha: 'dd-mm-yyyy'
    """
    codigo_indicador = TIPOS_INDICADORES.get(opcion)
    if not codigo_indicador:
        return None, "Opción inválida"

    url = f"https://mindicador.cl/api/{codigo_indicador}"
    
    # Si hay fecha específica, la agregamos a la URL
    if fecha_consulta:
        url += f"/{fecha_consulta}"

    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            return None, f"Error al conectar con la API (Código {response.status_code})"

        # USO DE IMPORT JSON (Requerimiento 3.1.3)
        data = json.loads(response.text)

        # Procesamos la respuesta para obtener el valor
        # La estructura de la API cambia un poco si es por fecha o actual
        if fecha_consulta:
            # Cuando pides por fecha, 'serie' es una lista
            if len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha'][:10] # Tomamos solo YYYY-MM-DD
            else:
                return None, "No hay datos para esa fecha."
        else:
            # Valor actual (a veces mindicador devuelve series, tomamos el primero)
            if 'serie' in data and len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha'][:10]
            else:
                return None, "Datos no disponibles por el momento."

        # Retornamos un diccionario limpio
        resultado = {
            "indicador": data['nombre'],
            "valor": valor,
            "fecha_valor": fecha_valor,
            "origen": "mindicador.cl"
        }
        return resultado, "OK"

    except Exception as e:
        return None, f"Excepción capturada: {e}"

def guardar_consulta_indicador(datos):
    """
    Registra la consulta en la BBDD (Requerimiento 3.1.4)
    """
    try:
        cone = getConexion()
        cursor = cone.cursor()
        
        sql = """
            INSERT INTO registro_indicadores 
            (nombre_indicador, valor, fecha_valor, fecha_consulta, usuario_consulta, origen_datos)
            VALUES (%s, %s, %s, NOW(), %s, %s)
        """
        
        usuario_actual = sesion.usuario_actual if sesion.usuario_actual else "Anónimo"
        
        cursor.execute(sql, (
            datos['indicador'],
            datos['valor'],
            datos['fecha_valor'],
            usuario_actual,
            datos['origen']
        ))
        
        cone.commit()
        cursor.close()
        cone.close()
        return True
        
    except Exception as ex:
        print(f"Error guardando en BD: {ex}")
        return False