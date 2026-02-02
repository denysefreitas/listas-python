# python pythonprogressivo/testecondicional/listafinal/Questao09.py

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% 

#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R$ 1100,00
#    (-) IR (5%)                                : R$   55,00 
#    (-) INSS ( 10%)                       : R$  110,00
#    FGTS (11%)                            : R$  121,00
#    Total de descontos                : R$  165,00
#    Salário Liquido                       : R$  935,00

valor_hora = float(input("Informe o valor da sua hora: "))

if valor_hora < 0:
    print("Você informou um valor impossível. O programa não será executado.")
else:
    horas = int(input("Informe a quantidade de horas trabalhadas: "))

    if horas < 0:
        print("Você informou uma quantidade de horas inválida. O programa não será executado.")
    else:
        salario_bruto = valor_hora * horas
        fgts = salario_bruto * 0.11
        inss = salario_bruto * 0.1

        if salario_bruto <= 900:
            desconto = 0
        elif salario_bruto <= 1500:
            desconto = 0.05
        elif salario_bruto <= 2500:
            desconto = 0.1
        else:
            desconto = 0.2
        
        ir = salario_bruto * desconto
        total_descontos = ir + inss
        salario_liquido = salario_bruto - total_descontos

        print("Salário Bruto (%d * %.2f)       : R$ %.2f" % (horas, valor_hora, salario_liquido))
        print("(-) IR (%d)                       : R$ %.2f" % (desconto * 100, ir))
        print("(-) INSS (10%)                   : R$", inss)
        print("FGTS (11%)                       : R$", fgts)
        print("Total de descontos               : R$", total_descontos)
        print("Salário Líquido                  : R$", salario_liquido)

        