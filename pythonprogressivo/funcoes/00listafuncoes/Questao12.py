# python pythonprogressivo/funcoes/00listafuncoes/Questao12.py

# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter(horas, min):
    if horas > 12:
        horasP = horas - 12
        sigla = 'P'
    elif horas == 12 or horas == 0:
        horasP = 12
        if horas == 12:
            sigla = 'P'
        else:
            sigla = 'A'
    else:
        horasP = horas
        sigla = 'A'

    exibir(horasP, horas, min, sigla)

def exibir(horasP, horasA, min, sigla):
    print(f"{horasA}:{min} corresponde a {horasP}:{min} {sigla}.M.")

while True:
    print("Esse programa realiza a conversão da notação de 24h para 12h.")
    while True:
        h = int(input("Informe as horas (0h até 23h): "))
        
        if h >= 0 and h <= 23:
            break
    
    while True:
        min = int(input("Informe os minutos (0 até 59): "))
        
        if min >= 0 and min <= 59:
            break
    
    converter(h, min)
    opcao = input("Se deseja encerrar as conversões, digite 'X'. Caso contrário, prossiga com outro caractere (ex: 'S'): ")

    if opcao == 'X':
        break