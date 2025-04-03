#### FUNCIONES UTILES ####
lista = [1,2,3,4,5]
multiplos = list(map(lambda x : x*2, lista ))
print(type(multiplos))
print(isinstance(multiplos,int))
print(multiplos)
for i in multiplos:
    print(i)
print(multiplos.count(2))
lista_comas = ['esta , es mi , lista, de simepre', 'Ahora y nunca, me la , van a ,quitar',',,']
nueva_lista = []
for i in lista_comas:
    nueva_lista.append((i).replace(',',''))
print(nueva_lista)
ultra_nueva_lista = []
for i in nueva_lista:
    listita = (i.split())
    for j in listita:
        ultra_nueva_lista.append(j)
print('Esta es mi nueva lista, sin comas y sin espacios:',ultra_nueva_lista)

# Aquí hay una breve descripción y ejemplos de las funciones mencionadas en Python:

# 1. `filter`: Esta función se utiliza para filtrar elementos de una secuencia según una condición dada. 
# Recibe una función de prueba y una secuencia, y devuelve una nueva secuencia con los elementos que cumplen con la condición. 
# Ejemplo: `filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])` devuelve `[2, 4]`.

# 2. `map`: Esta función se utiliza para aplicar una función a cada elemento de una secuencia y devolver una nueva secuencia con los resultados. 
# Recibe una función y una secuencia, y devuelve una nueva secuencia con los resultados de aplicar la función a cada elemento. 
# Ejemplo: `map(lambda x: x * 2, [1, 2, 3, 4, 5])` devuelve `[2, 4, 6, 8, 10]`.

# 3. `zip`: Esta función se utiliza para combinar elementos de varias secuencias en pares. 
# Recibe varias secuencias y devuelve una nueva secuencia de tuplas con los elementos correspondientes de cada secuencia. 
# Ejemplo: `zip([1, 2, 3], ['a', 'b', 'c'])` devuelve `[(1, 'a'), (2, 'b'), (3, 'c')]`.

# 4. `enumerate`: Esta función se utiliza para agregar un índice a cada elemento de una secuencia. 
# Recibe una secuencia y devuelve una nueva secuencia de tuplas con el índice y el elemento correspondiente. 
# Ejemplo: `enumerate(['a', 'b', 'c'])` devuelve `[(0, 'a'), (1, 'b'), (2, 'c')]`.

# 5. `sorted`: Esta función se utiliza para ordenar una secuencia. 
# Recibe una secuencia y devuelve una nueva secuencia ordenada. 
# Ejemplo: `sorted([5, 3, 1, 4, 2])` devuelve `[1, 2, 3, 4, 5]`.

# 6. `type`: Esta función se utiliza para obtener el tipo de un objeto. 
# Recibe un objeto y devuelve su tipo. 
# Ejemplo: `type(5)` devuelve `<class 'int'>`.

# 7. `isinstance`: Esta función se utiliza para comprobar si un objeto es de un tipo específico. 
# Recibe un objeto y un tipo, y devuelve `True` si el objeto es del tipo especificado y `False` en caso contrario. 
# Ejemplo: `isinstance(5, int)` devuelve `True`.

# 8. `reversed`: Esta función se utiliza para invertir el orden de los elementos de una secuencia. 
# Recibe una secuencia y devuelve una nueva secuencia con los elementos invertidos. 
# Ejemplo: `reversed([1, 2, 3, 4, 5])` devuelve `[5, 4, 3, 2, 1]`.

# 9. `list`: Esta función se utiliza para convertir un objeto iterable en una lista. 
# Recibe un objeto iterable y devuelve una nueva lista con los elementos del objeto iterable. 
# Ejemplo: `list(range(5))` devuelve `[0, 1, 2, 3, 4]`.

# 10. `tuple`: Esta función se utiliza para convertir un objeto iterable en una tupla. 
# Recibe un objeto iterable y devuelve una nueva tupla con los elementos del objeto iterable. 
# Ejemplo: `tuple([1, 2, 3, 4, 5])` devuelve `(1, 2, 3, 4, 5)`.

# 11. `ascii`: Esta función se utiliza para convertir un carácter o una cadena en su representación ASCII. 
# Recibe un carácter o una cadena y devuelve una cadena con la representación ASCII del carácter o de la cadena. 
# Ejemplo: `ascii('a')` devuelve `'a'`.

# 12. `count()`: Esta función se utiliza para contar la cantidad de apariciones de un elemento específico en una secuencia. 
# Recibe una secuencia y un elemento, y devuelve el número de apariciones del elemento en la secuencia. 
# Ejemplo: `'abcabc'.count('a')` devuelve `2`.

# 13. `strip()`: Esta función se utiliza para eliminar espacios en blanco al principio y al final de una cadena. 
# Recibe una cadena y devuelve una nueva cadena con los espacios en blanco eliminados. 
# Ejemplo: `'  hello  '.strip()` devuelve `'hello'`.

# 14. La función split() es un método incorporado en Python que se utiliza para dividir 
# una cadena en una lista de subcadenas basándose en un delimitador específico. 
# El delimitador es el carácter o secuencia que separa las subcadenas en la cadena original.

# Parámetros:
# split(separador, maxsplit=-1): La función split() toma dos parámetros opcionales:
# separador: Este parámetro especifica el delimitador que se utilizará para dividir la cadena. 
# Si no se proporciona ningún separador, la cadena se dividirá basándose en los caracteres en blanco.
# maxsplit: Este parámetro especifica el número máximo de divisiones a realizar. 
# Si maxsplit no se proporciona o es negativo, la cadena se dividirá en tantas subcadenas como sea posible.





#### menu() ####

def menu():
    # camiones = []
    # patente_camiones = []
    while True:
        print("\nMenú:")
        print("a. ")
        print("b. ")
        print("c. ")
        print("d. ")
        print("e. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "a":
            pass
        elif opcion == "b":
            pass
        elif opcion == "c":
            pass
        elif opcion == "d": 
            pass
        elif opcion == "e": 
            break
        else:
            print("Opción incorrecta. Intente de nuevo.")
