# python pythonprogressivo/funcoes/listaargumentoseparametros/exercicios/Questao03.py

# Crie uma função que recebe 4 notas de um aluno, e exiba a média dele.

def pedirNota():
    nota = float(input("Informe a sua nota: "))
    return nota

def calcularMedia(n):
    soma = 0.0

    for i in range(n):
        soma += pedirNota()

    print("Média do aluno:", soma / n)

calcularMedia(4)