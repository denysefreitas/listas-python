# python pythonprogressivo/testecondicional/listaifelse/exemplos/ExGenero.py

# Faça um programa que pergunta o gênero da pessoa. Se ela for mulher, digite 1. Se for homem, digite 2. Outro, 3.

# Para cada um, ele deve exibir uma mensagem dizendo o gênero escolhido.

genero = input("""Informe o seu gênero:
    1 - Mulher
    2 - Homem
    3 - Outro """)

if genero == '1':
    print("Você é mulher")
elif genero == '2':
    print("Você é homem")
else: 
    print("Outro gênero")