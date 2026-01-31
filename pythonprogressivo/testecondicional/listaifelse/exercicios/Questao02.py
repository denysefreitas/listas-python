# python pythonprogressivo/testecondicional/listaifelse/exercicios/Questao02.py

# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Informe um valor: "))

if valor > 0:
    print("O valor %.2f é positivo" % valor)
elif valor == 0:
    print("O valor não é positivo nem negativo, pois é o %.2f" % valor)
else:
    print("O valor %.2f é negativo" % valor)