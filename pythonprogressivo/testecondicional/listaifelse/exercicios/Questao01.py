# python pythonprogressivo/testecondicional/listaifelse/exercicios/Questao01.py

#Faça um programa que peça dois números e imprima o maior deles.

a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))

if a > b:
    print("O número %.2f é maior do que o %.2f" % (a, b))
elif a == b:
    print("Os números são iguais")
else:
    print("O número %.2f é maior do que o %.2f" % (b, a))