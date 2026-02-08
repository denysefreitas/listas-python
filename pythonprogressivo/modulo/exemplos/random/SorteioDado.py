# python pythonprogressivo/modulo/exemplos/random/SorteioDado.py

# Crie um programa em Python que simula o resultado de um dado, ou seja, gera números aleatórios de 1 até 6, quantas vezes o usuário desejar.

import random 

while True:
    num_sorteado = random.randint(1, 6)
    print("O número sorteado foi...", num_sorteado)

    opcao = input("Deseja sortear outro número? (S - SIM / N - NÃO): ")

    if opcao == "N":
        break