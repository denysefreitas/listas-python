# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao32.py

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

n = int(input("Informe um número inteiro: "))
count = 0
fatorial = 1

print("Fatorial de:", n)
print(f"{n}! =", end = " ")
while count < n:
    fatorial *= (n - count)
    
    count += 1

    if count == (n - 1):
        print(f"{n - count} =", end = " ")
    elif n != count:
        print(f"{n - count} .", end = " ")

print(fatorial)