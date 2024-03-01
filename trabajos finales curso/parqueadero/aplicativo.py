import os
from Parqueadero import *
from Vehiculo import *
from Cliente import *
from Contrato import *
import pickle

'''

'''

#Función para crear parqueadero si el archivo no existe
def abrir_parqueadero():
    try:
        tarifa_motos = int(input("Ingrese la tarifa para motos: "))
        tarifa_carros = int(input("Ingrese la tarifa para carros: "))
        tarifa_pernoctacion = int(input("Ingrese la tarifa de pernoctación: "))
        cantidad_espacios_libres_motos = int(input("Ingrese la cantidad de espacios libres para motos: "))
        cantidad_espacios_libres_carros = int(input("Ingrese la cantidad de espacios libres para carros: "))
        espacios_libres_motos = []
        espacios_libres_carros = []
        for i in range(1, cantidad_espacios_libres_motos+1):
            espacios_libres_motos.append(f"M{i}")
        for i in range(1, cantidad_espacios_libres_carros+1):
            espacios_libres_carros.append(f"C{i}")
        parqueadero = Parqueadero(tarifa_motos=tarifa_motos, tarifa_carros=tarifa_carros, espacios_libres_motos=espacios_libres_motos, espacios_libres_carros=espacios_libres_carros, tarifa_pernoctacion=tarifa_pernoctacion)
        print("Parqueadero abierto exitosamente")
        return parqueadero
    except:
        print("Ha ocurrido un error al abrir el parqueadero, por favor inténtelo nuevamente.")
    return None

#Función para cargar los datos del parqueadero si el archivo ya existe
def cargar_parqueadero():
    try:
        with open("parqueadero.dat", "rb") as archivo_parqueadero:
            parqueadero = pickle.load(archivo_parqueadero)
        return parqueadero
    except:
        print("Ha ocurrido un error al cargar los datos del parqueadero, por favor inténtelo nuevamente.")

#Función para salir del parqueadero y guardar datos en el archivo
def salir(parqueadero):
    try:
        with open("parqueadero.dat", "wb") as archivo_parqueadero:
            pickle.dump(parqueadero, archivo_parqueadero)
            print("Datos guardados correctamente.")
            os.system("pause")
    except:
        print("Ha ocurrido un error al guardar los datos del parqueadero, por favor inténtelo nuevamente.")

