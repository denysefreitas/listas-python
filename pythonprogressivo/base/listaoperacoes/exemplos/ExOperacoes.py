# python pythonprogressivo/base/listadados/exemplos/ExOperacoes.py

var1 = int(input("Informe um número inteiro: "))
var2 = int(input("Informe outro número inteiro: "))

soma = var1 + var2
subtracao = var1 - var2
multiplicacao = var1 * var2
exponenciacao = var1 ** var2
resto_divisao = var1 % var2

if var2 == 0:
    divisao = "não existe"
else:
    divisao = var1 / var2

print(f"Soma: {var1} + {var2} = {soma}")
print(f"Subtração: {var1} - {var2} = {subtracao}")
print(f"Multiplicação: {var1} * {var2} = {multiplicacao}")
print(f"Divisão: {var1} / {var2} = {divisao}")
print(f"Exponenciação: {var1} ** {var2} = {exponenciacao}")
print(f"Resto da divisão: {var1} % {var2} = {resto_divisao}")