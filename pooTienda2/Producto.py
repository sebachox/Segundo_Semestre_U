class Producto:
    def __init__(self,nombre,tipo,valorUnitario,cantidadBodega,cantidadMinima,cantidadVendida):
        self.nombre=nombre
        self.tipo=tipo
        self.valorUnitario=valorUnitario
        self.cantidadBodega=cantidadBodega
        self.cantidadMinima=cantidadMinima
                
    def __str__(self):
        return (f'Nombre: {self.nombre} Valor: {self.valorUnitario} Tipo: {self.tipo} Cantidad: {self.cantidadBodega}')
    
       
    