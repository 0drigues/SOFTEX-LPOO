'''Operações'''

import numpy as np

def Op(valor1, valor2, operacao):
    if (operacao == 1):
        res = (valor1 + valor2)

    elif (operacao == 2):
        res = (valor1 - valor2)

    elif (operacao == 3):
        res = (valor1 * valor2)

    elif (operacao == 4):
        res = (valor1 / valor2)

    else:
        res = 0
        print("A operação registrada não é válida.")

    return res


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
print("Catálogo de operações:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
n3 = int(input("Selecione a operação desejada: "))

resultado = Op(n1, n2, n3)

print("O resultado da operação é: ", resultado)