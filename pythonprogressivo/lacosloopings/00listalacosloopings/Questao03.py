# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao03.py

# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

while True:
    nome = input("Informe um nome (mín. 4 caracteres): ")

    if len(nome) > 3:
        break

while True:
    idade = int(input("Informe uma idade [0 - 150]: "))

    if idade > 0 and idade < 150:
        break
    
while True:
    salario = float(input("Informe o seu salário: "))

    if salario > 0:
        break

while True:
    sexo = input("Informe o seu sexo (F - Feminino ou M - Masculino): ")

    if sexo == "F" or sexo == "M":
        break

while True:
    print("S - Solteiro(a)")
    print("C - Casado(a)")
    print("V - Viúvo(a)")
    print("D - Divorciado(a)")
    estadoCivil = input("Informe o seu estado civil: ")

    if estadoCivil == "S" or estadoCivil == "C" or estadoCivil == "V" or estadoCivil == "D":
        break
    
print("Todos os dados foram validados.")