# python pythonprogressivo/lacosloopings/listafor/Fatorial.py

#  Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.

fatorial = 1
n = int(input("Informe um número inteiro: "))

for i in range(n):
    fatorial *= (n - i)

print("%d! = %d" % (n, fatorial))