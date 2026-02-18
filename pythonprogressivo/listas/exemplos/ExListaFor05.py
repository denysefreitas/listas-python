# python pythonprogressivo/listas/exemplos/ExListaFor05.py

# Faça um script que exiba a uma lista que tem os números de 1 até 10, na seguinte maneira:
#Numero  1:  1
#Numero  2:  2
#Numero  3:  3
#...
#Numero 10: 10

numeros = []

for i in range(1, 11):
    numeros.append(i)

for i in range(1, len(numeros) + 1):
    print(f"Número {i}: {i}")