# python pythonprogressivo/funcoes/listaargumentoseparametros/exemplos/Calculadora.py

# Crie um programa que peça ao usuário dois valores. Estes números deverão ser repassados para uma função chamada calculadora, que vai mostrar a soma, subtração, divisão e multiplicação desses números.

def calculadora(a, b):
    print("CALCULADORA")
    print("-------------------------")
    print("Soma:", a + b)
    print("Subtração:", a - b)
    print("Multiplicação:", a * b)
    if(isZero(b)):
        print("Divisão: impossível")
    else:
        print("Divisão:", a / b)

def isZero(b):
    return b == 0

a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))

calculadora(a, b)