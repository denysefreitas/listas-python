# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao27.py

# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

count = 0
count = int(count)

def pedirTurma():
    while True:
        turmas = int(input("Informe a quantidade de turmas: "))

        if turmas > 0:
            return turmas

def pedirAlunos():
    global count

    while True:
        alunos = int(input(f"Informe a quantidade de alunos [0 - 40] na turma {count + 1}: "))

        if alunos <= 40 and alunos > 0:
            count += 1
            return alunos
        
        print("Quantidade de alunos inválida.")
        
def calcularMedia(soma, turmas):
    print(f"Média de alunos por turma: {soma / turmas:.1f} alunos")
    
soma = 0
soma = int(soma)

qnt_turmas = pedirTurma()

for i in range(qnt_turmas):
    soma += pedirAlunos()

calcularMedia(soma, qnt_turmas)
