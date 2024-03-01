import pickle
# lista =["jaksajk", 2324]
# lista2 =["hola mi bro"]

# fichero = open("archivolista", "wb")
# pickle.dump(lista, fichero)
# fichero.close()

# archivo = open("archivolista", "rb")

# listarecuperada = pickle.load(archivo)
# print(listarecuperada)


fichero = open("archivolista", "wb")
pickle.dump("hola como estas", fichero)
fichero.close()

archivo = open("archivolista", "rb")
varirecu = pickle.load(archivo)
print(varirecu)