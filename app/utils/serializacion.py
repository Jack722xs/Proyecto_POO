import json

def exportar_datos_a_json(datos, nombre_archivo):
    if not nombre_archivo.endswith('.json'):
        nombre_archivo += '.json'
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True, f"Archivo guardado: {nombre_archivo}"
    except Exception as e:
        return False, f"Error al guardar JSON: {e}"