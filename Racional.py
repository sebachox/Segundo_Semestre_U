#realizar clase de numeros reacionales y crear todas sus operaciones basicas 
#crear un objeto del resultado 
class NumRacional:
    def __init__(self, nummerador, denominador):
        self.numerador = nummerador
        self.denominador = denominador
    
    def __str__(self):
        return (f"numerador = {self.numerador}\ndenominador = {self.denominador}")
    #metodos de instancia
    def SumaRac(self, OtroRacional):#otro racional como parametro
        Rnumerador = (self.numerador * OtroRacional.denominador) + (self.denominador * OtroRacional.numerador)
        Rdenominador = self.denominador * OtroRacional.denominador
        return NumRacional(Rnumerador, Rdenominador)

    def RestaRac(self, OtroRacional):
        Rnumerador = (self.numerador * OtroRacional.denominador) - (self.denominador * OtroRacional.numerador)
        Rdenominador = self.denominador * OtroRacional.denominador
        return NumRacional(Rnumerador, Rdenominador)
    
    def MulpRac(self, OtroRacional):
        Rnumerador = self.numerador * OtroRacional.numerador
        Rdenominador = self.denominador * OtroRacional.denominador
        return NumRacional(Rnumerador, Rdenominador)

    def DivRac(self, OtroRacional):
        Rnumerador = self.numerador * OtroRacional.denominador
        Rdenominador = self.denominador * OtroRacional.numerador
        return NumRacional(Rnumerador, Rdenominador)
    




