#Exercicio 1
'''
texto = 'Python'
invertida = texto[::-1]
print(invertida)
'''

#Exercicio 2
'''
nome = 'Maria'
idade = 30
frase = f'{nome} tem {idade} anos'
print(frase)
'''

#Exercicio 3
'''
nome_completo = 'João da Silva'
lista = nome_completo.split() 
silva = lista[2]
print(silva)'
'''

#Exercicio 4
'''
frase = 'Aprender Python é divertido'
separar_palavras = frase.split()
separar_hifens = ('-').join(separar_palavras)
print(separar_hifens)
'''

#Exercicio 5
'''
mensagem = 'bom dia'
maiusculo = mensagem.upper()
print(maiusculo)
'''

#Exercicio 6
'''
palavra = 'computador'
iniciais = palavra[0:3]
print(iniciais)
'''

#Exercicio 7
'''
email = 'aluno@exemplo.com'
usuario, sep, dominio = email.partition('@')
print(dominio)
'''

#Exercicio 8
'''
titulo = 'Capitulo 1'
hifens = '##############################'
print(hifens,titulo,hifens)
'''

#Exercicio 9
'''
mensagem = 'banana'
print(mensagem.count('a'))
'''

#Exercicio 10
'''
texto = '   Ola Mundo   '
print(texto.rstrip().lstrip())
'''

#Exercicio 11
'''
nome_completo = 'Carlos Eduardo'
nome, sobrenome = nome_completo.split()
nome_invertido = f'{sobrenome} {nome}'
print(nome_invertido)
'''

#Exercicio 12
'''
frase = "Python é uma linguagem poderosa"
vogais = 'aeiouéíAEIOUÉÍ'
# subsituir_vogais = str.maketrans('','',vogais  )
# print(frase.translate(subsituir_vogais))
frase.replace(vogais,'')'
'''

#Exericio 13
'''
nome_completo = 'Ana Clara Souza'
nomes_separados = nome_completo.split()
todosNomes = nomes_separados[0][0], nomes_separados[1][0], nomes_separados[2][0]

print(('.').join(todosNomes))
'''

#Exercicio 14
'''
palavra = 'eco ' * 3
lista = palavra.split()
print('...'.join(lista))
'''

#Exercicio 15
'''
frase = 'Desenvolvimento de software'
maiusculas = frase.title()
sem_espaco = maiusculas.split()
frase_certa = ''.join(sem_espaco)
print(len(frase_certa)) # 25

print(frase_certa.rjust(26, '#'))
'''

#Exericio 16
'''
palavra = 'python'
print('*'.join(palavra))
'''

#Exercicio 17
'''
arquivo = "relatorio_final_2024.pdf"
nome_arquivo, separador, dominio = arquivo.partition('.')
print(dominio)
'''

#Exercicio 18
'''
mensagem = "Python   é    top"
sem_espaco = mensagem.split()
print(sem_espaco)
mensagem_corrigida = ' '.join(sem_espaco)
print(mensagem_corrigida)
'''

#Exercicio 19
'''
cpf = "12345678900"
cpf_formatado = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
print(cpf_formatado)
'''

#Exercicio 20
'''
senha = 'segredo'
tabela = str.maketrans('aeiou', '@310$')
print(senha.translate(tabela))
'''



