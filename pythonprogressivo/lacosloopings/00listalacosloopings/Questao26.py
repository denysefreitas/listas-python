# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao26.py

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votos_a = 0
votos_a = int(votos_a)
votos_b = 0
votos_b = int(votos_b)
votos_c = 0
votos_c = int(votos_c)

def pedirVotos():
    while True:
        print("Números dos candidatos:")
        print("1. Candidato A")
        print("2. Candidato B")
        print("3. Candidato C")
        voto = int(input(f"Eleitor {i + 1}, faça a sua escolha: "))
    
        if(voto == 1 or voto == 2 or voto == 3):
            return voto
    
        print("Número de candidato inválido. Atente-se aos números dos candidatos.")

def contarVotos(voto):
    global votos_a
    global votos_b
    global votos_c

    if voto == 1:
        votos_a += 1
    elif voto == 2:
        votos_b += 1
    else:
        votos_c += 1

def imprimirVotos():
    print(f"Candidato A: {votos_a} voto(s)")
    print(f"Candidato B: {votos_b} voto(s)")
    print(f"Candidato C: {votos_c} voto(s)")


total_eleitores = int(input("Informe o número total de eleitores: "))

for i in range(total_eleitores):
    contarVotos(pedirVotos())

imprimirVotos()