# python pythonprogressivo/testecondicional/listafinal/Questao13.py

# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

#PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)

import math

print("Equaçao do 2° grau da forma: ax² + bx + c")
a = float(input("Informe o valor do coeficiente 'a': "))

if a == 0:
    print("A equação não é do segundo grau. O programa não será executado.")
else:
    b = float(input("Informe o valor do coeficiente 'b': "))
    c = float(input("Informe o valor do coeficiente 'c': "))

    delta = (b * b) - (4 * a * c)
    
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        r1 = (-b + math.sqrt(delta)) / (2 * a)

        print("A equação possui uma única raiz real, x =", r1)
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)

        print("A equação possui duas raízes reais distintas, x = %d e x' = %d" % (r1, r2))
    