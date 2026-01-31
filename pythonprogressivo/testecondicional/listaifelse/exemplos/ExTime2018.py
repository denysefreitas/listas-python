# python pythonprogressivo/testecondicional/listaifelse/exemplos/ExTime2018.py

# A seguir, temos a tabela dos melhores times de 2018, da CBF.
#Você deve criar um programa que pede 'Digite um número de 1 até 10', e de acordo com o número fornecido pelo usuário, indicar qual o time está naquela posição do ranking.

print("A CBF divulgou a lista dos 10 melhores times de 2018")
n = int(input("Informe a posição que você deseja saber: "))

if n == 1:
    print("1 - Palmeiras")
elif n == 2:
    print("2 - Cruzeiro")
elif n == 3:
    print("3 - Grêmio")
elif n == 4:
    print("4 - Santos")
elif n == 5:
    print("5 - Atlético-MG")
elif n == 6:
    print("6 - Corinthians")
elif n == 7:
    print("7 - Flamengo")
elif n == 8:
    print("8 - Botafogo")
elif n == 9:
    print("9 - Atlético-PR")
elif n == 10:
    print("10 - Internacional")
else:
    print("Não tenho a informação sobre a posição %d. Foram divulgados apenas os 10 melhores no ranking." % n)