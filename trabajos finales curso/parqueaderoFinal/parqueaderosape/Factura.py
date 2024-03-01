class Factura:
    def __init__(self,idFactura,tiempoEstadia,fechaFactura,subtotal,descuento,valor,tipo_contrato):
        self.id = idFactura
        self.tiempoEstadia = tiempoEstadia
        self.fechaFactura = fechaFactura
        self.subtotal = subtotal
        self.valor=valor
        self.descuento = descuento
        self.tipo_contrato = tipo_contrato
        
    def MostrarFactura(self,usuario,vehiculo):
        if self.tipo_contrato==1:
            tiempo = f'{self.tiempoEstadia}h'
        elif self.tipo_contrato ==2:
            tiempo = f'{self.tiempoEstadia} Dias'
        else:
            if self.tiempoEstadia ==1:
                tiempo = f'{self.tiempoEstadia} Mes'
            else:
                tiempo = f'{self.tiempoEstadia} Meses'

        print('       PARQUEADERO EL SAPITO        ')
        print('....................................')
        print(f'Factura No. {self.id}')
        print(f'Fecha: {self.fechaFactura}')
        print('....................................')
        print(f'Tipo de plaza: {vehiculo.tipoVehiculo}')
        print(f'Placa: {vehiculo.placa}')
        print(f'Propietario: {usuario.nombre} {usuario.apellido}')
        print(f'Documento: {usuario.documento}')
        print(f'Tiempo: {tiempo}')
        print('....................................')
        print(f'Subtotal: ${self.subtotal}')
        print(f'Descuento: ${self.descuento}')
        print('....................................')
        print(f'Valor total: ${self.valor}')
        
        