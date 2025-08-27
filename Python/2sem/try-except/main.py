numero = 10
lista = []


try:
    print(lista[2])
except ZeroDivisionError as e:
    print("Nao posso dividir por zero", e)

except Exception as e:
    print("Deu erro: ", e)
finally:
    print("Encerrando")