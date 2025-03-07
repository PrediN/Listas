# 25. Criar uma lista com 5 elementos e verificar se um número específico está presente.

# Declaração de variaveis

lista = [1, 2, 3, 4, 5]
num = int(input("Digite um numero: "))

# Apresentação de resultados

if num in lista:
    print(f"O numero {num} está presente na lista")
else:
    print(f"O numero {num} não está presente na lista")