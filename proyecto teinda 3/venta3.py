from factura3 import Factura
from tienda3 import Tienda
class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def __str__(self):
        return f"nombre : {self.producto.nombre}\n valor venta : {self.producto.valorUnitario*self.cantidad}"
    
    def realizarVentaBodega(producto, cantidad, valor):
        if producto.cantidadBodega >= cantidad:
            producto.cantidadBodega -= cantidad 
            venta = valor * cantidad
            return venta
            
        else:
            print("No hay suficioende producto en la tienda")
            return 0
        
    