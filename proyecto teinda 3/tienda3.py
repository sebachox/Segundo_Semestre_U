from producto3 import Producto
from factura3 import Factura
from leer import Leer

class Tienda:
    dineroEnCaja = 0
    numeroFactura = 1
    
    def __init__(self):
        self.producto = []  # Inicializa la lista de productos en el constructor
        self.factura = []

    # def hacer_pedido(self):
    #     self.mostrarProductos()
    #     pro = Leer.leer_string("ingrese el nombre del producto que desea hacer el pedido: -> ")
        
    #     if self.consultarProducto(pro):
    #         cantidad = Leer.leer_int("ingrese la cantidad que desea pedir -> : ")
    #         if cantidad >= pro.cantidaMinima:
    #             pro.cantidaBodega += cantidad 
    #         else: 
    #             print("la cantidad pedida no supera la cantidad minima para pedir")
    #         venta = pro.valorUNitario * cantidad
    #         self.dineroEnCaja -= venta
    #         print("productos actualizados exitozamente :)")
    #         self.mostrarProductos()
    #     else:
    #         print("el producto a pedir no se encuentra en la tienda")

    def hacer_pedido(self):
        self.mostrarProductos()
        nombre_producto = input("Ingrese el nombre del producto que desea hacer el pedido: ")

        producto_existente = self.consultarProducto(nombre_producto.lower())

        if producto_existente:
            cantidad_pedido = int(input(f"Ingrese la cantidad de {producto_existente.nombre} que desea pedir: "))

            if cantidad_pedido >= producto_existente.cantidadMinima:
                producto_existente.cantidadBodega += cantidad_pedido
                venta = producto_existente.valorUnitario * cantidad_pedido
                self.dineroEnCaja -= venta
                print("Productos actualizados exitosamente.")
                self.mostrarProductos()
            else:
                print("La cantidad pedida no supera la cantidad mínima para pedir.")
        else:
            print("El producto a pedir no se encuentra en la tienda.")


    def mostrar_Todas_facturas(self):
        if not self.factura:
            print("No hay facturas para mostrar.")
        else:
            for factura in self.factura:
                factura.mostrar_factura()

    def generar_factura(self, productos_vendidos, numero_factura):
        factura_actual = Factura(numero_factura)
        for producto, cantidad, valor in productos_vendidos:
            factura_actual.agregarVenta(producto, cantidad, valor)

        self.factura.append(factura_actual)
        self.numeroFactura += 1
    
    def adicionarProductosTienda(self):
        nump = Leer.leer_int("Cuantos productos desea ingresar? -> ")
        for i in range(nump):
            nombre = Leer.leer_string("\nIngrese el nombre del producto -> ")
            tipo = Leer.leer_int("Ingrese el tipo de producto -> ")
            valor = Leer.leer_int("Ingrese el valor unitario que tiene este producto -> ")
            cantidadb = Leer.leer_int("Ingrese la cantidad de productos en bodega -> ")
            cantidadm = Leer.leer_int("Ingrese la cantidad mínima para pedidos -> ")
            self.producto.append(Producto(nombre, tipo, valor, cantidadb, cantidadm))
        print(f"Se han creado con éxito los {nump} productos ingresados")

    def mostrarProductos(self):
        p = open("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\productos.txt", "r")
        l = p.readlines()
        for linea in l:
            linea.split(linea)
            linea.strip(linea)
            print(linea)
        p.close()

    def consultarProducto(self, producto):
        for p in self.producto:
            if p.nombre == producto:
                return p
        return None

    
    
    def valor_unitario(self, nombre_producto):
        for nombre_producto in self.producto:
            if nombre_producto.nombre == nombre_producto:
                valor =int(nombre_producto.valorUnitario())
                return valor


    # def productoMasVendido():

    # def promedioVentas():

    # def totalVentasTienda():

    
#teinda =tienda([],[]) asi se crea la tienda porque productos esta vacio y factura igual 

