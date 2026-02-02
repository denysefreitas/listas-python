# python pythonprogressivo/lacosloopings/listawhile/Exemplo02.py

# Faça um programa que peça um número maior que 1 ao usuário. Em seguida, imprima todos os números, de 1 até o número que o usuário informou

max = int(input("Informe um número: "))
max += 1

count = 1

while count <= max:
    print(count)
    count += 1