#python pythonprogressivo/base/listaprint/exemplos/ExPrintFormatado02.py

total = float(input("Informe o prêmio total da Mega-Sena: "))
num_ganhadores = int(input("Informa a quantidade de ganhadores da Mega-Sena: "))

print(f"O prêmio total foi de R$ {total} e teve {num_ganhadores} ganhadores")
print("Cada um deles receberá %.2f" % (total/num_ganhadores))