# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/Return04.py

def fazerCadastro():
    nome = input("Informe o seu nome: ")

    while True:
        idade = int(input("Informe a sua idade: ") )

        if idade > 0:
            return nome, idade

        print("Valor inválido")

print("Iniciando cadastro...")
nome, idade = fazerCadastro()

print("Cadastro realizado com sucesso:")
print(f"Seu nome é {nome} e você tem {idade} anos de idade.")