# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao15.py

# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

a1 = 0
a1 = int(a1)
a2 = 1
a2 = int(a2)

n = int(input("Informe a quantidade de números da série de Fibonnaci: "))

for i in range(n):
    print(a1, end = " ")
    a2 += a1
    a1 = a2 - a1
    

