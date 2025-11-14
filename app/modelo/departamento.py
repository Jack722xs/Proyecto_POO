class departamento:

    def __init__(self, id_depart, proposito_depart, nombre_depart, gerente_asociado):
        self.id_depart = id_depart
        self.proposito_depart = proposito_depart
        self.nombre_depart = nombre_depart
        self.gerente_asociado = gerente_asociado

    def get_id_depart(self):
        return self.id_depart

    def get_proposito_depart(self):
        return self.proposito_depart

    def get_nombre_depart(self):
        return self.nombre_depart

    def get_gerente_asociado(self):
        return self.gerente_asociado    

    def __str__(self):
        return f"id departamento: {self.id_depart} - Nombre: {self.nombre_depart} - Proposito:{self.proposito_depart} - Gerente asociado: {self.gerente_asociado}"