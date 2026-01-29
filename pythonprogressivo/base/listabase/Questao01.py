# python pythonprogressivo/base/listabase/Questao01.py

#Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.

#Para saber o valor do pi, faça:
#import math
#print(math.pi)

#Pronto, para saber o valor de pi, basta usar 'math.pi', que é um float

import math

r = float(input("Informe o valor do raio do círculo: "))
comprimento = 2 * math.pi * r
area = math.pi * r * r

print("Perímetro do círculo: %.2f" % comprimento)
print("Área do círculo: %.2f" % area)