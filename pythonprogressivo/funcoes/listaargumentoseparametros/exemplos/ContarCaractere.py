# python pythonprogressivo/funcoes/listaargumentoseparametros/exemplos/ContarCaractere.py

# Crie um script em Python que pede uma frase (string) ao usuário e em seguida um caractere. Em seguida, seu script deve dizer quantas vezes aquele caractere apareceu na frase digitar. Use função com parâmetros.

def buscarCaractere(frase, char):
    quantidade = 0

    for letra in frase:
        if letra == char:
            quantidade += 1
    
    print("O caractere '%s' foi encontrado %d vezes na frase '%s'" % (char, quantidade, frase))

frase = input("Informe uma frase: ")
char = input("Informe um caractere a ser buscado na frase (ex: 'e'): ")
buscarCaractere(frase, char)

