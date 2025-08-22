# EX 1
# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# soma_elementos = 0
# for linha in matriz:
#     for elemento in linha:
#         soma_elementos += elemento
# print(soma_elementos)

# ------------------------------------------------

# EX 2
# import random
#
# def criar_matriz_quadrada(m, n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(random.randint(1, 10))
#         matriz.append(linha)
#     return matriz
#
# def verificar_matriz(matriz):
#     soma_elementos = 0
#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             if i == j:
#                 soma_elementos += matriz[i][j]
#     print(soma_elementos)
#
# def print_matriz(matriz):
#     for linha in matriz:
#         print(linha)
#
# matriz = criar_matriz_quadrada(3,3)
# print_matriz(matriz)
# verificar_matriz(matriz)

# ------------------------------------------------

# EX 3
# import random
#
# def criar_matriz_diagonal_secundaria(m, n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(random.randint(1,10))
#         matriz.append(linha)
#     return matriz
#
# def verificar_matriz(matriz):
#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             if i + j == len(matriz) - 1:
#                 print(matriz[i][j])
#
# def print_matriz(matriz):
#     for linha in matriz:
#         print(linha)
#
# matriz = criar_matriz_diagonal_secundaria(3,3)
# print_matriz(matriz)
# verificar_matriz(matriz)

# ------------------------------------------------

# EX 4
# from random import randint
# def criar_matriz_aleatoria(m, n):
#     matriz = []
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             linha.append(randint(1,10))
#         matriz.append(linha)
#     return matriz

# def transposta(matriz):
#     m = len(matriz)
#     n = len(matriz[0])
#     matriz_transposta = []
#     for linha in range(n):
#         matriz_transposta.append([])
#         for coluna in range(m):
#             matriz_transposta[coluna].append(matriz[linha][coluna])
#     return matriz_transposta

# matriz = criar_matriz_aleatoria(3,2)
# matriz_tranposta = transposta(matriz)

# for linha in matriz:
#     print(linha)
# ------------------------------------------------

# EX 6
from random import randint

def criar_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(randint(1,10))
        matriz.append(linha)
        # for elemento in linha:
        #     elemento = elemento * 2
        #     print(elemento)

    return matriz

def multiplicar_elementos_matriz(matriz, numero_multiplicacao):
    matriz_multiplicada = criar_matriz(3,3)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_multiplicada[i][j] = matriz[i][j] * numero_multiplicacao
    return matriz_multiplicada          

matriz = criar_matriz(3,3)
print(matriz)
print(multiplicar_elementos_matriz(matriz, 2))


