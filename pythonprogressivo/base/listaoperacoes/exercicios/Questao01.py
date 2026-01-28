# python pythonprogressivo/base/listaoperacoes/exercicios/Questao01.py

# Sua primeira tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.
# Você deve mostrar uma tabela contendo:
# Preço original do produto
# Valor do desconto em R$ (tipo 'Você ganho R$ xx,xx de desconto')
# Valor do produto com o desconto

valor_original = float(input("Informe o valor original do produto: "))

taxa_desconto = 0.25
valor_do_desconto = valor_original * taxa_desconto
valor_com_desconto = valor_original - valor_do_desconto

print(f"O valor original do produto é R$ {valor_original}")
print(f"O valor do desconto ({taxa_desconto * 100}%) é R$ {valor_do_desconto}")
print(f"O valor do produto com o desconto é R$ {valor_com_desconto}")

