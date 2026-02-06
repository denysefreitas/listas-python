# python pythonprogressivo/funcoes/listaargumentoseparametros/exemplos/ArgumentoNomeado01.py

def mediaNotas(mat, quim, fis):
    media = (mat + quim + fis / 3)
    print("Média: %.2f" % media)

mediaNotas(7, 8, 10) # -> argumento posicional
mediaNotas(fis = 10, mat = 7, quim = 8) # -> argumento nomeado
mediaNotas(7, 8, fis = 10) # -> uso de ambos; posicionais SEMPRE primeiro



