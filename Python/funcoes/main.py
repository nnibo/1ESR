'''
def saudacao(nome):
    return f'Ola {nome} seu noia'

mensagem = saudacao('Felipe')
print(mensagem)
'''
# ------------------------------------------------------------------------------
'''
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return f'A sua média é {media}'
print(calcular_media(9,8))
'''
# ------------------------------------------------------------------------------
'''
def somar(a, b):
    return a + b
args = [3, 5]
resultado = somar(*args) # Usa * para desempacotar a lista
print(resultado) # Saida: 8

kwargs = {'a': 3, 'b': 5}
resultado2 = somar(**kwargs) # Usa ** para desempacotar o dicionario
print(resultado2) # Saida: 8
'''
# ------------------------------------------------------------------------------
'''
def somar(a = 2, b = 3):
    return a + b
print(somar())
'''
# ------------------------------------------------------------------------------
'''
def criar_usuario(nome, idade = 18, cidade = 'São Paulo'):
    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

# Chamadas de função
criar_usuario("Ana") # Saída: Nome: Ana, Idade: 18, Cidade: São Paulo
criar_usuario("Pedro", 25) # Saída: Nome: Pedro, Idade: 25, Cidade: São Paulo
criar_usuario("Clara", 30, "Rio de Janeiro") # Saída: Nome: Clara, Idade: 30, Cidade: Rio de Janeiro
'''
# ------------------------------------------------------------------------------
'''
def altera_a(a):
    a = a + 1
    print(a)
    
a = 2
altera_a(a)

print(a)
'''
# ------------------------------------------------------------------------------
'''
def altera_lista(lista):
    lista.append(2)
    lista.append(5)

    print(lista)

lista = [1, 7, 8, 3]
altera_lista(lista)

print(lista)
# Para resgatar a lista original fazer:
    altera_lista(lista[:])
'''
# ------------------------------------------------------------------------------
'''
def soma_total(*numeros): # O # diz que podem ser varios numeros na chamada da funcao
    return sum(numeros)

print(soma_total(1, 2, 3)) # Saida: 6
print(soma_total(10, 20, 30, 100)) # Saida: 160
print(soma_total()) # Saida 0
'''
# ------------------------------------------------------------------------------
'''
def exibir_informacoes(**informacoes):
    for chave, valor in informacoes.items():
        print(f'{chave}: {valor}')

exibir_informacoes(nome = 'Ana', idade = 18, cidade = 'Sao Paulo\n')
exibir_informacoes(produto = 'Notebook', preco = 2500.00, marca = 'Dell')
'''





