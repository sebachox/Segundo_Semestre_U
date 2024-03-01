from Administrador import *
from Factura import *
from Parqueadero import *
from Persona import *
from Usuario import *
from Vehiculo import *
import pickle
import os
sapito=Parqueadero()
def serializarParqueadero(parqueadero):
    listaInfo=[parqueadero.listarecepcionistas,parqueadero.listausuarios,parqueadero.cantmotos,parqueadero.cantcarros,parqueadero.cantvehiculosp,parqueadero.ganancias,parqueadero.contadorfacturas,parqueadero.listaFacturas,parqueadero.listaplazas,parqueadero.listaadmin]
    with open('Informacion','wb') as archivo:
        pickle.dump(listaInfo,archivo)

def deserializarParqueadero(parqueadero):
    with open('Informacion','rb') as archivo:
        listaInfo=pickle.load(archivo)
        parqueadero.listarecepcionistas=listaInfo[0]
        parqueadero.listausuarios=listaInfo[1]
        parqueadero.cantmotos=listaInfo[2]
        parqueadero.cantcarros=listaInfo[3]
        parqueadero.cantvehiculosp=listaInfo[4]
        parqueadero.ganancias=listaInfo[5]
        parqueadero.contadorfacturas=listaInfo[6]
        parqueadero.listaFacturas=listaInfo[7]
        parqueadero.listaplazas=listaInfo[8]
        parqueadero.listaadmin=listaInfo[9]

def main():
    os.system('cls')
    while True:
        print('....................................')
        print('.          MENÚ PRINCIPAL          .')
        print('....................................')
        print('. 1. Administrador                 .')
        print('. 2. Recepcionista                 .')
        print('....................................')
        print('. 3. Salir                         .')
        print('..................................-.')  
        try:
            print('Elija su rol')
            opcion = int(input('Eliga una opcion-> '))
            match opcion:
                case 1:
                    os.system('cls')
                    clavea=int(input('Digite su clave de administrador-> '))
                    b=0
                    for i in sapito.listaadmin:
                        if i.clave==clavea:
                            b=1
                            MenuAdministrador()
                    if b==0:
                        print('Clave no encontrada')
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    claveb=int(input('Digite su clave de recepcionista o administrador-> '))
                    b=0
                    for recepcionista in sapito.listarecepcionistas:
                        if recepcionista.clave == claveb:
                            b=1
                            MenuRecepcionista()
                    for administrador in sapito.listaadmin:
                        if administrador.clave == claveb:
                            b=1
                            MenuRecepcionista()
                    if b==0:
                        print('Clave no encontrada')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    print('Gracias por su visita')
                    break
                case other:
                    os.system('cls')
                    print('ERROR: Digíte valor correcto')
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('ERROR: Digíte valor correcto')
            os.system('pause')
            os.system('cls')

def MenuAdministrador():
    os.system('cls')
    while True:
        print('...........................')
        print('.    MENU ADMINISTRADOR   .')
        print('...........................')
        print('. 1. Modificar Precios    .')
        print('. 2. Consultar Precios    .')
        print('. 3. Consultar Usuario    .')
        print('. 4. Mostrar Usuarios     .')
        print('. 5. Añadir administrador .')
        print('. 6. Añadir recepcionista .')
        print('. 7. Mostrar personal     .')
        print('. 8. Estadisticas         .')
        print('. 9. Consultar Factura    .')
        print('...........................')
        print('. 10. Salir               .')
        print('...........................')
        try:
            opcion = int(input('Eliga una opcion-> '))
            match opcion:
                case 1:
                    os.system('cls')
                    Parqueadero.ModificarPrecios(sapito)
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    Parqueadero.consultarPrecios(sapito)
                    os.system('pause')
                    os.system('cls')   
                case 3:
                    os.system('cls')
                    Usuario.consultarUsuario(sapito)
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    sapito.MostrarUsuarios()
                    os.system('pause')
                    os.system('cls')   
                case 5:
                    os.system('cls')
                    sapito.AñadirAdmin()
                    os.system('pause')
                    os.system('cls')
                case 6:
                    os.system('cls')
                    sapito.AñadirRecepcionista()
                    os.system('pause')
                    os.system('cls')
                case 7:
                    os.system('cls')
                    sapito.MostrarPersonal()
                    os.system('pause')
                    os.system('cls')
                case 8:
                    os.system('cls')
                    Estadisticas()
                    os.system('pause')
                    os.system('cls')
                case 9:
                    os.system('cls')
                    sapito.ConsultarFactura()
                    os.system('pause')
                    os.system('cls')
                case 10:
                    os.system('cls')
                    print('Regresando al menú principal....')
                    break
                    os.system('pause')
                case other:
                    os.system('cls')
                    print('ERROR: Digíte valor correcto')
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('ERROR: Digíte valor correcto')
            os.system('pause') 
            os.system('cls')

def MenuRecepcionista():
    os.system('cls')
    while True:
        print('...........................')
        print('.    MENU RECEPCIONISTA   .')
        print('...........................')
        print('. 1. Ingresar vehículo    .')
        print('. 2. Modificar usuario    .')
        print('. 3. Consultar usuario    .')
        print('. 4. Plazas Disponibles   .')
        print('. 5. Salida y facturación .')
        print('...........................')
        print('. 6. Salir                .')
        print('...........................')
        try:
            opcion = int(input('Eliga una opcion-> '))
            match opcion:
                case 1:
                    os.system('cls')
                    sapito.IngresarVehiculo()
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    sapito.MostrarUsuarios()
                    Usuario.modificarUsuario(sapito)
                    os.system('pause')
                    os.system('cls')   
                case 3:
                    os.system('cls')
                    Usuario.consultarUsuario(sapito)
                    os.system('pause')
                    os.system('cls')  
                case 4:
                    os.system('cls')
                    sapito.mostrarPlazasDisponibles()
                    os.system('pause')
                    os.system('cls')        
                case 5:
                    os.system('cls')
                    sapito.SalidaFacturacion()
                    os.system('pause')
                    os.system('cls')           
                case 6:
                    os.system('cls')
                    print('Regresando al menú principal....')
                    os.system('pause')
                    os.system('cls')
                    break
                case other:
                    os.system('cls')
                    print('ERROR: Digíte valor correcto')
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('ERROR: Digíte valor correcto')
            os.system('pause') 
            os.system('cls')
    
def Estadisticas():
    os.system('cls')
    while True:
        print('...................................')
        print('.        MENU ESTADISTICAS        .')
        print('...................................')
        print('. 1. Estadisticas por tipo        .')
        print('. 2. Ganancias Totales            .')
        print('. 3. Ocupación Plazas             .')
        print('...................................')
        print('. 4. Salir                        .')
        print('...................................')
        try:
            opcion = int(input('Eliga una opcion-> '))
            match opcion:
                case 1:
                    os.system('cls')
                    sapito.estadisticasTipo()
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    sapito.gananciasTotales()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    sapito.ocupacionPlazas()
                    os.system('pause')
                    os.system('cls')              
                case 4:
                    os.system('cls')
                    print('Regresando al menú principal....')
                    break

                case other:
                    os.system('cls')
                    print('ERROR: Digíte un valor correcto')
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('ERROR: Digíte un valor correcto')
            os.system('pause') 
            os.system('cls')


deserializarParqueadero(sapito)

if __name__ == '__main__':
    main()  

serializarParqueadero(sapito)




