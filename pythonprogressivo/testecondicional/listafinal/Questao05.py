# python pythonprogressivo/testecondicional/listafinal/Questao05.py

# Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

a = int(input("Informe um número inteiro: "))
b = int(input("Informe um número inteiro: "))

print("Primeiro número: %d\nSegundo número: %d" % (a, b))
print("Invertendo as variáveis...")

aux = b
b = a
a = aux

print("Variáveis invertidas com sucesso!\nPrimeiro número: %d\nSegundo número: %d" % (a, b))