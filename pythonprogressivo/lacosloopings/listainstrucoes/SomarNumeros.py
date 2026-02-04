# python pythonprogressivo/lacosloopings/listainstrucoes/SomarNumeros.py

# Escreva um programa em Python que vai somar todos os números de 1 até 1 milhão, menos os que são múltiplos de 3.

#A soma total ficará armazenada em total.

total = 0

for num in range(1, 1000001):
    if num % 3 != 0:
        total += num

print("Soma:", total)