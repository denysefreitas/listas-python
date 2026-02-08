# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao31.py

# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
#...

soma = 0.0
count = 1
count = int(count)

def informarProdutos():
    global count
    while True:
        valor = float(input(f"Produto {count}: R$ "))

        if valor >= 0:
            count += 1
            return valor
        
        print("Valor inválido")

def informarDinheiro():
    global soma

    while True:
        dinheiro = float(input("Dinheiro: R$ "))

        if dinheiro > soma:
            print("Dinheiro: R$", dinheiro)
            print("Troco: R$", dinheiro - soma)
            break

        print("Valor insuficiente")

while True:
    print("Lojas Tabajara")
    while True:
        valor = float(informarProdutos())
        soma += valor

        if valor == 0:
            break

    print("Total: R$", soma)
    informarDinheiro()

    resposta = input("Deseja informar uma nova compra? (S - SIM / N - NÃO) ")

    if resposta == "N":
        break