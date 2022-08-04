'''Calculadora'''

from tracemalloc import stop
import numpy as np

def Soma(v1, v2):
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    res = v1 + v2
    return res

def Subtracao(v1, v2):
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    res = v1 - v2
    return res

def Multiplicacao(v1, v2):
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    res = v1 * v2
    return res

def Divisao(v1, v2):
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    res = v1 / v2
    return res


operacao = 1
v1 = 0
v2 = 0


while operacao:
    print("Digite qual operação deseja realizar:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\n")
    operacao = int(input())

    if(operacao == 0):
        print("Fim da execução.")
        stop
    
    if(operacao == 1):
        resultado = Soma(v1, v2)
        print("O resultado é: ", resultado)
        print("\n>>>>>>>>>>FIM DA OPERAÇÃO<<<<<<<<<<\n")

    
    if(operacao == 2):
        resultado = Subtracao(v1, v2)
        print("O resultado é: ", resultado)
        print("\n>>>>>>>>>>FIM DA OPERAÇÃO<<<<<<<<<<\n")


    if(operacao == 3):
        resultado = Multiplicacao(v1, v2)
        print("O resultado é: ", resultado)
        print("\n>>>>>>>>>>FIM DA OPERAÇÃO<<<<<<<<<<\n")

    
    if(operacao == 4):
        resultado = Divisao(v1, v2)
        print("O resultado é: ", resultado)
        print("\n>>>>>>>>>>FIM DA OPERAÇÃO<<<<<<<<<<\n")
