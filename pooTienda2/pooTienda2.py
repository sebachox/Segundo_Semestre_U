import os
from Tienda import *
from Producto import *
from Factura import *
from Venta import *



def crearTienda():
    tienda=Tienda([],[])
    tienda.adicionarProductosTienda()
    return tienda

def consultarVentaProducto(tienda):
    tienda.mostrarProductos()
    producto=input('Digitar producto -> ')
    productoal=tienda.consultarProducto(producto)
    if productoal!=None:
        tienda.consultarDetalleVentasProducto(producto)
    else:
        print('Producto no existe')

def consultarVentas(tienda):
    print('Ventas productos tienda ')
    tienda.consultarVentas()
    print(f'\nValor todal ventas: {tienda.dineroEnCaja}')
    
def consultarVentasTotales(tienda):
    tienda.consultarVentas()
    print(f'Valor todal ventas: {tienda.dineroEnCaja}')
    os.system('pause')
    
def realizarTodosLosPedido(tienda):
    listaPedidos=tienda.productosPedido()
    for prod in listaPedidos:
        print(prod)
        while True:
            cantidadPedida=leerInt('Digitar cantidad pedida ->')
            if cantidadPedida>0:
                prod.cantidadBodega+=cantidadPedida
                break
            else:
                print('cantidad no es válida ')
    tienda.mostrarProductos()
    
               
def realizarPedidoPorProductos(tienda):
    tienda.mostrarProductos()
    producto=input('Digitar producto -> ')
    productoal=tienda.consultarProducto(producto)
    if productoal!=None:
        tienda.mostrarProducto(producto)
        
        while True:
            cantidad=leerInt('digitar cantidad pedida ->')
            if cantidad>0:
                productoal.cantidadBodega+=cantidad
                break
               
            else:
                print('cantidad no valida ')
        print(productoal)
            
        if productoal.cantidadBodega>cantidad:
            cantidadv=cantidad
        elif productoal.cantidadBodega>0:
            cantidadv=productoal.cantidadBodega
        else:
            print('No hay productos a la venta ')
            return 
    
def mostrarFactura(tienda):
    tienda.mostrarFacturasResumen()
    numfactura=leerInt('Número de factura -> ')
    factura=tienda.consultarFacturaNumero(numfactura)
    factura.mostrarFacturaDetalle()
    
def manejoVentas(tienda):
    while True:
        print ('Manejo Ventas')
        print('------------------------------')
        print('1. Realizar venta ')
        print('2. Mostrar Facturas Resumen')
        print('3. Mostrar Facturas con detalle ')
        print('4. Mostrar factura detalle ')
        print('5. Mostrar venta por producto ')
        print('6. Regresar menu principal ')
        print('------------------------------ ')
        
        opcion=leerInt('Opcion --> ')
        match opcion:
            case 1:
                tienda.realizarVenta2()
                os.system('pause')
                
            case 2:
                tienda.mostrarFacturasResumen()
                os.system('pause')
                
            case 3:
                tienda.mostrarFacturasDetalle()
                os.system('pause')
            case 4:
                mostrarFactura(tienda)
                os.system('pause')
            
            case 5:
                consultarVentaProducto(tienda)
                os.system('pause')
            
            case 6:
                break
            case other:
                print('error opcion invalida ')
                        

def manejoPedidos(tienda):
    while True:
        print ('Manejo Pedidos')
        print('------------------------------')
        print('1. Pedido por producto ')
        print('2. Realizar todos los pedidos ')
        print('3. Regresar menú principal ')
        print('------------------------------ ')
        
        opcion=leerInt('Opcion --> ')
        match opcion:
            case 1:
                realizarPedidoPorProductos(tienda)
                os.system('pause')
                
            case 2:
                realizarTodosLosPedido(tienda)
                os.system('pause')
            
            case 3:
                break
            case other:
                print('error opcion invalida ')
                        



def menuPrincipal():
     creada=False
     while True:
        print ('Menu Tienda')
        print('------------------------------')
        print('1. Crear tienda con productos ')
        print('2. Mostrar tienda')
        print('3. Manejo de ventas ')
        print('4. Manejo de pedidos ')
        print('5. Manejo de Estadísticas ')
        
        print('6. Salir ')
        print('------------------------------ ')
        
        opcion=leerInt('Opcion --> ')
        match opcion:
            case 1:
                if not creada:
                    tienda=crearTienda()
                    creada=True
                else:
                    print('Ya hay productos en la tienda')
                os.system('pause')
            case 2:
                if creada:
                    print('tienda uno')
                    tienda.mostrarProductos()
                
                else:
                    print('no se ha creado tienda. ejecutar opcion 1')
                os.system('pause')
            case 3:
                if creada:
                    manejoVentas(tienda)
                
                else:
                    print('no se ha creado tienda. ejecutar opcion 1')
                os.system('pause')
                
            case 4:
                if creada:
                    manejoPedidos(tienda)
                
                else:
                    print('no se ha creado tienda. ejecutar opcion 1')
                os.system('pause')
                
            case 5:
                manejoEstadisticas(tienda)
                os.system('pause')
            
            case 6:
                break
            case other:
                print('error opcion invalida ')

def manejoEstadisticas(tienda):
     while True:
        print ('Menu Estadísticas')
        print('------------------------------')
        print('1. Total ventas ')
        print('2. Promedio de ventas')
        print('3. Venta por Producto ')
        print('4. promedio venta producto')
        print('5. Producto más vendido ')
        
        print('6. Salir ')
        print('------------------------------ ')
        
        opcion=leerInt('Opcion --> ')
        match opcion:
            case 1:
                tienda.totalVentaProductos()
                os.system('pause')
            
            case 2:
                tienda.promedioVentas()
                os.system('pause')
                
            case 3:
                consultarVentaProducto(tienda)
                os.system('pause')
            case 4:
                tienda.promedioVentasProducto()
                os.system('pause')
            
            case 5:
                tienda.productoMasVendido()
                os.system('pause')
            case 6:
                
                break
            case other:
                print('error opcion invalida ')
                                
def main():
    menuPrincipal()
    
    
if __name__ == '__main__':
    main()

