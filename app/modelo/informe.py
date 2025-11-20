from datetime import datetime

class Informe:
    """Modelo simple para representar un informe"""
    
    def __init__(self, titulo, tipo_informe):
        self.titulo = titulo
        self.tipo_informe = tipo_informe
        self.fecha_generacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.datos = {}
    
    def agregar_empleados(self, empleados):
        self.datos['empleados'] = empleados
    
    def agregar_departamentos(self, departamentos):
        self.datos['departamentos'] = departamentos
    
    def agregar_proyectos(self, proyectos):
        self.datos['proyectos'] = proyectos
    
    def get_titulo(self):
        return self.titulo
    
    def get_tipo(self):
        return self.tipo_informe
    
    def get_datos(self):
        return self.datos
    
    def get_fecha(self):
        return self.fecha_generacion
