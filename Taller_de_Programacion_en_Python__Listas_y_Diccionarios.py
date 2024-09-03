#Ejercicio 1: Manipulación de Listas
# Creación de la lista inicial
nombres = ["Juan", "Ana", "Luis", "Pedro"]

# 1. Modificar el tercer elemento
nombres[2] = "Carlos"

# 2. Agregar un nuevo nombre al final
nombres.append("Lucía")

# 3. Eliminar el primer nombre de la lista
nombres.pop(0)

# 4. Mostrar todos los elementos en una sola línea sin corchetes ni comas
print(" ".join(nombres))

# 5. Imprimir la cantidad total de nombres en la lista
print(len(nombres))



#Ejercicio 2: Diccionarios Básicos
# Creación del diccionario inicial
edades = {"Juan": 25, "Ana": 30, "Luis": 28}

# 1. Acceder y mostrar la edad de Ana
print(edades["Ana"])

# 2. Cambiar la edad de Luis a 29
edades["Luis"] = 29

# 3. Agregar un nuevo par clave-valor
edades["Pedro"] = 22

# 4. Eliminar el registro de Juan del diccionario
del edades["Juan"]

# 5. Mostrar el diccionario final
print(edades)


#Ejercicio 3: Diccionarios Anidados
# Creación del diccionario inicial
libros = {
    "Don Quijote de la Mancha": {"autor": "Miguel de Cervantes", "año": 1605, "género": "Novela"},
    "Cien Años de Soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo Mágico"}
}

# 1. Acceder y mostrar el autor de Don Quijote de la Mancha
print(libros["Don Quijote de la Mancha"]["autor"])

# 2. Agregar un nuevo libro al diccionario
libros["Fahrenheit 451"] = {"autor": "Ray Bradbury", "año": 1953, "género": "Ciencia Ficción"}

# 3. Modificar el año de publicación de Cien Años de Soledad a 1965
libros["Cien Años de Soledad"]["año"] = 1965

# 4. Mostrar todos los títulos de libros disponibles
for titulo in libros.keys():
    print(titulo)


#Ejercicio 4: Iteración y Enumeración en Listas
# Creación de la lista inicial
colores = ["Rojo", "Verde", "Azul", "Amarillo"]

# 1. Imprimir cada color con su posición usando enumerate
for index, color in enumerate(colores, start=1):
    print(f"{index}. {color}")

# 2. Modificar la lista para que el primer color sea "Naranja"
colores[0] = "Naranja"

# 3. Eliminar el último color de la lista
colores.pop()

# 4. Mostrar la lista final
print(colores)


#Ejercicio 5: Enumerar Productos en un Inventario
# Creación del diccionario inicial
inventario = {
    "Manzanas": [20, 30, 50],
    "Plátanos": [15, 25, 35]
}

# 1. Iterar sobre la lista de cantidades de "Manzanas"
for index, cantidad in enumerate(inventario["Manzanas"], start=1):
    print(f"Almacén {index}: {cantidad} Manzanas")

# 2. Iterar sobre la lista de cantidades de "Plátanos"
for index, cantidad in enumerate(inventario["Plátanos"], start=1):
    print(f"Almacén {index}: {cantidad} Plátanos")
