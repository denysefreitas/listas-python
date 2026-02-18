# python pythonprogressivo/funcoes/00listafuncoes/Questao03.py

# Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através de outra função.

def isMaior(maior, num):
    if num > maior:
        return num
    else:
        return maior
    
def isMenor(menor, num):
    if num < menor:
        return num
    else:
        return menor

qnd_numeros = 3
for i in range(qnd_numeros):
    num = float(input(f"Informe um número ({i + 1}/{qnd_numeros}): "))

    if i == 0:
        maior = num
        menor = num
    else:
        maior = isMaior(maior, num)
        menor = isMenor(menor, num)

print(f"Maior número: {maior:.2f}")
print(f"Menor número: {menor:.2f}")