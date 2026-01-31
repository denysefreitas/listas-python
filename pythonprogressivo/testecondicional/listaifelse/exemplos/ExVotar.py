# python pythonprogressivo/testecondicional/listaifelse/exemplos/ExVotar.py

# Para votar, você deve ter entre 18 anos e menos de 65 anos.
# Escreva um programa que pergunte sua idade e diga se você é obrigado a votar ou não.

idade = int(input("Informe a sua idade: "))

if idade < 0:
    print("Você digitou uma idade inválida. O programa não será executado.")
else: 
    if idade >= 18 and idade <= 65:
        print("Você é obrigado a votar")
    else:
        print("O voto não é obrigatório, pois você tem %d anos" % idade)