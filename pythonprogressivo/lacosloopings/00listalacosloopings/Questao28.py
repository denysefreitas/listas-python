# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao28.py

# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

count = 0
count = int(count)

def custoCd():
    global count

    while True:
        valor = float(input(f"Informe o valor gasto no CD {count + 1}:"))
    
        if valor >= 0:
            count += 1
            return valor

        print("Valor inválido.")

def quantidadeCd():
    while True:
        quantidade = int(input("Informe a quantidade de CDs adquiridos: "))

        if quantidade > 0:
            return quantidade
        
        print("Quantidade inválida.")

def imprimirGastos(soma, cds):
    print(f"Valor total: {soma:.2f}")
    print(f"Valor médio por CD: {soma / cds:.2f}")

soma = 0.0

for i in range(quantidadeCd()):
    soma += custoCd()

imprimirGastos(soma, count)