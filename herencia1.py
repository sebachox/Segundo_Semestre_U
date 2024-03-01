class Animal():
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass
    
    def moverse(self):
        pass

    def describirme(self):
        print(f"soy un animal de tipo {type(self).__name__}")#nombre del objeto que tengo ahi 

class Perro(Animal):
    #ALTERNATIVA 1
    # def __init__(self, especie, edad, dueño):
    #     self.especie = especie
    #     self.edad = edad
    #     self.dueño = dueño
    #ALTERNATIVA 2
    # o se puede hacer esto
    #     super().__init__(especie, edad)
    #     self.dueño = dueño


    #se sobreescriben los metodos de animal ya que en animal no hacen nada
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuuuu")
    def moverse(self):
        print("caminando con 4 patas")
    
class Abeja(Animal):
    def hablar(self):
        print("Bzzzz")
    def moverse(self):
        print("volando")
    #se define un nuevo metodo
    def picar(self):
        print("Picar!")

mi_perro = Perro("mamifero", 5)
mi_vaca = Vaca("mamifero", 10)
mi_abeja = Abeja("insecto", 1)

mi_perro.hablar()
mi_vaca.hablar()
mi_perro.describirme()
mi_abeja.describirme()
mi_abeja.picar()


# #muestra clases que heredo
# print(Perro.__bases__)

# #muestra clases que dejo herencia
# print(Animal.__subclasses__())


# class c1:
#     pass
# class c2:
#     pass
# class c3(c1,c2):
#     pass

# print(c3.__mro__)