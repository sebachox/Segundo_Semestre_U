# 1.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
# determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, 
# es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
import random 
import os
from colorama  import init,Fore

init()
def leerMatriz():
    while True:
        try: 
            nf = int(input('Cantidad de filas matriz -> '))
            nc = int(input('Cantidad de columnas matriz -> '))
            matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
            return matriz
        except ValueError:
            print("el caracter ingresado no coincide con el caracter pedido, porfavor vuelve a digitarlo")

def leerVectorR():
    while True:
        try:
            cd = int(input('Cantidad de datos lista -> '))
            lista = [random.randint(1, 10) for _ in range(cd)]
            return lista
        except ValueError:
            print("el caracter ingresado no coincide con el caracter pedido, porfavor vuelve a digitarlo")

def fibonacci(valor):
        a=0
        b=1
        t=0
        while t<valor :
            t=a+b
            a=b
            b=t
        if t==valor:
            return True
        else:
            return False

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def factorial(dato):
    factorial=dato
    multiplo=dato-1
    while multiplo>0:
        factorial=factorial*multiplo
        multiplo-=1
    return factorial

def contar_primos_en_matrices(matriz_1, matriz_2):
    diccionario = {}
    
    for fila in matriz_1:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1
    
    for fila in matriz_2:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1

    return diccionario

def contar_caracteres(cadena):
    diccionario_digito = {}
    diccionario_caracter = {}

    for caracter in cadena:
        if caracter.isdigit():
            if caracter in diccionario_digito:
                diccionario_digito[caracter] += 1
            else:
                diccionario_digito[caracter] = 1
        elif caracter.isalpha():
            if caracter in diccionario_caracter:
                diccionario_caracter[caracter] += 1
            else:
                diccionario_caracter[caracter] = 1

    return diccionario_digito, diccionario_caracter


def punto_1():
    print("""1.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
          determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, 
          es un numero Fibonacci, si no lo es determinar si es primo y su factorial."""
          )
    perimetro=0
    matriz=leerMatriz()
    z=0
    x=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j==0:
                a=matriz[i][j]
            elif j==1:
                b=matriz[i][j]
            elif j==2:
                c=matriz[i][j]    
        
        if a==b==c:
            z+=1
            if z==2 or z==4:
                perimetro+=a+b+c
                
        if a!=b!=c!=a:
            x+=1
            if x==2:
                perimetro+=a+b+c
                
    valor = perimetro        
    print("la matriz ingresada es ")
    for i in matriz:
        print(i)
    if fibonacci(valor):
        print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero fibonacci : {perimetro}")
    elif primo(valor):
            print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero primo : {perimetro}, y su factorial es : {factorial(perimetro)}")
    else:
        print(f"la suma de los perimetros del segundo y cuarto equilatero y el segundo escaleno : {perimetro}, no es ni fibonacci ni primo")


def punto_3():
    print("""3.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.\n""")
    lista_1=leerVectorR()
    lista_2=leerVectorR()
    lista_primos=[]
    print(f"lista ingresada N° 1 : {lista_1}")
    print(f"lista ingresada N° 2 : {lista_2}")
    for i in range(len(lista_1)):
        if primo(lista_1[i]):
            if lista_1[i] not in lista_primos and lista_1[i]  in lista_2:
                lista_primos.append(lista_1[i])

    print(f"la lista con los primos  comunes sin repetidos es : {lista_primos}")
                

def punto_5():
    print("""5.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
           determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada,
           es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
        """)
    perimetro=0
    matriz=leerMatriz()
    z=0
    x=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j==0:
                a=matriz[i][j]
            elif j==1:
                b=matriz[i][j]
            elif j==2:
                c=matriz[i][j]    
        
        if a==b==c:
            z+=1
            if z==2 or z==4:
                perimetro+=a+b+c
                
        if a!=b!=c!=a:
            x+=1
            if x==2:
                perimetro+=a+b+c
                
    valor = perimetro        
    print("la matriz ingresada es ")
    for i in matriz:
        print(i)
    if fibonacci(valor):
        print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero fibonacci : {perimetro}")
    elif primo(valor):
            print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero primo : {perimetro}, y su factorial es : {factorial(perimetro)}")
    else:
        print(f"la suma de los perimetros del segundo y cuarto equilatero y el segundo escaleno : {perimetro}, no es ni fibonacci ni primo")


