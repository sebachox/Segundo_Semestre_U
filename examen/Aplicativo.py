import pickle
import os
class Recurso:
    def __init__(self, codigo, nombre, disponible=True):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = disponible
class Usuario:
    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
class Prestamo:
    def __init__(self, recurso, usuario):
        self.recurso = recurso
        self.usuario = usuario
class CentralPrestamos:
    def __init__(self):
        self.recursos = []
        self.usuarios = []
        self.prestamos = []
    def agregar_recurso(self, codigo, nombre):
        recurso = Recurso(codigo, nombre)
        self.recursos.append(recurso)
    def agregar_usuario(self, codigo, nombre, tipo):
        usuario = Usuario(codigo, nombre, tipo)
        self.usuarios.append(usuario)
    def registrar_prestamo(self, codigo_recurso, codigo_usuario):
        recurso = self.buscar_recurso(codigo_recurso)
        usuario = self.buscar_usuario(codigo_usuario)
        if recurso and usuario:
            if recurso.disponible and self.puede_prestar(usuario):
                prestamo = Prestamo(recurso, usuario)
                self.prestamos.append(prestamo)
                recurso.disponible = False
                print(f"Préstamo exitoso. {usuario.tipo} {usuario.nombre} ha prestado {recurso.nombre}.")
            else:
                print("El recurso no está disponible para préstamo o el usuario no puede realizar más préstamos.")
        else:
            print("Recurso o usuario no encontrados.")
    def buscar_recurso(self, codigo_recurso):
        for recurso in self.recursos:
            if recurso.codigo == codigo_recurso:
                return recurso
        return None
    def buscar_usuario(self, codigo_usuario):
        for usuario in self.usuarios:
            if usuario.codigo == codigo_usuario:
                return usuario
        return None
    def puede_prestar(self, usuario):
        if usuario.tipo == 1:  # Estudiante
            return True
        elif usuario.tipo == 2:  # Docente
            return len([p for p in self.prestamos if p.usuario == usuario]) < 2
        elif usuario.tipo == 3:  # Trabajador
            return len([p for p in self.prestamos if p.usuario == usuario]) < 1
        else:
            return False  # Tipo de usuario no reconocido
    def consultar_usuario_prestamo(self, codigo_recurso):
        recurso = self.buscar_recurso(codigo_recurso)
        if recurso:
            prestamo = next((p for p in self.prestamos if p.recurso == recurso), None)
            if prestamo:
                print(f"El recurso {recurso.nombre} está prestado a {prestamo.usuario.tipo} {prestamo.usuario.nombre}.")
            else:
                print(f"El recurso {recurso.nombre} no está prestado actualmente.")
        else:
            print("Recurso no encontrado.")
    def consultar_recursos_prestados_usuario(self, codigo_usuario):
        usuario = self.buscar_usuario(codigo_usuario)
        if usuario:
            prestamos_usuario = [p.recurso.nombre for p in self.prestamos if p.usuario == usuario]
            if prestamos_usuario:
                print(f"{usuario.tipo} {usuario.nombre} tiene los siguientes recursos prestados:")
                for recurso_nombre in prestamos_usuario:
                    print(f"- {recurso_nombre}")
            else:
                print(f"{usuario.tipo} {usuario.nombre} no tiene recursos prestados actualmente.")
        else:
            print("Usuario no encontrado.")
    
    def devolver_recurso(self, codigo_recurso):
        recurso = self.buscar_recurso(codigo_recurso)
        if recurso:
            prestamo = next((p for p in self.prestamos if p.recurso == recurso), None)
            if prestamo:
                prestamo_usuario_nombre = f"{prestamo.usuario.tipo} {prestamo.usuario.nombre}"
                self.prestamos.remove(prestamo)
                recurso.disponible = True
                print(f"Devolución exitosa. {prestamo_usuario_nombre} ha devuelto {recurso.nombre}.")
            else:
                print(f"El recurso {recurso.nombre} no está prestado actualmente.")
        else:
            print("Recurso no encontrado.")
            
def mostrar_menu_principal():
    print("\n------------- Menú Principal -------------")
    print("1. Manejo de Recursos")
    print("2. Manejo de Usuarios")
    print("3. Manejo de Préstamos y Devoluciones")
    print('------------------------------------------------------')
    print("4. Salir")
def mostrar_menu_recursos():
    print("\n------------- Menú Manejo de Recursos -------------")
    print("1. Agregar Recurso")
    print("2. Consultar Recurso")
    print("3. Modificar Recurso")
    print("4. Mostrar Recursos")
    print("5. Eliminar Recurso")
    print('------------------------------------------------------')
    print("6. Salir")
def mostrar_menu_usuarios():
    print("\n------------- Menú Manejo de Usuarios -------------")
    print("1. Agregar Usuario")
    print("2. Consultar Usuario")
    print("3. Modificar Usuario")
    print("4. Eliminar Usuario")
    print("5. Mostrar Usuarios")
    print('------------------------------------------------------')
    print("6. Salir")
