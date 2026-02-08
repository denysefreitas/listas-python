# python pythonprogressivo/lacosloopings/00listalacosloopings/Questao40.py

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

qntCidades = 5
qntMenos2000Veiculos = 0
somaVeiculos = 0.0
somaAcidentes = 0

for i in range(qntCidades):
    codigo = input(f"Informe o código da {i + 1}º cidade: ")
    veiculosPasseio = int(input(f"Informe a quantidade de veículos de passeio na cidade de código {codigo} (em 1999): "))
    somaVeiculos += veiculosPasseio

    nAcidentes = int(input(f"Informe a quantidade de acidentes de trânsito com vítimas na cidade de código {codigo} (em 1999): "))
    if veiculosPasseio < 2000:
        somaAcidentes += nAcidentes
        qntMenos2000Veiculos += 1

    if i == 0:
        maiorAcidentes = nAcidentes
        codigoMaiorAcidentes = codigo

        menorAcidentes = nAcidentes
        codigoMenorAcidentes = codigo
    else:
        if nAcidentes > maiorAcidentes:
            maiorAcidentes = nAcidentes
            codigoMaiorAcidentes = codigo

        if nAcidentes < menorAcidentes:
            menorAcidentes = nAcidentes
            codigoMenorAcidentes = codigo

print("\nRESULTADOS\n---------------------------")
print(f"Maior índice de acidentes (cidade de código {codigoMaiorAcidentes}): {maiorAcidentes} acidente(s)")
print(f"Menor índice de acientes (cidade de código {codigoMenorAcidentes}): {menorAcidentes} acidente(s)")
print(f"Média de veículos de passeio nas cidades: {somaVeiculos / qntCidades:.2f} veículo(s)")

if qntMenos2000Veiculos > 0:
    print(f"Média de acidentes de trânsito nas cidades de 2000 veículos de passeio: {somaAcidentes / qntMenos2000Veiculos:.2f} acidente(s)")