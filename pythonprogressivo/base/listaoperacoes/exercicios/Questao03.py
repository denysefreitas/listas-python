# python pythonprogressivo/base/listaoperacoes/exercicios/Questao03.py

# Você vai perguntar o valor inicial investido na poupança, a rentabilidade mensal, quantos meses o cliente deseja deixar o dinheiro investido e mostrar o valor final na conta do cliente do banco.

valor_inicial = float(input("Informe o valor inicial investido: "))

taxa_mensal = float(input("Informe a rentabilidade (taxa) mensal: "))
taxa_mensal /= 100

t = int(input("Informe por quantos meses você deseja investir: "))

valor_final = valor_inicial * (1 + taxa_mensal) ** t

print(f"O valor R$ {valor_inicial} sob uma taxa mensal de {taxa_mensal*100}% renderá R$ {valor_final} em {t} meses")