# python pythonprogressivo/base/listabase/Questao02.py

# Você está no Brasil, e para temperatura usamos o grau Celsius.
#Porém, quando você for contrato para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit.
# Ou seja, você fornece a temperatura em graus Celsius, e seu script faz a conversão para graus Fahrenheit.

graus_c = float(input("Informe a temperatura em graus Celsius: "))
graus_f = 9 * graus_c / 5 + 32

print("%.2f°C equivale a %.2f°F" % (graus_c, graus_f))