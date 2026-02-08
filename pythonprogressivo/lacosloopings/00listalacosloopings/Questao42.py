# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao42.py

# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

intervalo1 = 0 
intervalo2 = 0 
intervalo3 = 0 
intervalo4 = 0

while True:
    num = float(input("Informe um valor [0 - 100]: "))

    if num < 0:
        break

    if num >= 0 and num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    elif num <= 100:
        intervalo4 += 1
    
print("Analisando os números informados...")
print(f"{intervalo1} número(s) estão no intervalo [0-25]")
print(f"{intervalo2} número(s) estão no intervalo [26-50]")
print(f"{intervalo3} número(s) estão no intervalo [51-75]")
print(f"{intervalo4} número(s) estão no intervalo [76-100]")
print("Programa finalizado.")