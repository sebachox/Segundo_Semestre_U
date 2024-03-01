
class Producto:
    def __init__(self, nom, tipo, valunitario, cantB, cantM, ):
        self.nombre = nom
        self.tipo = tipo
        self.valorUnitario = valunitario
        self.cantidadBodega = cantB
        self.cantidadMinima = cantM
        
    
    def __str__(self):
        return (f" nombre : {self.nombre}\n tipo : {self.tipo}\n valor unitario : {self.valorUnitario}\n cantidad en bodega : {self.cantidadBodega}\n")
    
    
