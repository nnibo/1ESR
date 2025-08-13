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
def criar_matriz_contra_diagonal(m, n):
    matriz = []
    for i in range(m):
        linha = []

        for j in range(n):
            linha.append(0)
        linha[j - i] = 1
        matriz.append(linha)
    return matriz
matriz_diagonal = criar_matriz_contra_diagonal(5,5)
print(matriz_diagonal)

# -------------------------------------------------------------------------

# EX 15 DA LISTA DE REVISAO
# texto = 'bom dia, boa tarde, boa noite, voce é boa'
#
# lista = texto.split()
# ocorrencias = {}
#
# for palavra in lista:
#     if palavra in ocorrencias:
#         ocorrencias[palavra] += 1
#     else:
#         ocorrencias[palavra] = 1
#
# print(ocorrencias)