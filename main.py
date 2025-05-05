# 1. Criar uma lista vazia
lista_compras = []

# 2. Adicionar itens à lista
lista_compras.append("leite")
lista_compras.append("pão")
lista_compras.append("ovos")
lista_compras.append("arroz")

# 3. Adicionar um item na segunda posição
lista_compras.insert(1, "manteiga")  # adicionando manteiga na posição 1 (segunda posição)

# 4. Exibir a lista completa e o terceiro item
print("Lista de compras completa:", lista_compras)
print("Terceiro item da lista:", lista_compras[2])

# 5. Remover um item (por exemplo, "pão")
lista_compras.remove("pão")

# 6. Remover o último item da lista
lista_compras.pop()

# 7. Substituir o primeiro item por "abacate"
lista_compras[0] = "abacate"

# 8. Mostrar a lista atualizada
print("\nLista atualizada:", lista_compras)

# 9. Exibir cada item individualmente
print("\nItens individualmente:")
for item in lista_compras:
    print("-", item)

# 10. Organizar a lista em ordem alfabética
lista_compras.sort()
print("\nLista em ordem alfabética:", lista_compras)
