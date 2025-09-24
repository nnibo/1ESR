import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Exemplo 1

# Pegando as 5 primeiras linhas do xlsx
# df = pd.read_excel('vendas_exemplo.xlsx', sheet_name='Vendas')
#
# print(df.head())
# # Pegando o nome das planilhas
# sheets = pd.read_excel('vendas_exemplo.xlsx', sheet_name=None)
# for sheet in sheets:
#     print(sheet)

# ----------------------------------------------------------------------


# Exemplo 2 - Escolhendo qual planilha pegar os dados
# sheets = pd.read_excel('vendas_exemplo.xlsx', sheet_name=None) # O none pega todas as planilhas
# nomes = [i for i in sheets]
# print('Planilhas do arquivo')
#
# for index, sheet in enumerate(nomes):
#     print(f'{index + 1} - {sheet}')
#
# opcao = int(input("Selecione uma planilha"))
#
# planilha = None
# match opcao:
#     case 1:
#         planilha = pd.read_excel('vendas_exemplo.xlsx', sheet_name=nomes[0])
#     case 2:
#         planilha = pd.read_excel('vendas_exemplo.xlsx', sheet_name=nomes[1])
# print(planilha.head())

# ----------------------------------------------------------------------

dados = {
'Produto': ['Notebook', 'Teclado', 'Mouse', 'Monitor', 'Impressora'],
'Quantidade': [12, 100, 75, 20, 15],
'Preço Unitário (R$)': [3700, 150, 70, 800, 450],
'Data da Venda': ['2024-01-10', '2024-02-05', '2024-02-20', '2024-03-15', '2024-04-10'],
'Vendedor': ['Carlos', 'Fernanda', 'Mariana', 'João', 'Ana']
}
# Criando o DataFrame
df_vendas = pd.DataFrame(dados)
# Salvando o DataFrame em um arquivo Excel com múltiplas planilhas
file_path = 'vendas_exemplo.xlsx'
# Escrevendo no arquivo Excel
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    df_vendas.to_excel(writer, sheet_name='Sheet1', index=False)
print(f"Arquivo salvo em: {file_path}")