class Usuario:
    def __init__(self, id_usuario, nombre, password_hash):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.password_hash = password_hash

    def get_id_usuario(self):
        return self.id_usuario

    def get_nombre(self):
        return self.nombre

    def get_password_hash(self):
        return self.password_hash

    def __str__(self):
        return f"Usuario: {self.id_usuario} - Nombre: {self.nombre}"
