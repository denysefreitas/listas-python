# python pythonprogressivo/base/listabase/Questao03.py

# Agora faça o contrário. Você fornece a temperatura em graus Fahrenheit, seu programa conversar para Celsius e exibe na tela.

graus_f = float(input("Informe a temperatura em graus Fahrenheit: "))
graus_c = (graus_f - 32) * 5 / 9

print("%.2f°F equivale a %.2f°C" % (graus_f, graus_c))