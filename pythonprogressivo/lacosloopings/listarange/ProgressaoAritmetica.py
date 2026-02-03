# python pythonprogressivo/lacosloopings/listarange/ProgressaoAritmetica.py

# Crie um programa que pergunte ao usuário o termo inicial e a razão de uma PA.
#Em seguida, pergunte a ele quantos elementos da PA ele deseja que seja impresso, e imprima todos os elementos dessa progressão Aritmética, do primeiro termo até o termo 'n' escolhido pelo usuário.

a1 = float(input("Informe o termo inicial da PA: "))
r = float(input("Informe a razão da PA: "))

if r == 0:
    print("Você informou um parâmetro inesperado. O programa não será executado.")
else:
    n = int(input("Informe quantos elementos você deseja que seja impresso: "))

    for i in range(n):
        an = a1 + i * r
        print("Termo %d: %.2f" % (i + 1, an))