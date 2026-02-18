# python pythonprogressivo/funcoes/00listafuncoes/Questao01.py

# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

def converterParaCelsius(grausF):
    return float((grausF - 32) * (5 / 9))

def converterParaFarenheit(grausC):
    return float(grausC * (9 / 5) + 32)

def menu():
    print("1. Converter °F para °C")
    print("2. Converter °C para °F")
    opcao = input("Opção: ")

    if opcao == "1":
        grausF = float(input("Informe a temperatura em Fahrenheit (°F) a ser convertida: "))
        print(f"{grausF}°F corresponde a {converterParaCelsius(grausF):.2f}°C")
    elif opcao == "2":
        grausC = float(input("Informe a temperatura em Celsius (°C) a ser convertida: "))
        print(f"{grausC}°C corresponde a {converterParaFarenheit(grausC):.2f}°F")
    else:
        print("Opção inválida.")
        menu()

while True:
    menu()
    continuar = input("Você deseja fazer outra conversão? (S - SIM / N - NÃO) ")

    if continuar == "N":
        break
