# python pythonprogressivo/lacosloopings/listaloopsaninhados/Tabuleiro.py

# Faça um programa em Python que solicite um número positivo inteiro ao usuário, e depois exiba um tabuleiro na tela, com igual número de linhas e colunas.

n = int(input("Informe um número inteiro positivo: "))

if n <= 0:
    print("Você informou um parâmetro inesperado. O programa não será executado")
else:
    for i in range(n):
        for j in range(n):
            print("X", end = " ")
        print()
        