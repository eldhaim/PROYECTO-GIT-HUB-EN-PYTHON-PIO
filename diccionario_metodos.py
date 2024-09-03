# Diccionario inicial
diccionario = {
    'nombre': 'Andres',
    'edad': 28,
    'ciudad': 'Cali',
    'profesión': 'Vendedor'
}

# 1. len() - Obtener el número de elementos (pares clave-valor) en el diccionario
longitud = len(diccionario)
print("Número de elementos en el diccionario:", longitud)  # Resultado: 4

# 2. get() - Obtener el valor de una clave específica
edad = diccionario.get('edad')
print("Valor de la clave 'edad':", edad)  # Resultado: 28

# 3. keys() - Obtener todas las claves del diccionario
claves = diccionario.keys()
print("Claves del diccionario:", claves)  # Resultado: dict_keys(['nombre', 'edad', 'ciudad', 'profesión'])

# 4. values() - Obtener todos los valores del diccionario
valores = diccionario.values()
print("Valores del diccionario:", valores)  # Resultado: dict_values(['Andres', 28, 'Cali', 'Vendedor'])

# 5. items() - Obtener todos los pares clave-valor como tuplas
pares = diccionario.items()
print("Pares clave-valor en el diccionario:", pares)  # Resultado: dict_items([('nombre', 'Andres'), ('edad', 28), ('ciudad', 'Cali'), ('profesión', 'Vendedor')])

# 6. update() - Actualizar el diccionario con otro diccionario o con pares clave-valor
diccionario.update({'edad': 29, 'pais': 'Colombia'})
print("Diccionario después de update():", diccionario)  # Resultado: {'nombre': 'Andres', 'edad': 29, 'ciudad': 'Cali', 'profesión': 'Vendedor', 'pais': 'Colombia'}

# 7. pop() - Eliminar un par clave-valor y devolver su valor
profesion = diccionario.pop('profesión')
print("Valor eliminado con pop():", profesion)  # Resultado: 'Vendedor'
print("Diccionario después de pop():", diccionario)  # Resultado: {'nombre': 'Andres', 'edad': 29, 'ciudad': 'Cali', 'pais': 'Colombia'}

# 8. popitem() - Eliminar y devolver el último par clave-valor añadido
ultimo_par = diccionario.popitem()
print("Último par eliminado con popitem():", ultimo_par)  # Resultado: ('pais', 'Colombia')
print("Diccionario después de popitem():", diccionario)  # Resultado: {'nombre': 'Andres', 'edad': 29, 'ciudad': 'Cali'}

# 9. clear() - Eliminar todos los elementos del diccionario
diccionario.clear()
print("Diccionario después de clear():", diccionario)  # Resultado: {}

# 10. copy() - Crear una copia superficial del diccionario
diccionario_original = {'a': 1, 'b': 2, 'c': 3}
copia_diccionario = diccionario_original.copy()
print("Copia del diccionario:", copia_diccionario)  # Resultado: {'a': 1, 'b': 2, 'c': 3}

# 11. fromkeys() - Crear un nuevo diccionario con claves de un iterable y un valor predeterminado
nuevas_claves = ['x', 'y', 'z']
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print("Nuevo diccionario creado con fromkeys():", nuevo_diccionario)  # Resultado: {'x': 0, 'y': 0, 'z': 0}

# 12. setdefault() - Obtener el valor de una clave; si no existe, añadir la clave con un valor por defecto
valor_default = diccionario_original.setdefault('d', 4)
print("Valor obtenido con setdefault():", valor_default)  # Resultado: 4
print("Diccionario después de setdefault():", diccionario_original)  # Resultado: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
