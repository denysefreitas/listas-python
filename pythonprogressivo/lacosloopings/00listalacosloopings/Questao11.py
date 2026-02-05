# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao11.py

# Altere o programa anterior para mostrar no final a soma dos números.

soma = 0
a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

if a > b:
    inicio = b
    final = a
else:
    inicio = a
    final = b

for i in range(inicio + 1, final):
    soma += i
    print(i, end = " ")

print("\nSoma:", soma)