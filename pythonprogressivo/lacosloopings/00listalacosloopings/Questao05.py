# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao05.py

print("O objetivo do programa é descobrir em quantos anos a população A iguala ou ultrapassa a população B. Vamos iniciar!")

pop_a = int(input("Informe a população A: "))

while pop_a < 0:
    print("A população deve ser de pelo menos 1 habitante")
    pop_a = int(input("Informe a população A: "))

taxa_crescimento_a = float(input("Informe a taxa de crescimento da população A em porcentagem [0 - 100]: "))


pop_b = int(input("Informe a população B: "))

while pop_b < 0:
    print("A população deve ser de pelo menos 1 habitante")
    pop_b = int(input("Informe a população B: "))

taxa_crescimento_b = float(input("Informe a taxa de crescimento da população B em porcentagem [0 - 100]: "))

anos = 0
anos = int(anos)

while pop_a < pop_b:
    pop_b *= (1 + taxa_crescimento_b/100)
    pop_a *= (1 + taxa_crescimento_a/100)
    anos += 1

print("A população A iguala ou ultrapassa a população B em %d anos" % anos)