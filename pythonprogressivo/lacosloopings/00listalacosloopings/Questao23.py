# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao23.py

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

divisoes = 0
divisores = 0
n = int(input("Informe um número: "))

print("Números primos entre %d e %d:" % (2, n), end = " ")
for num in range(2, n + 1):
    for j in range(1, num):
        divisoes += 1
        if num % j == 0:
            divisores += 1
    
    if divisores < 2 or divisores == 1:
        print(num, end = " ")
    
    divisores = 0

print("\nNo total, foram realizadas", divisoes, "divisões")
    

