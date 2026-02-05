# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/SomarDoisNumeros.py

# Crie uma função que pede dois números, faz a soma e exibe o resultado, através de uma função. O usuário pode executar a função quantas vezes desejar.

def somar(a, b):
    return a + b

while True:
    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))

    print("Soma:", somar(a, b))
    
    resposta = input("Deseja continuar? S - Sim / N - Não ")

    if resposta == "N":
        break

