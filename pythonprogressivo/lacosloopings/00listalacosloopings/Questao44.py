# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao44.py

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

def imprimirCandidatos():
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    print("4. Candidato D")
    print("5. Voto Nulo")
    print("6. Voto em Branco")

votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0
votosBrancos = 0
votosNulos = 0

while True:
    imprimirCandidatos()
    voto = int(input("Opção: "))

    if voto == 1 or voto == 2 or voto == 3 or voto == 4 or voto == 5 or voto == 6:
        print("Voto computado com sucesso.")
        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        elif voto == 4:
            votos4 += 1
        elif voto == 5:
            votosNulos += 1
        else:
            votosBrancos += 1
    elif voto == 0:
        break
    else:
        print("Opção sem correspondência a candidatos. Atenção aos números dos candidatos.")

totalVotos = votos1 + votos2 + votos3 + votos4 + votosBrancos + votosNulos
print("RESULTADOS\n----------------------------")
print(f"Total de votos do 'Candidato A': {votos1}")
print(f"Total de votos do 'Candidato B': {votos2}")
print(f"Total de votos do 'Candidato C': {votos3}")
print(f"Total de votos do 'Candidato D': {votos4}")
print(f"Total de votos do 'Candidato D': {votos4}")
print(f"Total de votos do 'em branco': {votosBrancos}")
print(f"Total de votos do 'nulos': {votosNulos}")
print(f"Porcentagem (%) de 'Votos em branco': {(votosBrancos * 100) / totalVotos:.2f}%")
print(f"Porcentagem (%) de 'Votos nulos': {(votosNulos * 100) / totalVotos:.2f}%")
