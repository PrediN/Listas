# 24. Verificar se duas listas são idênticas (mesmo tamanho e valores na mesma ordem).

# Declaração de variaveis

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]

# Apresentação de resultados

if len(lista1) != len(lista2):
    print("As listas não são idênticas")
else:
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            print(f"O item {i} é igual nas duas listas")
        else:
            print(f"O item {i} não é igual nas duas listas")