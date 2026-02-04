# python pythonprogressivo/lacosloopings/listaloopsaninhados/MediaTurma.py

# Primeiro, pergunta a quem vai usar o script quantos alunos tem na sala.
#Depois, quantas matérias cada aluno estuda.

#Em seguida o usuário vai preenchendo a nota de cada matéria, de cada aluno.
# Seu programa deve fornecer a média de cada aluno e a média geral da turma.

soma_aluno = 0.0
soma_sala = 0.0
alunos = int(input("Informe quantos alunos tem na sala: "))

for aluno in range(alunos):
    qnt_materias = int(input("Informe a quantidade de matérias que o aluno %d estuda: " % (aluno+1)))

    for materia in range(qnt_materias):
        nota = float(input("Informe a nota da matéria %d do aluno %d: " % (materia+ 1, aluno + 1)))
        soma_aluno += nota
    
    media_aluno = soma_aluno / qnt_materias
    print("Média do aluno %d: %.2f" % (aluno + 1, media_aluno))
    soma_sala += media_aluno

print("A média da sala é: ", soma_sala/alunos)