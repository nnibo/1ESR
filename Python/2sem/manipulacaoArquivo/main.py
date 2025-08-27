# EXEMPLO 1
# # Abrir um arquivo no modo de escrita ('w' para escrita, 'a' para adição)
# with open('exemplo.txt', 'w') as arquivo:
#     # Escrever algumas linhas no arquivo
#     arquivo.write('Olá, este é um exemplo de escrita em arquivo.\n')
#     arquivo.write('Python é poderoso e versátil!\n')
#     arquivo.write('Fechando o arquivo automaticamente com o bloco "with".\n')
#
# # O arquivo é automaticamente fechado quando saímos do bloco "with"

# --------------------------------------------------------------------------------

# EXEMPLO 2 - Cria um diretorio e arquivo dentro do diretorio criado
# import os
# directory_name = "my_new_directory"
# os.mkdir(directory_name)
#
# with open(f'{directory_name}/exemplo.py', 'w') as arquivo:
#     print("Arquivo criado")

# --------------------------------------------------------------------------------

# EXEMPLO 3 - Le as linhas do arquivo
# with open('exemplo.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

# --------------------------------------------------------------------------------

# EXEMPLO 4 - Verificar existencia arquivos
# import os
#
# caminho_arquivo = "exemplo.txt"
#
# if os.path.exists(caminho_arquivo):
#     os.remove(caminho_arquivo)
#     print(f'O arquivo {caminho_arquivo} foi excluido')
# else:
#     print(f'O arquivo {caminho_arquivo} não existe')

# --------------------------------------------------------------------------------

# EXEMPLO 5

# LOGS
import logging
# Configurando o logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Exemplo de diferentes níveis de log
# logging.debug('Isso é uma mensagem de depuração')
# logging.info('Isso é uma mensagem informativa')
# logging.warning('Isso é um alerta')
# logging.error('Ocorreu um erro!')
# logging.critical('Erro crítico! O sistema pode parar de funcionar.')

# Exemplo de como usaria em um programa real
logging.info("Iniciando programa")
try:
    print(10/0)
    logging.info("Operacao realizada")
except Exception as e:
    logging.error(f"Ocorreu um erro inesperado: {e}")