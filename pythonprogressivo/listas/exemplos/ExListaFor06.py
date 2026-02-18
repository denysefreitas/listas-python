# python pythonprogressivo/listas/exemplos/ExListaFor06.py

# Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo.

# Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista.

# Ao final, seu script deverá fornecer a média geral do aluno.

notas = []
soma = 0.0
qnt_materias = int(input("Informe o número de matérias: "))

for n_materia in range(qnt_materias):
    notas.append(float(input(f"Informe a sua nota da matéria {n_materia + 1}: ")))
    soma += notas[n_materia]

print(f"Notas: {notas}")
print(f"Média geral: {soma / qnt_materias}")