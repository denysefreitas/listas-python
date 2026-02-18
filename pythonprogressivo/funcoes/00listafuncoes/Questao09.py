# python pythonprogressivo/funcoes/00listafuncoes/Questao09.py

#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimirLinhas(n):
    for i in range(1, n + 1):
        imprimirColunas(i)
        print()

def imprimirColunas(i):
    for j in range(i):
        print(j + 1, end = " ")

n = int(input("Informe um número: "))
imprimirLinhas(n)

