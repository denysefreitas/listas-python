# python pythonprogressivo/funcoes/listarecursividade/exemplos/FibonacciRecursivo.py

def eValido(n):
    return n > 2

def imprimirFibonacci(num):
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else:
        return imprimirFibonacci(num - 1) + imprimirFibonacci(num - 2)

while True:
    n = int(input("Exibir até o termo (maior que 2): "))

    if eValido(n):
        break

    print("Valor inválido. Observe o intervalo permitido.")

print(f"Sequência de Fibonacci do 1º termo ao {n}º termo:")
for i in range(1, n + 1):
    print(imprimirFibonacci(i))