def punto_7():
    print("""7. Se tiene un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas
                 del primo que más se repite con el primo que menos se repite.
            """)
    lista = leerVectorR()
    contador_primos = {}  # Un diccionario para contar las repeticiones de primos únicos
    
    for numero in lista:
        if primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    
    primos = list(contador_primos.keys())  # Lista de primos únicos
    primos.sort(key=lambda x: contador_primos[x])  # Ordena la lista de primos por repeticiones
    
    if len(primos) < 2:
        print("No hay suficientes primos en la lista.")
        return
    
    primo_menos_repetido = primos[0]
    primo_mas_repetido = primos[-1]
    
    resultado = primo_menos_repetido * primo_mas_repetido
    
    print(f"""
          El vector ingresado para el ejercicio fue : {lista}, 
          El primo que menos se repitió de la lista fue : {primo_menos_repetido} con {contador_primos[primo_menos_repetido]} repeticiones,
          El más repetido fue : {primo_mas_repetido} con {contador_primos[primo_mas_repetido]} repeticiones,
          La multiplicación de estos dos primos fue : {resultado}
            """)

def punto_9():
    print("""9. Se tiene un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas
                 del primo que más se repite con el primo que menos se repite.
            """)
    lista = leerVectorR()
    contador_primos = {}  # Un diccionario para contar las repeticiones de primos únicos
    
    for numero in lista:
        if primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    
    primos = list(contador_primos.keys())  # Lista de primos únicos
    primos.sort(key=lambda x: contador_primos[x])  # Ordena la lista de primos por repeticiones
    
    if len(primos) < 2:
        print("No hay suficientes primos en la lista.")
        return
    
    primo_menos_repetido = primos[0]
    primo_mas_repetido = primos[-1]
    
    resultado = primo_menos_repetido * primo_mas_repetido
    
    print(f"""
          El vector ingresado para el ejercicio fue : {lista}, 
          El primo que menos se repitió de la lista fue : {primo_menos_repetido} con {contador_primos[primo_menos_repetido]} repeticiones,
          El más repetido fue : {primo_mas_repetido} con {contador_primos[primo_mas_repetido]} repeticiones,
          La multiplicación de estos dos primos fue : {resultado}
            """)



def punto_11():
    print("11.	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos ")
    matriz= leerMatriz()
    
    print("matriz a trabajar : ")
    for i in matriz:
        print(i)
    
    primos = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz[0])) if primo(matriz[i][j])]
    
    if len(primos) < 4:
        print("No se encontraron los primos 2 y 4 en la matriz.")
    else:
        consecutivos = primos[3] - primos[1] == 2
        for i in range(1, len(primos) - 2):
            if primos[i+2] - primos[i] == 2:
                consecutivos = False
                break

        if consecutivos:
            print(f"El primo 2 ({primos[1]}) y el primo 4 ({primos[3]}) son consecutivos.")
        else:
            print(f"Entre el primo 2 ({primos[1]}) y el primo 4 ({primos[3]}) hay números primos, por lo tanto, no son consecutivos.")

    
    

def punto_13():
    print("""
    13. Se tiene un conjunto y una matriz con datos numéricos,
    hallar el primo mayor del conjunto y su factorial y llenar este valor en las posiciones comprendidas
    entre el par menor y el Fibonacci mayor de la matriz
    """)
    lista = leerVectorR()
    matriz = leerMatriz()

    z = 0
    f = 0
    p = 0

    for i in range(len(lista)):
        if primo(lista[i]):
            if z == 0:
                primo_mayor = lista[i]
                z = 1
            elif lista[i] > primo_mayor:
                primo_mayor = lista[i]

    factor = factorial(primo_mayor)

    print(f"la lista ingresada es : {lista}")

    print("la matriz ingresada es : \n")
    for i in matriz:
        print(i)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if fibonacci(matriz[i][j]):
                if f == 0:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
                    f = 1
                elif matriz[i][j] > fibonacci_mayor:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
            if matriz[i][j] % 2 == 0:
                if p == 0:
                    par_menor = matriz[i][j]
                    par_menor_i = i
                    par_menor_j = j
                    p = 1
                elif matriz[i][j] < par_menor:
                    par_menor = matriz[i][j]
                    par_menor_i = i
                    par_menor_j = j

    if par_menor_i < fibonacci_mayor_i:
        for i in range(par_menor_i, fibonacci_mayor_i + 1):
            for j in range(par_menor_j, fibonacci_mayor_j + 1):
                matriz[i][j] = factor
    elif par_menor_i > fibonacci_mayor_i:
        for i in range(fibonacci_mayor_i, par_menor_i + 1):
            for j in range(fibonacci_mayor_j, par_menor_j + 1):
                matriz[i][j] = factor


    print(f"el primo mayor del conjunto es : {primo_mayor} y su factorial es : {factor}")
    print(f"el par menor de la matriz es : {par_menor} con posición i: {par_menor_i + 1} y j: {par_menor_j + 1}")
    print(f"el Fibonacci mayor de la matriz es : {fibonacci_mayor} con posición i: {fibonacci_mayor_i + 1} y j: {fibonacci_mayor_j + 1}")
    print(" y la matriz resultante del ejercicio queda :")
    for i in matriz:
        print(i)



