# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao39.py

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

def atualizar(maior, menor, num):
    if num > maior:
        return "maior"
    elif num < menor:
        return "menor"

for i in range(10):
    numeroAluno = int(input("Informe o número do aluno: "))
    alturaAluno = float(input(f"Informe a altura do {i + 1}º aluno (número: {numeroAluno}): "))

    if i == 0:
        numeroDoMaior = numeroAluno
        maiorAltura = alturaAluno
        
        numeroDoMenor = numeroAluno
        menorAltura = alturaAluno
    else: 
        if alturaAluno > maiorAltura:
            numeroDoMaior = numeroAluno
            maiorAltura = alturaAluno
        
        if alturaAluno < menorAltura:
            numeroDoMenor = numeroAluno
            menorAltura = alturaAluno
        
print("\nRESULTADOS\n---------------------------")
print(f"Maior altura (aluno de nº {numeroDoMaior}): {maiorAltura} m")
print(f"Menor altura (aluno de nº {numeroDoMenor}): {menorAltura} m")