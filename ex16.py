# 16. Criar uma lista de nomes e exibir apenas os nomes que começam com a letra "A".

# Declaração de variáveis

lista = ['Ana', 'Bia', 'Carla', 'Alice', 'Amanda', 'Beatriz', 'Clara']

# Apresentação de resultados

for i in lista:
    if i.startswith('A'):
        print(i, end=' ')