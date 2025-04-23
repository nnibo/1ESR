# EXEMPLOS FOR
'''
frase = 'boa noite, estou com uma bixeira na testa'

for c in frase:
    print(c, end='#') # A cada fim de um caractere, um # é adicionado
'''
# -----------------------------------------------------------------------------
'''
for i in range(0, 30, 2): #O 2 do lado direito, pula o numero de 2 em 2
    print(i)
'''
# -----------------------------------------------------------------------------
'''
lista = ['a', 'd', 'y', 'p']

for i, c in enumerate(lista): # o i recebe o indice, o c recebe o elemento
    print(i, ':', c)
'''
# -----------------------------------------------------------------------------
'''
lista = ['a', 'b', 'c', 'd']

if 'a' in lista:
    print('A lista contem a letra a')
'''
# -----------------------------------------------------------------------------
'''
for i in range(0, 30):
    if i == 15:
        break
    print(i)
'''
# -----------------------------------------------------------------------------
'''
for i in range(0, 30):
    if i%2 != 0:
        continue
    print(i)
'''
# -----------------------------------------------------------------------------
'''
for i in range(0, 30):
    if i == 15:
        print('Encontrei')
        break
else:
    print('nao encontrei')
'''
# -----------------------------------------------------------------------------
'''
a = ('John', 'Charles', 'Mike')
b = ('Jenny', "Christy", "Monica")

x = zip(a, b)
print(list(x))

names = ['John', 'Robert']
surnames = ['Smith', 'De Niro']
numbers = [1, 2]

for name, surname, number in zip(names, surnames, numbers) :
    print(name, surname, numbers)
'''
# -----------------------------------------------------------------------------
'''
pares = []

for i in range(0, 101, 2):
        if i%2 == 0:
            pares.append(i)
print(pares)
'''

# EXEMPLOS WHILE
'''
currentNumber = 0

while currentNumber <= 10:
    print(currentNumber)
    currentNumber += 1
'''
# -----------------------------------------------------------------------------
'''
while True:
    entrada = input('Digite algo: ')

    if entrada == 'quit':
        break
    else:
        print('o texto digitado foi: ', entrada)
'''
# -----------------------------------------------------------------------------
'''
currentNumber = 0

while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue
    else:
        print(currentNumber)
'''