# Lista inicial
lista = [1, 2, 3, 4, 5, 'a', 'b', 'c']

# 1. len() - Obtener la longitud de la lista (número de elementos)
longitud = len(lista)
print("Longitud de la lista:", longitud)  # Resultado: 8

# 2. max() - Obtener el valor máximo (solo funciona con elementos comparables, como todos números)
numeros = [10, 20, 30, 40, 50]
valor_maximo = max(numeros)
print("Valor máximo en la lista de números:", valor_maximo)  # Resultado: 50

# 3. min() - Obtener el valor mínimo (solo funciona con elementos comparables)
valor_minimo = min(numeros)
print("Valor mínimo en la lista de números:", valor_minimo)  # Resultado: 10

# 4. sum() - Obtener la suma de los elementos (solo funciona con números)
suma_total = sum(numeros)
print("Suma de todos los números en la lista:", suma_total)  # Resultado: 150

# 5. in - Comprobar si un elemento existe en la lista
existe = 'a' in lista
print("¿'a' está en la lista?:", existe)  # Resultado: True

# 6. index() - Obtener el índice de la primera aparición de un elemento
indice_a = lista.index('a')
print("Índice de 'a' en la lista:", indice_a)  # Resultado: 5

# 7. count() - Contar cuántas veces aparece un elemento en la lista
conteo_a = lista.count('a')
print("Cantidad de veces que 'a' aparece en la lista:", conteo_a)  # Resultado: 1

# 8. reverse() - Invertir el orden de los elementos en la lista
lista.reverse()
print("Lista después de reverse():", lista)  # Resultado: ['c', 'b', 'a', 5, 4, 3, 2, 1]

# 9. sort() - Ordenar la lista (solo funciona si los elementos son comparables)
numeros.sort()  # Ordena de menor a mayor
print("Lista de números después de sort():", numeros)  # Resultado: [10, 20, 30, 40, 50]

# 10. sorted() - Devolver una nueva lista ordenada sin modificar la original
lista_original = [3, 1, 4, 2]
lista_ordenada = sorted(lista_original)
print("Lista original:", lista_original)  # Resultado: [3, 1, 4, 2]
print("Lista ordenada:", lista_ordenada)  # Resultado: [1, 2, 3, 4]

# 11. copy() - Crear una copia superficial de la lista
copia_lista = lista.copy()
print("Copia de la lista:", copia_lista)  # Resultado: ['c', 'b', 'a', 5, 4, 3, 2, 1]

# 12. clear() - Eliminar todos los elementos de la lista
lista.clear()
print("Lista después de clear():", lista)  # Resultado: []

# 13. append() - Agregar un elemento al final de la lista
lista.append(100)
print("Lista después de append(100):", lista)  # Resultado: [100]

# 14. extend() - Agregar múltiples elementos al final de la lista
lista.extend([200, 300, 400])
print("Lista después de extend([200, 300, 400]):", lista)  # Resultado: [100, 200, 300, 400]

# 15. insert() - Insertar un elemento en una posición específica
lista.insert(1, 'insertado')
print("Lista después de insert(1, 'insertado'):", lista)  # Resultado: [100, 'insertado', 200, 300, 400]

# 16. pop() - Eliminar y devolver el elemento en la posición dada (por defecto el último)
elemento_pop = lista.pop()
print("Elemento eliminado con pop():", elemento_pop)  # Resultado: 400
print("Lista después de pop():", lista)  # Resultado: [100, 'insertado', 200, 300]

# 17. remove() - Eliminar la primera aparición de un valor específico
lista.remove('insertado')
print("Lista después de remove('insertado'):", lista)  # Resultado: [100, 200, 300]
