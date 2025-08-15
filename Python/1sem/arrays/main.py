#Exemplo lista
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0]) # 'trek'
'''

#Adicionar uma string a lista
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles.append('Nibaum')
print(bicycles)
'''

#Adicionar em uma posição especifica
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(1,'Ducati')
print(bicycles)
'''

#Para remover um item
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[1]
print(bicycles)
'''

#Para remover um item escrito
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.remove('redline')
print(bicycles)
'''

#Usando pop especificadamente
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles.pop(0))
print(bicycles)
'''

#Ordem alfabetica
'''
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
'''

#Ordem alfabetica reversa
'''
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
'''

#Não altera a lista, apenas motra como é em ordem alfabetica
'''
cars = ['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)
'''

#Exercicio fodase
nome_completo = 'Ana Clara Souza'
nomes_separados = nome_completo.split()
todosNomes = nomes_separados[0][0], nomes_separados[1][0], nomes_separados[2][0]

print(('.').join(todosNomes))
