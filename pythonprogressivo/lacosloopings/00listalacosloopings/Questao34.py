# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao34.py

# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

def ePrimo(num):
    multiplos = 0
    multiplos = int(multiplos)

    for i in range(2, num):
        if num % i == 0:
            multiplos += 1
    
    return multiplos == 0

num = int(input("Informe um número: "))

if (ePrimo(num)):
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")