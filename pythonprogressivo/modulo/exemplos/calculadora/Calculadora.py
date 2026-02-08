# Esse módulo realiza as quatro operações básicas

def imprimirOperacoes():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    print("Opção: ")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if isZero(b):
        return "impossível"
    else:
        return a / b
    
def isZero(b):
    return b == 0