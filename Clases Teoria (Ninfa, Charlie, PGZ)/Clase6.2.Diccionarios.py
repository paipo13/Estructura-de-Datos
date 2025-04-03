###DICCIONARIOS###
# Los diccionarios en Python son estructuras de datos que almacenan pares de clave-valor.
# Son muy útiles cuando necesitas asociar una clave única a un valor y luego acceder a ese
# valor de manera rápida usando la clave. Estos cumplen las caracteristicas de ser de forma Mutable, Indexada y Anidada:
# Mutable: Ya que puede cambiar durante el tiempo de ejecucion
# Indesada: Ya que puede ingresar un elemento especifico del diccionario solo con el uso de la clave correspondiente.
# Anidada: Ya que puede el mismo diccionario puede contener otros diccionarios adentro del mismo. 
# Como si fuera una lista de listas pero de diccionarios.

# Obs. Los diccionarios son ordenados, ya que se mantiene el orden en el que se ingresan los datos.

# Obs. Cada elemento del diccionario es una pareja. Y cada pareja tiene una clave (key) y un valor (value).

# Obs. Las claves (keys) deben ser objetos inmutables y unicos. Como por ejemplo: objetos de tipo int, float, str y tuplas.

# Nota: Cuando crear un elemento en el diccionario pongo la clave (que no exista) y el valor del mismo. 
# Cuando yo queiro modificar el valor de un elemento lo que hago es pongo la clave de este y 
# el nuevo valor (el nuevo valor se a sobreescribir al valor antiguo)

# Notacion:  
# diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ...}
# Obs. Observar en el ejmeplo anterior como primero va la clave luego un ':' y luego el valor.
# Luego una vez que pusimos la ',' ya pasamos a otro elemento.
# Obs. La notacion tambien podria haber sido:
# diccionario = dict(clave1: valor1, clave2: valor2, clave3: valor3, ...)









###METODOS/FUNCIONES###
# 1. dietodos/Funciones para el uso de diccionarios.ct.get(key[, default])
# Descripción: Devuelve el valor de la clave especificada. Si la clave no existe, devuelve None o el valor predeterminado proporcionado.
# Aplicación: Es útil cuando no estás seguro si una clave existe en el diccionario y no quieres que se lance una excepción.
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
valor = mi_diccionario.get('b')  # Devuelve 2
valor_inexistente = mi_diccionario.get('d', 'No encontrado')  # Devuelve 'No encontrado'

# 2. dict.keys()
# Descripción: Devuelve una vista de las claves en el diccionario.
# Aplicación: Es útil cuando necesitas iterar sobre todas las claves del diccionario o verificar si una clave específica existe.
claves = mi_diccionario.keys()
for clave in claves:
    print(clave)
# Salida esperada: 'a', 'b', 'c'

# 3. dict.values()
# Descripción: Devuelve una vista de los valores en el diccionario.
# Aplicación: Útil para iterar sobre todos los valores del diccionario.
valores = mi_diccionario.values()
for valor in valores:
    print(valor)
# Salida esperada: 1, 2, 3

# 4. dict.items()
# Descripción: Devuelve una vista de los pares clave-valor en el diccionario como tuplas.
# Aplicación: Útil para iterar sobre ambos, claves y valores, simultáneamente.
elementos = mi_diccionario.items()
for clave, valor in elementos:
    print(f'{clave}: {valor}')
# Salida esperada: 'a: 1', 'b: 2', 'c: 3'

# 5. dict.update([other])
# Descripción: Actualiza el diccionario con los pares clave-valor de otro diccionario, sobrescribiendo los valores existentes.
# Aplicación: Útil para fusionar dos diccionarios o actualizar un diccionario con nuevos valores.
otro_diccionario = {'b': 3, 'c': 4}
mi_diccionario.update(otro_diccionario)
print(mi_diccionario)
# Salida esperada: {'a': 1, 'b': 3, 'c': 4}

# 6. dict.pop(key[, default])
# Descripción: Elimina la clave especificada y devuelve su valor. Si la clave no existe, devuelve el valor predeterminado o lanza una excepción si no se proporciona.
# Aplicación: Útil cuando necesitas obtener y eliminar un elemento del diccionario.
valor_eliminado = mi_diccionario.pop('b')
print(valor_eliminado)  # Salida esperada: 3
print(mi_diccionario)  # Salida esperada: {'a': 1, 'c': 4}

# 7. dict.setdefault(key[, default])
# Descripción: Devuelve el valor de la clave especificada. Si la clave no existe, la inserta con el valor predeterminado proporcionado.
# Aplicación: Útil cuando deseas garantizar que una clave exista en el diccionario, con un valor predeterminado si no está presente.
valor = mi_diccionario.setdefault('c', 3)
print(mi_diccionario)  # Salida esperada: {'a': 1, 'c': 4}

# 8. dict.clear()
# Descripción: Elimina todos los elementos del diccionario.
# Aplicación: Útil cuando necesitas reiniciar un diccionario o eliminar todos sus elementos.
mi_diccionario.clear()
print(mi_diccionario)  # Salida esperada: {}

# 9. dict.copy()
# Descripción: Devuelve una copia superficial del diccionario.
# Aplicación: Útil cuando necesitas una copia independiente del diccionario original para modificar sin afectar el original.
mi_diccionario = {'a': 1, 'b': 2}
copia_diccionario = mi_diccionario.copy()
print(copia_diccionario)  # Salida esperada: {'a': 1, 'b': 2}

# 10. in (Operador de Pertenencia)
# Descripción: Verifica si una clave está en el diccionario.
# Aplicación: Útil para realizar comprobaciones antes de acceder a una clave para evitar errores.
if 'b' in mi_diccionario:
    print('Clave "b" está en el diccionario')
# Salida esperada: 'Clave "b" está en el diccionario'
