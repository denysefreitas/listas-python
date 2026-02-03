# python pythonprogressivo/testecondicional/listafinal/Questao18.py

#  Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Informe o valor a ser sacado (R$10 - R$600): "))

if saque >= 10 and saque <= 600:
    print("[AVISO] O caixa eletrônico vai fornecer a menor quantidade de notas possíveis.")
    # Quantidade de notas de R$ 100 e informar o resto a ser sacado
    notas_cem = saque // 100
    resto_saque = saque - (notas_cem * 100)

    # Quantidade de notas de R$ 50 e atualizar o resto a ser sacado
    notas_cinquenta = resto_saque // 50
    resto_saque = resto_saque - (notas_cinquenta * 50)

    # Quantidade de notas de R$ 10 e atualizar o resto a ser sacado
    notas_dez = resto_saque // 10
    resto_saque = resto_saque - (notas_dez * 10)

    # Quantidade de notas de R$ 5 e atualizar o resto a ser sacado
    notas_cinco = resto_saque // 5
    resto_saque = resto_saque - (notas_cinco * 5)

    # Quantidade de notas de R$ 1
    notas_um = resto_saque

    print("O valor R$%d será sacado em: %d nota(s) de R$100, %d nota(s) de R$50, %d nota(s) de R$10, %d nota(s) de R$5, %d nota(s) de R$1" % (saque, notas_cem, notas_cinquenta, notas_dez, notas_cinco, notas_um))
else:
    print("Você informou um valor inesperado. O programa não será executado.")