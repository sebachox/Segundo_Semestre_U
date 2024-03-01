import os
from colorama import init, Fore
import random
import lista
import Entero
import Matriz
import Racional
def main():
    init()
    def leer_matriz():
        while True:
            try:
                matriz = []
                filas = int(input("Cantidad de filas: "))
                columnas = int(input("Cantidad de columnas: "))
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        dato = random.randint(1, 11)  
                        fila.append(dato)
                    matriz.append(fila)

                print("Matriz generada automáticamente: ")
                for fila in matriz:
                    print(fila)
                return matriz
                break
            except ValueError:
                print("Has digitado algún carácter incorrecto, por favor inténtalo de nuevo")
    def leerVectorR():
        while True:
            try:
                cd = int(input('Cantidad de datos lista -> '))
                lista = [random.randint(1, 10) for _ in range(cd)]
                return lista
            except ValueError:
                print("el caracter ingresado no coincide con el caracter pedido, porfavor vuelve a digitarlo")
    # def ejercicio1():

    # def ejercicio2():

    # def ejercicio3():

    # def ejercicio4():

    # def ejercicio5():

    # def ejercicio6():

    def ejercicio7():
        print("Se tiene una matriz con datos numéricos formar un diccionario con la veces que se repite cada número.")
        m_l = leer_matriz
        m = Matriz(m_l)
        l = m.lista_primos_matriz()
        print("Lista primos= ",l)
        print(m.dicPrimosRepetidos(l))

    # def ejercicio8():

    def menu_principal():
        os.system("cls")
        while True:
            try:
                print(Fore.GREEN+"""
    <<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>
                    
                1. ejercicio 1
                2. ejercicio 2
                3. ejercicio 3
                4. ejercicio 4
                5. ejercicio 5
                6. ejercicio 6
                7. ejercicio 7
                8. ejercicio 8
                0. SALIR
    """)
                opcion = int(input("ingrese la opcion que desse : -> "))
                match opcion:
                    # case 1:
                    #     ejercicio1()
                    #     os.system("pause")
                    # case 2:
                    #     ejercicio2()
                    #     os.system("pause")
                    # case 3:
                    #     ejercicio3()
                    #     os.system("pause")
                    # case 4:
                    #     ejercicio4()
                    #     os.system("pause")
                    # case 5:
                    #     ejercicio5()
                    #     os.system("pause")
                    # case 6:
                    #     ejercicio6()
                    #     os.system("pause")
                    case 7:
                        ejercicio7()
                        os.system("pause")
                    # case 8:
                    #     ejercicio8()
                    #     os.system("pause")    
                    case 0:
                        print("vale, adios")
                        break
                    case other:
                        print(Fore.RED+"la opcion que ingresaste es invalida")
                        os.system("pause")
            except ValueError:
                print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
    menu_principal()   
main()