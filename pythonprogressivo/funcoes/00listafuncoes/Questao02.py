# python pythonprogressivo/funcoes/00listafuncoes/Questao02.py

# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função. Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.

def somar(a, b, c):
    return a + b + c

def calcularMedia (a, b, c):
    soma = somar(a, b, c)
    print(f"Média dos números ({a}, {b}, {c}): {soma / 3:.2f}")

num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))
num3 = float(input("Informe um número: "))

calcularMedia(num1, num2, num3)