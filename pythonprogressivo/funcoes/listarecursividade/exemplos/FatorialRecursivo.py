# python pythonprogressivo/funcoes/listarecursividade/exemplos/FatorialRecursivo.py

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

while True:
    num = int(input("informe um número [1 - 16] para ser calculado o seu fatorial: "))

    if num > 1 and num < 16:
        break

    print("Valor inválido. Atenção ao intervalo informado.")
    
print(f"{num}! = {fatorial(num)}")