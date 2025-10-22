import random
from time import time

def ordnacao_selecao(A):
    n = len(A)
    #Percoree o arranjo A
    for i in range(n):
        #Encontra o elemento minimo em A
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento minimo na posição correta\
        A[i], A[minimo] = A[minimo], A[i]

tempo_inicial = time()
A = random.sample(range(-10000, 10000), 10000)

print("Arranjo não ordenado: ", A)

ordnacao_selecao(A)
print("Arranjo ordenado: ", A)
print("Tempo demorado: ", time() - tempo_inicial)

# quick sort
def quick_sort(A):
    if len(A) <= 1:
        return A
    pivo = A[0]
    menores = []
    maiores = []

    for i in A[1:]:
        if i <= pivo:
            menores.append(i)
        else:
            maiores.append(i)

    return quick_sort(menores) + [pivo] + quick_sort(maiores)

