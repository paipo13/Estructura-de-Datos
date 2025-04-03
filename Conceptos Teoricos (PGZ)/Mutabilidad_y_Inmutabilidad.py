### MUTABILIDAD Y INMUTABILIDAD ###

# Los objetos en phyton pueden ser inmutables y mutables. 
# (SOBRE ESTO SE RECONTRA PUEDE TOMAR EN LA PARTE TEORICA DEL EXAMEN)

# OBJETOS INMUTABLES --> Un objeto inmutable es aquel cuyo valor no puede cambiar después de su creación. 
# Si intentamos modificarlo, Python en realidad crea un nuevo objeto en memoria en lugar de modificar el original.
# 
# Casos comunes de esto son los objetos de tipo int, float, string, tuplas, etc...

# Ejemplo:
a = 10
print(id(a))  # Muestra la dirección de memoria de 'a'

a = a + 5
print(id(a))  # Dirección de memoria diferente (nuevo objeto)

# Con cadenas de texto
texto = "Hola"
print(id(texto))  # Dirección de memoria inicial

texto += " Mundo"
print(id(texto))  # Dirección de memoria diferente (nuevo objeto)

# Obs. Cuando modificamos a o texto, no cambiamos el objeto original, sino que creamos uno nuevo en memoria.



#OBJETOS MUTABLES --> Un objeto mutable es aquel cuyo valor puede cambiar después de su creación,
#sin necesidad de crear un nuevo objeto en memoria.
#
# Casos comunes de esto son listas, dictionarios, sets, etc...

#Ejemplo:
lista = [1, 2, 3]
print(id(lista))  # Dirección de memoria inicial

lista.append(4)  # Modificamos la lista
print(id(lista))  # Misma dirección de memoria (se modificó el objeto)

# Obs. A diferencia de los datos inmutables, aquí la dirección de memoria se mantiene igual, 
# ya que modificamos el mismo objeto en lugar de crear uno nuevo.



# NOTA(Diferencia entre "is" y "=="):
#Cuando comparamos objetos, debemos diferenciar entre contenido (==) y identidad en memoria (is).
# a = "Hola"
b = "Hola"
print(a == b)  # True  (Mismo contenido)
print(a is b)  # True en algunos casos, pero no siempre (mismo objeto en caché)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 == lista2)  # True  (Mismo contenido)
print(lista1 is lista2)  # False (Distintos objetos en memoria)

# Obs. Por lo que "==" compara el contenido de los objetos. Mientras que "is" compara la dirección de memoria.
