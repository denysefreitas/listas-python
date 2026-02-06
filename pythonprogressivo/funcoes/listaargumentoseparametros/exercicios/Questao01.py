# python pythonprogressivo/funcoes/listaargumentoseparametros/exercicios/Questao01.py

# Crie uma função que recebe um número e exiba seu quadrado.

def exibirQuadrado(a):
    print("%.2f ao quadrado é %.2f" % (a, a ** 2))

num = float(input("Informe um número a ser elevado ao quadrado: "))
exibirQuadrado(num)