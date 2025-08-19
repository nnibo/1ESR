# alunos = [
#     {
#     "Nome": "André",
#     "Sexualidade": "Homo"
#     },
#     {
#     "Nome": "João",
#     "Sexualidade": "Hetero"
#     }
#
# ]
#
# print(alunos[1]["Nome"])
# print(alunos[0]["Sexualidade"])

# -----------------------------------------------------------------------------

# Exemplo 1
# numero = int(input("Digite um quantos zeros você quer colocar na lista: "))
# numeros = []
#
# for n in range(numero):
#     numeros.append(0)
#
# print(numeros)

# -------------------------------------------------------------------------------

# Exemplo 2
# numeros = [[0, 1, 2],
#        [3, 4, 5, ],
#        [6, 7, 8]]
#
# for i in range(len(numeros)):
#     for j in range(len(numeros[i])):
#         print(numeros[i][j])

# -------------------------------------------------------------------

# Exemplo 3
# matriz = []
# m = 10
# n = 10
#
# for i in range(m):
#     matriz.append([])
#     for j in range(n):
#         matriz[i].append(0)
#
# for i in matriz:
#     print(i)

# ---------------------------------------------------------------------

# Exemplo 4
# def criar_matriz_zeros(m, n):
#     # Inicializa uma mariz vazia
#     matriz = []
#
#     # Loop para criar m linhas
#     for i in range(m):
#         linha = [] # Cria uma nova linha vazia
#
#         # Loop para adicionar n zeros na linha
#         for j in range(n):
#             linha.append(0)
#         # Adiciona a linha criada a matriz
#         matriz.append(linha)
#     return matriz
#
# matriz = criar_matriz_zeros(2,2)
# print(matriz)

# -------------------------------------------------------------------------

# EX 1
# Matriz identidade tem 1 apenas na diagonal principal
# def criar_matriz_identidade(m, n):
#     matriz = []
#
#     for i in range(m):
#         linha = []
#         for j in range(n):
#             if i == j:
#                 linha.append(1)
#             else:
#                 linha.append(0)
#         matriz.append(linha)
#     return matriz
#
# matriz_identidade = criar_matriz_identidade(5,5)
# print(matriz_identidade)

# -------------------------------------------------------------------------

# EX 2
# def criar_matriz_contra_diagonal(m, n):
#     matriz = []

#     for i in range(m):
#         linha = []

#         for j in range(n):
#             if i + j == m - 1:
#                 linha.append(1)
#             else:
#                 linha.append(0)
#         matriz.append(linha)
#     return matriz

# def print_matriz(matriz):
#     for linha in matriz:
#         print(linha)

# print_matriz(criar_matriz_contra_diagonal(4,4))

# -------------------------------------------------------------------------

# EX 3
# import random

# def criar_matriz_numeros_aleatorios(m, n):
#     matriz = []

#     for i in range(m):
#         linha = []

#         for j in range(n):
#             linha.append(random.randint(1, 200))
#         matriz.append(linha)
#     return matriz

# def print_matriz(matriz):
#     for linha in matriz:
#         print(linha)

# print_matriz(criar_matriz_numeros_aleatorios(4,4))

# -------------------------------------------------------------------------

# EX 4
# import random

# def soma_elementos_diagonal_principal(m, n):
#     matriz = []
#     soma_elementos = 0
#     for i in range(m):
#         linha = []

#         for j in range(n):
#             linha.append(random.randint(1, 9))

#             if i == j:
#                 soma_elementos += linha[j]
#         matriz.append(linha)
#     return matriz, soma_elementos
  
# def print_matriz(matriz):
#     for linha in matriz:
#         print(linha)

# print_matriz(soma_elementos_diagonal_principal(4,4))

# -------------------------------------------------------------------------

# EX 5
def criar_matriz_identidade(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(m)
            else:
                linha.append(n)
        matriz.append(linha)
    return matriz

print(criar_matriz_identidade(5,6))
# -------------------------------------------------------------------------

# EX 6