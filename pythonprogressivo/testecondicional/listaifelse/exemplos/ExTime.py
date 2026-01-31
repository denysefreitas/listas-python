# python pythonprogressivo/testecondicional/listaifelse/exemplos/ExTime.py

# Escreva um código que exiba o nome de dois times, em seguida pergunta ao usuário qual deles é o melhor.

# Com a resposta em mãos, usando IF e ELSE, imprima na tela uma mensagem dizendo qual time ele torce.

print("1 - Cruzeiro")
print("2 - Flamengo")
print("3 - Corinthians")
resposta = int(input("Qual time é o melhor do mundo? "))

if resposta == 1:
    print("Você também deve torcer pro Cruzeiro")
elif resposta == 2:
    print("Você deve torcer pro Flamengo")
elif resposta == 3:
    print("Você deve torcer pro Corinthians")
else:
    print("Certamente você não torce para nenhum dos times citados")