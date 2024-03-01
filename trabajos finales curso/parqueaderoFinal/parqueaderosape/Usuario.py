from Persona import Persona

class Usuario(Persona):
    def __init__(self, nombres, apellidos, telefono, documento):
        Persona.__init__(self,nombres, apellidos, telefono, documento)
        self.listavehiculos=[]
        
    def __str__(self):
        return f'Nombre: {self.nombre}  \nApellido: {self.apellido} \nTelefono: {self.telefono} \nDocumento: {self.documento}'
    
    def MostrarVehiculos(self):
        print('Vehiculos del usuario:')
        for vehiculo in self.listavehiculos:
            if vehiculo.tipoVehiculo==1:
                print(f'-Vehiculo: {vehiculo.placa} - tipo: moto ')
            if vehiculo.tipoVehiculo==2:
                print(f'-Vehiculo: {vehiculo.placa} - tipo: carro ')
            if vehiculo.tipoVehiculo==3:
                print(f'-Vehiculo: {vehiculo.placa} - tipo: vehiculo pesado ')
        
    def consultarUsuario(self):
        identificacion = int(input('Ingrese identificacion del usuario a consultar: '))
        encontrado=False
        for usuario in self.listausuarios:
            if identificacion == usuario.documento:
                print(str(usuario))
                usuario.MostrarVehiculos()
                encontrado=True
                break
        if not encontrado:
            print('Usuario no encontrado')
    
    def modificarUsuario(self):
        identificacion = int(input('Ingrese identificacion del usuario a modificar: '))
        encontrado=False
        for usuario in self.listausuarios:
            if identificacion == usuario.documento:
                encontrado=True
                mod= int(input(f'Ingrese que dato quiere modificar\n 1: Nombre\n 2: Apellido\n 3: Telefono\n 4: Documento\n 5: Placa\n '))
                if mod == 1:
                    nombre = input('Ingrese nuevo nombre: ')
                    usuario.nombre = nombre
                if mod ==2:
                    apellido = input('Ingrese nuevo apellido: ')
                    usuario.apellido = apellido
                if mod == 3:
                    telefono = int(input('Ingrese nuevo telefono: '))
                    usuario.telefono = telefono
                if mod == 4:
                    documento = int(input('Ingrese nuevo documento: '))
                    usuario.documento = documento
                if mod == 5:
                    p = input('Ingrese la placa que quiere modificar: ')
                    for vehiculo in usuario.listavehiculos:
                        if p == vehiculo.placa:
                            placa = input('Ingrese nueva placa: ')
                            vehiculo.placa = placa
                            break
                    else:
                        print('Numero de placa no encontrada')
                break
        if not encontrado:
            print('Usuario no encontrado')

    def AgregarVehiculo(self,vehiculo):
        self.listavehiculos.append(vehiculo)
            