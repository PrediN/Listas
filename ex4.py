# 4. Verificar se um número específico está presente na lista.

# Declaração de variaveis

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input("Digite um número: "))

# Apresentação de resultados

if numero in lista:
    print(f"O número {numero} está presente na lista.")

else:
    print(f"O número {numero} não está presente na lista.")