# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao08.py

# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0.0

for i in range(5):
    num = float(input("Informe um número (%d/5): " % (i+1)))
    soma += num
    

print("Soma:", soma)
print("Média:", soma/5)