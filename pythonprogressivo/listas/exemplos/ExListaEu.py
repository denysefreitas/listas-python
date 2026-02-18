# python pythonprogressivo/listas/exemplos/ExListaEu.py

# Crie um programa em Python que peça seu nome, sua idade, sua altura, seu peso e True se for casado ou False para solteiro.
#Em seguida, ele deve armazenar todas essas informações numa lista chamada eu. Por fim, imprima essa lista na tela.

def imprimirDados(lista):
    print(f"Nome         : {lista[0]}")
    print(f"Idade        : {lista[1]} anos")
    print(f"Altura       : {lista[2]:.2f} m")
    print(f"Peso         : {lista[3]} kg")
    print(f"É casado(a)? : {lista[4]}")

nome = input("Informe o seu nome: ")

while True:
    idade = int(input("Informe a sua idade: "))

    if idade >= 0 and idade <= 150:
        break

    print("Idade inválida")

while True:
    altura = float(input("Informe a sua altura (metros): "))

    if altura >= 0 and altura <= 3:
        break

    print("Altura inválida")

while True:
    peso = float(input("Informe o seu peso (kg): "))

    if peso >= 0 and peso <= 200:
        break

    print("Peso inválido")

while True:
    print("1. Casado(a)\n2. Solteiro(a)")
    estadoCivil = int(input("Informe o seu estado civil, baseado nas opções informadas: "))

    if estadoCivil == 1 or estadoCivil == 2:
        break

    print("Estado civil inválido. Atente-se às opções")

if estadoCivil == 2:
    estadoCivil = False
else:
    estadoCivil = True

eu = [nome, idade, altura, peso, estadoCivil]

imprimirDados(eu)