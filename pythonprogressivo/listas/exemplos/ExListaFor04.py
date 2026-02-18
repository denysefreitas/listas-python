# python pythonprogressivo/listas/exemplos/ExListaFor04.py

# Faça um script que exibe uma lista de 10 elementos, contados de 1 até 10.
# Depois, dobre cada valor dessa lista e exiba. Veja que agora são todos pares.

numeros = []

for i in range(1, 11):
    numeros.append(i)
    print(i)

for i in range(len(numeros)):
    numeros[i] *= 2
    print(numeros[i])