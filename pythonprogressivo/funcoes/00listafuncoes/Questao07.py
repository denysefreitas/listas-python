# python pythonprogressivo/funcoes/00listafuncoes/Questao07.py

# Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um inteiro e dizer se é perfeito ou não. Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.

def isNumeroPerfeito(num):
    somaDivisores = 0

    for i in range(1, num):
        if num % i == 0:
            somaDivisores += i
    
    if num == somaDivisores:
        return True
    else:
        return False
    
def encontrarNumerosPerfeitos(n):
    print(f"Números perfeitos de 1 até {n}")
    for i in range(1, n + 1):
        if(isNumeroPerfeito(i)):
            print(i, end = " ")

def receberNumero():
    print("Descubra se um número é perfeito")
    num = int(input("Informe um número: "))

    if(isNumeroPerfeito(num)):
        print(f"O número {num} é perfeito")
    else:  
        print(f"O número {num} não é perfeito")

def receberQuantidadeDeNumeros():
    print("Vamos descobrir quais números perfeitos de 1 até o número informado.")
    n = int(input("Informe um número: "))
    encontrarNumerosPerfeitos(n)

receberNumero()
receberQuantidadeDeNumeros()