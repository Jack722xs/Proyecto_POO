class Rol:

    def __init__(self, nombre):
        self._nombre = nombre  # admin, gerente, empleado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, v):
        self._nombre = v

    def __str__(self):
        return f"Rol: {self._nombre}"