def punto_15():
    print("15. Se tienen dos matrices con datos numéricos. Formar un diccionario con los primos como clave y las veces que aparecen como valor, ordenado por la clave.")
    matriz_1 = leerMatriz() 
    print ("matriz ingresada :")
    for i in matriz_1:
        print(i) 
    matriz_2 = leerMatriz()  
    print ("matriz ingresada :")
    for i in matriz_2:
        print(i) 
    print("Las matrices que se van a trabajar son:")
    print("Matriz 1\n")
    for fila in matriz_1:
        print(fila)
    print("\nMatriz 2\n")
    for fila in matriz_2:
        print(fila)

    diccionario_final = contar_primos_en_matrices(matriz_1, matriz_2)

    # Ordenar el diccionario por las claves.
    diccionario_ordenado = dict(sorted(diccionario_final.items()))

    print(f"Los primos de las matrices y las veces que se repiten son: {diccionario_ordenado}")



def punto_17():
    print("""
    17.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
    Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
    Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave 
    """)
    cadena_1 =input("ingrese su cadena alfanumerica N° 1")
    cadena_2 =input("ingrese su cadena alfanumerica N° 2")
    cadena_3 =input("ingrese su cadena alfanumerica N° 3")
    cadena_final = cadena_1 + cadena_2 + cadena_3
    dic_digito, dic_caracter = contar_caracteres(cadena_final)
    dic_digito_final = dict(sorted(dic_digito.items(), key = lambda t : t[0]))
    dic_caracter_final = dict(sorted(dic_caracter.items(), key = lambda t : t[0]))
    print(f"diccionario con digitos : {dic_digito_final}, diccionario con caracteres : {dic_caracter_final}")


def punto_19():
    print("""
    19.	Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
    el par mayor y las veces que se repite
    el primo menor y las veces que se repite
    el Fibonacci menor y las veces que se repite
    Con estos datos hallar:
    El factorial de la suma del par y del primo
    La multiplicación con sumas de los contadores del primo y del Fibonacci.

    """)
    lista = leerVectorR()
    print(f"lista ingresada : {lista}")
    matriz = leerMatriz()
    print("matriz ingresada")
    for i in matriz:
        print(i)
    l_par = []
    l_primo = []
    l_fibonacci = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            l_par.append(lista[i])
        elif primo(lista[i]):
            l_primo.append(lista[i])
        elif fibonacci(lista[i]):
            l_fibonacci.append(lista[i])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                l_par.append(matriz[i][j])
            elif primo(matriz[i][j]):
                l_primo.append(matriz[i][j])
            elif fibonacci(matriz[i][j]):
                l_fibonacci.append(matriz[i][j])
    par_mayor = max(l_par)
    rep_par = lista.count(par_mayor) + matriz.count(par_mayor)
    primo_menor = min(l_primo)
    rep_primo = lista.count(primo_menor) + matriz.count(primo_menor)
    fibonacci_menor = min(l_fibonacci)
    rep_fibo = lista.count(fibonacci_menor) + matriz.count(fibonacci_menor)

    sum_fib_pri = primo_menor + par_mayor
    fac_sum_fib_pri = factorial(sum_fib_pri)
    
    men = 0
    r = 0
    while men < rep_fibo:
        r += rep_primo
        men += 1
    print(f"""
    el par mayor : {par_mayor} las veces que se repite : {rep_par}
    el primo menor : {primo_menor} las veces que se repite : {rep_primo}
    el Fibonacci menor : {fibonacci_menor} las veces que se repite : {rep_fibo}
    El factorial de la suma del par y del primo : {fac_sum_fib_pri}
    La multiplicación con sumas de los contadores del primo y del Fibonacci : {r}
    """)
        

