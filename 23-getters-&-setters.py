#Algoritmo para remoção de km's mal calibrados

import numpy as np
import cmath as cm

class Carro:
    def __init__(self, marca, modelo, km_rodados):
        self.marca = marca
        self.modelo = modelo
        self.km_rodados = km_rodados

    def Correcao_Km(self, km_removidos):
        self.km_removidos = self.km_rodados - km_removidos

    #Getter
    @property
    def km_rodados(self):
        return self._km_rodados

    #Setter
    @km_rodados.setter
    def km_rodados(self, km_corrigidos):
        if isinstance(km_corrigidos, str):
            km_corrigidos = float(km_corrigidos.replace('km', ''))

        self._km_rodados = km_corrigidos

#Exemplo de teste

c1 = Carro("Chevrolet", "Onix", "120000")
c1.Correcao_Km(5000)
print(c1.marca, c1.modelo, c1.km_removidos)

c2 = Carro("Honda", "Fit", "30000km")
c2.Correcao_Km(5000)
print(c2.marca, c2.modelo, c2.km_removidos)

c3 = Carro(input("Digite qual é a marca do seu carro: "), input("Digite qual é o modelo: "), input("Digite quantos km estão marcados no contador: "))
c3.Correcao_Km(5000)
print(c3.marca, c3.modelo, c3.km_removidos)
