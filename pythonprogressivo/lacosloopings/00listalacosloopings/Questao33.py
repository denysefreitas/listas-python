# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao33.py

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

somaTemperaturas = 0.0
count = 0
count = int(count)

while True:
    temperatura = float(input("Informe uma temperatura (°C): "))
    somaTemperaturas += temperatura
    count += 1

    if count == 1:
        maiorTemperatura = temperatura
        menorTemperatura = temperatura
    
    if temperatura > maiorTemperatura:
        maiorTemperatura = temperatura
    
    if temperatura < menorTemperatura:
        menorTemperatura = temperatura

    print("Deseja encerrar a sessão? (S - SIM / N - NÃO) ")
    continuar = input("Resposta: ")

    if continuar == 'S':
        break

print(f"Maior temperatura: {maiorTemperatura:.2f}°C")
print(f"Menor temperatura: {menorTemperatura:.2f}°C")
print(f"Média das temperaturas: {somaTemperaturas / count:.2f}°C")