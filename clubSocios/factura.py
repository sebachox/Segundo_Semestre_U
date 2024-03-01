class Factura:

    def __init__(self, nombre):
        self.numeroFactura = None
        self.consumos = []
        self.nombre = nombre
    
    def agregarConsumo(self, concepto, valor):
        consumo = {'concepto': concepto, 'valor': valor}
        self.consumos.append(consumo)

    def asignarNumeroFactura(self, numero_factura):
        self.numero = numero_factura


