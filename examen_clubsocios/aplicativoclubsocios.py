import pickle

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class Socio(Persona):
    def __init__(self, nombre, cedula, categoria):
        super().__init__(nombre, cedula)
        self.categoria = categoria

class SocioPlatino(Socio):
    def __init__(self, nombre, cedula, limite_autorizados=float('inf')):
        super().__init__(nombre, cedula, 'Platino')
        self.descuento = 0.15
        self.limite_autorizados = limite_autorizados
        self.autorizados = []

    def adicionar_autorizado(self, autorizado):
        if not isinstance(autorizado, Autorizado):
            raise ValueError("El objeto no es una instancia de Autorizado.")
        
        if len(self.autorizados) < self.limite_autorizados:
            self.autorizados.append(autorizado)
        else:
            raise ValueError("Se alcanzó el límite de personas autorizadas.")

class SocioOro(Socio):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula, 'Oro')
        self.descuento = 0.10
        self.limite_autorizados = 10
        self.autorizados = []

    def adicionar_autorizado(self, autorizado):
        if not isinstance(autorizado, Autorizado):
            raise ValueError("El objeto no es una instancia de Autorizado.")
        
        if len(self.autorizados) < self.limite_autorizados:
            self.autorizados.append(autorizado)
        else:
            raise ValueError("Se alcanzó el límite de personas autorizadas.")

class SocioPlata(Socio):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula, 'Plata')
        self.descuento = 0.05
        self.limite_autorizados = 5
        self.autorizados = []

    def adicionar_autorizado(self, autorizado):
        if not isinstance(autorizado, Autorizado):
            raise ValueError("El objeto no es una instancia de Autorizado.")
        
        if len(self.autorizados) < self.limite_autorizados:
            self.autorizados.append(autorizado)
        else:
            raise ValueError("Se alcanzó el límite de personas autorizadas.")

class Autorizado(Persona):
    def __init__(self, nombre, cedula, socio_autorizante=None):
        super().__init__(nombre, cedula)
        self.socio_autorizante = socio_autorizante

class Factura:
    def __init__(self, concepto, valor, cedula):
        self.concepto = concepto
        self.valor = valor
        self.cedula = cedula

