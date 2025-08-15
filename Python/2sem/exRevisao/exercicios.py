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

# Ex 3
tarefas = [{
    'titulo': str,
    'prioridade': str,
    'concluida': bool
}]


# Ex 6
opcao = 1
contatos = []
while opcao != 0:
    opcao = int(input("""
    Digite uma opção:
    1 - Listar Contatos
    2 - Adicionar um Contato
    3 - Editar um contato
    4 - Apagar um contato
    0 - Sair
    """))

    match opcao:
        case 1:
            for contato in contatos:
                print("Nome:",contato['Nome'])
                print("Telefone:",contato['Telefone'])
        case 2:
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            contatos.append({"Nome": nome, "Telefone": telefone})

        case 3:
            nome = input("Digite o nome: ")
            for contato in contatos:
                if contato["Nome"] == nome:
                    telefone = input("Digite o telefone: ")
                    contato["Telefone"] = telefone
        case 4:
            nome = input("Digite o nome: ")
            for contato in contatos:
                if contato["Nome"] == nome:
                    contatos.remove(contato)
        case 0:
            print("Finalizando o programa...")
            break