# 14. Concatenar duas listas e imprimir o resultado.

# Declaração de variáveis

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Apresentação de resultados

print('Lista 1:', lista1)
print('Lista 2:', lista2)

for i in lista2:
    lista1.append(i)

print('Lista concatenada:', lista1)