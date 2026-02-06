# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao20.py

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

fatorial = 1

while True:
    n = int(input("Informe um número inteiro para ser calculado o seu fatorial [0-16]: "))

    if n > 0 and n < 16:
        for i in range(n):
            fatorial *= (n - i)
        break;

    print("Valor inválido")

print("%d! = %d" % (n, fatorial))