# python pythonprogressivo/modulo/exemplos/calculadora/testcalculadora.py

import Calculadora # importa todo o módulo
from CalculadoraMensagem import imprimirMensagemFinal # importa uma função específica do módulo

while True:
    Calculadora.imprimirOperacoes()

    opcao = int(input())

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
        a = float(input("Informe um número: "))
        b = float(input("Informe outro número: "))

        if opcao == 1:
            print(f"{a} + {b} = {Calculadora.soma(a, b)}")
        elif opcao == 2:
            print(f"{a} - {b} = {Calculadora.subtracao(a, b)}")
        elif opcao == 3:
            print(f"{a} * {b} = {Calculadora.multiplicacao(a, b)}")
        else:
            print(f"{a} / {b} = {Calculadora.divisao(a, b)}")
    elif opcao == 0:
        break
    else:
        print("Operação inválida.")
    
imprimirMensagemFinal()