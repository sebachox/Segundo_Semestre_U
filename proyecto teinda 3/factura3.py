
class Factura:
    valorFacturaTotal = 0  # Class variable to track the total value of all invoices

    def __init__(self, numero):
        self.numfactura = numero
        self.valorfactura = 0
        self.ventas = []

    # def mostrarFacturaC(self):
    #     print(f"""
    #     FACTURA N° {self.numfactura}
    #     Productos:""")
        
    #     for i in self.ventas:
    #         print(f"Producto: {self.ventas[i][0]}, Cantidad: {self.ventas[i][1]}, Valor: {self.ventas[i][2]}")

    #     print(f"\nTOTAL A PAGAR: {self.valorfactura}")

    def mostrar_lista_ventas(self):
        for producto in self.ventas:
            nproducto, cantidad, valor = producto
            print(f"Nombre : {nproducto.nombre}, Cantidad vendida : {cantidad}, Valor Unitario : {valor}, Valor Total Producto : {cantidad*valor}")
    
    def mostrar_lista_ventasDetalle(self):
        for producto in self.ventas:
            nproducto, cantidad, valor = producto
            print(f"{nproducto} Cantidad vendida : {cantidad}\n Valor Total Producto : {cantidad*valor}\n")
        
    def mostrar_factura(self):
        print(f"FACTURA N° {self.numfactura}")
        self.mostrar_lista_ventas()
        print(f"VALOR FINAL A PAGAR : {self.valorFacturaTotal}")

    def mostrar_facturaDetalle(self):
        print(f"FACTURA N° {self.numfactura}")
        self.mostrar_lista_ventasDetalle()
        print(f"VALOR FINAL A PAGAR : {self.valorFacturaTotal}")

    def agregarVenta(self, producto, cantidad, valor):
        # Verificar si el producto ya está en la factura
        for venta in self.ventas:
            if venta['producto'] == producto:
                # Si el producto ya está en la factura, preguntar al usuario si quiere agregar más cantidad
                respuesta = input(f"El producto '{producto.nombre}' ya está en la factura. ¿Desea agregar la cantidad digitada anteriormente? (si/no): ")
                if respuesta.lower() == "si":
                    venta['cantidad'] += cantidad
                    # Convertir valor a numérico antes de sumar
                    venta['valor'] += float(valor)
                    self.valorfactura += float(valor)
                    return  # Sale de la función después de actualizar la cantidad
                else:
                    return  # Sale de la función sin agregar una nueva venta
            else: 
                # Si el producto no está en la factura, agregar una nueva venta
                venta_nueva = {"producto": producto, "cantidad": cantidad, "valor": float(valor)}
                print("Venta nueva:", venta_nueva)  # Agrega esta línea para imprimir la nueva venta
                self.ventas.append(venta_nueva)
                self.valorfactura += float(valor)
                # Agrega esta línea para imprimir la lista de ventas después de agregar la nueva venta
                print("Lista de ventas después de agregar la nueva venta:", self.ventas)
                break

        
        # for producto in self.ventas:
        #     nombre_producto, cantidad_ventas, valor_cobrado = producto
        #     print(f"nombre: {nombre_producto}, cantidad vendida: {cantidad_ventas}, valor : {valor_cobrado}")

    
            


        