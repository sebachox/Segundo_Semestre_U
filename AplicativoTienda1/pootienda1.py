#programa principal 
import os
from colorama  import init,Fore
from producto1 import Producto
from tienda1 import Tienda

def main():
    init()
    def crearTienda():
        p1 = Producto("lapiz", 1, 2000, 50, 0, 0)
        p2 = Producto("cuaderno", 1, 2000, 50, 0, 0)
        p3 = Producto("aspirina", 1, 2000, 50, 0, 0)
        p4 = Producto("arroz", 1, 2000, 50, 0, 0)
        tienda = Tienda(p1,p2,p3,p4)
        return tienda 
    

    def realizarVenta(tienda):
        tienda = crearTienda()
        tienda.mostrarProductos()
        producto = input("Producto a vender: ")
        producto_seleccionado = tienda.consultarProducto(producto.lower())
        if producto_seleccionado.nombre == producto.lower():
            tienda.mostrarProductos()
            cantidad=int(input(f'Digite la cantidad de {producto_seleccionado.nombre} que desea: '))
            if cantidad>0:
                valor = int(tienda.valor_unitario(producto_seleccionado))
                venta = tienda.realizarVenta(producto_seleccionado, cantidad, valor)
                if venta>0:
                    tienda.dinero_en_caja += venta
                    print("Venta realizada. Su valor a cancelar es: ",venta," El costo por unidad incluido el iva fue de: ",valor)
                else:
                    print("No se realizo la venta")
            else:
                print("La cantidad debe ser mayor que cero")
        else:
            print("El producto no existe")


    def menu_ventas():
        os.system("cls")
        while True:
            try:
                print(Fore.GREEN+"""
    <<<<<<<<<<<<< MENU VENTAS >>>>>>>>>>>>>
                    
                1. realizar venta
                    
                2. mostrar ventas  
                    
                3. venta por producto

                4. estadisticas

                0. SALIR
    """)
                opcion = int(input("ingrese la opcion que desse : -> "))
                tienda = crearTienda()
                match opcion:
                    case 1:
                        realizarVenta(tienda)
                        os.system("pause")
                    case 2:
                        tienda.mostrarProductos()
                        os.system("pause")
                    case 3:
                        menu_pedidos()
                        os.system("pause")
                    case 4:
                        menu_estadisticas()
                        os.system("pause")
                    case 0:
                        break
                    case other:
                        print(Fore.RED+"la opcion que ingresaste es invalida")
                        os.system("pause")
            except ValueError:
                print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
        
    def menu_pedidos():
        os.system("cls")
        while True:
            try:
                print(Fore.GREEN+"""
    <<<<<<<<<<<<< MENU PEDIDOS >>>>>>>>>>>>>
                    
                1. mostrar  pedido
                    
                2. determinar pedido  
                    
                3. realizar pedido 

                0. SALIR
    """)
                opcion = int(input("ingrese la opcion que desse : -> "))
                tienda = crearTienda()
                match opcion:
                    case 1:
                        tienda.mostrarProductos()
                        os.system("pause")
                    case 2:
                        menu_ventas()
                        os.system("pause")
                    case 3:
                        menu_pedidos()
                        os.system("pause")
                    case 0:
                        break
                    case other:
                        print(Fore.RED+"la opcion que ingresaste es invalida")
                        os.system("pause")
            except ValueError:
                print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
    
    def menu_estadisticas():
        os.system("cls")
        while True:
            try:
                print(Fore.GREEN+"""
    <<<<<<<<<<<<< MENU ESTADISTICAS >>>>>>>>>>>>>
                    
                1. ventas totales
                    
                2. venta por producto  
                    
                3. promedio de vetas

                4. producto mas vendido

                0. SALIR
    """)
                opcion = int(input("ingrese la opcion que desse : -> "))
                tienda = crearTienda()
                match opcion:
                    case 1:
                        tienda.totalVentaTienda()
                        os.system("pause")
                    # case 2:
                    #     tienda.
                    #     os.system("pause")
                    case 3:
                        tienda.promedioVentas()
                        os.system("pause")
                    case 4:
                        tienda.productoMasVendido()
                        os.system("pause")
                    case 0:
                        break
                    case other:
                        print(Fore.RED+"la opcion que ingresaste es invalida")
                        os.system("pause")
            except ValueError:
                print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")

    def menu_principal():
        os.system("cls")
        creada = 0 
        while True:
            try:
                print(Fore.GREEN+"""
    <<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>

                1. crear tienda
                
                2. mostrar productos 
            
                3. realizar ventas  
                    
                4. realizar pedidos

                5. estadisticas 

                0. SALIR
    """)
                opcion = int(input("ingrese la opcion que desse : -> "))
                match opcion:
                    case 1: 
                        if not creada:
                            tienda=crearTienda()
                            creada=True
                            print("la tienda ha sido creada con exito :)")
                        else:
                            print("ya hay productos en la tienda")
                            os.system("pause")
                    case 2:
                        if creada==True:
                            tienda.mostrarProductos()
                        else:
                            print("No hay productos")
                            os.system("pause")
                    case 3:
                        menu_ventas()
                        os.system("pause")
                    case 4:
                        menu_pedidos()
                        os.system("pause")
                    case 5:
                        menu_estadisticas()
                        os.system("pause")
                    case 0:
                        break
                    case other:
                        print(Fore.RED+"la opcion que ingresaste es invalida")
                        os.system("pause")
            except ValueError:
                print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
    menu_principal()
main()







