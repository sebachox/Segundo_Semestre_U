from Persona import*
class Recepcionista(Persona):
    def __init__(self, nombre, apellido, telefono, documento,clave):
        super().__init__(nombre, apellido, telefono, documento)
        self.clave = clave
    def __str__(self):
            return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} - Documento: {self.documento}'