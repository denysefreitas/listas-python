# python pythonprogressivo/funcoes/listavariaveis/exemplos/ConstantesGlobais.py

# Crie um programa em Python que peça o raio de uma circunferência ao usuário, em seguida exiba o perímetro e a área desse círculo.

pi =  3.14

def calcularPerimetro(r):
    return 2 * pi * r

def calcularArea(r):
    return pi * r * r

while True:
    raio = float(input("Informe o valor do raio: "))

    if raio > 0:
        break

    print("Valor inválido.")

print(f"Perímetro: {calcularPerimetro(raio):.2f}")
print(f"Área: {calcularArea(raio):.2f}")

