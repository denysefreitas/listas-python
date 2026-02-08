# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao43.py

# O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

def imprimirCardapio():
    print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00""")
    
def calcularPreco(codigo, quantidade):
    if codigo == "100":
        valor = 1.2
    elif codigo == "101":
        valor = 1.3
    elif codigo == "102":
        valor = 1.5
    elif codigo == "103":
        valor = 1.2
    elif codigo == "104":
        valor = 1.3
    else:
        valor = 1
    
    return valor * quantidade

soma = 0.0

while True:
    imprimirCardapio()

    while True:
        codigo = input("Informe o código do produto: ")

        if codigo == "100" or codigo == "101" or codigo == "102" or codigo == "103" or codigo == "104" or codigo == "105":
            break

        print("Código inválido")

    while True:
        qnt = int(input(f"Informe a quantidade desejada do produto de código {codigo}: "))

        if qnt > 0:
            break

        print("Quantidade inválida.")

    valor = calcularPreco(codigo, qnt)
    soma += valor
    print(f"Valor a ser pago (código do produto: {codigo}): R$ {valor:.2f}")

    opcao = input("Deseja encerrar o pedido? (S - SIM / N - NÃO): ")

    if opcao == "S":
        break

print(f"Valor total da compra: R$ {soma:.2f}")