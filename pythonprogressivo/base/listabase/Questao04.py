# python pythonprogressivo/base/listabase/Questao04.py

#Um novo modelo de carro, super econômico foi lançado.
#Ele faz 20 km com 1 litro de combustível.
#Cada litro de combustível custa R$ 5,00.

#Faça um programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível ele pode comprar e quantos kilometros o carro consegue andar com este tanto de combustível.

#Seu script será usado no computador de bordo do carro

dinheiro = float(input("Informe o valor que você possui: "))

litro = dinheiro / 5
km = litro * 20

print("Com R$ %.2f, é possível comprar %.2f litros de combustível e rodar %.2f km" % (dinheiro, litro, km))