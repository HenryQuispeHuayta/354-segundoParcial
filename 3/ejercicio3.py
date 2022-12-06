import pandas as pd

datos = pd.read_csv('matriz.csv', header=0)

array1 = []
array2 = []
top = 0
inf = 0
min1 = []
min2 = []
PG = []
MG = []
distancias = []

for j in range(4):
    fila = datos.iloc[j]
    for i in range(4):
        array2.append(fila[i])
    array1.append(array2)
    array2 = []

for i in range(4):
    for j in range(4):
        if array1[i][j] != 0:
            min1.append(array1[i][j])
    min2.append(min(min1))
    min1 = []

min1moG = sum(min2)

for j in range(4):

    PL = []
    topaux = 0
    infaux = 0
    ML = []
    nodoM = 9999
    listaM = []
    ifal = 0
    ifals = []
    yfals = []
    k = 0
    l = 0

    if j != 0:
        top = j
        inf = 0
        PL.append(inf)
        PL.append(top)
        ML.append(array1[0][j])
        topaux = top
        ifal = inf
        ifals.append(ifal)
        yfals.append(topaux)
        while k < 4:
            ifal = topaux
            if ifal not in ifals:
                ifals.append(ifal)
                while l < 4:
                    if l not in yfals and l != 0:
                        if array1[ifal][l] != 0:
                            if array1[ifal][l] < nodoM:
                                nodoM = array1[ifal][l]
                                infaux = ifal
                                topaux = l
                    l += 1
                    if l != 0 and topaux not in yfals:
                        yfals.append(topaux)
                        PL.append(topaux)
                        ML.append(nodoM)
                        ifal = topaux
            k += 1
            l = 0
            nodoM = 9999
            if len(ML) == 3:
                ML.append(array1[topaux][0])
    k = 0
    MG.append(ML)
    PG.append(PL)
    distancias.append(sum(ML))

print('Recorridos: ', distancias)
