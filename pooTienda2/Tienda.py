from Producto import *
from Venta import *
from Factura import *
from Leer import leer 
import os

class Tienda:
    numeroFactura=0
    dineroEnCaja=0
    def __init__(self,productos,facturas):
       self.productos=productos
       self.facturas=facturas
              

    def adicionarProductosTienda(self):
        self.productos.append(Producto('lapiz',1,2000,50,5,0))
        self.productos.append(Producto('cuaderno',1,4000,50,5,0))
        self.productos.append(Producto('aspirina',2,4000,50,5,0))
        self.productos.append(Producto('arroz',3,5000,20,5,0))
        self.productos.append(Producto('papa',3,4000,50,5,0))
        print('Se ha creado una tienda con 5 productos ')
    
    
    def mostrarProductos(self):
        if len(self.productos)>0:
            for prod in self.productos:
                print (prod)
        else:
            print('no hay productos en la tienda')
         
        
    def consultarProducto(self,producto):
        for prod in self.productos:
            if prod.nombre==producto:
                return prod
        return None
    
        
    def mostrarProducto(self,producto):
        for prod in self.productos:
            if prod.nombre==producto:
                print(prod)
               
    def llenarProducto(self,producto):
        self.productos.append(producto)    
    
        
    def realizarVenta(self):
        #obtener numero factura
        numeroFactura=Tienda.numeroFactura+1
        #crear objeto factura
        factura=Factura(numeroFactura)
        #realizar ciclo para llenar ventas
        while True:
            #mostrar productos
            self.mostrarProductos()
            #obtener producto  
            producto=input('Digitar producto -> ')
            #validar producto
            productoal=self.consultarProducto(producto)
            if productoal!=None:
                #mostrar información producto
                print(productoal)
                #self.mostrarProducto(producto)
                #determinar cantidad
                cantidad=leerInt('digitar cantidad ->')
                #validar cantidad
                if productoal.cantidadBodega>cantidad:
                    cantidadv=cantidad
                elif productoal.cantidadBodega>0:
                    cantidadv=productoal.cantidadBodega
                else:
                    print('No hay productos a la venta ')
                    continue 
                #con información válida se genera la venta
                valorVenta=productoal.valorUnitario*cantidadv
                print('Detalles venta \n ----------------------')
                print(f'Cantidad {cantidadv} \nValor unitario {productoal.valorUnitario} \nTotal venta = {valorVenta}')
                #actualiza dinero en caja de la tienda
                Tienda.dineroEnCaja=Tienda.dineroEnCaja + valorVenta
                #genera objeto venta para llenar en factura
                venta=Venta(productoal,cantidad)
                #adiciona venta a factura
                factura.ventas.append(venta)
                #lleva el valor de la factura
                factura.valorFactura+=valorVenta
                #disminuye la cantidad de productos vendidos
                productoal.cantidadBodega-=cantidadv
                resp=leerCadena('Adicionar más productos? (s/n) ->')
                if resp=='N' or resp=='n':
                    #si no hay más productos se adiciona la venta a la factura
                    self.facturas.append(factura)
                    #muestra el el detalle de la factura
                    factura.mostrarFacturaDetalle()
                    #actualiza el número de factura
                    Tienda.numeroFactura+=1
                    break
            else:
                print('producto {producto} no existe')
                
        
    def realizarVenta2(self):
        #mostrar productos
        numeroFactura=Tienda.numeroFactura+1
        #crear objeto factura
        factura=Factura(numeroFactura)
        #realizar ciclo para llenar productos
        while True:
            b1=0
            #mostrar productos
            self.mostrarProductos()
            #obtener producto  
            producto=input('Digitar producto -> ')
            #validar producto
            productoal=self.consultarProducto(producto)
            if productoal!=None:
                ventafactura,indice=factura.buscarProductoFactura(producto)
                if ventafactura!=None:
                    #actualizar cantidad de producto que ya está en la factura
                    print(f'producto {producto} ya está en la factura \n')
                    print(ventafactura)
                    
                    respv=leerCadena('Adicionar más cantidad s/n')
                    if respv=='S' or respv=='s':
                        print(ventafactura.producto)
                        while True:
                            cantidadventa=leerInt('digitar cantidad ->')
                            if cantidadventa>0 and cantidadventa<=ventafactura.producto.cantidadBodega:
                                #ventafactura.cantidad+=cantidadventa
                                cantidadv=ventafactura.cantidad+cantidadventa
                                ventafactura.producto.cantidadBodega+=ventafactura.cantidad
                                factura.valorFactura-=ventafactura.cantidad*ventafactura.producto.valorUnitario
                                Tienda.dineroEnCaja-=ventafactura.cantidad*ventafactura.producto.valorUnitario
                                factura.eliminarProductoFactura(indice)
                                break
                            else:
                                print('cantidad invalida')
                    else:
                        b1=1
                else:    
                    #mostrar información producto
                    print(productoal)
                    #self.mostrarProducto(producto)
                    #determinar cantidad
                    cantidad=leerInt('digitar cantidad ->')
                    #validar cantidad
                    if productoal.cantidadBodega>cantidad:
                        cantidadv=cantidad
                    elif productoal.cantidadBodega>0:
                        cantidadv=productoal.cantidadBodega
                    else:
                        print('No hay productos a la venta ')
                        continue 
                    #con información válida se genera la venta
                if b1==0:
                    valorVenta=productoal.valorUnitario*cantidadv
                    print('Detalles venta \n ----------------------')
                    print(f'Cantidad {cantidadv} \nValor unitario {productoal.valorUnitario} \nTotal venta = {valorVenta}')
                    #actualiza dinero en caja de la tienda
                    Tienda.dineroEnCaja=Tienda.dineroEnCaja + valorVenta
                    #genera objeto venta para llenar en factura
                    venta=Venta(productoal,cantidadv)
                    #adiciona venta a factura
                    factura.ventas.append(venta)
                    #lleva el valor de la factura
                    factura.valorFactura+=valorVenta
                    #disminuye la cantidad de productos vendidos
                    productoal.cantidadBodega-=cantidadv
            resp=leerCadena('Adicionar más productos? (s/n) ->')
            if (resp=='N' or resp=='n'):
                #si no hay más productos se adiciona la factura a las facturas
                self.facturas.append(factura)
                #muestra el el detalle de la factura
                factura.mostrarFacturaDetalle()
                #actualiza el número de factura
                Tienda.numeroFactura+=1
                break
            else:
                print('producto {producto} no existe')
    
    def mostrarFacturasDetalle(self):
        #muestra el detalle de todas las facturas de la tienda
        if len(self.facturas)>0:
            print ('Facturas tienda xx')
            print('---------------------')
            for factura in self.facturas:
                print('------------------------')
                factura.mostrarFacturaDetalle()
        else:
            print('No se han realizado ventas')        
        
    def mostrarFacturasResumen(self):
        #muestra un resumen de las facturas
        if len(self.facturas)>0:
            print ('Facturas tienda xx')
            print('---------------------')
            for factura in self.facturas:
                factura.mostrarFacturaResumen()
                print('------------------------')
        else:
            print('No se han realizado ventas')        
    
    def consultarFacturaNumero(self,numfactura):
        for factura in self.facturas:
            if factura.numeroFactura==numfactura:
                return factura
        return None
    
    def consultarDetalleVentasProducto(self,producto):
        ventaProducto=0
        cantidadVendida=0
        for factura in self.facturas:
            for venta in factura.ventas:
                if venta.producto.nombre==producto:
                    print(f'Numero factura {factura.numeroFactura}')
                    print(venta)
                    ventaProducto+=venta.producto.valorUnitario*venta.cantidad
                    cantidadVendida+=venta.cantidad
        print(f'Cantidad vendida: {cantidadVendida}  Valor venta: {ventaProducto} ')
        return cantidadVendida,ventaProducto 
    
    def totalVentaProductos(self):
        totalVentas=0
        valorTotal=0
        print('---------------------------------')
        for prod in self.productos:
            if self.consultarProductoEnVentas(prod.nombre):
                cantidad,venta=self.consultarVentaProducto(prod.nombre)
                totalVentas+=cantidad
                valorTotal+=venta
                print(f'Producto {prod.nombre} cantidad vendida {cantidad} Valor venta {venta}')
        print('---------------------------------')
        print(f'Total ventas {totalVentas} valor total {valorTotal}')    
    
    def consultarVentaProducto(self,producto):
        ventaProducto=0
        cantidadVendida=0
        for factura in self.facturas:
            for venta in factura.ventas:
                if venta.producto.nombre==producto:
                    ventaProducto+=venta.producto.valorUnitario*venta.cantidad
                    cantidadVendida+=venta.cantidad
        return cantidadVendida,ventaProducto 
    
    
    def consultarProductoEnVentas(self,producto):
        for factura in self.facturas:
            for venta in factura.ventas:
                if venta.producto.nombre==producto:
                    return True
        return False 
    
    def productoMasVendido(self):
        canmay=0
        for prod in self.productos:
            if self.consultarProductoEnVentas(prod.nombre):
                cantidad,venta=self.consultarVentaProducto(prod.nombre)
                if cantidad>canmay:
                    canmay=cantidad
                    prodmay=prod.nombre
        print(f'Producto mas vendido {prodmay} cantidad {canmay}')
        
    def promedioVentas(self):
        cantidadProductos=0
        sumaVentas=0
        for prod in self.productos:
            cantidad,venta=self.consultarVentaProducto(prod.nombre)
            cantidadProductos+=cantidad
            sumaVentas+=venta
            
        if cantidadProductos>0:
            promedio=Tienda.dineroEnCaja/cantidadProductos
            print(f'Total valor ventas {Tienda.dineroEnCaja}')
            print(f'Total cantidad de productos vendidos -> {cantidadProductos}')
            print(f'Promedio ventas -> {promedio}')
        else:
            print('no hay ventas')
        
    def promedioVentasProducto(self):
        self.mostrarProductos()
        while True:
            producto=leerCadena('DigitarProducto')
            productosel=self.consultarProducto(producto)
            if productosel!=None:
                cantidad,venta=self.consultarVentaProducto(producto)
                promedio=venta/cantidad
                print(f'promedio venta producto {producto} =  {promedio}')
                break
            else:
                print('Producto {producto} no existe')
                
    
                            
    def realizarPedido(self,producto,pedido):            
        if self.producto1.nombre==producto:
            self.producto1.cantidadBodega=self.producto1.cantidadBodega+pedido
        elif self.producto2.nombre==producto:
            self.producto2.cantidadBodega=self.producto1.cantidadBodega+pedido
        elif self.producto3.nombre==producto:
            self.producto3.cantidadBodega=self.producto1.cantidadBodega+pedido
        elif self.producto4.nombre==producto:
            self.producto4.cantidadBodega=self.producto1.cantidadBodega+pedido
        
    def productosPedido(self):
        listaPedidos=[]
        if self.producto1.cantidadBodega<self.producto1.cantidadMinima:
            print(self.producto1)
            listaPedidos.append(self.producto1)
        if self.producto2.cantidadBodega<self.producto2.cantidadMinima:
            print(self.producto2)
            listaPedidos.append(self.producto2)
        if self.producto3.cantidadBodega<self.producto3.cantidadMinima:
            print(self.producto4)
            listaPedidos.append(self.producto3)
        if self.producto4.cantidadBodega<self.producto4.cantidadMinima:
            print(self.producto4)
            listaPedidos.append(self.producto4)
        return listaPedidos