import datetime
import os
from Plaza import*
from Administrador import*
from Recepcionista import*
from Usuario import*
from Factura import*
from Vehiculo import*
class Parqueadero:
    def __init__(self):
        self.listarecepcionistas=[]
        self.listausuarios=[]
        self.cantmotos=0
        self.cantcarros=0
        self.cantvehiculosp=0
        self.ganancias=0
        self.contadorfacturas=0
        self.listaFacturas=[]
        lista1=[]
        lista2=[]
        lista3=[]
        contadorplazas=0
        codigoplazas=1
        for i in range(30):
            if contadorplazas < 4:
                plaza=Plaza(codigoplazas,1,1500,4000,50000)
                lista1.append(plaza)
            elif contadorplazas >= 4 and contadorplazas < 8:
                plaza=Plaza(codigoplazas,2,3500,7000,70000)
                lista1.append(plaza)
            elif contadorplazas >= 8 and contadorplazas < 10:
                plaza=Plaza(codigoplazas,3,8000,10000,80000)
                lista1.append(plaza)
            elif contadorplazas >= 10 and contadorplazas < 14:
                plaza=Plaza(codigoplazas,1,1500,4000,50000)
                lista2.append(plaza)
            elif contadorplazas >= 14 and contadorplazas < 18:
                plaza=Plaza(codigoplazas,2,3500,7000,70000)
                lista2.append(plaza)
            elif contadorplazas >= 18 and contadorplazas < 20:
                plaza=Plaza(codigoplazas,3,8000,10000,80000)
                lista2.append(plaza)
            elif contadorplazas >= 20 and contadorplazas < 24:
                plaza=Plaza(codigoplazas,1,1500,4000,50000)
                lista3.append(plaza)
            elif contadorplazas >= 24 and contadorplazas < 28:
                plaza=Plaza(codigoplazas,2,3500,7000,70000)
                lista3.append(plaza)
            elif contadorplazas >= 28 and contadorplazas < 30:
                plaza=Plaza(codigoplazas,3,8000,10000,80000)
                lista3.append(plaza)
            codigoplazas+=1
            contadorplazas+=1
        self.listaplazas=[lista1,lista2,lista3]
        sapito1=Administrador('Melany','Solarte',3152715827,1085762345,223034100)
        sapito2=Administrador('Sofia','Coral',3185388195,1081100253,223034075)
        sapito3=Administrador('Nathaly','Telag',3126250789,1087409348,223034060)
        sapito4=Administrador('Jesús','Tumal',3105207472,1081272956,223034080)
        self.listaadmin=[sapito1,sapito2,sapito3,sapito4]

    def ModificarPrecios(self):
        try:
            tipo_plaza = int(input('Digite el tipo de plaza para modificar -> '))
            if tipo_plaza in (1, 2, 3):
                self.mostrarPrecios(tipo_plaza)
                tipo_contrato = int(input('Dijite la opcion a modificar:\n1. Valor Hora\n2. Valor Dia\n3. Valor Mes\n -> '))
                if tipo_contrato in (1,2,3):
                    nuevo_valor = int(input(f'Digite el nuevo valor para las plazas de tipo {tipo_plaza} -> '))
                    for lista in self.listaplazas:
                        if tipo_plaza == 1:
                            if tipo_contrato ==1:
                                for plaza in lista[:4]:
                                    plaza.valorHora = nuevo_valor
                            elif tipo_contrato ==2:
                                for plaza in lista[:4]:
                                    plaza.valorDia = nuevo_valor
                            else:
                                for plaza in lista[:4]:
                                    plaza.valorMes = nuevo_valor
                        elif tipo_plaza == 2:
                            if tipo_contrato == 1:
                                for plaza in lista[4:8]:
                                    plaza.valorHora = nuevo_valor
                            elif tipo_contrato ==2:
                                for plaza in lista[4:8]:
                                    plaza.valorDia = nuevo_valor
                            else:
                                for plaza in lista[4:8]:
                                    plaza.valorMes = nuevo_valor
                        else:
                            if tipo_contrato == 1:
                                for plaza in lista[8:]:
                                    plaza.valorHora = nuevo_valor
                            elif tipo_contrato == 2:
                                for plaza in lista[8:]:
                                    plaza.valorDia = nuevo_valor
                            else:
                                for plaza in lista[8:]:
                                    plaza.valorMes = nuevo_valor
                else:
                    raise ValueError
        except ValueError:
            print('ERROR: Digíte un valor correcto')
    
    def consultarPrecios(self):
        tipo = int(input('Ingrese el tipo de vehiculo \n 1.Moto\n 2.Carro \n 3.Vehiculo Pesado\n ->'))  
        encontrado = False
        for sucursal in self.listaplazas:
            for plaza in sucursal:
                if plaza.tipo == tipo:
                    encontrado = True
                    break
            if encontrado:
                break
        if encontrado:  
            tipo_contrato = int(input('Dijite la opcion a consultar:\n1.Valor Hora\n2.Valor Dia\n3.Valor Mes\n -> '))
            if tipo == 1:
                if tipo_contrato ==1:
                    print(f'Valor Hora Moto: {plaza.valorHora}')
                elif tipo_contrato ==2:
                    print(f'Valor Dia Moto: {plaza.valorDia}')
                else:
                    print(f'Valor Mes Moto: {plaza.valorMes}')
            elif tipo ==2:
                if tipo_contrato==1:
                    print(f'Valor Hora Carro: {plaza.valorHora}')
                elif tipo_contrato ==2:
                    print(f'Valor Dia Carro: {plaza.valorDia}')
                else:
                    print(f'Valor Mes Carro: {plaza.valorMes}')
            else:
                if tipo_contrato==1:
                    print(f'Valor Hora Vehiculo Pesado: {plaza.valorHora}')
                elif tipo_contrato ==2:
                    print(f'Valor Dia Vehiculo Pesado: {plaza.valorDia}')
                else:
                    print(f'Valor Mes Vehiculo Pesado: {plaza.valorMes}')
        else:
           print( 'El tipo de vehículo que ingresó no es válido')           
    
    def SalidaFacturacion(self):
        salida=False
        encontrar_usuario=False
        documento=int(input('Digite el número de documento-> '))
        for usuario in self.listausuarios:
            if usuario.documento==documento:
                encontrar_usuario=True
                placa=input('Digite la placa del vehiculo -> ')
                encontrar_placa=False
                for vehiculo in usuario.listavehiculos:
                    if vehiculo.placa==placa:
                        encontrar_placa=True
                        vehiculo_factura=vehiculo
                        usuario_factura=usuario
                        for sucursal in self.listaplazas:
                            for plaza in sucursal:
                                if plaza.placa_asociada==placa:
                                    plaza.estado=True
                                    plaza.placa_asociada=None 
                                    salida=True
                                    contrato = int(input('Ingrese su tipo de contrato:\n1.Estadia por hora\n2.Estadia por Dia\n3.Estadia por Mes\n->'))
                                    if contrato in (1,2,3):
                                        tiempo=float(input('Digite el tiempo de estadía del vehiculo->'))
                                        if contrato ==1:
                                            subtotal=plaza.valorHora * tiempo
                                            valor = subtotal
                                            descuento = 0
                                        elif contrato ==2:
                                            if tiempo >=7:
                                                subtotal = plaza.valorDia * tiempo
                                                descuento = subtotal * 5/100
                                                valor = subtotal - descuento
                                            else:
                                                valor = plaza.valorDia * tiempo
                                                subtotal = valor
                                                descuento = 0
                                        else:
                                            subtotal = plaza.valorMes * tiempo
                                            descuento = subtotal * 10/100
                                            valor = subtotal - descuento
                                    self.ganancias+=valor
                                    encontrar_placa=True
                if not encontrar_placa:
                    print(f'Vehiculo no encontrado')
        if not encontrar_usuario:
            print('Usuario no encontrado')
        if salida:
            self.contadorfacturas+=1
            fecha=datetime.datetime.now()
            factura=Factura(self.contadorfacturas,tiempo,fecha,subtotal, descuento,valor,contrato)
            os.system('cls') 
            facturaRegistro=[factura,usuario_factura,vehiculo_factura]
            self.listaFacturas.append(facturaRegistro)
            factura.MostrarFactura(usuario_factura,vehiculo_factura)

    def mostrarPlazasDisponibles(self):
        tipo = int(input('Ingrese el tipo de plaza que quiere consultar\n1.Plazas moto\n2.Plazas carro \n3.Plazas vehiculos pesados\n -> '))
        for listaplazas in self.listaplazas:
            if tipo == 1:
                for plaza in listaplazas[:4]:
                    if plaza.estado == True:
                        print (f'{plaza.codigo} = disponible')
            elif tipo == 2:
                for plaza in listaplazas[4:8]:
                    if plaza.estado == True:
                        print (f'{plaza.codigo} = disponible')
            elif tipo == 3:
                for plaza in listaplazas[8:]:
                    if plaza.estado == True:
                        print (f'{plaza.codigo} = disponible')
            else:
                print('Tipo de plaza incorrecto')
        
    def IngresarVehiculo(self):
        encontrar_usuario = False
        documento = int(input('Digite el número de documento -> '))
        for usuarioo in self.listausuarios:
            if usuarioo.documento == documento:
                encontrar_usuario = True
                encontrar_plaza = False
                placa = input('Digite la placa del vehículo-> ')
                vehiculoEstacionado = False
                for sucursal in self.listaplazas:
                    for plaza in sucursal:
                        if placa == plaza.placa_asociada:
                            vehiculoEstacionado = True
                if not vehiculoEstacionado:
                    for vehiculo in usuarioo.listavehiculos:
                        if vehiculo.placa == placa:
                            encontrar_plaza = False
                            for sucursal in self.listaplazas:
                                for plazzzza in sucursal:
                                    if plazzzza.tipo == vehiculo.tipoVehiculo and plazzzza.estado == True:
                                        plazzzza.estado = False
                                        plazzzza.placa_asociada = placa 
                                        if plazzzza.codigo > 10 and plazzzza.codigo <= 20:
                                            print('Diríjase a nuestra sucursal 2')
                                        elif plazzzza.codigo > 20 and plazzzza.codigo <= 30:
                                            print('Diríjase a nuestra sucursal 3')
                                        print(f'La plaza {plazzzza.codigo} se ha reservado para el vehículo {placa}')
                                        encontrar_plaza = True
                                        break
                                if encontrar_plaza:
                                    break
                            if not encontrar_plaza:
                                print('Lo sentimos, no tenemos plazas disponibles. Diríjase a otra sucursal.')
                            break  
                    if not encontrar_plaza:
                        tipo = int(input('Digite el tipo de vehículo-> '))
                        if tipo > 3 or tipo < 0:
                            print('El tipo de vehículo es inválido')
                        else:
                            if tipo == 1:
                                self.cantmotos += 1
                            elif tipo == 2:
                                self.cantcarros += 1
                            else:
                                self.cantvehiculosp += 1
                            vehiculo = Vehiculo(placa, tipo)
                            usuarioo.AgregarVehiculo(vehiculo)
                            encontrar_plaza = False
                            for sucursal in self.listaplazas:
                                for plaza in sucursal:
                                    if tipo == plaza.tipo and plaza.estado == True:
                                        plaza.estado = False
                                        plaza.placa_asociada = placa
                                        if plaza.codigo > 10 and plaza.codigo <= 20:
                                            print('Diríjase a nuestra sucursal 2')
                                        elif plaza.codigo > 20 and plaza.codigo <= 30:
                                            print('Diríjase a nuestra sucursal 3')
                                        print(f'La plaza {plaza.codigo} se ha reservado para el vehículo {vehiculo.placa}')
                                        encontrar_plaza = True
                                        break
                                if encontrar_plaza:
                                    break
                            if not encontrar_plaza:
                                print('Lo sentimos, no tenemos plazas disponibles. Diríjase a otra sucursal.')
                if vehiculoEstacionado:
                    print('El vehículo ya se encuentra estacionado')
        if not encontrar_usuario:
            nombre = input('Digite el nombre-> ')
            apellido = input('Digite el apellido-> ')
            telefono = int(input('Digite el teléfono->  '))
            placa = input('Digite la placa del vehículo->  ')
            vehiculoEstacionado = False
            for sucursal in self.listaplazas:
                for plaza in sucursal:
                    if placa == plaza.placa_asociada:
                        vehiculoEstacionado = True
            if not vehiculoEstacionado:
                tipo = int(input('Digite el tipo de vehículo-> '))
                if tipo > 3 or tipo < 0:
                    print('El tipo de vehículo es inválido')
                else:
                    usuario = Usuario(nombre, apellido, telefono, documento)
                    self.listausuarios.append(usuario)
                    if tipo == 1:
                        self.cantmotos += 1
                    elif tipo == 2:
                        self.cantcarros += 1
                    else:
                        self.cantvehiculosp += 1
                    vehiculo = Vehiculo(placa, tipo)
                    usuario.AgregarVehiculo(vehiculo)
                    encontrar_plaza = False
                    for sucursal in self.listaplazas:
                        for plaza in sucursal:
                            if tipo == plaza.tipo and plaza.estado == True:
                                plaza.estado = False
                                plaza.placa_asociada = placa
                                if plaza.codigo > 10 and plaza.codigo <= 20:
                                    print('Diríjase a nuestra sucursal 2')
                                elif plaza.codigo > 20 and plaza.codigo <= 30:
                                    print('Diríjase a nuestra sucursal 3')
                                print(f'La plaza {plaza.codigo} se ha reservado para el vehículo {vehiculo.placa}')
                                encontrar_plaza = True
                                break
                        if encontrar_plaza:
                            break
                    if not encontrar_plaza:
                        print('Lo sentimos, no tenemos plazas disponibles. Diríjase a otra sucursal.')
            if vehiculoEstacionado:
                print('El vehículo ya se encuentra estacionado')


    def estadisticasTipo (self):
        print (f'La cantidad de motos que ha ingresado al parqueadero es: {self.cantmotos}\nLa cantidad de carros que ha ingresado al parqueadero es: {self.cantcarros}\nLa cantidad de vehiculos pesados ha ingresado al parqueadero es: {self.cantvehiculosp}')

    def gananciasTotales(self):
        print(f'Ganancias totales del parqueadero: {self.ganancias}')
                    
    def ocupacionPlazas(self):
        cpMotos = 0
        cpCarros = 0
        cpVehiculosp = 0
        contPlazas = 0
        opcion = int(input('Ingrese la opción que quiere consultar\n1.Plazas moto\n2.Plazas carro \n3.Plazas vehículos pesados\n4.Plazas Totales\n -> '))

        if opcion == 1:
            for sucursal in self.listaplazas:
                for plaza in sucursal:
                    if plaza.tipo == 1 and not plaza.estado:
                        cpMotos += 1
            promediom = cpMotos / 12
            pmotos = promediom * 100
            print(f'Las plazas de motos están ocupadas en un {pmotos}%')

        elif opcion == 2:
            for sucursal in self.listaplazas:
                for plaza in sucursal:
                    if plaza.tipo == 2 and not plaza.estado:
                        cpCarros += 1
            promediom = cpCarros / 12
            pcarros = promediom * 100
            print(f'Las plazas de carros están ocupadas en un {pcarros}%')

        elif opcion == 3:
            for sucursal in self.listaplazas:
                for plaza in sucursal:
                    if plaza.tipo == 3 and not plaza.estado:
                        cpVehiculosp += 1
            promediom = cpVehiculosp / 6
            pvehiculos = promediom * 100
            print(f'Las plazas de vehículos pesados están ocupadas en un {pvehiculos}%')

        elif opcion == 4:
            for sucursal in self.listaplazas:
                for plaza in sucursal:
                    if not plaza.estado:
                        contPlazas += 1
            promediom = contPlazas / 30
            porcentajeTotal = promediom * 100
            print(f'Las plazas del parqueadero están ocupadas en un {porcentajeTotal}%')

        else:
            print('Opción inválida')


    def AñadirAdmin(self):
        clave = int(input('Ingrese la clave del administrador: '))
        encontrar_clave=False
        for admin in self.listaadmin:
            if admin.clave==clave:
                encontrar_clave=True
                break
        if not encontrar_clave:
            nombre = input('Ingrese el nombre del administrador: ')
            apellido = input('Ingrese el apellido del administrador: ')
            telefono = int(input('Ingrese el teléfono del administrador: '))
            documento = int(input('Ingrese el documento del administrador: '))
            administrador = Administrador(nombre, apellido, telefono, documento, clave)
            self.listaadmin.append(administrador)
            print(f'Administrador {nombre} {apellido} agregado con éxito.')
        else: 
            print('Esta clave ya está en uso')
    
    def AñadirRecepcionista(self):
        clave = int(input('Ingrese la clave del recepcionista: '))
        encontrar_clave=False
        for recepcionista in self.listarecepcionistas:
            if recepcionista.clave==clave:
                encontrar_clave=True
                break
        if not encontrar_clave:
            nombre = input('Ingrese el nombre del recepcionista: ')
            apellido = input('Ingrese el apellido del recepcionista: ')
            telefono = int(input('Ingrese el teléfono del recepcionista: '))
            documento = int(input('Ingrese el documento del recepcionista: '))
            recepcionista = Recepcionista(nombre, apellido, telefono, documento, clave)
            self.listarecepcionistas.append(recepcionista)
            print(f'Recepcionista {nombre} {apellido} agregado con éxito.')
        else: 
            print('Esta clave ya está en uso')

    def MostrarPersonal(self):
        print("\nLista de Administradores:")
        for admin in self.listaadmin:
            print(str(admin))
            
        print("\nLista de Recepcionistas:")
        for recepcionista in self.listarecepcionistas:
            print(str(recepcionista))
    
    def MostrarUsuarios(self):
        print('Lista de usuarios:')
        for usuario in self.listausuarios:
            print(usuario)
            print('')

    def ConsultarFactura(self):
        numeroFactura=int(input('Digite el número de la factura-> '))
        encontrarFactura=False
        for factura in self.listaFacturas:
            if factura[0].id==numeroFactura:
                factura[0].MostrarFactura(factura[1],factura[2])
                encontrarFactura=True
        if not encontrarFactura:
            print('Factura no encontrada')

    def mostrarPrecios(self, tipo):
        for plaza in self.listaplazas[tipo - 1]:  
            if tipo == 1 and plaza == self.listaplazas[tipo - 1][0]:
                print('--------------Precios Plazas Moto---------------')
            elif tipo == 2 and plaza == self.listaplazas[tipo - 1][0]:
                print('--------------Precios Plazas Carro--------------')
            elif tipo == 3 and plaza == self.listaplazas[tipo - 1][0]:
                print('--------------Precios Plazas Vehiculos----------')

            print(f'Valor Hora: {plaza.valorHora} - Valor Dia: {plaza.valorDia} - Valor Mes: {plaza.valorMes}')
            break




                