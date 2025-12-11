class proyecto:
    """
    Proyecto tiene:
    - Relacion con departamento (id_depart)
    - Relacion con empleados (lista de ids de empleados)
    """

    def __init__(self, id_proyecto, descripcion, estado_proyecto, fecha_fin, fecha_inicio, nombre, id_depart=None):
        self._id_proyecto = id_proyecto
        self._descripcion = descripcion
        self._estado_proyecto = estado_proyecto
        self._fecha_fin = fecha_fin
        self._fecha_inicio = fecha_inicio
        self._nombre = nombre
        self._id_depart = id_depart
        self._empleados = []    


    def get_descripcion(self):
        return self._descripcion

    def get_estado_proyecto(self):
        return self._estado_proyecto

    def get_fecha_fin(self):
        return self._fecha_fin

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_id_proyecto(self):
        return self._id_proyecto

    def get_nombre(self):
        return self._nombre

    def get_id_depart(self):
        return self._id_depart

    def set_id_depart(self, id_depart):
        self._id_depart = id_depart

    def agregar_empleado(self, id_empleado):
        if id_empleado not in self._empleados:
            self._empleados.append(id_empleado)

    def quitar_empleado(self, id_empleado):
        if id_empleado in self._empleados:
            self._empleados.remove(id_empleado)

    def get_empleados(self):
        return list(self._empleados)

    def __str__(self):
        return (f"id proyecto: {self._id_proyecto} - Nombre: {self._nombre} - Descripcion: {self._descripcion} - "
                f"Estado: {self._estado_proyecto} - Fecha inicio: {self._fecha_inicio} - Fecha fin: {self._fecha_fin} "
                f"- Departamento: {self._id_depart} - Empleados: {self._empleados}")
