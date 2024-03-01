import random
def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
    return matriz

def leerVectorR():
    cd = int(input('Cantidad de datos lista -> '))
    lista = [random.randint(1, 10) for _ in range(cd)]
    return lista

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
    
#determinar si un valor es primo 

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

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
    matriz = [
        [4,3,5,4],
        [4,7,4,3],
        [4,4,4,4],
        [4,4,8,4]
    ]
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

