from abc import ABC, abstractmethod
import math
class Figura(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Triangulo(Figura):
    
    def __init__(self, lado1, lado2, lado3, base, altura ):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return self.lado1 +self.lado2 + self.lado3
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

culo = Circulo(5)
print(culo.perimetro())

t1 = Triangulo(5,2,5,4,6)
print(f"area = {t1.area()}")

