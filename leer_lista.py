# Lista inicial
lista = [1, 2, 3, 4, 5, 'a', 'b', 'c']

# 1. Leer todos los elementos de la lista usando un bucle for
print("Leer todos los elementos con un bucle for:")
for elemento in lista:
    print(elemento)  # Imprime cada elemento de la lista

# 2. Acceder a un elemento específico usando su índice
print("\nAcceder al elemento en la posición 3:")
elemento = lista[3]  # Accede al cuarto elemento (índice 3)
print(elemento)  # Resultado: 4

# 3. Acceder a un rango de elementos usando slicing (rebanado)
print("\nAcceder a un rango de elementos del índice 2 al 5:")
sublista = lista[2:6]  # Accede a los elementos en las posiciones 2, 3, 4 y 5
print(sublista)  # Resultado: [3, 4, 5, 'a']

# 4. Leer elementos en orden inverso usando slicing
print("\nLeer la lista en orden inverso:")
lista_inversa = lista[::-1]  # Invierte la lista
print(lista_inversa)  # Resultado: ['c', 'b', 'a', 5, 4, 3, 2, 1]

# 5. Leer todos los índices y valores de la lista usando enumerate()
print("\nLeer índices y valores usando enumerate():")
for indice, valor in enumerate(lista):
    print(f"Índice {indice}: {valor}")  # Imprime el índice y el valor correspondiente

# 6. Leer elementos que cumplen con una condición
print("\nLeer elementos que son números (int):")
numeros = [x for x in lista if isinstance(x, int)]  # Filtra los elementos que son enteros
print(numeros)  # Resultado: [1, 2, 3, 4, 5]

# 7. Usar un bucle while para leer la lista manualmente
print("\nLeer la lista usando un bucle while:")
i = 0
while i < len(lista):
    print(lista[i])  # Imprime el elemento en la posición i
    i += 1

# 8. Leer el primer y último elemento de la lista
print("\nLeer el primer y último elemento:")
primer_elemento = lista[0]  # Primer elemento
ultimo_elemento = lista[-1]  # Último elemento
print("Primer elemento:", primer_elemento)  # Resultado: 1
print("Último elemento:", ultimo_elemento)  # Resultado: 'c'
