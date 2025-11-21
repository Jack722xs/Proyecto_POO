from app.modelo.usuario import Usuario

class empleado(Usuario):
    """
    Un empleado ES un usuario (hereda de usuario)
    ademas tiene datos laborales propios.
    """

    def __init__(self,
                 id_empleado,
                 nombre,
                 apellido,
                 direccion,
                 email,
                 salario,
                 telefono=None,
                 es_gerente=False,
                 nombre_usuario=None,
                 contraseña=None):
        """
        Nota importante:
        - Para mantener compatibilidad con tu codigo actual,
          los primeros 7 parametros son los mismos que antes.
        - nombre_usuario y contraseña son opcionales.
        - Si no se pasan, se generan a partir de otros datos.
        """

        # Si no nos dan nombre de usuario/contraseña, generamos algo razonable
        if nombre_usuario is None:
            nombre_usuario = nombre  # por defecto, el nombre
        if contraseña is None:
            contraseña = ""  # podrias cambiar esto luego

        # Inicializamos la parte de usuario (herencia)
        super().__init__(contraseña, email, nombre_usuario)

        # Atributos propios de empleado (encapsulados con _)
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._salario = salario
        self._telefono = telefono
        self._es_gerente = es_gerente  # BOOLEAN
        self._id_depart = None         # se puede asignar luego a un departamento

    # Getters compatibles con tu DAO/vistas actuales
    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_direccion(self):
        return self._direccion

    def get_email(self):
        # usamos el atributo heredado de usuario
        return self._email

    def get_salario(self):
        return self._salario

    def get_telefono(self):
        return self._telefono

    def get_es_gerente(self):
        return self._es_gerente

    def set_es_gerente(self, es_gerente: bool):
        self._es_gerente = bool(es_gerente)

    def get_id_depart(self):
        return self._id_depart

    def set_id_depart(self, id_depart):
        self._id_depart = id_depart

    # Polimorfismo: sobreescribimos describir() del usuario
    def describir(self):
        rol = "Gerente" if self._es_gerente else "Empleado"
        return f"{rol} {self._nombre} {self._apellido} - Email: {self._email}"

    def __str__(self):
        return (f"id empleado: {self._id_empleado} - Nombre: {self._nombre} - Apellido: {self._apellido} - "
                f"Direccion: {self._direccion} - Email: {self._email} - "
                f"Salario: {self._salario} - Telefono: {self._telefono} - "
                f"Gerente: {self._es_gerente}")
