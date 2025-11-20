class usuario:

    def __init__(self, contraseña, email, nombre_usuario):
        # Encapsulamos con un guion bajo
        self._contraseña = contraseña
        self._email = email
        self._nombre_usuario = nombre_usuario

    # Getters (puedes dejarlos asi o luego convertirlos en @property)
    def get_contraseña(self):
        return self._contraseña

    def get_email(self):
        return self._email

    def get_nombre_usuario(self):
        return self._nombre_usuario

    # Polimorfismo: método común que puede sobreescribirse
    def describir(self):
        return f"Usuario: {self._nombre_usuario} - Email: {self._email}"

    def __str__(self):
        return (f"Nombre de usuario: {self._nombre_usuario} - "
                f"Email: {self._email} - Contraseña: {self._contraseña}")
