# 23. Criar uma lista de 5 números e calcular a média dos elementos.

# Declaração de variaveis

lista = [1, 2, 3, 4, 5]
soma = 0

# Apresentação de resultados

for i in lista:
    soma += i

print(f"A média da lista é: {soma/len(lista)}")