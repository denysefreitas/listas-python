# python pythonprogressivo/funcoes/00listafuncoes/Questao10.py

# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def isPositivo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'

num = int(input("Informe um número: "))
resposta = isPositivo(num)

if resposta == 'P':
    print(f"O número {num} é positivo")
else:
    print(f"O número {num} é nulo ou negativo")