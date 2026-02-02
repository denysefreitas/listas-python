# python pythonprogressivo/testecondicional/listafinal/Questao08.py

#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5%
 
# Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.

salario = float(input("Informe o salário do colaborador: "))

if salario < 0:
    print("Você informou um valor impossível. O programa não será executado.")
else:
    if salario <= 280:
        percentual_aumento = 0.2
        
    elif salario <= 700:
        percentual_aumento = 0.15

    elif salario <= 1500:
        percentual_aumento = 0.1

    else:
        percentual_aumento = 0.05

    valor_aumento = salario * percentual_aumento
    salario_novo = salario + valor_aumento
            
    print("Salário atual: %.2f" % salario)
    print("Percentual de aumento:", percentual_aumento, "%")
    print("Valor de aumento: %.2f" % valor_aumento)
    print("Novo salário: %.2f" % salario_novo)