class Venta:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad
        
    def __str__(self):
        return (f'Producto {self.producto.nombre} cantidad {self.cantidad} valor {self.producto.valorUnitario*self.cantidad}')
    
    def mostrarVenta(self):
        print(f'Producto {self.producto.nombre} cantidad {self.cantidad} valor {self.producto.valorUnitario*self.cantidad}')