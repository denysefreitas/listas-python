# python pythonprogressivo/funcoes/00listafuncoes/Questao13.py



def contarCasas(num):
    num = abs(num)
    casas = 0

    while num > 0:
        casas += 1
        num //= 10

    return casas

print("Esse programa conta a quantidade de dígitos de um número: ")
num = int(input("Informe um número inteiro: "))

print(f"O número {num} possui {contarCasas(num)} dígitos")