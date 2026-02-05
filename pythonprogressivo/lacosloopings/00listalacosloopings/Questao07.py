# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao07.py

# Faça um programa que leia 5 números e informe o maior número.

for i in range(5):
    num = float(input("Informe um número (%d/5): " % (i+1)))

    if i == 0:
        maior = num
    
    if num > maior:
        maior = num

print("O maior número é", maior)