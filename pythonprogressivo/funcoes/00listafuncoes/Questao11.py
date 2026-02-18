# python pythonprogressivo/funcoes/00listafuncoes/Questao11.py

# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    return custo * (1 + (taxaImposto / 100))

taxa = float(input("Informe a taxa (%) de imposto (ex: 10 -> 10%): "))
custo = float(input("Informe o custo de um item antes do imposto: "))

print(f"O custo do produto antes da taxa é R${custo:.2f}")
print(f"O novo custo do produto é R${somaImposto(taxa, custo):.2f}")