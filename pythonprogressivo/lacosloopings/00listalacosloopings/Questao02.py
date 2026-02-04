# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao02.py

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Defina um nome de usuário: ")

while True:
    senha = input("Defina uma senha para o usuário '%s' diferente do seu próprio nome: " % nome)

    if senha == nome:
        print("Senha inválida")
    else:
        print("Senha válida.")
        break