def ingreso_vehiculo(parqueadero):
    while True:
        os.system("cls")
        placa = input("Ingrese la placa del vehículo: ").upper()
        print("+====================================+")
        print("|          Ingreso vehículo          |")
        print("+====================================+")
        print("| 1. Moto.                           |")
        print("| 2. Carro.                          |")
        print("+------------------------------------+")
        print("| 3. Regresar                        |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            consulta = parqueadero.consultar_vehiculo(placa)
            if consulta == None:
                match opcion:
                    case 1:
                        if len(parqueadero.espacios_libres_motos) > 0:
                            espacio = parqueadero.espacios_libres_motos[0]
                            vehiculo = Moto(placa, espacio)
                        else:
                            print("No hay espacios para moto disponibles en el parqueadero")
                            os.system("pause")
                            break  
                    case 2:
                        if len(parqueadero.espacios_libres_carros) > 0:
                            espacio = parqueadero.espacios_libres_carros[0]
                            vehiculo = Carro(placa, espacio)
                        else:
                            print("No hay espacios para carro disponibles en el parqueadero")
                            os.system("pause")
                            break  
                    case 3:
                        break
                    case _:
                        print("La opción ingresada no existe.")
                parqueadero.ingresar_vehiculo(vehiculo)
                print("+====================================+")
                print("|          Ingreso exitoso           |")
                print("+====================================+")
                print(f"| Placa: {vehiculo.placa}")
                print(f"| Espacio asignado: {vehiculo.espacio}")
                print(f"| Hora y fecha ingreso: {vehiculo.hora_fecha_entrada}")
                print(f"| Tipo de vehiculo: {'moto' if isinstance(vehiculo, Moto) else 'carro'}")
                print("+------------------------------------+")
                os.system("pause")
                break
            else:
                print("El vehículo ya se encuentra en el parqueadero.")
        except:
            print("Ha ocurrido un error, inténtelo nuevamente.")


def salida_vehiculo(parqueadero):
    os.system("cls")
    if len(parqueadero.vehiculos) > 0:
        print("+====================================================================+")
        print("|                          Salida vehículo                           |")
        print("+====================================================================+")
        parqueadero.mostrar_vehiculos_parqueadero()
        placa = input("| Ingrese la placa del vehículo para salir del parqueadero: ").upper()
        vehiculo = parqueadero.consultar_vehiculo(placa)
        if vehiculo != None:
            os.system("cls")
            parqueadero.salida_vehiculo(vehiculo)
        else:
            print("El vehículo no se encuentra en el parqueadero.")
    else:
        print("Aún no hay vehículos en el parqueadero")
        
def manejo_parqueadero(parqueadero):
    while True:
        os.system("cls")
        print("+====================================+")
        print("|         Manejo Parqueadero         |")
        print("+====================================+")
        print("| 1. Ingreso vehículo.               |")
        print("| 2. Salida vehículo.                |")
        print("+------------------------------------+")
        print("| 3. Regresar                        |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    ingreso_vehiculo(parqueadero)
                case 2:
                    if len(parqueadero.vehiculos) > 0:
                        salida_vehiculo(parqueadero)
                    else:
                        print("Aún no hay vehículos en el parqueadero.")
                case 3:
                    break
                case _:
                    print("La opción ingresada no existe.")
        except:
            print("Ingrese un dato válido.")
        os.system("pause")
        
def nuevo_contrato(parqueadero):
    while True:
        os.system("cls")
        print("+====================================+")
        print("|   Seleccione el tipo de vehículo   |")
        print("+====================================+")
        print("| 1. Moto.                           |")
        print("| 2. Carro.                          |")
        print("+------------------------------------+")
        print("| 3. Regresar.                       |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1 or opcion == 2:
                parqueadero.crear_nuevo_contrato(opcion)
            elif opcion == 3:
                break
            else:
                print("La opción ingresada no existe.")
        except:
            print("Ha ocurrido un error al crear el contrato, por favor inténtelo de nuevo")
        os.system("pause")
        
        
def consultar_contrato(parqueadero):
    if len(parqueadero.contratos) > 0:
        print('         Contratos Disponibles')
        for contrato in parqueadero.contratos:
            print(f"Número contrato: {contrato.numero_contrato}")
            print(f"ID cliente: {contrato.cliente.identificacion}")
            print("-----------------------------------")
        numero_contrato = input("Ingrese el número de contrato a consultar: ").upper()
        contrato = parqueadero.consultar_contrato(numero_contrato)
        if contrato != None:
            parqueadero.mostrar_detalle_contrato(contrato)
        else:
            print("El contrato no existe")
    else:
        print("No hay contratos")
        
def ingreso_vehiculo_contrato(parqueadero):
    if len(parqueadero.contratos) > 0:
        numero_contrato = input("Ingrese el número de contrato asignado: ").upper()
        contrato_consulta = parqueadero.consultar_contrato(numero_contrato)
        if contrato_consulta != None:
            parqueadero.ingreso_vehiculo_contrato(contrato_consulta)
        else:
            print("El contrato no existe.")
    else:
        print("Aún no hay contratos.")
        
def salida_vehiculo_contrato(parqueadero):
    if len(parqueadero.contratos) > 0:
        numero_contrato = input("Ingrese el número de contrato asignado: ").upper()
        contrato_consulta = parqueadero.consultar_contrato(numero_contrato)
        if contrato_consulta != None:
            parqueadero.salida_vehiculo_contrato(contrato_consulta)
        else:
            print("El contrato no existe.")
    else:
        print("Aún no hay contratos.")
        
def cancelar_contrato(parqueadero):
    if len(parqueadero.contratos) > 0:
        numero_contrato = input("Ingrese el número de contrato asignado: ").upper()
        contrato_consulta = parqueadero.consultar_contrato(numero_contrato)
        if contrato_consulta != None:
            parqueadero.cancelar_contrato(contrato_consulta)
        else:
            print("El contrato no existe.")
    else:
        print("Aún no hay contratos.")
            
def manejo_parqueadero_contratos(parqueadero):
    while True:
        os.system("cls")
        print("+========================================+")
        print("|    Manejo Parqueadero con Contratos    |")
        print("+========================================+")
        print("|     1. Ingreso vehículo con contrato.  |")
        print("|    2. Salida vehículo con contrato.    |")
        print("|    3. Nuevo contrato.                  |")
        print("|    4. Consultar contrato.              |")
        print("|    5. Cancelar contrato.               |")
        print("+----------------------------------------+")
        print("|    6. Regresar                         |")
        print("+========================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    ingreso_vehiculo_contrato(parqueadero)
                case 2:
                    if len(parqueadero.vehiculos) > 0:
                        salida_vehiculo_contrato(parqueadero)
                    else:
                        print("Aún no hay vehículos en el parqueadero.")
                case 3:
                    nuevo_contrato(parqueadero)
                case 4:
                    consultar_contrato(parqueadero)
                case 5:
                    cancelar_contrato(parqueadero)
                case 6:
                    break
                case _:
                    print("La opción ingresada no existe.")
        except:
            print("Ingrese un dato válido.")
        os.system("pause")
        
def modificar_tarifas(parqueadero):
    while True:
        os.system("cls")
        print("+====================================+")
        print("|         Modificar tarifas          |")
        print("+====================================+")
        print("| 1. Modificar tarifa motos.         |")
        print("| 2. Modificar tarifa carros.        |")
        print("| 3. Modificar tarifa pernoctación.  |")
        print("+------------------------------------+")
        print("| 4. Regresar.                       |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1 or opcion == 2 or opcion == 3:
                try:
                    nueva_tarifa = int(input("Ingrese la nueva tarifa: "))
                    parqueadero.modificar_tarifa(opcion, nueva_tarifa)
                    print("Tarifa modificada correctamente.")
                except:
                    print("Ha ocurrido un error.")
            elif opcion == 4:
                break
            else:
                print("La opción ingresada no existe.")
        except:
            print("Ingrese un dato válido")
        os.system("pause")
        
def administracion_parqueadero(parqueadero):
    while True:
        os.system("cls")
        print("+====================================+")
        print("|    Administración parqueadero      |")
        print("+====================================+")
        print("| 1. Modificar tarifas.              |")
        print("+------------------------------------+")
        print("| 2. Regresar.                       |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    modificar_tarifas(parqueadero)
                case 2:
                    break
                case _:
                    print("La opción ingresada no existe")
        except:
            print("Ingrese un dato válido")
        os.system("pause")
        
def contratos_por_cliente(parqueadero):
    identificacion_cliente = input("Ingrese el número de identificación del cliente: ")
    parqueadero.contratos_por_cliente(identificacion_cliente)
        
def estadisticas(parqueadero):
    while True:
        os.system("cls")
        print("+====================================+")
        print("|      Estadísticas parqueadero      |")
        print("+====================================+")
        print("| 1. Dinero en caja.                 |")
        print("| 2. Vehículos en el parqueadero.    |")
        print("| 3. Contratos.                      |")
        print("| 4. Contratos por cliente.          |")
        print("| 5. Clientes contratos.             |")
        print("| 6. Espacios libres y ocupados.     |")
        print("+------------------------------------+")
        print("| 7. Salir.                          |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    parqueadero.mostrar_dinero_caja()
                case 2:
                    parqueadero.mostrar_vehiculos_parqueadero()
                case 3:
                    parqueadero.mostrar_contratos()
                case 4:
                    contratos_por_cliente(parqueadero)
                case 5:
                    parqueadero.mostrar_cliente_contrato()
                case 6:
                    parqueadero.espacios()
                case 7:
                    break
                case _:
                    print("La opción ingresada no existe.")
        except:
            print("Ingrese un dato válido.")
        os.system("pause")
        
#Función menú principal  
def menu_principal():
    abierto = False
    while True:
        os.system("cls")
        print("+====================================+")
        print('|   Parqueadero "El Mas Generico"    |')
        print("+====================================+")
        print('|     Andres Dario Tello Burbano     |')
        print('|     Valentina Melo Solarte         |')
        print('|     Miguel Angel Narvaez Portilla  |')
        print('|     Darwin David Muñoz Benavidez   |')
        print("+====================================+")
        print("| 1. Abrir parqueadero.              |")
        print("| 2. Manejo parqueadero.             |")
        print("| 3. Manejo parqueadero contratos.   |")
        print("| 4. Administración parqueadero.     |")
        print("| 5. Estadísticas parqueadero.       |")
        print("+------------------------------------+")
        print("| 6. Salir y guardar datos.          |")
        print("| 7. Salir.                          |")
        print("+====================================+")
        try:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    if not abierto:
                        if os.path.exists("parqueadero.dat"):
                            parqueadero = cargar_parqueadero()
                            print("Datos cargados correctamente.")
                        else:
                            parqueadero = abrir_parqueadero()
                        if parqueadero != None:
                            abierto = True
                    else:
                        print("El parqueadero ya fue abierto.")
                case 2:
                    if abierto:
                        manejo_parqueadero(parqueadero)
                    else:
                        print("Aún no ha abierto el parqueadero.")
                case 3:
                    if abierto:
                        manejo_parqueadero_contratos(parqueadero)
                    else:
                        print("Aún no ha abierto el parqueadero.")
                case 4:
                    if abierto:
                        administracion_parqueadero(parqueadero)
                    else:
                        print("Aún no ha abierto el parqueadero.")
                case 5:
                    if abierto:
                        estadisticas(parqueadero)
                    else:
                        print("Aún no ha abierto el parqueadero.")
                case 6:
                    if abierto:
                        salir(parqueadero)
                        break
                    else:
                        print("Aún no ha abierto el parqueadero.")
                case 7:
                    print("Hasta luego :)")
                    break
                case _:
                    print("La opción ingresada no existe.")
        except:
            print("Ingrese un dato válido.")
        os.system("pause")
menu_principal()