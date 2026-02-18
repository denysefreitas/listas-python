# python pythonprogressivo/funcoes/00listafuncoes/Questao08.py

#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimirLinhas(n):
    for i in range(1, n + 1):
        imprimirColunas(i)
        print()

def imprimirColunas(i):
    for j in range(i):
        print(i, end = " ")

n = int(input("Informe um número: "))
imprimirLinhas(n)