def mostrar_menu_prestamos():
    print("\n------------- Menú Manejo de Préstamos y Devoluciones -------------")
    print("1. Préstamo de Recurso")
    print("2. Devolución de Recurso")
    print("3. Consultar Usuario que tiene prestado un Recurso")
    print("4. Consultar Recursos prestados a un Usuario")
    print('---------------------------------------------')
    print("5. Salir")




def main():
    def crearCentral():
        archivo_path = "C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\examen\\archivoapli"
        
        try:
            valido = os.path.exists(archivo_path)
            if not valido:
                central = CentralPrestamos()
                with open(archivo_path, "wb") as f:
                    pickle.dump(central, f)
                    print(f"Archivo creado satisfactoriamente en {archivo_path}")
            else:
                with open(archivo_path, "rb") as f:
                    central = pickle.load(f)
                    print(f"Archivo cargado satisfactoriamente desde {archivo_path}")
        except Exception as e:
            print(f"Error al cargar o crear el archivo: {e}")
            # Manejar la excepción según tus necesidades
            central = CentralPrestamos()  # Otra opción, crear una instancia nueva

        return central

        return central
    central = crearCentral()
    while True:
        mostrar_menu_principal()
        try:
            opcion_principal = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            continue
        if opcion_principal == 1:
            while True:
                mostrar_menu_recursos()
                try:
                    opcion_recursos = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")
                    continue
                if opcion_recursos == 1:
                    codigo = int(input("Ingrese el código del recurso: "))
                    nombre = input("Ingrese el nombre del recurso: ")
                    central.agregar_recurso(codigo, nombre)
                    with open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\examen\\archivoapli", "wb") as f:
                        pickle.dump(central, f)
                        print("Cambios guardados en el archivo.")
                elif opcion_recursos == 2:
                    codigo = int(input("Ingrese el código del recurso a consultar: "))
                    recurso = central.buscar_recurso(codigo)
                    if recurso:
                        print(f"Recurso encontrado: {recurso.nombre}")
                    else:
                        print("Recurso no encontrado.")
                elif opcion_recursos == 3:
                    pass
                elif opcion_recursos == 4:
                    print("\nRecursos registrados:")
                    for recurso in central.recursos:
                        print(f"{recurso.codigo}: {recurso.nombre} {'(Disponible)' if recurso.disponible else '(No Disponible)'}")
                elif opcion_recursos == 5:
                    codigo = int(input("Ingrese el código del recurso a eliminar: "))
                    pass
                elif opcion_recursos == 6:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
                

        elif opcion_principal == 2:
            while True:
                mostrar_menu_usuarios()
                try:
                    opcion_usuarios = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")
                    continue
                if opcion_usuarios == 1:
                    codigo = int(input("Ingrese el código del usuario: "))
                    nombre = input("Ingrese el nombre del usuario: ")
                    tipo = int(input("Ingrese el tipo de usuario (1: Estudiante, 2: Docente, 3: Trabajador): "))
                    central.agregar_usuario(codigo, nombre, tipo)
                    with open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\examen\\archivoapli", "wb") as f:
                        pickle.dump(central, f)
                        print("Cambios guardados en el archivo.")
                elif opcion_usuarios == 2:
                    codigo = int(input("Ingrese el código del usuario a consultar: "))
                    usuario = central.buscar_usuario(codigo)
                    if usuario:
                        print(f"Usuario encontrado: {usuario.tipo} {usuario.nombre}")
                    else:
                        print("Usuario no encontrado.")
                elif opcion_usuarios == 3:
                    pass
                elif opcion_usuarios == 4:
                    codigo = int(input("Ingrese el código del usuario a eliminar: "))
                    pass
                elif opcion_usuarios == 5:
                    print("\nUsuarios registrados:")
                    for usuario in central.usuarios:
                        print(f"{usuario.codigo}: {usuario.nombre} (Tipo {usuario.tipo})")
                elif opcion_usuarios == 6:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion_principal == 3:
            while True:
                mostrar_menu_prestamos()
                
                try:
                    opcion_prestamos = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")
                    continue
                if opcion_prestamos == 1:
                    codigo_recurso = int(input("Ingrese el código del recurso a prestar: "))
                    codigo_usuario = int(input("Ingrese el código del usuario que realizará el préstamo: "))
                    central.registrar_prestamo(codigo_recurso, codigo_usuario)
                elif opcion_prestamos == 2:
                    codigo_recurso = int(input("Ingrese el código del recurso a devolver: "))
                    central.devolver_recurso(codigo_recurso)
                
                elif opcion_prestamos == 3:
                    codigo_recurso = int(input("Ingrese el código del recurso a consultar: "))
                    central.consultar_usuario_prestamo(codigo_recurso)
                elif opcion_prestamos == 4:
                    codigo_usuario = int(input("Ingrese el código del usuario a consultar: "))
                    central.consultar_recursos_prestados_usuario(codigo_usuario)
                elif opcion_prestamos == 5:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion_principal == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
