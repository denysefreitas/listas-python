# python pythonprogressivo/testecondicional/listafinal/Questao03.py

#  Faça um Programa que leia três números inteiros e mostre o maior deles.

a = int(input("Informe um número inteiro: "))
b = int(input("Informe outro número inteiro: "))

if a > b:
    maior = a
else:
    maior = b

c = int(input("Informe outro número inteiro: "))

if c > maior:
    maior = c

print("O maior número é %d" % maior)

