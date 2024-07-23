def primeiro(numero):
    print('INSIDE: PRIMEIRO')
    if numero % 2 == 0:
        return numero
    else:
        raise

def segundo(numero):
    print('INSIDE: SEGUNDO')
    if numero % 3 == 0:
        return numero
    else:
        raise

colateral = []
execucoes = 0
falhas = 0
sucessos = 0
execucoes_primeiro = 0
execucoes_segundo = 0

for i in range(10):
    execucoes += 1
    try:
        a = primeiro(i)
        execucoes_primeiro += 1
        b = segundo(i)
        execucoes_segundo += 1
        # if i == a or i == b:
            # colateral.append(a)
            # sucessos += 1
        print(f'funcionou: {i}')
        sucessos += 1

    except Exception as e:
        falhas += 1
        print('falhou')

print(f"Colateral: {colateral}")
print(f"Execuções: {execucoes}")
print(f"Execuções Primeiro: {execucoes_primeiro}")
print(f"Execuções Segundo: {execucoes_segundo}")
print(f"Falhas: {falhas}")
print(f"Sucessos: {sucessos}")