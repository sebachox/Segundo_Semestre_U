import datetime

class Vehiculo:
    def __init__(self, placa, espacio):
        self.placa = placa
        self.hora_fecha_entrada = datetime.datetime.now()
        self.espacio = espacio
    def __str__(self):
        return f"Placa: {self.placa} \nHora entrada {self.hora_fecha_entrada}"

class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
    pass