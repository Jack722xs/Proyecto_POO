from app.bbdd.conexion import getConexion
from app.sesion.sesion import usuario_actual
from app.utils.api_helper import consultar_api_mindicador 

TIPOS_INDICADORES = {
    "1": "uf", "2": "ivp", "3": "ipc", "4": "utm", "5": "dolar", "6": "euro"
}

def obtener_indicador(opcion, fecha_consulta=None):
    codigo_indicador = TIPOS_INDICADORES.get(opcion)
    if not codigo_indicador:
        return None, "Opción inválida"
    
    data, mensaje = consultar_api_mindicador(codigo_indicador, fecha_consulta)
    
    if not data:
        return None, mensaje
    try:
        if fecha_consulta:
            if len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha'][:10]
            else:
                return None, "No hay datos para esa fecha."
        else:
            if 'serie' in data and len(data['serie']) > 0:
                valor = data['serie'][0]['valor']
                fecha_valor = data['serie'][0]['fecha'][:10]
            else:
                return None, "Datos no disponibles."

        resultado = {
            "indicador": data['nombre'],
            "valor": valor,
            "fecha_valor": fecha_valor,
            "origen": "mindicador.cl"
        }
        return resultado, "OK"

    except Exception as e:
        return None, f"Error procesando datos: {e}"

def guardar_consulta_indicador(datos):
    try:
        cone = getConexion()
        cursor = cone.cursor()
        sql = "INSERT INTO registro_indicadores (nombre_indicador, valor, fecha_valor, fecha_consulta, usuario_consulta, origen_datos) VALUES (%s, %s, %s, NOW(), %s, %s)"
        cursor.execute(sql, (datos['indicador'], datos['valor'], datos['fecha_valor'], usuario_actual if usuario_actual else "Anónimo", datos['origen']))
        cone.commit()
        cone.close()
        return True
    except Exception as ex:
        print(f"Error BD: {ex}")
        return False