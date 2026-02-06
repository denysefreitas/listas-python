#python pythonprogressivo/base/listaprint/exemplos/ExPrintFormatado03.py

num = 10.234
x = "|"
frase = "Olá mundo!"

print(f"{x:7} {frase}")   # largura 10
print(f"{x:<10} {frase}")     # alinhado à esquerda
print(f"{x:>10} {frase}")     # à direita
print(f"{x:^10} {frase}")     # centralizado

print(f"{num:.2f}")
print(f"{num:.3f}")
print(f"{num:.0f}")
