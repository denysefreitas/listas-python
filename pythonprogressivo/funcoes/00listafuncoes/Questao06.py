# python pythonprogressivo/funcoes/00listafuncoes/Questao06.py

# Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.

def isPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    # se nenhum número dividir, sai do for e retorna 'True'
    return True

num = int(input("Informe um número: "))

print(f"Os números primos de 1 até {num} são:")
for i in range(2, num + 1):
    if isPrimo(i):
        print(i, end = " ")