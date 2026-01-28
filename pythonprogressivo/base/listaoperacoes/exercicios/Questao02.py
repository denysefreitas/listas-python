# python pythonprogressivo/base/listaoperacoes/exercicios/Questao02.py

# Retorne ao enunciado da Questão 1 para mais detalhes
# A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas, 10% em outra, nada em outro produto e até 30% em alguns outros produtos.
# Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido.

valor_original = float(input("Informe o valor original do produto: "))
taxa_desconto = float(input("Informe o valor da taxa de desconto: "))

taxa_desconto /= 100
valor_do_desconto = valor_original * taxa_desconto
valor_com_desconto = valor_original - valor_do_desconto

print(f"O valor original do produto é R$ {valor_original}")
print(f"O valor do desconto ({taxa_desconto * 100}%) é R$ {valor_do_desconto}")
print(f"O valor do produto com o desconto é R$ {valor_com_desconto}")