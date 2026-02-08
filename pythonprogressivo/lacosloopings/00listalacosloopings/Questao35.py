# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao35.py

# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def ePrimo(num):
    multiplos = 0
    multiplos = int(multiplos)

    for i in range(2, num):
        if num % i == 0:
            multiplos += 1
    
    return multiplos == 0

num = int(input("Informe um número: "))

for i in range(2, num):
    if (ePrimo(i)):
        print(i, end = " ")