# python pythonprogressivo/lacosloopings/listawhile/SolucaoEx06.py

alunos=int(input("Numeros de alunos na turma: "))

count=1; soma = 0.0
while count <= alunos:
    print("Nota do aluno ", count, ":")
    nota = float( input() )
    soma += nota
    count += 1

print("Media da turma: ", (soma/alunos) )