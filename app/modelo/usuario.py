class usuario:

    def __init__(self, contraseña, email, nombre_usuario):
        self.contraseña = contraseña
        self.email = email
        self.nombre_usuario = nombre_usuario

    def get_contraseña(self):
        return self.contraseña

    def get_email(self):
        return self.email

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def __str__(self):
        return (f"Nombre de usuario: {self.nombre_usuario} - Email: {self.email} - Contraseña: {self.contraseña}")
