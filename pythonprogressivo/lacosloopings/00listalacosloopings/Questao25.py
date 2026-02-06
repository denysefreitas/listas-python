# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao25.py

# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

soma = 0
n = int(input("Informe a quantidade de pessoas que irão participar da pesquisa: "))

for i in range(n):
    idade = int(input("Informe a sua idade (%d/%d): " % (i+1, n)))
    soma += idade

media = soma / n

if media >= 0 and media <= 25:
    classificao = "jovem"
elif media <= 60:
    classificao = "adulta"
else:
    classificao = "idosa"

print("A turma foi classificada como '%s', pois a média das idades informadas foi de %.1f anos" % (classificao, media))