class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    def __str__(self):
        return f" Nombre: {self.nombre} \n Identificación: {self.identificacion}"