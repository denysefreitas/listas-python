# python pythonprogressivo/base/listaoperacoes/exemplos/ExMedia02.py

# Faça um programa em Python que receba as notas de Português, Inglês e Matemática de um aluno, e em seguida forneça a média aritmética dessas notas.

nota_portugues = float(input("Informe a nota de Português: "))
nota_ingles = float(input("Informe a nota de Inglês: "))
nota_matematica = float(input("Informe a nota de Matemática: "))

media = (nota_portugues + nota_ingles + nota_matematica)/3

print(f"A média das notas é {media}")