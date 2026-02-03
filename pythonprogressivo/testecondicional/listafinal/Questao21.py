# python pythonprogressivo/testecondicional/listafinal/Questao21.py

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

parar = False

print("Antes de iniciar as perguntas, preste atenção nas regras: ")
print("1 - Seja sincero, pois tudo que você disser poderá ser utilizado contra você")
print("2 - Responda as perguntas com S (Sim) e N (Não). Outras respostas não serão validadas e o processo terá de ser reiniciado.")
print("Posto isso, podemos começar.")

total = 0
total = int(total)

for pergunta in ["Telefonou para a vítima? ", 
                 "Esteve no local do crime? ",
                 "Mora perto da vítima? ",
                 "Devia para a vítima? ",
                 "Já trabalhou com a vítima? "]:
    resposta = input(pergunta)
    reposta = resposta.upper()

    if resposta == "S":
        total += 1
    elif resposta != "N":
        parar = True
        break

if parar:
    print("Você informou um caractere inesperado. O processo terá de ser reiniciado.")
else:
    if total == 2:
        print("Suspeita")
    elif total == 3 or total == 4:
        print("Cúmplice")
    elif total == 5:
        print("Culpado")
    else:
        print("Inocente")