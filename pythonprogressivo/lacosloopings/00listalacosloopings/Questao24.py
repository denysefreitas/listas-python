# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao24.py

# Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0.0
n = int(input("Informe a quantidade de notas: "))

for i in range(n):
    nota = float(input("Informe uma nota (%d/%d): " % (i + 1, n)))
    soma += nota

print("Média aritmética:", soma/n)
