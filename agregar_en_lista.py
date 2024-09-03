# Lista inicial
lista = [1, 2, 3]

# 1. Usar append() para agregar un solo elemento al final de la lista
lista.append(4)  # Agrega el número 4 al final
print("Después de append(4):", lista)  # Resultado: [1, 2, 3, 4]

# 2. Usar insert() para agregar un elemento en una posición específica
lista.insert(1, 'a')  # Inserta 'a' en la posición 1
print("Después de insert(1, 'a'):", lista)  # Resultado: [1, 'a', 2, 3, 4]

# 3. Usar extend() para agregar múltiples elementos al final de la lista
lista.extend([5, 6, 7])  # Agrega 5, 6, y 7 al final
print("Después de extend([5, 6, 7]):", lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7]

# 4. Usar el operador + para concatenar listas (esto crea una nueva lista)
nueva_lista = lista + [8, 9]  # Crea una nueva lista agregando 8 y 9
print("Después de concatenar con + [8, 9]:", nueva_lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7, 8, 9]

# 5. Usar el operador += para extender la lista actual
lista += [10, 11]  # Agrega 10 y 11 al final de la lista existente
print("Después de usar += [10, 11]:", lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7, 10, 11]

# 6. Usar un bucle para agregar elementos individualmente (cuando necesitas agregar elementos bajo una condición)
for i in range(12, 15):
    lista.append(i)  # Agrega los números 12, 13, y 14
print("Después de bucle con append:", lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14]

# 7. Usar el método extend() con un iterable (como una cadena o un rango)
lista.extend(range(15, 18))  # Agrega 15, 16, y 17 usando un rango
print("Después de extend(range(15, 18)):", lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17]

# 8. Usar insert() para agregar elementos en una posición basada en una condición o cálculo
lista.insert(len(lista), 'final')  # Inserta 'final' al final de la lista
print("Después de insert(len(lista), 'final'):", lista)  # Resultado: [1, 'a', 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 'final']
