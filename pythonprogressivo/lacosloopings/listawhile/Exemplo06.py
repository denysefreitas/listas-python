# python pythonprogressivo/lacosloopings/listawhile/Exemplo06.py

# Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, seu único script serve para todos os casos

qnt_alunos = 0
soma = 0

char = 'S'

while char == 'S':
    nota = float(input("Informe uma nota: "))
    qnt_alunos += 1
    soma += nota

    char = input("Você deseja informar outra nota? (S - Sim / N - Não) ")

print("A média da turma é de", soma/qnt_alunos)