# Lista inicial
lista = [1, 2, 3, 4, 5]

# 1. Actualizar un elemento específico usando su índice
print("Actualizar el elemento en la posición 2:")
lista[2] = 10  # Cambia el valor en la posición 2 (tercer elemento) a 10
print(lista)  # Resultado: [1, 2, 10, 4, 5]

# 2. Actualizar múltiples elementos usando slicing (rebanado)
print("\nActualizar múltiples elementos del índice 1 al 3:")
lista[1:4] = [20, 30, 40]  # Cambia los valores en las posiciones 1, 2, 3
print(lista)  # Resultado: [1, 20, 30, 40, 5]

# 3. Usar un bucle for para actualizar todos los elementos
print("\nMultiplicar todos los elementos por 2 usando un bucle for:")
for i in range(len(lista)):
    lista[i] *= 2  # Multiplica cada elemento por 2
print(lista)  # Resultado: [2, 40, 60, 80, 10]

# 4. Usar comprensión de listas para actualizar todos los elementos
print("\nDividir todos los elementos por 2 usando comprensión de listas:")
lista = [x / 2 for x in lista]  # Divide cada elemento por 2
print(lista)  # Resultado: [1.0, 20.0, 30.0, 40.0, 5.0]

# 5. Reemplazar todos los elementos que cumplen una condición
print("\nReemplazar todos los elementos mayores a 10 con 100:")
lista = [100 if x > 10 else x for x in lista]  # Reemplaza elementos mayores a 10 con 100
print(lista)  # Resultado: [1.0, 100, 100, 100, 5.0]

# 6. Usar map() para aplicar una función a todos los elementos
print("\nAgregar 5 a todos los elementos usando map():")
lista = list(map(lambda x: x + 5, lista))  # Agrega 5 a cada elemento
print(lista)  # Resultado: [6.0, 105, 105, 105, 10.0]

# 7. Actualizar un elemento basado en su valor (si lo encuentras)
print("\nActualizar el primer elemento con valor 105 a 50:")
if 105 in lista:
    lista[lista.index(105)] = 50  # Encuentra el primer 105 y lo cambia a 50
print(lista)  # Resultado: [6.0, 50, 105, 105, 10.0]

# 8. Usar un bucle while para actualizar elementos hasta que se cumpla una condición
print("\nMultiplicar por 2 los elementos hasta que un elemento sea mayor que 100:")
i = 0
while i < len(lista) and lista[i] <= 100:
    lista[i] *= 2
    i += 1
print(lista)  # Resultado: [12.0, 100, 105, 105, 10.0]
