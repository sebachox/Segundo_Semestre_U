class Plaza:
    def __init__(self,codigo,tipo,valorHora,valorDia,valorMes):
        #Tipo 1: Moto, Tipo 2: Carro, Tipo 3: Vehículo pesado
        self.codigo=codigo
        self.tipo= tipo
        self.valorHora=valorHora
        self.valorDia = valorDia
        self.valorMes = valorMes
        self.estado=True
        self.placa_asociada=None
        