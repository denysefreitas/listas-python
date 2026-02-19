# python pythonprogressivo/listas/jogo/JogoDaVelha.py

global tabuleiro
global jogadas
tabuleiro = []

# criar o módulo tabuleiro
def preencherTabuleiro():
    linhaSuperior = (' ', '|', ' ', '|', ' ')
    linhaCentral = ('-', '-', '-', '-', '-')

    for i in range(5):
        for j in range(5):
            if j % 2 == 0:
                tabuleiro.append(linhaSuperior)
            else:
                tabuleiro.append(linhaCentral)

def exibirRegras():
    print("REGRAS:\n1. Você, usuário, jogará com os dois players")
    print("Player 1: 0")
    print("Player 2: X")
    print("Você irá escolher a linha e coluna da coordenada que deseja preencher.")
    print("Coordenadas fora do limite [1-3] não serão aceitas. Será solicitado que informe outra dentro do limite pré-determinado.")
    print("O jogo será encerrado se algum dos jogadores vencer ou se der velha (ou seja, empate).")

def exibirTabuleiro():
    for i in range(5):
        for j in range(5):
            print(tabuleiro[i][j], end = ' ')
        print()

preencherTabuleiro()
exibirRegras()

exibirTabuleiro()
