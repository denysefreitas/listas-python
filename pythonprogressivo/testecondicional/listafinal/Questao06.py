# python pythonprogressivo/testecondicional/listafinal/Questao06.py

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro = int(input("Informe um número inteiro: "))
segundo = int(input("Informe um número inteiro: "))
terceiro = int(input("Informe um número inteiro: "))

print("Ordem inicial: %d, %d, %d" % (primeiro, segundo, terceiro))
print("Alterando a ordem das posições...")

if terceiro > segundo:
    aux = segundo
    segundo = terceiro
    terceiro = aux

if segundo > primeiro:
    aux = primeiro
    primeiro = segundo
    segundo = aux

if terceiro > primeiro:
    aux = segundo
    segundo = primeiro
    primeiro = terceiro
    terceiro = aux

print("Alterações realizadas com sucesso!")
print("Ordem atual: %d, %d, %d" % (primeiro, segundo, terceiro))

    
