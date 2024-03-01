import random
import math

def leerVectorR():
    cd = int(input('Cantidad de datos lista -> '))
    lista = [random.randint(1, 10) for _ in range(cd)]
    return lista

def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
    return matriz

def primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(math.sqrt(valor)) + 1):
        if valor % i == 0:
            return False
    return True

def factorial(dato):
    factorial = dato
    multiplo = dato - 1
    while multiplo > 0:
        factorial = factorial * multiplo
        multiplo -= 1
    return factorial

def fibonacci(valor):
    a, b, t = 0, 1, 0
    while t < valor:
        t = a + b
        a = b
        b = t
    if t == valor:
        return True
    else:
        return False

def obtener_listas_key_valor(diccionario):
    lista_keys = diccionario.keys()
    lista_values = diccionario.values()
    return lista_keys, lista_values
    

def formar_diccionario_listas(lista_clave, lista_valor):
    diccionario_1 = {}
    for i in range(lista_clave):
        diccionario_1[lista_clave[i]] = lista_valor[i]
    return diccionario_1

def ordenar_diccionario_clave(diccionario):
    lista_clave = diccionario.keys()
    lista_clave_ordenado = sorted(lista_clave)
    dic_ordenado = {}
    for ele in lista_clave_ordenado:
        dic_ordenado[ele] = diccionario[ele]
    return dic_ordenado
    

def ejercicios_1_diccinarios():
    print("1 se tiene una lista con datos numericos formar un diccionario donde la clave sea el dato unico y el valor las veces que se repite\n")
    lista = leerVectorR
    diccionario = {}
    
    for i in range(len(lista)):
        aux=lista[i]
        if aux not in diccionario.keys():
            contador=0
            for j in range(i, len(lista)):
                if aux == lista[j]:
                    contador+=1

            diccionario [aux] = contador
    print(f"lista con la que trabajo : {lista}")
    print(f"diccionario resultante : {diccionario}")


def ejercicios_2_diccinarios():
    print("""
    2 se tiene dos listas con datos numericos formar dos diccionarios asi: 
    -d1 con los pirmos comunes com clave y como valor su factorial, 
    -d2 con los fibonacci no comunes y los valores son numeros pares menores al fibonacci
""")
    lista_1 = leerVectorR()
    lista_2 = leerVectorR()
    diccionario_1 = {}
    diccionario_2 = {}
    for i in range(len(lista_1)):
        if primo(lista_1[i]) and lista_1[i] in lista_2 and lista_1[i] not in diccionario_1.keys():
            diccionario_1[lista_1[i]] = factorial(lista_1[i])
        vector=[]
        if fibonacci(lista_1[i]) and lista_1[i] not in lista_2 and lista_1[i] not in diccionario_2.keys():
            j=0
            while j<lista_1[i] :
                if j % 2 == 0:
                        vector.append(j)
                j+=1
            diccionario_2[lista_1[i]] = vector
    for j in range(len(lista_2)):
        vector=[]
        if fibonacci(lista_2[j]) and lista_2[j] not in lista_1 and lista_2[j] not in diccionario_2.keys():
            i=0
            while i < lista_2[j] :
                if i % 2 == 0:
                        vector.append(i)
                i+=1
            diccionario_2[lista_2[j]] = vector
    print(f"lista 1 ingresada : {lista_1}")
    print(f"lista 2 ingresada : {lista_2}")
    print(f"diccionario 1 donde key : primos comunes y clave : factorial del primo  = {diccionario_1}")
    print(f"diccionario 2 donde key : fibonacci no comunes y calve : numeros pares menores a ese factorial  = {diccionario_2}")


def ejercicios_3_diccinarios():
    print("""
    3 se tiene una cadena donde hay caracteres numericos y alfabeticos repetidos formar dos diccionarios asi: 
    -d1 con el digito y las veces que se repiten
    -d2 con la letra del alfabeto y las veces qye se reputen  
    (ordenados ascendentemente ambos por keys)

""")
    diccionario_1 = {}
    diccionario_2 = {}
    cadena = input("ingrese su cadena alfanumerico con datos repetidos : ")
    for i in range(len(cadena)):
        if cadena[i].isdigit() and cadena[i] not in diccionario_1.keys():
            aux = cadena[i]
            contador = 0
            for j in range(len(cadena)):
                if aux == cadena[j]:
                    contador += 1
            diccionario_1[aux] = contador
        if cadena[i].isalpha() and cadena[i] not in diccionario_2.keys():
            aux = cadena[i]
            contador = 0
            for j in range(len(cadena)):
                if aux == cadena[j]:
                    contador += 1
            diccionario_2[aux] = contador
    diccionario_ordenado_1 = dict(sorted(diccionario_1.items()))
    diccionario_ordenado_2 = dict(sorted(diccionario_2.items()))
    print(f"el diccionario 1 es : {diccionario_1}")
    print(f"el diccionario 2 es : {diccionario_2}")
    print(f"el diccionario 1 ordenado quedo : {diccionario_ordenado_1}")
    print(f"el diccionario 2 ordenado quedo : {diccionario_ordenado_2}")




def ejercicios_4_diccionarios():
    print("""
          tengo una lista con datos numericos repetidos  formar dos diccionarios con los datos y las veces que se repite asi :
          d1= ordenar diccionario por keys ascendente
          d2= ordenar el diccionario por clave ascendente
          """)
    #formar 2 listas con keys y values
    #ordenar lista 1 e intercambiar lista values para correspondencia
    #formar diccionario con las fos litas 
    lista = [7,2,4,7,7,4,2,1,9,7,9]
    diccionario = {}
    for i in range(len(lista)):
        aux=lista[i]
        if aux not in diccionario.keys():
            contador=0
            for j in range(i, len(lista)):
                if aux == lista[j]:
                    contador+=1
            diccionario [aux] = contador
    lista_diccionario = diccionario.items()
    #funciones landa
    diccionario_orden_clave = dict(sorted(lista_diccionario, key = lambda t : t[0]))
    diccionario_orden_valor = dict(sorted(lista_diccionario, key = lambda t : t[1]))
    print(f"diccionario ordenado por clave : {diccionario_orden_clave}")
    print(f"diccionario ordenado por valor : {diccionario_orden_valor}")



