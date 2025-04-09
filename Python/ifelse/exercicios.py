#Exercicio 1
'''
numero = int(input('Digite um numero, positivo, negativo ou zero: '))

if numero >= 1:
    print('Numero positivo')
elif numero == 0:
    print('Numero é zero')
else:
    print('numero é negativo')
'''

#Exercicio 2
'''
nota1 = int(input('Digite a primeira nota'))
nota2 = int(input('Digite a primeira nota'))
nota3 = int(input('Digite a primeira nota'))

media = (nota1 + nota2+ nota3)/3

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
'''

#Exercicio 3
'''
idade = int(input('Digite sua idade'))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
'''

#Exercicio 4
'''
tupla = (1, 3, 5)
maior = tupla[0]

if tupla[1] > maior:
    maior = tupla[1]

    if tupla[2] > maior:
        maior = tupla[2]

print(maior)
'''

#Exercicio 5
'''
numero = int(input('Digite um numero'))
if numero > 10 and numero < 50:
    print('Está no intervalo')
elif numero == 10:
    print('Numero é 10')
elif numero == 50:
    print('Numero é 50')
else:
    print('Numero nao esta no intervalo')
'''

#Exercicio 6
'''
lista = ['ASDASDASD', 'ADS', 'A']

num_caracteres_1 = len(lista[0])
num_caracteres_2 = len(lista[1])
num_caracteres_3 = len(lista[2])

if num_caracteres_1 > num_caracteres_2 and num_caracteres_1 > num_caracteres_3:
    print('Primeira string da lista tem o maior numero de caracteres')
elif num_caracteres_2 > num_caracteres_3 and num_caracteres_2 > num_caracteres_1:
    print('Segunda string tem o maior numero de caracteres')
else:
    print('Terceira string tem maior numero de caracteres')
'''

#Exercicio 7
'''
dia_semana = int(input('Digite um numero'))

match dia_semana:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7: 
        print('Sabado')
'''

#Exercicio 8
'''
tupla = (2, 4, 6)

if tupla[0] == tupla[1] == tupla[2]:
    print('Todos iguais')
elif tupla[0] != tupla[1] and tupla[0] != tupla[2] and tupla[1] != tupla[2]:
    print('Todos diferentes')
elif tupla[0] == tupla[1] or tupla[0] == tupla[2] or tupla[1] == tupla[2]:
    print('Dois valores iguais')
'''

#Exercicio 9
'''
lista_numeros = [2,2]

if lista_numeros[0]%lista_numeros[1] == 0:
    print('Numero é divisivel')
else:
    print('Numero não é divisivel')
'''

#Exercicio 10
'''
nome_mes = input('Digite um mes')

match nome_mes.lower():
    case 'janeiro':
        print('31 dias')
    case 'fevereiro':
        print('28 dias')
    case 'marco':
        print('31 dias')
    case 'abril':
        print('30 dias')
'''

#Exercicio 11
'''
lados_triangulo = [10, 20, 10]
if lados_triangulo[0] > lados_triangulo[1] + lados_triangulo[2] or lados_triangulo[1] > lados_triangulo[0] + lados_triangulo[2] or lados_triangulo[2] > lados_triangulo[0] + lados_triangulo[1]:
    print('Nao é triangulo')
else:
    print('é triangulo')
'''

#Exercicio 12
'''
numero = int(input('Digite um numero'))

if numero % 2 == 0:
    print('Numero par')
else:
    print('numero impar')
'''

#Exercicio 13
'''
nome_fruta = input("Digite o nome de uma fruta")
lista_frutas = ['maça', 'banana', 'abacaxi']

if nome_fruta.lower() == lista_frutas[0] or nome_fruta.lower() == lista_frutas[1] or nome_fruta.lower() == lista_frutas[2]:
    print('Fruta escolhida tem na lista')
else:
    print('Fruta escolhida não tem na lista')
'''

#Exercicio 14
'''
lista_numeros = [2, 4]
if lista_numeros[0] > lista_numeros[1]:
    print('primeiro numero na lista é maior que o segundo')
elif lista_numeros[0] == lista_numeros[1]:
    print('Numeros sao iguais')
else:
    print('Segundo numero na lista é maior que o primeiro')
'''

#Exercicio 15
'''
estado_civil = input('Digite seu estado civil')

match estado_civil.lower():
    case 'solteiro:
        print(1)
    case 'casado':
        print(2)
    case 'divorciado':
        print(3)
    case 'outro':
        print(0)
'''

#Exercicio 16
'''
tupla = (1, 3, 5, 7, 9)
numero = int(input("Digite um numero"))

if numero == tupla[0] or numero == tupla[1] or numero == tupla[2] or numero == tupla[3] or numero == tupla[4]:
    print('numero escolhido tem na tupla')
else:
    print('numero escolhido não tem na tupla')
'''
#Exercicio 17
'''
numero_mes = int(input("Digite um numero de um mes"))
if numero_mes == 12 or numero_mes == 1 or numero_mes == 2:
    print('Verão')
elif numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
    print('Outono')
elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
    print('Inverno')
else:
    print('Primavera')
'''

#Exercicio 18
'''
lista = ['pre', 'prefixo']
if lista[0].startswith('pre'):
    print('é prefixo')
else:
    print('nao é prefixo')
'''

#Exercicio 19
'''
tupla = ('nicolas', 19)
if tupla[1] >= 18:
    print('pode dirigir')
else:
    print('nao pdoe dirigir')
'''

#Exercicio 20
'''
lista_cores = ['vermelho', 'branco', 'amarelo']

if lista_cores[0] == 'vermelho' and lista_cores[1] == 'azul' and lista_cores[2] == 'amarelo':
    print('Todas as cores são primarias')
else :
    print('Não sao primarias')
'''


