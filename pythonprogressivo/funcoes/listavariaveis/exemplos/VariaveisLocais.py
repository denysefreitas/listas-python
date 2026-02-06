# python pythonprogressivo/funcoes/listavariaveis/exemplos/VariaveisLocais.py

def teste1():
    print("Estamos dentro da função teste1!")
    n = 111
    print("Valor de n:", n)

def teste2():
    print("Estamos dentro da função teste2!")
    n = 333
    print("Valor de n:", n)

def teste3():
    print("Estamos dentro da função teste3!")
    n = 777
    print("Valor de n:", n)

teste1()
teste2()
teste3()
 
# Conclusão: n é uma variável local da função teste(), portanto, possui um valor dentro de cada função