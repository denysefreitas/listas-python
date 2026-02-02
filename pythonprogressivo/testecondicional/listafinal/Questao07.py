# python pythonprogressivo/testecondicional/listafinal/Questao07.py

# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
char = input("Informe o turno que você estuda: ")
char = char.upper()

if char == 'M':
    mensagem = "Bom dia!"
elif char == 'V':
    mensagem = "Boa tarde!"
elif char == 'N':
    mensagem = "Boa noite!"
else:
    mensagem = "Caractere inválido!"

print(mensagem)