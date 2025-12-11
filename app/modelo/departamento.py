class departamento:
    """
    Un departamento tiene:
    - empleados
    - proyectos
    - un gerente asociado (id_empleado o None)
    """

    def __init__(self, id_depart, proposito_depart, nombre_depart, gerente_asociado=None):
        self._id_depart = id_depart
        self._proposito_depart = proposito_depart
        self._nombre_depart = nombre_depart
        self._gerente_asociado = gerente_asociado  
        self._empleados = []  
        self._proyectos = [] 

    def get_id_depart(self):
        return self._id_depart

    def get_proposito_depart(self):
        return self._proposito_depart

    def get_nombre_depart(self):
        return self._nombre_depart

    def get_gerente_asociado(self):
        return self._gerente_asociado

    def agregar_empleado(self, id_empleado):
        if id_empleado not in self._empleados:
            self._empleados.append(id_empleado)

    def quitar_empleado(self, id_empleado):
        if id_empleado in self._empleados:
            self._empleados.remove(id_empleado)

    def get_empleados(self):
        return list(self._empleados)

    def agregar_proyecto(self, id_proyecto):
        if id_proyecto not in self._proyectos:
            self._proyectos.append(id_proyecto)

    def quitar_proyecto(self, id_proyecto):
        if id_proyecto in self._proyectos:
            self._proyectos.remove(id_proyecto)

    def get_proyectos(self):
        return list(self._proyectos)

    def __str__(self):
        return (f"id departamento: {self._id_depart} - Nombre: {self._nombre_depart} - "
                f"Proposito: {self._proposito_depart} - Gerente asociado (id_empleado): {self._gerente_asociado} - "
                f"Empleados: {self._empleados} - Proyectos: {self._proyectos}")
