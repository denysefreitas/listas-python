# python pythonprogressivo/lacosloopings/listawhile/Fatorial.py

#  Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.

n = int(input("Informe um número inteiro: "))
count = 0
fatorial = 1

while count < n:
    fatorial *= (n - count)
    count += 1

print("%d! = %d" % (n, fatorial))