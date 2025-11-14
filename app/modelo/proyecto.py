class proyecto:

    def __init__(self,id_proyecto, descripcion, estado_proyecto, fecha_fin, fecha_inicio, nombre):
        self.id_proyecto = id_proyecto
        self.descripcion = descripcion
        self.estado_proyecto = estado_proyecto
        self.fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.nombre = nombre

    def get_descripcion(self):
        return self.descripcion

    def get_estado_proyecto(self):
        return self.estado_proyecto

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_id_proyecto(self):
        return self.id_proyecto

    def get_nombre(self):
        return self.nombre
    
    def __str__(self):
        return (f"id proyecto: {self.id_proyecto} - Nombre: {self.nombre} - Descripción: {self.descripcion} - "
                f"Estado: {self.estado_proyecto} - Fecha inicio: {self.fecha_inicio} - Fecha fin: {self.fecha_fin}")
