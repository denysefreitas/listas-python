# python pythonprogressivo/funcoes/listarecursividade/exemplos/FuncaoRecursiva.py

# Crie um script que peça um inteiro positivo para o usuário
# Em seguida, exiba a soma do somatório de 1 até o número

def somar(num):
    if num == 1: # caso básico
        # return 1 -> retorna o caso básico
        return num
    else: # caso recursivo
        return num + somar(num - 1)

while True:
    num = int(input("Somatorio de 1 até: "))

    if num == -1:
        break

    print(f"Soma: {somar(num)}")
    print("Se deseja sair, digite -1")