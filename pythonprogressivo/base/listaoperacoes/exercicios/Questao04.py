# python pythonprogressivo/base/listaoperacoes/exercicios/Questao04.py

# Um cliente pediu que o sistema do banco tivesse a seguinte função:
# Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha um valor 'vf', supondo que este dinheiro esteja rendendo uma rentabilidade 'i' mensal, em porcentagem esse 'i'.

# Faça um programa que pede o valor final, o tanto de meses que vai ficar aplicado, a rentabilidade e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.

valor_final = float(input("Informe o valor final a ser recebido: "))

t = int(input("Informe por quantos meses você deseja investir: "))

taxa_mensal = float(input("Informe a rentabilidade (taxa) mensal: "))
taxa_mensal /= 100

valor_inicial = valor_final / (1 + taxa_mensal) ** t

print(f"Para atingir o valor de R$ {valor_final} sob uma taxa mensal de {taxa_mensal*100}% em {t} meses, é necessário investir R$ {valor_inicial}")