def punto_1_cadenas():
    print("1  se tiene una cadena contar las veces que se repite un caracter ")
    cadena=input("ingresar su frase")
    contar=input("ingrese el caracter a contar")
    print(f"la letra k se repite en la cadena : {cadena.count(contar)} veces")

def punto_2_cadenas():
    print("2. Se tiene una cadena, ordenarla en forma ascendente y en forma descendente")
    cadena = input("Ingrese su frase: ")
    lista_cadena = list(cadena)

    lista_cadena_ascendente = sorted(lista_cadena)
    lista_cadena_descendente = sorted(lista_cadena, reverse=True)

    cadena_ascendente = ''.join(lista_cadena_ascendente)
    cadena_descendente = ''.join(lista_cadena_descendente)

    print("Cadena ordenada en forma ascendente:", cadena_ascendente)
    print("Cadena ordenada en forma descendente:", cadena_descendente)

def punto_3_cadenas():
    print("3  convertir la cadena a mayusculas y minusculas ")
    cadena = input("Ingrese su frase: ")
    print(f"su cadena es mayusculas es :  {cadena.upper()}")
    print(f"su cadena en minusculas es : {cadena.lower()}")
    
def punto_4_cadenas():
    print("""
        de una cadena dada donde hay digitos y caracteres alfabetico formar dos cadenas , 
          -cadena1 con los digitos sin repetidos 
          -cadena2 con los alfabeticos sin repetidos
    """)
    string = (input("ingresar su cadena -> "))
    set_digit = set()
    set_alpha = set()
    list_string = list(string)
    for i in range(len(list_string)):
        if list_string[i].isdigit():
            set_digit.add(list_string[i])
        elif list_string[i].isalpha():
            set_alpha.add(list_string[i])
    str_digit = str(set_digit)
    str_alpha = str(set_alpha)
    print(f"cadena con digitos :{str_digit}, cadena con alphas : {str_alpha}")

def punto_5_cadenas():
    print("""
    #5  se tienen dos cadenas formar dos cadenas 
          -cadena 1 con los digitos no comunes de las dos cadenas 
          -cadena 2 con las letras comunes de las dos cadenas sin repetir
    """)
    cadena_1 = input("ingrese la cadena N° 1 :")
    cadena_2 = input("ingrese la cadena N° 2 :")

    lisCaden1 =list(cadena_1)
    lisCaden2 =list(cadena_2)

    conj1 = set()
    conj2 = set()
    for i in range(len(lisCaden1)):
        if lisCaden1[i].isnumeric() and lisCaden1[i] not in lisCaden2:
                conj1.add(lisCaden1[i])
        else:
            if lisCaden1[i].isalpha() and lisCaden1[i] in lisCaden2:
                conj2.add(lisCaden1[i])
    for i in range(len(lisCaden2)):
        if lisCaden2[i].isnumeric() and  lisCaden2[i] not in lisCaden1:
                conj1.add(lisCaden2[i])
    cadFinal1 = str(conj1)
    cadFinal2 = str(conj2)
    print(f"la cadena 1 con los digitos no comunes queda asi : {cadFinal1}")
    print(f"la cadena 2 con las letras comunes queda asi : {cadFinal2}")

def punto_6_cadenas():
     print(" #6  determinar cuantas palabras hay en un parrafo")
     parrafo = input("ingrese su parrafo : ")
     listaParrafo = parrafo.split()
     numPalabras = len(listaParrafo)
     print(f" el parrafo ingresado tiene : {numPalabras} palabras ")

def punto_7_cadenas():
     print("#7  remplazar un caracter de una cadena por otro caracter dado")
     cadena = input("ingrese su cadena : ")
     carac = input("ingrese el caracter que quiere remplazar en la cadena : ")
     caracterRemplazar = input("ingrese el caracter que quiere poner en la cadena : ")
     lisCadena = list(cadena)
     if carac in lisCadena:
          for i in range(len(lisCadena)):
               if lisCadena[i] == carac:
                    lisCadena[i] = caracterRemplazar
     else:
          print("el caracter que quiere remplazar en la cadena no existe en esta ")
     cadena_final = str(" ".join(lisCadena))
     print(f"la cadena con el caracter remplazado quedo asi : {cadena_final}")

