class Usuario:
 
    def __init__(self, nombre_usuario, email, password_hash, rol="empleado", id_empleado=None, contraseña=None):
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.password_hash = password_hash
        self.rol = rol
        self.id_empleado = id_empleado
        self.contraseña = contraseña 


    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_email(self):
        return self.email

    def get_password_hash(self):
        return self.password_hash

    def get_rol(self):
        return self.rol

    def get_id_empleado(self):
        return self.id_empleado

    def get_contraseña(self):
        """Retorna contraseña en texto plano (uso temporal solamente)"""
        return self.contraseña


    def set_email(self, email):
        self.email = email

    def set_password_hash(self, password_hash):
        self.password_hash = password_hash

    def set_rol(self, rol):
        self.rol = rol

    def set_id_empleado(self, id_empleado):
        self.id_empleado = id_empleado

    def set_contraseña(self, contraseña):
        """Actualiza contraseña en texto plano (uso temporal solamente)"""
        self.contraseña = contraseña

    def __str__(self):
        return (f"[Usuario: {self.nombre_usuario} | Rol: {self.rol} | "
                f"ID Empleado: {self.id_empleado}]")