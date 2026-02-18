# python pythonprogressivo/listas/exercicios/ExercicioProposto02.py

# Em seguida, cria uma lista com igual número de itens, onde o primeiro termo é 1!, o segundo é 2!, o terceiro é o valor de 3!, etc, até o termo que ele digitou. Ou seja, se digitou n, vai exibir até o termo de índice n-1, e lá na lista vai ter o valor de (n-1)!.

fatorial = 1
fatoriais = []
n = int(input("Informe um número inteiro: "))

for i in range(1, n + 1):
    fatorial *= i
    fatoriais.append(fatorial)   

for i in range(n):
    print(f"{i + 1}! = {fatoriais[i]}")