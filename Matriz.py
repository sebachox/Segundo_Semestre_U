import Entero as E
import random
class Matriz:
    cantidad_matrices=0
    def __init__(self,mt):
        self.matriz=mt

    def lista_primos_matriz(self):
        lista_primos_matrice=[]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                dato=E.entero(self.matriz[i][j])
                if dato.Primo():
                    lista_primos_matrice.append(self.matriz[i][j])
        return lista_primos_matrice    

    def lista_fibonaccis_matriz(self):
        lista_fibonaccis_matrice=[]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                dato= E.entero(self.matriz[i][j])
                if dato.Fibonacci():
                    lista_fibonaccis_matrice.append(self.matriz[i][j])
        
        return lista_fibonaccis_matrice

    def __str__(self):
        for i in self.matriz:
            return i

    @staticmethod
    def dicPrimosRepetidos(lista1):
        dic = {}
        for num in lista1:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        print(f"diccionario : {dic}")
        num_mas_repetido = max(dic, key=dic.get)
        return f"El número más repetido es {num_mas_repetido} con {dic[num_mas_repetido]} repeticiones."




#se tiene una matriz sacar un diccionario con los primos  y las veces que se repite el que mas se repite
#se tiene una matriz y un vector con datos num determinar fib mas repetido
#m =Matriz([[2, 3, 5, 7, 11, 13, 17, 19],
     #      [2, 3, 5, 7, 11, 13, 17, 19],
     #      [2, 3, 5, 7, 11, 13, 17, 19, 19]
      #     ])
