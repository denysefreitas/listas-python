# python pythonprogressivo/testecondicional/listafinal/Questao15.py

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int( input("Informe o dia: "))
mes = int( input("Informe o mês: "))
ano = int( input("Informe o ano: "))

EBissexto = False
EValidoDia = False
EValidoMes = False
EValidoAno = False

if (ano % 400 == 0 ) or (ano % 100 != 0 and ano % 4 == 0):
    EBissexto = True

if ano > 0:
    EValidoAno = True

if mes >= 0 and mes <= 12:
    EValidoMes = True

    if mes == 2:
        if EBissexto and dia <= 29:
            EValidoDia = True
        elif dia < 28:
            EValidoDia = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            EValidoDia = True
    else:
        if dia <= 31:
            EValidoDia = True

if EValidoDia and EValidoMes and EValidoAno:
    print("A data é válida: %d/%d/%d" % (dia, mes, ano))
else:
    print("A data não é válida")
    

