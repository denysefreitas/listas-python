# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao14.py

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

pares = 0
impares = 0

for i in range(10):
    num = int(input("Informe um número (%d/10): " % (i+1)))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares", impares)