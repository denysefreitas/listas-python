# python pythonprogressivo/lacosloopings/listarange/Exemplo04.py

# Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada

num = int(input("Informe a tabuada que você deseja ver: "))

for i in range (1, 11):
    print("%d x %d = %d" % (num, i, num * i))