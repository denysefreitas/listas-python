# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao36.py

# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

def imprimirTabuada(n, inicio, final):
    print(f"Tabuada de {n} começando em {inicio} e terminando em {final}:")

    for i in range(inicio, final + 1):
        print(f"{n} X {i} = {n * i}")

def conferirFinal(inicio, final):
    return final >= inicio

num = int(input("Informe o número que você deseja montar a tabuada: "))
inicio = int(input("Informe o número inicial da tabuada: "))

while True:
    final = int(input("Informe o número final da tabuada: "))
    
    if conferirFinal(inicio, final):
        break

    print("[AVISO] Valor final menor que o valor inicial. Valor inválido!")

imprimirTabuada(num, inicio, final)