import requests
import json

# = MINDICADOR ==
def consultar_api_mindicador(codigo_indicador, fecha=None):
    url = f"https://mindicador.cl/api/{codigo_indicador}"
    if fecha:
        url += f"/{fecha}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None, f"Error API (Código {response.status_code})"
        
        return response.json(), "OK"
    except Exception as e:
        return None, f"Error de conexión: {e}"

#  JSONPLACEHOLDER 
def obtener_socios_externos_api():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception:
        return []