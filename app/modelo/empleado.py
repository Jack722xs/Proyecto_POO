from app.modelo.usuario import Usuario

class empleado(Usuario):
    """
    Un empleado ES un usuario (hereda de usuario)
    ademas tiene datos laborales propios.
    """
    def __init__(self,id_empleado,nombre,apellido,direccion,email,salario,telefono=None,
                 es_gerente=False,nombre_usuario=None,contraseña=None):
 
        if nombre_usuario is None:
            nombre_usuario = nombre 
        
        super().__init__(nombre_usuario=nombre_usuario, email=email, password_hash=contraseña, id_empleado=id_empleado)

        self._id_empleado = id_empleado
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._salario = salario
        self._telefono = telefono
        self._es_gerente = es_gerente 
        self._id_depart = None  


    def get_id_empleado(self): 
        return self._id_empleado
    def get_nombre(self): 
        return self._nombre
    def get_apellido(self): 
        return self._apellido
    def get_direccion(self): 
        return self._direccion
    def get_salario(self): 
        return self._salario
    def get_telefono(self): 
        return self._telefono
    def get_es_gerente(self): 
        return self._es_gerente
    def get_id_depart(self): 
        return self._id_depart

    def set_es_gerente(self, es_gerente: bool):
        self._es_gerente = bool(es_gerente)

    def set_id_depart(self, id_depart):
        self._id_depart = id_depart

    def describir(self):
        rol = "Gerente" if self._es_gerente else "Empleado"
        return f"{rol} {self._nombre} {self._apellido} - Email: {self.get_email()}"

    def __str__(self):
        return (f"id empleado: {self._id_empleado} - Nombre: {self._nombre} - Apellido: {self._apellido} - "
                f"Direccion: {self._direccion} - Email: {self.get_email()} - "
                f"Salario: {self._salario} - Telefono: {self._telefono} - "
                f"Gerente: {self._es_gerente}")