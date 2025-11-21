class RegistroTiempo:

    def __init__(self, id_registro=None, id_empleado=None, id_proyecto=None,
                 fecha=None, horas=0.0, descripcion=""):
        
        self._id_registro = id_registro
        self._id_empleado = id_empleado
        self._id_proyecto = id_proyecto
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion

   
    def get_id_registro(self):
        return self._id_registro

    def get_id_empleado(self):
        return self._id_empleado

    def get_id_proyecto(self):
        return self._id_proyecto

    def get_fecha(self):
        return self._fecha

    def get_horas(self):
        return self._horas

    def get_descripcion(self):
        return self._descripcion

    
    def set_id_registro(self, v):
        self._id_registro = v

    def set_id_empleado(self, v):
        self._id_empleado = v

    def set_id_proyecto(self, v):
        self._id_proyecto = v

    def set_fecha(self, v):
        self._fecha = v

    def set_horas(self, v):
        self._horas = v

    def set_descripcion(self, v):
        self._descripcion = v

    def __str__(self):
        return (f"Registro #{self._id_registro} | Empleado: {self._id_empleado} | "
                f"Proyecto: {self._id_proyecto} | Fecha: {self._fecha} | "
                f"Horas: {self._horas} | Descripcion: {self._descripcion}")
