# 19. Criar uma lista e remover um elemento específico.

# Declaração de variaveis

lista = ["Rodo", "Vassoura", "Pá", "Balde", "Esponja"]
item = ""

# Apresentação de resultados

print(lista)

print()
item = str(input("Qual desses itens você já tem? "))
lista.remove(item)

print()
print(lista)