def punto_8_cadenas():
     print("#8  se tiene una cadena sacar cual es el caracter que mas se repite")
     cadena = input("ingrese su cadena : ")
     conj =set(cadena)
     lisCadena = list(conj)
     dic = {}
     for i in range(len(lisCadena)):
          dic[lisCadena[i]] = 0

     for caracter in cadena:
        if caracter in dic:
            dic[caracter] += 1
     caracter_mas_repetido = max(dic, key=dic.get)
     frecuencia_maxima = dic[caracter_mas_repetido]
     print(f"el caracter mas repetido es la letra : {caracter_mas_repetido} con una frecuencia de : {frecuencia_maxima} veces")


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
    lista = leerVectorR()
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
    print(f"lista ingresada :{lista}")
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

def punto_1_1():
    lista = [7,7,7,4,8,4,5,6,4,4,4,4]
    print(f"lista ingresada {lista}")
    matriz = [
        [4,4,4,4],
        [20,7,4,3],
        [4,4,4,4],
        [4,4,1,4]
    ]
    print("matriz ingresada :")
    for i in matriz:
        print(i)
    z = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if primo(matriz[i][j]):
                if z == 0:
                    prim_may = matriz[i][j]
                    primo_men = matriz[i][j]
                    prim_may_i = i
                    prim_men_i = i
                    prim_may_j = j
                    prim_men_j = j
                    z = 1
                else:
                    if matriz[i][j] > prim_may:
                        prim_may = matriz[i][j]
                        prim_may_i = i
                        prim_may_j = j
                    elif matriz[i][j] < primo_men:
                        primo_men = matriz[i][j]
                        prim_men_i = i
                        prim_men_j = j

    i, j, x, y = prim_may_i, prim_may_j, prim_men_i, prim_men_j
    b = 0
    contador = 0
    primer_prim = 0
    segundo_prim = 0

    while i < len(matriz) and b == 0:
        while j < len(matriz[0]) and b == 0:
            if i == j and x == y:
                b = 1
            else:
                if primo(matriz[i][j]):
                    contador += 1
                    if contador == 1:
                        primer_prim = matriz[i][j]
                    elif contador == 2:
                        segundo_prim = matriz[i][j]
            j += 1
        j = 0
        i += 1

    contador = 0
    segundo_fibo = 0
    segundo_fibo_i = 0

    while segundo_prim < len(lista):
        if fibonacci(lista[segundo_prim]):
            contador += 1
            if contador == 2:
                segundo_fibo = lista[segundo_prim]
                segundo_fibo_i = segundo_prim
        segundo_prim += 1

    print(f"El segundo Fibonacci entre el rango dado por el primer y segundo primo en la matriz dada por el primo mayor y menor es: {segundo_fibo} y su posición en el vector es: {segundo_fibo_i}")


#SEGUNDO PUNTO



def punto_2_1():
    dic = {
    3 : [4,9,19],
    4 : [13,4,9],
    8 : [4,5,10],
    13 : [2,4,4,8]
    }
    print(f"diccionario ingresado : {dic}")
    def primo_mayor_en_diccionario(diccionario):
        primo_mayor = None  # Inicializamos a None para capturar el primer número primo
        for lista in diccionario.values():  # Iteramos a través de todas las listas en el diccionario
            for numero in lista:
                if primo(numero):
                    if primo_mayor is None or numero > primo_mayor:
                        primo_mayor = numero
        return primo_mayor
    def encontrar_clave_por_valor(diccionario, valor_buscado):
        for clave, lista in diccionario.items():
            if valor_buscado in lista:
                return clave
        return None
    def fibo_men_en_diccionario(diccionario):
        fibo_menor = None
        for lista in diccionario.values():
            for numero in lista:
                if fibonacci(numero):
                    if fibo_menor is None or numero < fibo_menor:
                        fibo_menor = numero
        return fibo_menor
    lista_par = []
    primo_may = primo_mayor_en_diccionario(dic)
    fibo_men = fibo_men_en_diccionario(dic)
    key_prim = encontrar_clave_por_valor(dic, primo_may)
    key_fibo = encontrar_clave_por_valor(dic, fibo_men)
    if key_fibo < key_prim:
        while key_fibo < key_prim:
            if key_fibo % 2 == 0:
                lista_par.append(key_fibo)
            key_fibo +=1
    else:
        while key_prim < key_fibo:
            if key_prim % 2 == 0:
                lista_par.append(key_prim)
            key_prim += 1

    print(lista_par)

