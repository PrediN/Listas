# 9. Criar uma lista e limpar todos os elementos dela.

# Declaração de variáveis

lista = ['casa', 'carro', 'moto']

# Apresentação de resultados

for i in range(len(lista)):
    lista.remove(lista[0])

print('Lista limpa:', lista)