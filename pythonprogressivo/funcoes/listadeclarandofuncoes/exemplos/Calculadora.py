# python pythonprogressivo/funcoes/listadeclarandofuncoes/exemplos/Calculadora.py

# Faça uma calculadora, usando funções. O script pergunta qual operação o usuário deseja rodar (soma, subtração, multiplicação ou divisão) e executa a operação.

#A calculadora deve ser executada quantas vezes o usuário desejar.

def imprimirCalculadora():
    print("+ -> Soma")
    print("- -> Subtração")
    print("* -> Multiplicação")
    print("/ -> Divisão")
    print("Escolha a operação que você deseja realizar: ")

def somar(a, b):
    
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def isZero(denominador):
    return denominador == 0

while True:
    imprimirCalculadora()
    opcao = input()
    
    if opcao == "+" or opcao == "-" or opcao == "*" or opcao == "/":
        a = float(input("Informe um número: "))
        b = float(input("Informe outro número: "))

        if opcao == "+":
            r = somar(a, b)
        elif opcao == "-":
            r = subtrair(a, b)
        elif opcao == "*":
            r = multiplicar(a, b)
        elif opcao == "/":
            if isZero(b):
                semResposta = True
            else:
                r = dividir(a, b)

        if semResposta:
            print("Não é possível realizar divisão por zero")
            semResposta = False
        else:
            print("%d %s %d = %d" % (a, opcao, b, r))   
    else:
        print("Operação inválida.")
    

    resposta = input("Deseja continuar? S - Sim / N - Não ")

    if resposta == "N":
        break