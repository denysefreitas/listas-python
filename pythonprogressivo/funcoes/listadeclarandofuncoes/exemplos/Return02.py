# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/Return02.py

# Crie um programa em Python que peça o nome e o sobrenome de uma pessoa, depois exiba na tela a mensagem "Olá sobrenome, nome".

def imprimirMensagem():
    nome = input("Informe o seu nome: ")
    sobrenome = input("Informe o seu sobrenome: ")

    return f"Olá {sobrenome}, {nome}!"

print(imprimirMensagem())