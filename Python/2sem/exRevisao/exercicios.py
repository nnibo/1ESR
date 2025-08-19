# Ex 1

# filmes = [{
#     'nome': 'Filme1',
#     'ano': 1,
#     'genero': "A"
# }, {
#     'nome': 'Filme2',
#     'ano': 1,
#     'genero': "A"
# }, {
#     'nome': 'Filme3',
#     'ano': 1,
#     'genero': "C"
# }]
#
# def filtrarFilmes(listaFilmes):
#     filmes_filtrados = []
#
#     print("1- Genero\n"
#           "2- Ano")
#     opcao = input("Digite se quer filtrar por ano ou genero: ")
#
#     match opcao:
#         case '1':
#             escolhaGenero = input("Digite qual o genero que voce quer filtrar: ")
#             for filme in filmes:
#                 if (filme['genero'] == escolhaGenero):
#                     filmes_filtrados.append(filme)
#
#             print(filmes_filtrados)
#
#         case '2':
#             escolhaAno = int(input("Digite o ano que voce quer filtrar: "))
#             for filme in filmes:
#                 if(filme['ano'] == escolhaAno):
#                     filmes_filtrados.append(filme)
#
#             print(filmes_filtrados)
#
# filtrarFilmes(filmes)

# ---------------------------------------------------------------------------------

# Ex 2

# candidatos = [
#     {'nome': 'usuario1', 'votos': 0},
#     {'nome': 'usuario2', 'votos': 0},
#     {'nome': 'usuario3', 'votos': 0}
# ]
#
# while(True):
#     opcao = input("Digite ( votar ) ou ( sair ) ")
#     match opcao:
#         case 'votar':
#             escolhaCandidato = input("Digite em qual candidato voce quer votar: ")
#             for candidato in candidatos:
#                 if candidato['nome'] == escolhaCandidato:
#                     voto = int(input("Digite o seu voto: "))
#                     candidato['votos'] += voto
#                     print(candidato['nome'], candidato['votos'])
#
#         case 'sair':
#             print("Programa finalizando...")
#             break

# ---------------------------------------------------------------------------------

# EX 5
# opcao = 1
# alunos = []
# while opcao != 0:
#     opcao = int(input("Digite 1 para adicionar aluno, 2 para calcular media de algum aluno, 0 para sair: "))

#     match opcao:
#         case 1:
#             nome = input("Digite o nome do aluno: ")
#             nota1 = int(input("Digite a primeira nota: "))
#             nota2 = int(input("Digite a segunda nota: "))
#             nota3 = int(input("Digite a terceira nota: "))
#             listaNotas = [nota1, nota2, nota3]
#             alunos.append({"Nome": nome, "Notas": listaNotas})
#             print("Aluno", nome, "Adicionado")
#         case 2:
#             nome = input("Digite o nome do aluno no qual quer verificar a media: ")
#             for aluno in alunos:
#                 if aluno["Nome"] == nome:
#                     soma_notas = 0
#                     for nota in listaNotas:
#                         soma_notas += nota
#                         media = soma_notas / len(listaNotas)
#                     print("A média do aluno", nome, "é", media)
#         case 0:
#             print("Programa encerrando...")
#             break

# ---------------------------------------------------------------------------------

# # EX 6
# opcao = 1
# contatos = []
# while opcao != 0:
#     opcao = int(input("""
#     Digite uma opção:
#     1 - Listar Contatos
#     2 - Adicionar um Contato
#     3 - Editar um contato
#     4 - Apagar um contato
#     0 - Sair
#     """))

#     match opcao:
#         case 1:
#             for contato in contatos:
#                 print("Nome:",contato['Nome'])
#                 print("Telefone:",contato['Telefone'])
#         case 2:
#             nome = input("Digite o nome: ")
#             telefone = input("Digite o telefone: ")
#             contatos.append({"Nome": nome, "Telefone": telefone})

#         case 3:
#             nome = input("Digite o nome: ")
#             for contato in contatos:
#                 if contato["Nome"] == nome:
#                     telefone = input("Digite o telefone: ")
#                     contato["Telefone"] = telefone
#         case 4:
#             nome = input("Digite o nome: ")
#             for contato in contatos:
#                 if contato["Nome"] == nome:
#                     contatos.remove(contato)
#         case 0:
#             print("Finalizando o programa...")
#             break

# ---------------------------------------------------------------------------------

# EX 7
vendas = []
opcao = 1
while opcao != 0:
    opcao = int(input("Digite 1 para adicionar uma venda, 2 para ver as vendas de um produto especifico, 3 para ver as vendas gerais e 0 para sair: "))

    match opcao:
        case 1:
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite quantos foram vendidos: "))
            preco = float(input("Digite quanto custou: "))
            vendas.append({"Produto": produto, "Quantidade": quantidade, "Preco": preco})
            print("O produto ", produto, "foi adicionado as vendas")
        case 2:
            nome_produto = input("Digite o nome do produto que quer verificar")
            venda_geral = 0
            for produto in vendas:
                if produto["Produto"] == nome_produto:
                    venda_total_produto = produto["Quantidade"] * produto["Preco"]
                    venda_geral += produto["Preco"]
                    print("O produto", nome_produto, "teve R$" + venda_total_produto)
        case 3:
            print("Foi vendido R$" + venda_geral)
        



# ---------------------------------------------------------------------------------

# EX 15
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