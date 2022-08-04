"""Teste de aprovação"""

import numpy as np

print("Confira se você foi aprovado ou não abaixo:\n")

nome = str(input("Digite o seu nome e sobrenome:\n"))
nota_1 = float(input("Digite a sua primeira nota:\n"))
nota_2 = float(input("Digite a sua segunda nota:\n"))
faltas = int(input("Digite o seu número de faltas no semestre:\n"))

media = (nota_1 + nota_2)/2

if (media >= 7.0 and faltas <= 3):
    print(nome, ", você foi aprovado por média.")
    
if (media >= 7.0 and faltas > 3):
    print(nome, ", você foi reprovado por falta.")

if (media < 7.0 and faltas <= 3):
    print(nome, ", você foi reprovado por média.")

if (media < 7.0 and faltas > 3):
    print(nome, ", você foi reprovado por média e por falta.")

