class empleado:

    def __init__(self, id_empleado, nombre, apellido, direccion, email, salario, telefono=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.email = email
        self.salario = salario
        self.telefono = telefono

    def get_id_empleado(self):
        return self.id_empleado

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_direccion(self):
        return self.direccion

    def get_email(self):
        return self.email

    def get_salario(self):
        return self.salario

    def get_telefono(self):
        return self.telefono

    def __str__(self):
        return (f"id empleado: {self.id_empleado} - Nombre: {self.nombre} - Apellido: {self.apellido} - "
                f"Dirección: {self.direccion} - Email: {self.email} - Salario: {self.salario} - Teléfono: {self.telefono}")
