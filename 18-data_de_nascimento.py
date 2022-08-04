'''Data de Nascimento'''

import numpy as np
import datetime
from datetime import date
from tracemalloc import stop

def calc_idade(nascimento):
    hoje = date.today()
    print("Digite a sua data de nascimento abaixo:")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    nascimento = datetime.date(ano, mes, dia)

    if (ano < 1922) or (ano > 2021):
        '''idade = "err"'''
        raise Exception("Sua data de nascimento não é válida. Tente novamente.\n\n")

    else:
        print("Sua data de nascimento é: ", dia, "/", mes, "/", ano)
        idade = (hoje.year - nascimento.year)
    
    return idade

print(">>>>>>>>>>PROGRAMA IDADE<<<<<<<<<<")

nascimento = 1

rodar = True

while rodar:
    try:
        nome = input("Digite o seu nome completo:\n")
        idade = calc_idade(nascimento)
        print(nome,", a sua idade é: ", idade)
        rodar = False
    
    except Exception as e:
        print(e)
        rodar = True
