# python pythonprogressivo/testecondicional/listafinal/Questao17.py

# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Informe um número inteiro menor que 1000: "))

if num < 1000:
    centena = int(num / 100)
    dezena = int((num - centena * 100) / 10)
    unidade = int(num - (centena * 100)- (dezena * 10))

    if centena == 1:
        msg_c = "centena"
    else:
        msg_c = "centenas"

    if dezena == 1:
        msg_d = "dezena"
    else:
        msg_d = "dezenas"

    if unidade == 1:
        msg_u = "unidade"
    else:
        msg_u = "unidades"

    if centena == 0:
        if dezena == 0:
            print("%d %s" % (unidade, msg_u))
        else:
            print("%d %s e %d %s" % (dezena, msg_d, unidade, msg_u))
    else:
        print("%d %s, %d %s e %d %s" % (centena, msg_c, dezena, msg_d, unidade, msg_u))
else:
    print("Você informou um valor inesperado. O programa não será executado.")