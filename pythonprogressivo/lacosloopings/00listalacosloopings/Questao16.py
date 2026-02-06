# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao16.py

# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

count = 0
a1 = 0
a1 = int(a1)
a2 = 1
a2 = int(a2)

while True:
    if a1 > 500:
        break

    print(a1, end = " ")
    a2 += a1
    a1 = a2 - a1
    