'''Categorias de veículos'''

import numpy as np

print("Abaixo, veja em qual categoria o seu veículo se encaixa:\n\n")

qtd_rodas = int(input("Quantas rodas possuem o veículo?\n"))
peso = float(input("Qual é o peso do veículo?\n"))
qtd_pessoas = int(input("Quantas pessoas o veículo pode comportar?\n"))

if (qtd_rodas == 4) and (qtd_pessoas <= 8) and (peso <= 3500):
    print("Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg.")

elif (qtd_rodas >= 4) and (peso > 3500) and (peso <= 6000):
    print("Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg.")

elif (qtd_rodas >= 4) and (qtd_pessoas > 8):
    print("Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas.")

elif (qtd_rodas >= 4) and (peso > 6000):
    print("Veículos com quatro rodas ou mais e com mais de 6000 kg.")

elif (qtd_rodas == 2) or (qtd_rodas == 3):
    print("Veículos com 2 ou 3 rodas.")

else:
    print("O seu veículo não está dentre as categorias disponíveis.")