def punto_3_1():
    set_1 = set()
    set_2 = set()
    dic = {
    3 : [4,9,19],
    4 : [13,4,9],
    8 : [4,5,10],
    13 : [2,4,4,8]
    }
    print(f"el diccionario ingresado es : {dic}")
    for clave, valores in dic.items():
        if primo(clave):
            for valor in valores:
                if valor % 2 == 0:  # Verifica si el valor es par
                    set_1.add(valor)
        if fibonacci(clave):
            for valor in valores:
                if valor % 2 == 0:
                    set_2.add(valor)
    cadena_1 = str(set_1 & set_2)
    cadena_2 = str(set_1 ^ set_2)

    print(f"primoos : {set_1}")
    print(f"fibos : {set_2}")
    print(f"cadena 1 : {cadena_1}")
    print(f"cadena 2 : {cadena_2}")

def punto_3_2():
    dic = {
        4: [3,2,9,6],
        5: [14,10,2,7],
        8: [2,9,4,6],
        11: [20,10,5,30],
        13: [20,12,4],
        21: [7,2,9],
        3: [4,8,3],  
    }
    print(f"diccionario ingresado : {dic}")
    for key, lista in dic.items():
        if primo(key):
            list_orden = sorted(lista)
            dic[key] = list_orden
        if fibonacci(key) and not primo(key):
            list_orden = sorted(lista, reverse=True)
            dic[key] = list_orden
    print (dic)

def punto_2_2():
    dic = {
        5: [4,7,7,5],
        12: [9,13,8,8],
        8: [5,5,4,34,2],
        2: [9,5,11,11,2]
    }
    print(f"diccionario ingresado : {dic}")
    key_may = max(dic.keys())
    key_men = min(dic.keys())
    set_1 = set()
    set_2 = set()
    for lista in dic.values():
        for num in lista:
            if primo(num):
                set_1.add(num)
            if fibonacci(num):
                set_2.add(num)

    dic[key_may] = set_1
    dic[key_men] = set_2
    print(key_may)
    print(key_men)
    print(dic)

def punto_1_2():
    list = [7,7,10,4,8,4,5,6,4,2,4,4]
    print(f"lista ingresada {list}")
    matriz = [
        [4,3,5,4],
        [4,7,4,3],
        [4,4,4,4],
        [4,4,8,4]
    ]
    print("matriz ingresada :")
    for i in matriz:
        print(i)
    may = None
    men = None
    for i in range(len(list)):
        if may is None or list[i] > may:
            may = list[i]
            may_i = i
        if men is None or list[i] < men:
            men = list[i]
            men_i = i
    cont = 0
    fibo_1 = 0
    fibo_2 = 0
    if may_i < men_i:
        while may_i < len(list):
            if fibonacci(list[may_i]):
                cont +=1
                if cont == 1:
                    fibo_1 = list[may_i]
                elif cont == 2:
                    fibo_2 = list[may_i]
            may_i += 1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == fibo_1:
                i_1 = i
                j_1 = j
            if matriz[i][j] == fibo_2:
                i_2 = i
                j_2 = j
    if i_1 < i_2:
        b = 0
        cont = 0
        i = i_1+1
        while i < len(matriz)-1 and b == 0:
            while j_1 < len(matriz[0]) and b == 0:
                if i_1 == i_2 and j_1 == j_2:
                    b = 1
                else:
                    if primo(matriz[i_1][j_1]):
                        cont +=1
                        
                        if cont == 2:
                            primo_2 = matriz[i_1][j_1]
                            primo_i = i_1
                            primo_j = j_1
                            
                j_1 +=1
            j_1 = 0
            i_1 +=1
    else:
        if i_2 < i_1:
            b = 0
            cont = 0
            j_2 =j_2 + 1
            while i_2 < len(matriz) and b == 0:
                while j_2 < len(matriz[0]) and b == 0:
                    if i_2 == i_1 and j_2 == j_1:
                        b = 1
                    else:
                        if primo(matriz[i_2][j_2]):
                            cont +=1
                            if cont == 1:
                                print(matriz[i_2][j_2])
                            if cont == 2:
                                primo_2 = matriz[i_2][j_2]
                                primo_i = i_2
                                primo_j = j_2
                                
                    j_2 +=1
                j_2 = 0
                i_2 +=1

    print(f"el primo es : {primo_2} y sus posicion es {primo_i },{primo_j}")


