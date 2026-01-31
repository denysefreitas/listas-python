# python pythonprogressivo/testecondicional/listafinal/Questao02.py

# Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

    #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    #A mensagem "Reprovado", se a média for menor do que sete;
    #A mensagem "Aprovado com Distinção", se a média for igual a dez.

sum = 0
sum = float(sum)

nota1 = float(input("Informe a primeira nota do aluno: "))

if nota1 < 0 or nota1 > 10:
    print("Você informou uma nota fora dos parâmetros indicados. O programa não será executado.")
else: 
    sum += nota1

    nota2 = float(input("Informe a segunda nota do aluno: "))

    if nota2 < 0 or nota2 > 10:
        print("Você informou uma nota fora dos parâmetros indicados. O programa não será executado.")
    else: 
        sum += nota2
        media = sum / 2

        if media == 10:
            resultado = "Aprovado com Distinção"
        elif media >= 7:
            resultado = "Aprovado"
        else: 
            resultado = "Reprovado"

        print("Situação: %s" % resultado)
        print("Média:", media)