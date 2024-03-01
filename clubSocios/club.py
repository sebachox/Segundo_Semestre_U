from socio import Socio
from autorizado import PersonaAutorizado
from factura import Factura
class Club:

    def __init__(self):
          self.socios = []
          self.facturas = []
          self.numeroFacturaActual = 1
    
    def buscarSocio(self, cedula):

        for socio in self.socios:
            if socio.cedula == cedula:
                return True
        return False
    
    def afiliarSocio(self, cedula, nombre):

        if not self.buscarSocio(cedula):
            socio = Socio(nombre, cedula)
            self.socios.append(socio)
        else:
            print("el socio que intenta registrar ya se encuentra registrado ")

    def registrarAutorizado(self, cedulaSocio, nombreAutorizado):

        socioEncontrado = self.buscarSocio(cedulaSocio)
        if socioEncontrado:
            autorizado = PersonaAutorizado(nombreAutorizado)
            socioEncontrado.autorizados.append(autorizado)
        else:
            print("La cedula del socio no se encuentra registrada")
        
    def obtenerFacturaPendiente(self, socio):
        # Buscar y devolver la última factura pendiente del socio
        if socio.facturas_pendientes:
            return socio.facturas_pendientes[-1]
        return None

    def registrarConsumo(self, cedulaSocio, nombreConsumidor, concepto, valor):

        socioEncontrado = self.buscarSocio(cedulaSocio)
        if socioEncontrado:
            numeroFactura = self.numeroFacturaActual
            facturaExistente = self.obtenerFacturaPendiente(socioEncontrado)
            if facturaExistente:
                facturaExistente.agregarConsumo(concepto, valor)
            else:
                facturaNueva = Factura(nombreConsumidor)
                facturaNueva.agregarConsumo(concepto, valor)
                facturaNueva.asignarNumeroFactura(numeroFactura)
                socioEncontrado.facturasPendientes.append(facturaNueva)
                self.facturas.append(facturaNueva)
                self.numeroFacturaActual += 1
        else:
            print("la cedula del socio que se ingreso no se encuentra registrada ")

    def mostrarFacturasPendientesSocio(self, cedulaSocio):
        socio = self.buscarSocio(cedulaSocio)
        if socio:
            
        

    def pagarFactura(self, cedulaSocio, numeroFactura):
        pass
    