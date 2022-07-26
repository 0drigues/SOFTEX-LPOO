# -*- coding: utf-8 -*-
"""8-pandas_aprovacao

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ejW3VAh3iy5k2wdB_tj0wtAHq-E3nMm
"""

'''pandas - Aprovação dos alunos'''

import pandas as pd
import numpy as np

tabela = pd.read_csv("/notas_alunos.csv", sep = ";")

notas1 = tabela["nota_1"]
notas2 = tabela["nota_2"]
faltas = tabela["faltas"]

lista_de_nota1 = np.array(notas1)
lista_de_nota2 = np.array(notas2)
lista_de_faltas = np.array(faltas)
lista_de_medias = (lista_de_nota1 + lista_de_nota2)/2

lista_situacao = []

tabela["média"] = lista_de_medias

tabela.loc[tabela["média"] >= 7, "situacao"] = "APROVADO"
tabela.loc[tabela["faltas"] > 5, "situacao"] = "REPROVADO"
tabela.loc[tabela["média"] < 7, "situacao"] = "REPROVADO"
   
print(tabela.head())

tabela.to_csv("/notas_alunos.csv", sep = ";", index = False)