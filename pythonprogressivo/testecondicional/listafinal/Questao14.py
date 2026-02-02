# python pythonprogressivo/testecondicional/listafinal/Questao14.py

# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            situacao = "é bissexto"
        else: 
            situacao = "não é bissexto"
    else:
        situacao = "é bissexto"
else:
    situacao = "não é bissexto"

print("O ano %d %s" % (ano, situacao))