def menu_principal():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>
                  
            1. TALLER
                  
            2. EJERCICIOS 
                  
            3. PARCIALES

            0. SALIR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    menu_taller()
                    os.system("pause")
                case 2:
                    menu_ejercicios()
                    os.system("pause")
                case 3:
                    menu_parciales()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion que ingresaste es invalida")
                    os.system("pause")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
def menu_taller():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU TALLER >>>>>>>>>>>>>
                  
            1.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
                  
            3.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.
                  
            5.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
                  
            7.	Se tienen un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.
                  
            9.	Se tienen un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.
                  
            11.	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos 
                  
            13.	13.	Se tiene un conjunto y una matriz con datos numéricos, hallar el primo mayor del conjunto y su factorial y llenar este valor en las posiciones comprendidas entre el par menor y el Fibonacci mayor de la matriz
                  
            15.	Se tienen dos matrices con datos numéricos Formar un diccionario con los primos como clave y las veces que aparecen como valor, ordenado por la clave.
                  
            17.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
                Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
                Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave 
                  
            19.	Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
                el par mayor y las veces que se repite
                el primo menor y las veces que se repite
                el Fibonacci menor y las veces que se repite
                Con estos datos hallar:
                El factorial de la suma del par y del primo
                La multiplicación con sumas de los contadores del primo y del Fibonacci.
                
                
            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    punto_1()
                    os.system("pause")
                case 3:
                    punto_3()
                    os.system("pause")
                case 5:
                    punto_5()
                    os.system("pause")
                case 7:
                    punto_7()
                    os.system("pause")
                case 9:
                    punto_9()
                    os.system("pause")
                case 11:
                    punto_11()
                    os.system("pause")
                case 13:
                    punto_13()
                    os.system("pause")
                case 15:
                    punto_15()
                    os.system("pause")
                case 17:
                    punto_17()
                    os.system("pause")
                case 19:
                    punto_19()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")

def menu_ejercicios():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU EJERCICIOS >>>>>>>>>>>>>
                  
            1. CADENAS
            2. DICCIONARIOS 

            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    menu_cadenas()
                    os.system("pause")
                case 2:
                    menu_diccionarios()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")

def menu_cadenas():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU CADENAS >>>>>>>>>>>>>
                  
            1.  se tiene una cadena contar las veces que se repite un caracter 
                  
            2.  se tiene una cadena ordenarla en forma ascenedete y en forma descendente
                  
            3.  convertir la cadena a mayusculas y minusculas 
                  
            4.  de una cadena dada donde hay digitos y caracteres alfabetico formar dos cadenas , cadena1 con los digitos sin repetidos cadena2 con los alfabeticos sin repetidos
                  
            5.  se tienen dos cadenas formar dos cadenas cadena 1 con los digitos no comunes de las dos cadenas y cadena 2 con las letras comunes de las dos cadenas sin repetir
                  
            6.  determinar cuantas palabras hay en un parrafo
                  
            7.  remplazar un caracter de una cadena por otro caracter dado
                  
            8.  se tiene una cadena sacar cual es el caracter que mas se repite

            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    punto_1_cadenas()
                    os.system("pause")
                case 2:
                    punto_2_cadenas()
                    os.system("pause")
                case 3:
                    punto_3_cadenas()
                    os.system("pause")
                case 4:
                    punto_4_cadenas()
                    os.system("pause")
                case 5:
                    punto_5_cadenas()
                    os.system("pause")
                case 6:
                    punto_6_cadenas()
                    os.system("pause")
                case 7:
                    punto_7_cadenas()
                    os.system("pause")
                case 8:
                    punto_8_cadenas()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")

def menu_diccionarios():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU DICCIONARIOS >>>>>>>>>>>>>
                  
            1. se tiene una lista con datos numericos formar un diccionario donde la clave sea el dato unico y el valor las veces que se repite
                  
            2. se tiene dos listas con datos numericos formar dos diccionarios asi: 
              -d1 con los pirmos comunes com clave y como valor su factorial, 
              -d2 con los fibonacci no comunes y los valores son numeros pares menores al fibonacci
                  
            3. se tiene una cadena donde hay caracteres numericos y alfabeticos repetidos formar dos diccionarios asi: 
              -d1 con el digito y las veces que se repiten
              -d2 con la letra del alfabeto y las veces qye se reputen  
              (ordenados ascendentemente ambos por keys)
            
            4. tengo una lista con datos numericos repetidos  formar dos diccionarios con los datos y las veces que se repite asi :
               d1= ordenar diccionario por keys ascendente
               d2= ordenar el diccionario por clave ascendente


            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    ejercicios_1_diccinarios()
                    os.system("pause")
                case 2:
                    ejercicios_2_diccinarios()
                    os.system("pause")
                case 3:
                    ejercicios_3_diccinarios()
                    os.system("pause")
                case 4:
                    ejercicios_4_diccionarios()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")

