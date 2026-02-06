# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao18.py

# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

soma = 0.0
n = int(input("Informe a quantidade de valores: "))

for i in range(n):
    num = float(input("Informe um valor (%d/%d): " % (i + 1, n)))
    soma += num

    if i == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

print("Soma:", soma)
print("Menor:", menor)
print("Maior:", maior)