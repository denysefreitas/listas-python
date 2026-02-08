# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao41.py

# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67

valor_divida = float(input("Informe o valor da dívida: "))
valor_juros = 0.0
valor_parcela = 0.0
taxa = 0

print("Valor da Dívida | Valor dos Juros | Quantidade de parcelas | Valor da Parcela")
valor_parcela = valor_divida
print(f"R$ {valor_divida} |  {valor_juros}  | {1} |  R$ {valor_parcela}")
taxa += 10

for parcelas in range(3, 13, 3):
    valor_juros = valor_divida * (taxa / 100)
    valor_dividaAtual = valor_divida + valor_juros
    valor_parcela =  valor_dividaAtual / parcelas

    print(f"R$ {valor_dividaAtual} | {valor_juros} | {parcelas} | R$ {valor_parcela:.2f}")

    taxa += 5