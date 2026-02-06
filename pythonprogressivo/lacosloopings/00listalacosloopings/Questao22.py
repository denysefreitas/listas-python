# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao22.py

# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

divisores = 0
num = int(input("Informe um número: "))

print("O número %d é divisível pelos números:" % num, end = " ")
for i in range(2, num + 1):
    if num % i == 0:
        if i == num:
            print(i)
        else:
            print(i, end = ", ")
        divisores += 1

if divisores > 2:
    print("Logo, o número %d não é primo" % num)
else:
    print("Logo, o número %d é primo" % num)