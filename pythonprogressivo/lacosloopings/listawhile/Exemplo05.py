# python pythonprogressivo/lacosloopings/listawhile/Exemplo05.py

# Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha


senha = 1107
senha_usuario = int(input("Informe uma senha númerica de quatro dígitos: "))

while senha_usuario != senha:
    senha_usuario = int(input("Informe uma senha númerica de quatro dígitos: "))
    
print("Você acertou a senha!")