'''Calculadora'''

from tracemalloc import stop
import numpy as np

def Op (operacao, valor1, valor2):
    '''if (operacao == 0):
        res = print("Fim da execução.")'''

    '''el'''
    if (operacao == 1):
        res = (valor1 + valor2)

    elif (operacao == 2):
        res = (valor1 - valor2)

    elif (operacao == 3):
        res = (valor1 * valor2)

    elif (operacao == 4):
        res = (valor1 / valor2)

    else:
        res = print("Essa opção não existe.")

    return res

n1 = int(input("Digite qual operação deseja realizar:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\n"))
n2 = float(input("Digite o primeiro valor: "))
n3 = float(input("Digite o segundo valor: "))

resultado = 0

if (n1 == 0):
    print("Fim da execução.")
    stop

while (n1 != 0):
    resultado = Op(n1, n2, n3)
    print("O resultado da operação é: ", resultado)



