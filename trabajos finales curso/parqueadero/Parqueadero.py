import datetime
from Vehiculo import *
import os
from Cliente import *
from Contrato import *

class Parqueadero:
    def __init__(self, tarifa_motos, tarifa_carros, espacios_libres_motos, espacios_libres_carros, tarifa_pernoctacion):
        self.vehiculos = []
        self.contratos = []
        self.tarifa_motos = tarifa_motos
        self.tarifa_carros = tarifa_carros
        self.tarifa_pernoctacion = tarifa_pernoctacion
        self.espacios_libres_motos = espacios_libres_motos
        self.espacios_libres_carros = espacios_libres_carros
        self.espacios_ocupados_motos = []
        self.espacios_ocupados_carros = []
        self.cantidad_vehiculos = 0
        self.cantidad_contratos = 0
        self.dinero_en_caja = 0
    
    def consultar_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None
    
    def consultar_contrato(self, numero_contrato):
        for contrato in self.contratos:
            if contrato.numero_contrato == numero_contrato:
                return contrato
        return None
        
    def ingresar_vehiculo(self, vehiculo):
        if vehiculo not in self.vehiculos:
            self.vehiculos.append(vehiculo)
            if isinstance(vehiculo, Moto):
                self.espacios_libres_motos.remove(vehiculo.espacio)
                self.espacios_ocupados_motos.append(vehiculo.espacio)
            else:
                self.espacios_libres_carros.remove(vehiculo.espacio)
                self.espacios_ocupados_carros.append(vehiculo.espacio)
            self.cantidad_vehiculos+=1
        else:
            print("El vehículo ya está en el parqueadero.")
    
    def salida_vehiculo(self, vehiculo):
        hora_fecha_salida = datetime.datetime.now()
        diferencia = hora_fecha_salida - vehiculo.hora_fecha_entrada
        if diferencia.days > 0 or hora_fecha_salida.day > vehiculo.hora_fecha_entrada.day:
            print("Su vehículo ha pernoctado en nuestro parqueadero, por lo tanto deberá pagar la tarifa de pernoctación")
            valor_pago = self.tarifa_pernoctacion * diferencia.days if diferencia.days > 0 else self.tarifa_pernoctacion
        else:
            if isinstance(vehiculo, Moto):
                valor_pago = self.tarifa_motos
                self.espacios_libres_motos.append(vehiculo.espacio)
                self.espacios_ocupados_motos.remove(vehiculo.espacio)
            else:
                valor_pago = self.tarifa_carros
                self.espacios_libres_carros.append(vehiculo.espacio)
                self.espacios_ocupados_carros.remove(vehiculo.espacio)
            self.cantidad_vehiculos-=1
        print("+====================================+")
        print("|          Salida vehículo           |")
        print("+====================================+")
        print(f"| Placa: {vehiculo.placa}")
        print(f"| Total a pagar: {valor_pago}")
        print("+------------------------------------+")
        os.system("pause")
        print("+====================================+")
        print("|           Salida exitosa           |")
        print("+====================================+")
        print(f"| Placa: {vehiculo.placa}")
        print(f"| Valor pagado: {valor_pago}")
        print(f"| Hora fecha ingreso: {vehiculo.hora_fecha_entrada}")
        print(f"| Hora fecha salida: {hora_fecha_salida}")
        print(f"| Tiempo en el parqueadero: {hora_fecha_salida-vehiculo.hora_fecha_entrada}")
        print("+------------------------------------+")
        self.dinero_en_caja += valor_pago
        self.cantidad_vehiculos-=1
        self.vehiculos.remove(vehiculo)
            
    def mostrar_detalle_contrato(self, contrato):
        print("+==============================+")
        print("|       Detalle contrato       |")
        print("+==============================+")
        print(contrato)
        print("+==============================+")
        
    def crear_nuevo_contrato(self, opcion):
        match opcion:
            case 1:
                placa = input("Ingrese la placa del vehículo: ").upper()
                tiempo = int(input("Ingrese el tiempo del contrato en días (7, 15 o 30): "))
                if tiempo == 7 or tiempo == 15 or tiempo == 30:
                    if len(self.espacios_libres_motos) > 0:
                        espacio = self.espacios_libres_motos[0]
                        self.espacios_libres_motos.remove(espacio)
                        self.espacios_ocupados_motos.append(espacio)
                        vehiculo = Moto(placa, espacio)
                        match tiempo:
                            case 7:
                                valor_contrato = (self.tarifa_motos*7)-(self.tarifa_motos*7)*0.05
                            case 15:
                                valor_contrato = (self.tarifa_motos*15)-(self.tarifa_motos*15)*0.10
                            case 30:
                                valor_contrato = (self.tarifa_motos*30)-(self.tarifa_motos*30)*0.15  
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                        identificacion_cliente = input("Ingrese la identificación del cliente: ")
                        cliente = Cliente(nombre = nombre_cliente, identificacion=identificacion_cliente)
                        contrato = Contrato(dias = tiempo, valor = valor_contrato, numero_contrato=self.cantidad_contratos+1, vehiculo=vehiculo, cliente=cliente)
                        self.contratos.append(contrato)
                        self.cantidad_contratos+=1
                        self.dinero_en_caja+=contrato.valor
                        print("Contrato creado correctamente.")
                        self.mostrar_detalle_contrato(contrato)
                    else:
                        print("Lo sentimos, no hay espacios para moto disponibles en nuestro parqueadero.")
                else:
                    print("El tiempo ingresado no es válido") 
            case 2:
                placa = input("Ingrese la placa del vehículo: ").upper()
                tiempo = int(input("Ingrese el tiempo del contrato en días (7, 15 o 30): "))
                if tiempo == 7 or tiempo == 15 or tiempo == 30:
                    if len(self.espacios_libres_carros) > 0:
                        espacio = self.espacios_libres_carros[0]
                        self.espacios_libres_carros.remove(espacio)
                        self.espacios_ocupados_carros.append(espacio)
                        vehiculo = Carro(placa, espacio)
                        match tiempo:
                            case 7:
                                valor_contrato = (self.tarifa_carros*7)-(self.tarifa_carros*7)*0.05
                            case 15:
                                valor_contrato = (self.tarifa_carros*15)-(self.tarifa_carros*15)*0.10
                            case 30:
                                valor_contrato = (self.tarifa_carros*30)-(self.tarifa_carros*30)*0.15
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                        identificacion_cliente = input("Ingrese la identificación del cliente: ")
                        cliente = Cliente(nombre = nombre_cliente, identificacion=identificacion_cliente)
                        contrato = Contrato(dias = tiempo, valor = valor_contrato, numero_contrato=self.cantidad_contratos+1, vehiculo=vehiculo, cliente=cliente)
                        self.contratos.append(contrato)
                        self.cantidad_contratos+=1
                        self.dinero_en_caja+=contrato.valor
                        print("Contrato creado correctamente.")
                        self.mostrar_detalle_contrato(contrato)
                    else:
                        print("Lo sentimos, no hay espacios para carro disponibles en nuestro parqueadero.")
                else:
                    print("El tiempo ingresado no es válido")
    
    def renovar_contrato(self, contrato_consulta):
        dias = int(input("Ingrese los días para renovar su contrato (7, 15 o 30): "))
        fecha_actual = datetime.datetime.now()
        if dias == 7 or dias == 15 or dias == 30:
            for contrato in self.contratos:
                if contrato.numero_contrato == contrato_consulta.numero_contrato:
                    contrato.fecha_inicio = fecha_actual
                    contrato.fecha_finalizacion = contrato.fecha_inicio+datetime.timedelta(days=dias)
                    if isinstance(contrato.vehiculo, Moto):
                        if dias == 7:
                            contrato.valor_contrato = (self.tarifa_motos*7)-(self.tarifa_motos*7)*0.05
                        elif dias == 15:
                            contrato.valor_contrato = (self.tarifa_motos*15)-(self.tarifa_motos*15)*0.10
                        elif dias == 30:
                            contrato.valor_contrato = (self.tarifa_motos*30)-(self.tarifa_motos*30)*0.15
                        else:
                            print("Tiempo no válido.")
                            return
                    else:
                        if dias == 7:
                            contrato.valor_contrato = (self.tarifa_carros*7)-(self.tarifa_carros*7)*0.05
                        elif dias == 15:
                            contrato.valor_contrato = (self.tarifa_carros*15)-(self.tarifa_carros*15)*0.10
                        elif dias == 30:
                            contrato.valor_contrato = (self.tarifa_carros*30)-(self.tarifa_carros*30)*0.15
                        else:
                            print("Tiempo no válido.")
                            return
                    self.dinero_en_caja += contrato.valor
                    print("Contrato renovado exitosamente")
                    self.mostrar_detalle_contrato(contrato)
        else:
            print("El tiempo ingresado no es válido.")
    
    def cancelar_contrato(self, contrato_consulta):
        if isinstance(contrato_consulta.vehiculo, Moto):
            self.espacios_libres_motos.append(contrato_consulta.vehiculo.espacio)
            self.espacios_ocupados_motos.remove(contrato_consulta.vehiculo.espacio)
        else:
            self.espacios_libres_carros.append(contrato_consulta.vehiculo.espacio)
            self.espacios_ocupados_carros.remove(contrato_consulta.vehiculo.espacio)
        self.contratos.remove(contrato_consulta)
        print("+====================================+")
        print("|        Cancelación contrato        |")
        print("+====================================+")
        print(f"| Número contrato: {contrato_consulta.numero_contrato}")
        print(f"| Placa: {contrato_consulta.vehiculo.placa}")
        print(f"| Hora y fecha cancelacion: {datetime.datetime.now()}")
        print(f"| Tipo de vehiculo: {'moto' if isinstance(contrato_consulta.vehiculo, Moto) else 'carro'}")
        print("+------------------------------------+")
    
    def ingreso_vehiculo_contrato(self, contrato_consulta):
        fecha_actual = datetime.datetime.now()
        if contrato_consulta.fecha_finalizacion > fecha_actual:
            if contrato_consulta.vehiculo not in self. vehiculos:
                self.vehiculos.append(contrato_consulta.vehiculo)
                print("+====================================+")
                print("|      Ingreso vehículo contrato     |")
                print("+====================================+")
                print(f"| Placa: {contrato_consulta.vehiculo.placa}")
                print(f"| Hora y fecha ingreso: {fecha_actual}")
                print(f"| Tipo de vehiculo: {'moto' if isinstance(contrato_consulta.vehiculo, Moto) else 'carro'}")
                print("+------------------------------------+")
            else:
                print("El vehículo ya está en el parqueadero")
        else:
            print("Su contrato se encuentra vencido, ¿Qué desea hacer?: ")
            print("1. Renovar contrato.")
            print("2. Cancelar contrato.")
            try:
                opcion = int(input("Ingrese una opción: "))
                match opcion:
                    case 1:
                        self.renovar_contrato(contrato_consulta)
                    case 2:
                        self.cancelar_contrato(contrato_consulta)
                    case _:
                        print("La opción ingresada no existe.")
            except:
                print("Ingrese un dato válido.")
                
    def salida_vehiculo_contrato(self, contrato_consulta):
        if contrato_consulta.vehiculo in self.vehiculos:
            self.vehiculos.remove(contrato_consulta.vehiculo)
            print("+====================================+")
            print("|       Salida vehiculo contrato     |")
            print("+====================================+")
            print(f"| Placa: {contrato_consulta.vehiculo.placa}")
            print(f"| Hora fecha ingreso: {contrato_consulta.vehiculo.hora_fecha_entrada}")
            print(f"| Hora fecha salida: {datetime.datetime.now()}")
            print(f"| Tiempo en el parqueadero: {datetime.datetime.now()-contrato_consulta.vehiculo.hora_fecha_entrada}")
            print("+------------------------------------+")
            self.cantidad_vehiculos-=1
        else:
            print("El vehículo con contrato no ha ingresado al parqueadero.")
    
    def modificar_tarifa(self, opcion, nueva_tarifa):
        match opcion:
            case 1:
                self.tarifa_motos = nueva_tarifa
            case 2:
                self.tarifa_carros = nueva_tarifa
            case 3:
                self.tarifa_pernoctacion = nueva_tarifa
    
    def contratos_por_cliente(self, identificacion_cliente):
        encontrado = False
        for contrato in self. contratos:
            if contrato.cliente.identificacion == identificacion_cliente:
                encontrado = True
                print(contrato)
                print("+==============================+")
        if not encontrado:
            print("No se encontraron contratos con el número de identificación ingresado.")
            
    def mostrar_dinero_caja(self):
        if self.dinero_en_caja > 0:
            print(f"Hay ${self.dinero_en_caja} en la caja")
        else:
            print("No hay dinero en caja")
            
    def mostrar_vehiculos_parqueadero(self):
        if len(self.vehiculos) > 0:
            i=1
            for vehiculo in self.vehiculos:
                print (f'+====== Vehículo N° {i} ======+')
                print(vehiculo)
                print(f"Tipo: {'moto' if isinstance(vehiculo, Moto) else 'carro'}")
                i+=1
        else:
            print('No hay Vehiculos en el Parqueadero')
            
    def mostrar_contratos(self):
        if len(self.contratos)>0:
            for contrato in self.contratos:
                print (f'+=============================+')
                print(contrato)
        else:
            print('No hay Contratos Activos')
            
    def mostrar_cliente_contrato(self):
        if len(self.contratos)>0:
            for contrato in self.contratos:
                print (f'+====== Contrato N° {contrato.numero_contrato} ======+')
                print("Datos cliente")
                print(contrato.cliente)
        else:
            print("No hay contratos activos.")
            
    def espacios(self):
        print("+====================================+")
        print("|      Cantidad espacios libres      |")
        print("+====================================+")
        print(f" Espacios libres para motos: {len(self.espacios_libres_motos)}")
        print(f" Espacios ocupados para motos: {len(self.espacios_ocupados_motos)}")
        print("+------------------------------------+")
        print(f" Espacios libres para carros: {len(self.espacios_libres_carros)}")
        print(f" Espacios ocupados para carros: {len(self.espacios_ocupados_carros)}")
        print("+====================================+")