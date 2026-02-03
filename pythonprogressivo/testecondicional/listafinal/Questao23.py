# python pythonprogressivo/testecondicional/listafinal/Questao23.py

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                          Até 5 Kg                 Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

print("""               Até 5 Kg               Acima de 5 Kg
Morango      R$ 2,50 por Kg          R$ 2,20 por Kg  
Maçã         R$ 1,80 por Kg          R$ 1,50 por Kg""")

kg_morango = float(input("Informe a quantidade (em kg) que você deseja de morangos: "))
kg_maca = float(input("Informe a quantidade (em kg) que você deseja de maças: "))

if kg_morango == 0 and kg_maca == 0:
    print("Você informou um valor inesperado. O programa não será executado.")
else:
    if kg_morango <= 5:
        valor_morango = 2.5 * kg_morango
    else:
        valor_morango = 2.2 * kg_morango
    
    if kg_maca <= 5:
        valor_maca = 1.8 * kg_maca
    else:
        valor_maca = 1.5 * kg_maca
    
    valor_total = valor_morango + valor_maca

    if (kg_maca + kg_morango > 8) or valor_total > 25:
        valor_total = valor_total * 0.9

    print("Valor total: %.2f" % valor_total)