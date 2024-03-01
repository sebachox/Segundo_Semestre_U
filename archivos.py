ruta = r"C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\calificaiones.txt"
f = open(ruta, "w")
f.write("1 3.5 3.5 5\n")
f.write("2 1 1 1\n")
f.write("3 5 5 5\n")
f.write("4 4.5 4.5 4.5")
f = open(ruta, "r")
f.seek(0)
l = f.readlines()
l1 = []
for linea in l:
    linea.split(linea)
    linea.strip(linea)
    print(linea)
    l1.append(linea)
numero_s = []
aux = []
calificaciones = []
for i in range(len(l1)):
    for j in range(len(l[0])):
        if j == 0:
            numero_s.append(l1[i][0])
        else: aux.append(l1[i][j])
    calificaciones.append(aux)
    aux.clear

print(numero_s)
print(calificaciones)


            

