# python pythonprogressivo/funcoes/listavariaveis/exemplos/VariaveisGlobais.py

# Escreva um script em Python que pergunta o preço de um produto e mostre:
#Preço original
#Desconto em porcentagem
#Valor do desconto
#Preço com o desconto

#O desconto quem define é o gerente, na forma de variável global.

desconto = 10 # %

def calcularDesconto(valor):
    global desconto
    valorDesconto = valor * (1 - desconto/100)

    print(f"Preço original: {valor:.2f}")
    print(f"Desconto: {desconto:.2f}%")
    print(f"Valor do desconto: {valorDesconto:.2f}")
    print(f"Preço com o desconto: {valor - valorDesconto:.2f}")

calcularDesconto(10)

    