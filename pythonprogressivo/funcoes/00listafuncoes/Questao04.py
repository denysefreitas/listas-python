# python pythonprogressivo/funcoes/00listafuncoes/Questao04.py

# A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que simule 1 milhão de lançamentos de dados e mostre a frequência que deu para cada número.

import random

def sortear():
    return random.randint(1, 6)

def realizarLancamento(nLancamentos):
    qnt1 =  qnt2 = qnt3 = qnt4 = qnt5 = qnt6 = 0

    for lancamento in range(nLancamentos):
        numSorteado = sortear()

        if numSorteado == 1:
            qnt1 += 1
        elif numSorteado == 2:
            qnt2 += 1
        elif numSorteado == 3:
            qnt3 += 1
        elif numSorteado == 4:
            qnt4 += 1
        elif numSorteado == 5:
            qnt5 += 1
        else:
            qnt6 += 1
        
    imprimirProbabilidade(nLancamentos, qnt1, qnt2, qnt3, qnt4, qnt5, qnt6)

def imprimirProbabilidade(nLancamentos, qnt1, qnt2, qnt3, qnt4, qnt5, qnt6):
    print(f"O número 1 saiu {qnt1} vezes. Isso representa {(qnt1 / nLancamentos) * 100:.2f}% do total de lançamentos")
    print(f"O número 2 saiu {qnt2} vezes. Isso representa {(qnt2 / nLancamentos) * 100:.2f}% do total de lançamentos")
    print(f"O número 3 saiu {qnt3} vezes. Isso representa {(qnt3 / nLancamentos) * 100:.2f}% do total de lançamentos")
    print(f"O número 4 saiu {qnt4} vezes. Isso representa {(qnt4 / nLancamentos) * 100:.2f}% do total de lançamentos")
    print(f"O número 5 saiu {qnt5} vezes. Isso representa {(qnt5 / nLancamentos) * 100:.2f}% do total de lançamentos")
    print(f"O número 6 saiu {qnt6} vezes. Isso representa {(qnt6 / nLancamentos) * 100:.2f}% do total de lançamentos")

def soliciarLancamentos():
    nLancamentos = int(input("Informe a quantidade de lançamentos de dados a serem realizadas: "))
    realizarLancamento(nLancamentos)

soliciarLancamentos()