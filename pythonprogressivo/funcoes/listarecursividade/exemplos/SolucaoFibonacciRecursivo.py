

def imprimirFibonacci(num):
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else:
        return imprimirFibonacci(num - 1) + imprimirFibonacci(num - 2)

def exibir():
    n = int(input("Exibir ate o termo (maior que 2): "))

    for num in range(1, n + 1):
        print(imprimirFibonacci(num))
    
while True:
    exibir()