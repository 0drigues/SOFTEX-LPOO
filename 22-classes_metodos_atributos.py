import numpy as np
from random import randint

class Notebook:
    total_notebooks = 0
    def __init__(self, marca, memoria_ram, placa_de_video, tam_hd):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.tam_hd = tam_hd
    
    @staticmethod
    def gerador_serial():
        rand = randint(10000, 20000)
        print(rand)

    @staticmethod
    def num_notebooks():
        total_notebooks = 0
        total_notebooks = total_notebooks + 1
        print(total_notebooks)
        return total_notebooks

n1 = Notebook("Asus", "16GB", "Radeon", "500GB")
n1.num_notebooks
n1.gerador_serial
print(n1.marca, n1.memoria_ram, n1.placa_de_video, n1.tam_hd)
n2 = Notebook("Acer", "2GB", "Intel HD Graphics", "500GB")
n2.num_notebooks
n2.gerador_serial
print(n2.marca, n2.memoria_ram, n2.placa_de_video, n2.tam_hd)
n3 = Notebook("Lenovo", "12GB", "VX Vega", "1TB")
n3.gerador_serial
n3.num_notebooks
print(n3.marca, n3.memoria_ram, n3.placa_de_video, n3.tam_hd)
n4 = Notebook("Mac", "8GB", "Radeon/M1", "256GBSSD")
n4.gerador_serial
n4.num_notebooks
print(n4.marca, n4.memoria_ram, n4.placa_de_video, n4.tam_hd)