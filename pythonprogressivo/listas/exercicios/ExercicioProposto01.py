# python pythonprogressivo/listas/exercicios/ExercicioProposto01.py

fatorial = 1
fibonacci = [0, 1]
n = int(input("Informe um número inteiro positivo: "))
n += 2

for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])   

print(f"Sequência de Fibonacci de {n} termos:")
for i in range(n):
    print(fibonacci[i], end = " ")