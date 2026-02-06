# python pythonprogressivo/funcoes/listaargumentoseparametros/exercicios/Questao04.py

# Crie uma função que recebe 3 números e exiba o maior deles.

def pedirNumero():
    num = float(input("Informe um número: "))
    return num

def maiorNumero(n):
    for i in range(n):
        if i == 0:
            maior = pedirNumero()
            continue

        num = pedirNumero()
        
        if num > maior:
            maior = num
    
    print("Maior:", maior)

maiorNumero(3)