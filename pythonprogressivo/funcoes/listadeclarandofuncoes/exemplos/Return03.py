# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/Return03.py

# Crie um programa em Python que diz se o número inserido pelo usuário é par ou ímpar. Ele deve fazer isso através de uma função que recebe o inteiro e retorna True ou False.

def ePar(num):
    return num % 2 == 0

num = int(input("Informe um número: "))

if ePar(num):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")