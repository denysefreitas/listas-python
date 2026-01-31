# python pythonprogressivo/testecondicional/listafinal/Questao04.py

# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

a = int(input("Informe um número inteiro: "))
b = int(input("Informe outro número inteiro: "))
c = int(input("Informe outro número inteiro: "))

maior = a
menor = a

# Qual é o maior?
if b > maior:
    maior = b

if c > maior:
    maior = c

# Qual é o menor?
if b < menor:
    menor = b

if c < menor:
    menor = c

print("RESULTADOS\n------------------------------")
print("Maior: %d \nMenor: %d" % (maior, menor))