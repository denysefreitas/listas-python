# python pythonprogressivo/testecondicional/listafinal/Questao16.py

# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão): %

num = int(input("Informe um número: "))

if num % 2 == 0:
    print("O número %d é par" % num)
else:
    print("O número %d é ímpar" % num)