# python pythonprogressivo/listas/exemplos/ExMatriz02.py

matriz = []
aux = 0

for i in range(4):
    linha = []

    for j in range(4):
        linha.append(aux)
        aux += 1

    matriz.append(linha)

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end = " ")
    print()