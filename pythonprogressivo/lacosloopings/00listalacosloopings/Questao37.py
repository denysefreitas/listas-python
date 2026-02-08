# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao37.py

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

somaAlturas = 0.0
somaPesos = 0.0
count = 0
count = int(count)

def eValido (num):
    return num > 0

while True:
    codigo = input("Informe o seu código: ")

    if codigo == "0":
        break

    while True:
        altura = float(input("Informe a sua altura (em metros): "))

        if eValido(altura):
            somaAlturas += altura
            break
        
        print("[AVISO] Valor inválido.")

    while True:
        peso = float(input("Informe o seu peso (em kg): "))

        if eValido(peso):
            somaPesos += peso
            break
        
        print("[AVISO] Valor inválido.")

    count += 1

    if(count == 1):
        codigoAlto = codigo
        maisAlto = altura

        codigoBaixo = codigo
        maisBaixo = altura

        codigoGordo = codigo
        maisGordo = peso

        codigoMagro = codigo
        maisMagro = peso
    
    if altura > maisAlto:
        maisAlto = altura
        codigoAlto = codigo
    
    if altura < maisBaixo:
        maisBaixo = altura
        codigoBaixo = codigo
    
    if peso > maisGordo:
        maisGordo = peso
        codigoGordo = codigo
    
    if peso < maisMagro:
        maisMagro = peso
        codigoMagro = codigo

print("RESULTADOS\n-------------------------------")
print(f"Maior altura: {maisAlto} m")
print("Código do aluno(a) mais alto:", codigoAlto)
print(f"Menor altura: {maisBaixo} m")
print("Código do aluno(a) mais baixo:", codigoBaixo)
print(f"Maior peso: {maisGordo} kg")
print("Código do aluno(a) mais gordo:", codigoGordo)
print(f"Menor peso: {maisMagro} kg")
print("Código do aluno(a) mais magro:", codigoMagro)
print(f"Média das alturas: {somaAlturas / count:.2f} m")
print(f"Média dos pesos: {somaPesos / count:.2f} kg")