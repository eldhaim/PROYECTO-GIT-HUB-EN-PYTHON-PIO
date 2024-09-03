# Lista inicial
lista = [1, 2, 3, 4, 2, 5]

# 1. Usar remove() para eliminar la primera ocurrencia de un valor específico
lista.remove(2)  # Elimina la primera aparición de 2
print("Después de remove(2):", lista)  # Resultado: [1, 3, 4, 2, 5]

# 2. Usar pop() para eliminar y devolver un elemento en una posición específica
elemento_eliminado = lista.pop(2)  # Elimina el elemento en la posición 2
print("Después de pop(2):", lista)  # Resultado: [1, 3, 2, 5]
print("Elemento eliminado con pop:", elemento_eliminado)  # Resultado: 4

# 3. Usar del para eliminar un elemento en una posición específica
del lista[1]  # Elimina el elemento en la posición 1
print("Después de del lista[1]:", lista)  # Resultado: [1, 2, 5]

# 4. Usar del para eliminar un rango de elementos
lista = [1, 2, 3, 4, 2, 5]  # Restaurar lista original para este ejemplo
del lista[1:4]  # Elimina los elementos de la posición 1 a 3 (no incluye la 4)
print("Después de del lista[1:4]:", lista)  # Resultado: [1, 2, 5]

# 5. Usar comprensión de listas para eliminar todas las ocurrencias de un valor específico
lista = [1, 2, 3, 4, 2, 5]  # Restaurar lista original para este ejemplo
lista = [x for x in lista if x != 2]  # Elimina todas las apariciones de 2
print("Después de comprensión de listas:", lista)  # Resultado: [1, 3, 4, 5]

# 6. Usar clear() para eliminar todos los elementos de la lista
lista.clear()  # Vacía la lista por completo
print("Después de clear():", lista)  # Resultado: []

# 7. Asignar una lista vacía para eliminar todos los elementos
lista = [1, 2, 3, 4, 5]  # Restaurar lista original para este ejemplo
lista = []  # Asignación vacía
print("Después de asignación vacía:", lista)  # Resultado: []

# 8. Usar filter() para eliminar elementos según una condición
lista = [1, 2, 3, 4, 2, 5]  # Restaurar lista original para este ejemplo
lista = list(filter(lambda x: x != 2, lista))  # Filtra y elimina todos los 2
print("Después de filter(lambda x: x != 2):", lista)  # Resultado: [1, 3, 4, 5]
