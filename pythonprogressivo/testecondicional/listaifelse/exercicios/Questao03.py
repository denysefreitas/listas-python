# python pythonprogressivo/testecondicional/listaifelse/exercicios/Questao03.py

# Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = input("F - Feminino\nM - Masculino\nO - Não desejo informar\nInforme o seu sexo: ")

if sexo == "F" or sexo == "f":
    print("O seu sexo é feminino")
elif sexo == "M" or sexo == "m":
    print("O seu sexo é masculino")
elif sexo == "O" or sexo == "o":
    print("Você optou por não informar seu sexo")
else:
    print("Sexo inválido")