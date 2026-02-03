# python pythonprogressivo/testecondicional/listafinal/Questao22.py

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#    Álcool: até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro

#    Gasolina:
#    até 20 litros, desconto de 4% por litro
#    acima de 20 litros, desconto de 6% por litro 

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

valor_alcool = 1.9
valor_gasolina = 2.5

litros = int(input("Informe a quantidade de litros vendidos: "))

if litros <= 0:
    print("Você informou um parâmetro inesperado. O programa não será executado.")
else: 
    print("A - Álcool\nG - Gasolina")
    combustivel = input("Informe o tipo de combustível: ")
    combustivel = combustivel.upper()

    if combustivel != "A" and combustivel != "G":
        print("Você informou um parâmetro inesperado. O programa não será executado.")
    else:
        if litros <= 20:
            if combustivel == "A":
                valor_combustivel = valor_alcool
                desconto = 0.03
            else:
                valor_combustivel = valor_gasolina
                desconto = 0.04
        else:
            if combustivel == "A":
                valor_combustivel = valor_alcool
                desconto = 0.05
            else:
                valor_combustivel = valor_gasolina
                desconto = 0.06
        
        valor_total = valor_combustivel * (1 - desconto) * litros
        print("Valor total: %.2f" % valor_total)