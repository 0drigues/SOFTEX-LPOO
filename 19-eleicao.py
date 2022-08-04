'''O código não funciona da maneira devida. Não consegui criar uma lógica forte o suficiente em 
minha mente para montar um código que realizasse a atividade pedida. Upei desta forma na esperança
de alguém entender o que pode ser aprimorado no futuro.'''

'''Eleição'''

from tracemalloc import stop
from unittest.util import strclass
import numpy as np
import enum

class erro_voto(enum.Enum):
    erro_branco = 0
    erro_texto = "dnv"
    final = "finalizar"

def contador_voto(voto):
    voto = int(input())
    if voto == 889:
        c1 = c1 + 1
        total = total + 1
        print("Voto para o CANDIDATO 1 registrado.\n\n")
    
    elif voto == 847:
        c2 = c2 + 1
        total = total + 1
        print("Voto para o CANDIDATO 2 registrado.\n\n")
    
    elif voto == 515:
        c3 = c3 + 1
        total = total + 1
        print(print("Voto para o CANDIDATO 3 registrado.\n\n"))
    
    elif voto == 0:
        branco = branco + 1
        total = total + 1
    
    elif voto == "S":
        voto = "finalizar"
        print("Votação finalizada.")

    elif voto == strclass:
        erro_voto.erro_texto
        print("Seu voto não é válido. Tente novamente.")

    else:
        erro_voto.erro_branco
        branco = branco + 1
        total = total + 1
    
voto = 0
c1 = 0
c2 = 0
c3 = 0
branco = 0
total = 0
rodar = True
contador = 0

while rodar:
    try:
        print("Digite o número de seu voto.\nCaso deseje finalizar a votação, pressione a tecla S.")
        contador = contador_voto(voto)
        rodar = True

    except:
        voto = "finalizar"
        rodar = False
        print("DADOS FINAIS DA VOTAÇÃO:\n")
        print("Votos para o CANDIDATO 1: ", c1)
        print("Votos para o CANDIDATO 2: ", c2)
        print("Votos para o CANDIDATO 3: ", c3)
        print("Votos em BRANCO/NULOS: ", branco)
        print("Número final de votos: ", total)





