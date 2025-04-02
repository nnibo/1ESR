#Exemplo 1 - Menos usada
'''
numero = 10
texto = 'o valor é: %f' % numero
print(texto)
'''

#Exemplo 2 - Media usada
'''
numero_1 = int(input('Digite o primeiro numero'))
numero_2 = int(input('Digite o segundo numero'))
resultado = numero_1 * numero_2
texto = 'o valor de {} vezes {} é {}'.format(numero_1,numero_2 ,resultado)
print(texto)
'''

#Exemplo 3 - Mais usada e moderna USANDO O f
'''
numero_1 = int(input('Digite o primeiro numero'))
numero_2 = int(input('Digite o segundo numero'))
resultado = numero_1 * numero_2
texto = f'o valor de {numero_1} vezes {numero_2} é {resultado}'
print(texto)
'''

#Operacoes com Strings
#Exemplo1
'''
s = 'Ola, mundo!'
number = len(s)
#Tamanho da String
print(number)
'''

#Exemplo2
'''
s = 'Ola, mundo!'

#Substitui mundo na variavel s, por Nibaum
s1 = s.replace('mundo', 'Nibaum')
print(s1)

a = 'aaaaaaaaaa'
a1 = a.replace('a','b', 3) #Os 3 primeiros a vão ser trocados por b
'''

#Exemplo 3
'''
s = 'Ola mundo'
#A string s começa com 'Ola'?
print(s.startswith('Ola'))

#A string s termina com 'mundo'?
print(s.endswith('mundo'))

#Quantas vezes aparece a palavra abacate aparece na variavel
print(s.count('mundo'))
'''

#Exemplo 4
'''
# Como "capitalizar" (transformar a primeira letra da primeira palavra em maiúscula).
s = "ordem e progresso"
print(s.capitalize())

# Como verificar se uma string só possui números.
print('12345'.isdigit())
print('12345abc'.isdigit())

# Como verificar se uma string é alfanumérica (só possui letras e números).
print('12345abc'.isalnum())
'''

#Exemplo 5
'''
#String.find: procura uma substring em uma string e retorna o índice:
s = "Pedro, Paulo e Maria"
print(s.find("a"))

#Além disso, ela recebe um argumento adicional que especifica o
#índice pelo qual ela deve começar sua procura:
print(s.find("a", 10))

#Ord: Retorna o valor decimal de um caractere
print(ord('a'))

#chr: retorna o caractere de um valor decimal.
print(chr(97))
'''

#Exemplo 6
'''
s = 'Isso é um texto'
print(s.title())
print(s.lower())
print(s.upper())
'''

#Exemplo 7
'''
texto = 'isso é    '
texto2 = '    um texto'
print(texto + texto2)

texto = texto.rstrip()
texto2 = texto2.lstrip()
print(texto, texto2)
'''

#Exemplo 8
'''
frase = 'oi gente tudo bem'
comprimento = len(frase) - 1
print(frase[comprimento])

#Outro jeito de fazer
frase2 = 'oi legal ne pessoal'
print(frase2[-1])

#Outro exemplo
frase3 = 'eu sou o nibao'
print(frase3[0::2])
'''

#Exemplo 9
'''
frase = 'oi gente tudo bem hahah'
palavras = frase.split()
print('-'.join(palavras[::-1]))
'''

#Exemplo 10
#find(), rfind() e index()
#Localizam substrings:
'''
texto = "banana"
texto.find("na") # 2
texto.rfind("na") # 4
texto.index("ba") # 0
'''

#Exemplo 11
'''
#translate() com str.maketrans()
#Permite substituições múltiplas de caracteres:
tabela = str.maketrans("aeiou", "12345")
print("substituir vogais".translate(tabela))
# 's5bst3t43r v4g13s'
'''

