# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao10.py

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

if a > b:
    inicio = b
    final = a
else:
    inicio = a
    final = b

for i in range(inicio + 1, final):
    print(i, end = " ")