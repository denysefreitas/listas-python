# python pythonprogressivo/funcoes/listaargumentoseparametros/exercicios/Questao02.py

# Crie uma função que recebe um número e exiba seu quadrado.

def exibirQuadrado(a):
    print("%.2f ao cubo é %.2f" % (a, a ** 3))

num = float(input("Informe um número a ser elevado ao cubo: "))
exibirQuadrado(num)