class Club:
    def __init__(self):
        self.socios = []
        self.autorizados = []
        self.facturas = []

    def mostrar_menu_principal(self):
        print("\n----- Menú Principal -----")
        print("1. Gestionar Socios")
        print("2. Gestionar Autorizados")
        print("3. Menu Consumos")
        print("4. Menu Informe")
        print("5. Salir")

    def gestionar_socios(self):
        print("\n----- Menú Gestionar Socios -----")
        print("1. Agregar Socio")
        print("2. Listar Socios")
        print("3. Eliminar Socio")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.agregar_socio()
        elif opcion == "2":
            self.listar_socios()
        elif opcion == "3":
            self.eliminar_socio()
        elif opcion == "4":
            return
        else:
            print("Opción no válida. Intente de nuevo.")
        self.gestionar_socios()

    def menu_consumos(self):
        print("\n----- Menú Consumos -----")
        print("1. Registrar Consumo")
        print("2. Cancelar Factura")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.registrar_consumo()
        elif opcion == "2":
            self.cancelar_factura()
        elif opcion == "3":
            return
        else:
            print("Opción no válida. Intente de nuevo.")
        self.menu_consumos()

    def ejecutar(self):
        # Cargar registros al inicio
        self.cargar_registros()

        while True:
            self.mostrar_menu_principal()
            opcion_principal = input("Seleccione una opción: ")

            if opcion_principal == "1":
                self.gestionar_socios()
            elif opcion_principal == "2":
                self.gestionar_autorizados()
            elif opcion_principal == "3":
                self.menu_consumos()
            elif opcion_principal == "4":
                self.menu_informe()
            elif opcion_principal == "5":
                self.guardar_registros()
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


    def agregar_socio(self):
        nombre = input("Ingrese el nombre del socio: ")
        cedula = input("Ingrese la cédula del socio: ")
        categoria = input("Ingrese la categoría del socio (Platino, Oro, Plata): ")

        try:
            if categoria.lower() == 'platino':
                print("limite de personas a autorizar : ilimitado por defecto")
                socio = SocioPlatino(nombre, cedula)
            elif categoria.lower() == 'oro':
                print("limite de personas a autorizar : 10 personas")
                socio = SocioOro(nombre, cedula)
            elif categoria.lower() == 'plata':
                print("limite de personas a autorizar : 5 personas")
                socio = SocioPlata(nombre, cedula)
            else:
                print("Categoría no válida.")
                return

            self.socios.append(socio)
            print(f"Socio {categoria} agregado correctamente.")
            self.guardar_registros()
        except ValueError as e:
            print(f"Error al agregar socio: {e}")

    def listar_socios(self):
        print("\n----- Lista de Socios -----")
        for socio in self.socios:
            print(f"{socio.nombre} - Cédula: {socio.cedula} - Categoría: {socio.categoria}")

    def gestionar_autorizados(self):
        print("\n----- Menú Gestionar Autorizados -----")
        print("1. Agregar Autorizado")
        print("2. Listar Autorizados")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.agregar_autorizado()
        elif opcion == "2":
            self.listar_autorizados()
        elif opcion == "3":
            return
        else:
            print("Opción no válida. Intente de nuevo.")
        self.gestionar_autorizados()

    def agregar_autorizado(self):
        cedula_socio = input("Ingrese la cédula del socio que autoriza: ")
        socio = next((s for s in self.socios if s.cedula == cedula_socio), None)
        if socio:
            nombre = input("Ingrese el nombre del autorizado: ")
            cedula = input("Ingrese la cédula del autorizado: ")

            try:
                autorizado = Autorizado(nombre, cedula, socio)
                socio.adicionar_autorizado(autorizado)
                self.autorizados.append(autorizado)
                print("Autorizado agregado correctamente.")
                self.guardar_registros()
            except ValueError as e:
                print(f"Error al agregar autorizado: {e}")
        else:
            print("Socio no encontrado.")

    def listar_autorizados(self):
        print("\n----- Lista de Autorizados -----")
        for socio in self.socios:
            print(f"Socio: {socio.nombre} - Autorizados: {len(socio.autorizados)}")
            for autorizado in socio.autorizados:
                print(f"  - {autorizado.nombre} - Cédula: {autorizado.cedula}")

    def registrar_consumo(self):
        print("\n----- Menú Registrar Consumo -----")
        cedula = input("Ingrese la cédula del socio o autorizado que realiza el consumo: ")
        persona = next((p for p in self.socios + self.autorizados if p.cedula == cedula), None)

        if persona:
            concepto = input("Ingrese el concepto del consumo: ")
            valor = float(input("Ingrese el valor del consumo: "))

            try:
                if isinstance(persona, Socio):
                    descuento = persona.descuento
                elif isinstance(persona, Autorizado):
                    socio_asociado = persona.socio_autorizante
                    if isinstance(socio_asociado, Socio):
                        descuento = socio_asociado.descuento
                    else:
                        descuento = 0.0
                else:
                    descuento = 0.0

                valor_con_descuento = valor - (valor * descuento)
                factura = Factura(concepto, valor_con_descuento, cedula)
                self.facturas.append(factura)
                print(f"Consumo registrado. Factura #{len(self.facturas)} - Valor con descuento: ${valor_con_descuento:.2f}")
                self.guardar_registros()
            except ValueError as e:
                print(f"Error al registrar consumo: {e}")
        else:
            print("Persona no encontrada.")


    def registrar_factura(self, concepto, valor, cedula):
        persona = next((p for p in self.socios + self.autorizados if p.cedula == cedula), None)

        if isinstance(persona, Socio):
            descuento = persona.descuento
        elif isinstance(persona, Autorizado):
            descuento = 0.0
        else:
            raise ValueError("Persona no encontrada como Socio o Autorizado.")

        valor_con_descuento = valor - (valor * descuento)
        factura = Factura(concepto, valor_con_descuento, cedula)
        self.facturas.append(factura)
        self.guardar_registros()
        return factura

    def cancelar_factura(self):
        print("\n----- Menú Cancelar Factura -----")
        factura_numero = int(input("Ingrese el número de factura que desea cancelar: "))

        if 1 <= factura_numero <= len(self.facturas):
            factura = self.facturas[factura_numero - 1]
            print(f"Factura #{factura_numero} - Concepto: {factura.concepto} - Valor: ${factura.valor:.2f}")
            
            confirmacion = input("¿Desea cancelar esta factura? (Sí/No): ").lower()
            if confirmacion == "si":
                self.facturas.remove(factura)
                print("Factura cancelada correctamente.")
                self.guardar_registros()
            else:
                print("Operación cancelada.")
        else:
            print("Número de factura no válido.")

    def eliminar_socio(self):
        cedula_socio = input("Ingrese la cédula del socio que desea eliminar: ")
        socio = next((s for s in self.socios if s.cedula == cedula_socio), None)

        if socio:
            self.socios.remove(socio)
            print("Socio eliminado correctamente.")
            self.guardar_registros()
        else:
            print("Socio no encontrado.")

    def adicionar_consumo(self):
        self.registrar_consumo()

    def pagar_consumo(self):
        self.menu_consumos()

    def menu_informe(self):
        print("\n----- Menú Informe -----")
        print("1. Total de Consumos")
        print("2. Consumo por Tipo de Socio")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.total_consumos()
        elif opcion == "2":
            self.consumo_por_tipo_socio()
        elif opcion == "3":
            return
        else:
            print("Opción no válida. Intente de nuevo.")
        self.menu_informe()

    def total_consumos(self):
        total = sum(factura.valor for factura in self.facturas)
        print(f"El total de consumos es: ${total:.2f}")

    def consumo_por_tipo_socio(self):
        for categoria in ["Platino", "Oro", "Plata"]:
            total_categoria = sum(factura.valor for factura in self.facturas if factura.cedula in [socio.cedula for socio in self.socios if isinstance(socio, Socio) and socio.categoria == categoria])
            print(f"Total de consumos para la categoría {categoria}: ${total_categoria:.2f}")

    def cargar_registros(self):
        try:
            with open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\examen_clubsocios\\registros", "rb") as f:
                data = pickle.load(f)
                self.socios = data.socios
                self.autorizados = data.autorizados
                self.facturas = data.facturas
                print("Registros cargados correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de registros.")
        except Exception as e:
            print(f"Error al cargar registros: {e}")

    def guardar_registros(self):
        try:
            with open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\examen_clubsocios\\registros", "wb") as f:
                pickle.dump(self, f)
                print("Cambios guardados en el archivo.")
        except Exception as e:
            print(f"Error al guardar registros: {e}")


club = Club()
club.ejecutar()
