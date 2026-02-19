# python pythonprogressivo/listas/exemplos/ExMatriz03.py

matriz = [ [1 for i in range(4)] for j in range(4)]

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end = " ")
    print()