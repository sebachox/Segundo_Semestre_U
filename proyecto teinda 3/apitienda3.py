import os
from colorama  import init,Fore
from producto3 import Producto
from tienda3 import Tienda
from factura3 import Factura
from venta3 import Venta
from leer import Leer

init()


def crearTienda():
    tienda = Tienda()
    return tienda
tienda = crearTienda()

# if not creada:
#     tienda=crearTienda()
#     creada=True
#     print("la tienda ha sido creada con exito :)")
# else:
#     print("ya hay productos en la tienda")
#     os.system("pause")

def realizarVenta(tienda):
    tienda.mostrarProductos()
    res = "si"
    nueva_Factura = Factura(tienda.numeroFactura)
    
    while res.lower() == "si":  # Asegura que la respuesta sea "si" independientemente de las mayúsculas
        producto = input("\nIngrese el nombre del producto que desea: ")
        producto_seleccionado = tienda.consultarProducto(producto.lower())

        if producto_seleccionado.nombre == producto.lower():
            cantidad = int(input(f'\nDigite la cantidad de {producto_seleccionado.nombre} que desea: '))

            if cantidad > 0:
                valor = producto_seleccionado.valorUnitario
                venta = Venta.realizarVentaBodega(producto_seleccionado, cantidad, valor)
                nueva_Factura.agregarVenta(producto_seleccionado, cantidad, venta)
                tienda.dineroEnCaja += venta
            else:
                print("La cantidad debe ser mayor que cero")
        else:
            print("El producto no existe")
        
        res = input("¿Desea comprar otro producto? (si/no) -> ").lower()  # Convierte la respuesta a minúsculas
        
    tienda.generar_factura(nueva_Factura.ventas, nueva_Factura.numfactura)
    return nueva_Factura
    
def grabarProducto(tienda):
    p = open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\productos.txt", "w")
    registro = ""
    for producto in tienda.producto:
        registro = producto.nombre+" "+str(producto.tipo)+" "+str(producto.valorUnitario)+" "+str(producto.cantidadBodega)+" "+str(producto.cantidadMinima)+" "+"\n"
        p.write(registro)
    p.close()


def manejo_productos():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MANEJO DE PRODUCTOS >>>>>>>>>>>>>
        
            1. ADICIONAR PRODUCTOS
        
            2. MOSTRAR PRODUCTOS
        
            3. HACER PEDIDOS
                
            4. GRABAR PRODUCTOS
                
            0. SALIR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    tienda.adicionarProductosTienda()
                    os.system("pause")
                    os.system("cls")
                case 2:
                    tienda.mostrarProductos()
                    os.system("pause")
                case 3:
                    tienda.hacer_pedido()
                    os.system("pause")
                case 4:
                    grabarProducto(tienda)
                case 0:
                        os.system("cls")
                        break
                case other:
                    print(Fore.RED+"la opcion que ingresaste es invalida")
                    os.system("pause")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")


def manejo_ventas():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MANEJO DE VENTAS >>>>>>>>>>>>>
        
            1. REALIZAR VENTA
        
            2. MOSTRAR FACTURA RESUMEN
        
            3. MOSTRAR FACTURAS CON DETALLE

            4. MOSTRAR TODAS LAS FACTURAS  
                
            0. SALIR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1: 
                    realizarVenta(tienda)
                    os.system("pause")
                    os.system("cls")
                case 2:
                    if tienda.factura:
                        tienda.factura[-1].mostrar_factura()
                        os.system("pause")
                    else:
                        print("No hay facturas para imprimir.")
                case 3:
                    if tienda.factura:
                        tienda.factura[-1].mostrar_facturaDetalle()
                        os.system("pause")
                    else:
                        print("No hay facturas para imprimir.")
                    
                case 4:
                    tienda.mostrar_Todas_facturas()
                    os.system("pause")
                case 0:
                    os.system("cls")
                    break

                case other:
                    print(Fore.RED+"la opcion que ingresaste es invalida")
                    os.system("pause")

        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo  ")

def manejo_estadisticas():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MANEJO DE ESTADISTICAS >>>>>>>>>>>>>
        
            1. TOTAL VENTAS
        
            2. PROMEDIO DE VENTAS
        
            3. VENTA POR PRODUCTO
                  
            4. PROMEDIO VENTA PRODUCTO
            
            5. PRODUCTO MAS VENDIDO
                
            0. SALIR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1: 
                    "TOTAL VENTAS"

                case 0:
                    os.system("cls")
                    break

                case other:
                    print(Fore.RED+"la opcion que ingresaste es invalida")
                    os.system("pause")

        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")



def menuprincipal():
    os.system("cls")
    creada = 0
    while True:
        try:
            print(Fore.GREEN+"la tienda se ha creado con exito")
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>
        
            1. MANEJO DE PRODUCTOS
        
            2. MANEJO DE VENTAS
        
            3. GENERAR ESTADISTICAS
                
            0. SALIR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1: 
                    manejo_productos()

                case 2:
                    manejo_ventas()

                case 3:
                    manejo_estadisticas()

                case 0:
                    os.system("cls")
                    break

                case other:
                    print(Fore.RED+"la opcion que ingresaste es invalida")
                    os.system("pause")

        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
menuprincipal()