def menu_parciales():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU PARCIALES >>>>>>>>>>>>>
            1. parcial N° 1
            2. parcial N° 2

            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    menu_parcial_1()
                    os.system("pause")
                case 2:
                    menu_parcial_2()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
def menu_parcial_1():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU PARCIAl N° 1 >>>>>>>>>>>>>
                  
            UNIVERSIDAD DE NARIÑO
            FACULTAD DE INGENIERÍA
            INGENIERIA DE SISTEMAS
            PROGRAMACIÓN II
            EVALUACIÓN 1


            1.	Se tiene un vector y una matriz con datos numéricos, buscar un dato en el vector que tiene estas condiciones:
                El dato es el segundo Fibonacci de un rango en un vector cuyos límites están determinados por el primo1 y primo2 presentes en el rango de la matriz comprendido entre el mayor y el menor es esta.
                Mostrar el dato y su posición.

            2.	Se tiene un diccionario con la siguiente información
                Clave numero entero
                Valor lista de números
                Hallar la clave del primo mayor y Fibonacci menor que están en las listas de los valores y formar una lista con los pares comprendidos entre estos dos valores y el promedio de estos.
            
            3.	Se tiene un diccionario con la siguiente información
                Clave numero entero
                Valor lista de números
                Formar dos conjuntos asi:
                Conjunto 1 con los número pares de la lista valor de aquellas claves que son primos 
                Conjunto 2 con los número pares de la lista valor de aquella claves que son fibonacci
                Con estos dos conjuntos formar dos cadenas
                Cadena1 con los pares comunes
                Cadena2 con la unión de los pares sin elementos comunes


            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    punto_1_1()
                    os.system("pause")
                case 2:
                    punto_2_1()
                    os.system("pause")
                case 3:
                    punto_3_1()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
def menu_parcial_2():
    os.system("cls")
    while True:
        try:
            print(Fore.GREEN+"""
<<<<<<<<<<<<< MENU PARCIAl N° 2 >>>>>>>>>>>>>
                  
            UNIVERSIDAD DE NARIÑO
            FACULTAD DE INGENIERÍA
            INGENIERIA DE SISTEMAS
            PROGRAMACIÓN II
            EVALUACIÓN 1



            1.	Se tiene un vector y una matriz con datos numéricos
                Buscar un dato en una matriz.
                El dato es el segundo primo de un rango de la matriz cuyos límites están determinados por el Fibonacci 1 y 2 del rango del vector determinado por el número mayor y menor de este.
                Mostrar el dato y su posición

            2.	Se tiene un diccionario con la siguiente información
                Clave numero entero
                Valor lista de números
                Modificar las claves de la clave mayor y la clave menor con la siguiente información:
                Clave mayor: conjunto1
                Clave menor: conjunto2
                Los  conjuntos están formados así:
                Conjunto 1 con los número primos presentes en las diferentes listas sin repetidos 
                Conjunto 2 con los número Fibonacci de las diferentes listas de valores sin repetidos
                  
            3.	Se tiene un diccionario con la siguiente información
                Clave numero entero
                Valor lista de números
                Ordenar las listas de los valores asi:
                En orden ascendente aquellas claves que sean primos
                En orden descendente aquellas claves que sen fibonacci

            0. REGRESAR
""")
            opcion = int(input("ingrese la opcion que desse : -> "))
            match opcion:
                case 1:
                    punto_1_2()
                    os.system("pause")
                case 2:
                    punto_2_2()
                    os.system("pause")
                case 3:
                    punto_3_2()
                    os.system("pause")
                case 0:
                    print("vale, adios")
                    break
                case other:
                    print(Fore.RED+"la opcion ingresada es incorrecta")
        except ValueError:
            print(Fore.RED+"la opcion que digistaste no es la correcta, vuelve a intentarlo :) ")
menu_principal()
