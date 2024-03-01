#clases
from producto1 import Producto
class Tienda:
    dineroEnCaja = 0
    def __init__(self, p1, p2, p3, p4):
        self.producto1 = p1
        self.producto2 = p2
        self.producto3 = p3
        self.producto4 = p4

    def mostrarProductos(self):
        print(self.producto1 ,"\n")
        print(self.producto2 ,"\n")
        print(self.producto3 ,"\n")
        print(self.producto4 ,"\n")

    def consultarProducto(self, producto):
        if self.producto1.nombre == producto:
            return self.producto1
        elif self.producto2.nombre == producto:
            return self.producto2
        elif self.producto3.nombre == producto:
            return self.producto3
        elif self.producto4.nombre == producto:
            return self.producto4
        else:
            return None
    def mostrarProductounico(self, producto):
        if self.producto1.nombre == producto:
            print(self.producto1)
        elif self.producto2.nombre == producto:
            print(self.producto1)
        elif self.producto3.nombre == producto:
            print(self.producto1)
        elif self.producto4.nombre == producto:
            print(self.producto1)
        else:
            return None

    def realizarVenta(self,producto, cantidad, valor):
        if producto.cantidadBodega >= cantidad:
            producto.cantidadBodega -= cantidad 
            producto.cantidadVendida += cantidad
            venta = valor * cantidad
            return venta
        else:
            print("No hay suficioende producto en la tienda")
            return 0
    
    def productoMasVendido(self):
        productos = [self.producto1, self.producto2, self.producto3, self.producto4]
        mas_vendido = max(productos, key=lambda p: p.cantidadVendida)
        return f"el producto mas vendido es {mas_vendido}"

    def promedioVentas(self):
        total_ventas = self.totalVentaTienda()
        cantidad_productos = 4  
        if cantidad_productos > 0:
            promedio = total_ventas / cantidad_productos
            return f"el promedio de ventas es {promedio}"
        else:
            print("No hay productos en la tienda para calcular el promedio de ventas.")
            return 0

    def totalVentaTienda(self):
        total = 0
        total += self.realizarVenta(self.producto1, self.producto1.cantidadVendida, self.producto1.valorUnitario)
        total += self.realizarVenta(self.producto2, self.producto2.cantidadVendida, self.producto2.valorUnitario)
        total += self.realizarVenta(self.producto3, self.producto3.cantidadVendida, self.producto3.valorUnitario)
        total += self.realizarVenta(self.producto4, self.producto4.cantidadVendida, self.producto4.valorUnitario)
        return f"el total de ventas realizadas es de {total}"
    
    def valor_unitario(self,producto):
        if producto==self.producto1.nombre:
            valor=self.producto1.valorUnitario
            valor_cobrar=valor+self.producto1.valorUnitario
            return valor_cobrar
        elif producto==self.producto2.nombre:
            valor=self.producto2.valor_unitario
            valor_cobrar=valor+self.producto2.valorUnitario
            return valor_cobrar
        elif producto==self.producto3.nombre:
            valor=self.producto3.valorUnitario
            valor_cobrar=valor+self.producto3.valorUnitario
            return valor_cobrar
        elif producto==self.producto4.nombre:
            valor=self.producto4.valor_unitario
            valor_cobrar=valor+self.producto4.valorUnitario
            return valor_cobrar


    
    
