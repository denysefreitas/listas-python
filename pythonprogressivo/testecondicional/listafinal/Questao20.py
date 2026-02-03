# python pythonprogressivo/testecondicional/listafinal/Questao20.py

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#    par ou ímpar;
#    positivo ou negativo;
#    inteiro ou decimal.

continuar = True
a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))

print("+ -> Adição")
print("- -> Subtração")
print("* -> Multiplicação")
print("/ -> Divisão")
operacao = input("Informe a operação a ser realizada com os números %.2f e %.2f: " % (a, b))

if operacao == "+":
    r = a + b
elif operacao == "-":
    r = a - b
elif operacao == "*":
    r = a * b
elif operacao == "/":
    if b != 0:
        r = a / b
    else:
        print("Não é possível realizar uma divisão por zero. O programa não será executado.")
        continuar = False
else:
    print("Você informou um caractere inesperado. O programa não será executado.")
    continuar = False

if continuar:
    # par ou ímpar
    if r % 2 == 0:
        paridade = "Par"
    else:
        paridade = "Ímpar"
    
    # positivo ou negativo
    if r > 0:
        sinal = "Positivo"
    elif r == 0:
        sinal = "Nulo"
    else:
        sinal = "Negativo"
    
    # inteiro ou decimal
    if r == round(r):
        tipo = "Inteiro"
        r = int(r)
    else:
        tipo = "Decimal"

    print("%.2f %s %.2f = %.2f" % (a, operacao, b, r))
    print("Par ou ímpar:", paridade)
    print("Positivo ou negativo:", sinal)
    print("Inteiro ou decimal:", tipo)