# python pythonprogressivo/testecondicional/listafinal/Questao12.py

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

 #   Dicas:
 #   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
 #   Triângulo Equilátero: três lados iguais;
 #   Triângulo Isósceles: quaisquer dois lados iguais;
 #   Triângulo Escaleno: três lados diferentes;

print("Para formar um triângulo, é necessário 3 lados")
a = int(input("Informe o valor do primeiro lado: "))
b = int(input("Informe o valor do segundo lado: "))
c = int(input("Informe o valor do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        tipo = "Equilátero"
    if a != b and b != c and c != a:
        tipo = "Escaleno"
    else:
        tipo = "Isósceles"

    print("Triângulo:", tipo)
else:
    print("Não é possível formar um triângulo com os lados informados.")