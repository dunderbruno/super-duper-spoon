from math_operations import divide


# print(globals())

# a = globals()

# for i in a:
#     print(i)

# Obtendo o dicionário de variáveis globais
globais = globals().copy()

# Iterando sobre os itens do dicionário
for chave, valor in globais.items():
    print(f"{chave}: {valor}")


print(globais['divide'](2,2))

# def intermadiaria():
#     divide(4,0)

# try:
#     intermadiaria()
# except Exception as e:
#     print(f"Aconteceu isso aqui: {e}")

