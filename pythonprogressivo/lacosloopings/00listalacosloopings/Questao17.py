# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao17.py

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial = 1
n = int(input("Informe um número inteiro: "))

for i in range(n):
    fatorial *= (n - i)

print("%d! = %d" % (n, fatorial))