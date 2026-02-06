# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao21.py

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

divisores = 0
num = int(input("Informe um número: "))

for i in range(2, num + 1):
    if num % i == 0:
        divisores += 1

if divisores > 2:
    print("O número %d não é primo" % num)
else:
    print("O número %d é primo" % num)