import datetime
class Contrato:
    def __init__(self, cliente, dias, valor, numero_contrato, vehiculo):
        self.numero_contrato = f"CN{numero_contrato}"
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.valor = valor
        self.dias = dias
        self.fecha_inicio = datetime.datetime.now()
        self.fecha_finalizacion = self.fecha_inicio+datetime.timedelta(days=self.dias)
    def __str__(self):
        return f" Contrato número {self.numero_contrato} \n Placa vehículo: {self.vehiculo.placa} \n Dias de servicio: {self.dias} \n Espacio asignado: {self.vehiculo.espacio} \n Valor contrato: {self.valor} \n Fecha y hora de inicio: {self.fecha_inicio} \n Fecha y hora de finalización: {self.fecha_finalizacion} \n Estado: {'activo' if datetime.datetime.now() < self.fecha_finalizacion else 'vencido'} \n Cliente \n{self.cliente}"