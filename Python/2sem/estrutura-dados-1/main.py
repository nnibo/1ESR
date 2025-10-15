from random import randint
from time import time
def ramdom_list():
    lista = []
    for i in range(1000000):
        lista.append(randint(0, 99999))
    return lista

def busca_sequencial(lista, e):
    operacoes = 0
    for i in lista:
        operacoes += 1
        if i == e:
            print('O elemento está na lista')
            print('Operações: {}'.format(operacoes))
            return
    print('O elemento não está na lista')
    print('Operações: {}'.format(operacoes))

lista = ramdom_list()

tempo_inicial = time()

busca_sequencial(lista, 1234)
print("Tempo: ", time() - tempo_inicial)