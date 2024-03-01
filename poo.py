
class entero:
    def __init__(self, ent):
        self.entero = ent

    def Primo(self):
        if self.entero < 2:
            return False
        for i in range(2, self.entero):
            if self.entero % i == 0:
                return False
        return True

    def Fibonacci(self):
        a=0
        b=1
        t=0
        while t<self.entero :
            t=a+b
            a=b
            b=t
        if t == self.entero:
            return True
        else:
            return False
    
    def Par(self):
        if self.entero % 2 == 0:
            return True
        else:
            return False
    
    def Impar(self):
        if self.entero % 2 != 0:
            return True
        else:
            return False




#definir una cantidad dada de triangulos y determinar cuantos de esos triangulos tienen como perimetro un numero primo
# se tiene una cantidad de trian dados mostrarlos en orden ascendente de acuerdo al perimetro  queda en estanbay

#definir una clase lista que tiene como atributo de instancia una lista desarrollar los metods siguientes 
#- mayor de la lista -menor de la lista -promedio de la lista -fibonacci de la lista  -primos de la lista - listas sin repetido
class Lista:
    def __init__(self, l):
        self.lista = l

    def mayorLista(self):
        return max(self.lista)
    
    def menorLista(self):
        return min(self.lista)
    
    def promLista(self):
        return sum(self.lista)/len(self.lista)
    
    def fibonaccisLista(self):
        listaFibo = []
        for i in range(len(self.lista)):
            dato = entero(self.lista[i])
            if dato.Fibonacci():
                listaFibo.append(dato)
        return listaFibo


    def primosLista(self):
        listaPrimos = []
        for i in range(len(self.lista)):
            dato = entero(self.lista[i])
            if dato.Primo():
                listaPrimos.append(dato)
        return listaPrimos
        
    
    def sinRepLista(self):
        conj = set(self.list)
        return list(conj)








class Triangulo:
    #variables de clases
    cantidadTriangulos = 0
    sumaPerimetros = 0
    #metodos
    def __init__(self, l1, l2, l3, base, altura):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3
        self.base = base
        self.altura = altura
        Triangulo.cantidadTriangulos += 1

    def areaTriangulo(self):
        area = self.base * self.altura / 2
        return area
    
    def perimetroTriangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro
    
    def tipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return "Equilatero"
        else:
            if self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado2 == self.lado3:
                return "isoceles"
            else:
                return "escaleno"
    
    def mostrarTriangulo(self):
        return f" lado 1 : {self.lado1}\n lado 2 : {self.lado2}\n lado 3 : {self.lado3}"

t1 = Triangulo(5,5,5,4,5)
t2 = Triangulo(7,5,4,4,5)

#t1.atributo = nuevo valor , t1.lado1 = 7
#t1.angulo = 45