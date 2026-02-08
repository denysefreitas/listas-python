# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao38.py

# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario_inicial = 1000.00
percentual_inicial = 1.5

def calcularSalario(anos, salario, taxa):
    for ano in range(1, anos + 1):
        salario *= (1 + (taxa)/100)
        taxa *= 2
    
    return salario

def eValido(ano):
    return ano - 1995 > 0 

while True:
    ano_atual = int(input("Informe o ano atual: "))

    if eValido(ano_atual):
        anos = ano_atual - 1995
        break

    print("Ano inválido. Informe um ano superior ao atual (1995).")

print(f"Salário atual (ano: {ano_atual}): R$ {calcularSalario(anos, salario_inicial, percentual_inicial):.2f}")