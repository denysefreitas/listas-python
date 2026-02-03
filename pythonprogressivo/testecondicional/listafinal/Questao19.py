# python pythonprogressivo/testecondicional/listafinal/Questao19.py

# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Informe um número: "))

if num == round(num):
    print("Número inteiro")
else:
    print("Número decimal")