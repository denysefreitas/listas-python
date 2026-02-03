# python pythonprogressivo/testecondicional/listafinal/Questao24.py

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                          Até 5 Kg               Acima de 5 Kg
#    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#    Alcatra           R$ 5,90 por Kg          R$ 6,80 por Kg
#    Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg

#    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar

print("""                          Até 5 Kg               Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra           R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg""")
print("Você pode levar somente um tipo de carne da promoção. Não há limites de quantidade de quilos da carne escolhida.")
carne = input("Informe o tipo de carne escolhido: ")
carne = carne.upper()

if carne != "FILE DUPLO" and carne != "ALCATRA" and carne != "PICANHA":
    print("Você informou um valor inesperado. O programa não será executado.")
else:
    if carne == "FILE DUPLO":
        nome_carne = "Filé Duplo"
    elif carne == "ALCATRA":
        nome_carne = "Alcatra"
    else:
        nome_carne = "Picanha"
    
    kg = float(input("Informe a quantidade de %s que você deseja: " % nome_carne))
    
    if kg <= 0:
        print("Você informou um valor inesperado. O programa não será executado.")
    else:
        if kg <= 5:
            if carne == "FILE DUPLO":
                valor_kg = 4.9
            elif carne == "ALCATRA":
                valor_kg = 5.9
            else:
                valor_kg = 6.9
        else:
            if carne == "FILE DUPLO":
                valor_kg = 5.8
            elif carne == "ALCATRA":
                valor_kg = 6.8
            else:
                valor_kg = 7.8
        
        valor_total = valor_kg * kg

        print("Método de pagamento: ")
        print("P - Pix")
        print("D - Débito")
        print("C - Crédito")
        print("T - Cartão Tabajara")
        metodo_pagamento = input("Informe o método de pagamento escolhido: ")
        metodo_pagamento = metodo_pagamento.upper()

        if metodo_pagamento != "P" and metodo_pagamento != "D" and metodo_pagamento != "C" and metodo_pagamento != "T":
            print("Você informou um valor inesperado. O programa não será executado.")
        else:
            if metodo_pagamento == "P":
                nome_metodo = "Pix"
            elif metodo_pagamento == "D":
                nome_metodo = "Débito"
            elif metodo_pagamento == "C":
                nome_metodo = "Crédito"
            else:
                nome_metodo = "Cartão Tabajara"

            if metodo_pagamento == "T":
                desconto = 0.1 * valor_total
            else:
                desconto = 0
            
            valor_com_desconto = valor_total - desconto

            print("CUPOM FISCAL\n-------------------------")
            print("Tipo de carne:", nome_carne)
            print("Quantidade de carne: %.2f kg" % kg)
            print("Preço total: %.2f" % valor_total)
            print("Tipo de pagamento:", nome_metodo)
            print("Valor do desconto: R$", desconto)
            print("Valor a pagar: R$", valor_com_desconto)