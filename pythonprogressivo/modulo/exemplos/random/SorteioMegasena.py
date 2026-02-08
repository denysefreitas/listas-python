# python pythonprogressivo/modulo/exemplos/random/SorteioMegasena.py

import random

n1 = random.randint(1, 60)

while True:
    n2 = random.randint(1, 60)
    if n2 != n1:
        break

while True:
    n3 = random.randint(1, 60)
    if n3 != n1 and n3 != n2:
        break

while True:
    n4 = random.randint(1, 60)
    if n4 != n1 and n4 != n2 and n4 != n3:
        break

while True:
    n5 = random.randint(1, 60)
    if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4:
        break

while True:
    n6 = random.randint(1, 60)
    if n6 != n1 and n6 != n2 and n6 != n3 and n6 != n4 and n6 != n5:
        break

print(n1, n2, n3, n4, n5, n6)
