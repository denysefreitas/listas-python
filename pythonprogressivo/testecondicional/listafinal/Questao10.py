# python pythonprogressivo/testecondicional/listafinal/Questao10.py

# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input("Informe um valor (1 - 7) para ser exibido o dia da semana correspondente: "))

if num == 1:
    msg = "Domingo"
elif num == 2:
    msg = "Segunda"
elif num == 3:
    msg = "Terça-feira"
elif num == 4:
    msg = "Quarta-feira"
elif num == 5:
    msg = "Quinta-feira"
elif num == 6:
    msg = "Sexta-feira"
elif num == 7:
    msg = "Sábado"
else:
    msg = "Valor inválido"

print(msg)