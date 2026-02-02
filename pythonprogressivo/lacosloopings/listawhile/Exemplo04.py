# python pythonprogressivo/lacosloopings/listawhile/Exemplo04.py

# Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido

count = 1
max = int(input("Informe um número: "))

if max <= 0:
    print("O valor informado está fora dos parâmetros esperados. O programa não será executado.")
else:
    while count <= max:
        if count % 2 == 0:
            print(count)
            
        count += 1
