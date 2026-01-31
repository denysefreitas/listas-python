# python pythonprogressivo/testecondicional/listaifelse/exemplos/ExFilaPrioridade.py

# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. Escreva um programa que pergunta a situação do usuário (se é idoso, se é gestante, se é cadeirante ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.

print("1 - Idoso")
print("2 - Gestante")
print("3 - Cadeirante")
print("4 - Nenhuma das opções anteriores")
resposta = int(input("Indique o índice que você se enquadra: "))

if resposta == 1 or resposta == 2 or resposta == 3:
    print("Você tem direito à fila prioritária")
elif resposta == 4:
    print("Você não tem direito à fila prioritária")
else:
    print("Você informou um índice fora dos parâmetros definidos. O programa não será executado.")