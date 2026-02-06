# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao19.py

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma = 0.0
n = int(input("Informe a quantidade de valores: "))

for i in range(n):
    while True:
        num = float(input("Informe um valor entre 0 e 1000 (%d/%d): " % (i + 1, n)))

        if num >= 0 and num <= 1000:
            soma += num

            if i == 0:
                maior = num
                menor = num

            if num > maior:
                maior = num
            
            if num < menor:
                menor = num
            break;

        print("Valor inválido")

print("Soma:", soma)
print("Menor:", menor)
print("Maior:", maior)