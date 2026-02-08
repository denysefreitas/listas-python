# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/Return01.py

# Crie um programa em Python que tenha a função soma(x,y) que recebe dois números e retorna o valor da soma deles

def calcularSoma(a, b):
    return a + b

a = float(input("Informe um valor: "))
b = float(input("Informe outro valor: "))

print(f"{a:.2f} + {b:.2f} = {calcularSoma(a, b):.2f}")