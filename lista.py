import Entero

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
            dato = Entero(self.lista[i])
            if dato.Fibonacci():
                listaFibo.append(dato)
        return listaFibo


    def primosLista(self):
        listaPrimos = []
        for i in range(len(self.lista)):
            dato = Entero(self.lista[i])
            if dato.Primo():
                listaPrimos.append(dato)
        return listaPrimos
        
    
    def sinRepLista(self):
        conj = set(self.list)
        return list(conj)
    
    def __str__(self):
        return (f"lista : {self.lista}")