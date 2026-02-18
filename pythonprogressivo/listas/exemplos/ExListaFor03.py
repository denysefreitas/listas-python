# python pythonprogressivo/listas/exemplos/ExListaFor03.py

# Faça com que o script anterior também calcule a soma de todos os elementos na lista numeros e exiba seu resultado.

numeros = []
soma = 0

for i in range(10):
    numeros.append(i)

for item in range(len(numeros)):
    print(item)
    soma += item

print(f"Soma: {soma}")