### OBJETOS ###

#Me voy a cansar de decirlo pero es asi: TODO en phyton son OBJETOS!!!
 
# En Python, todo es un objeto. Cada número, cadena, lista o función es una instancia de una clase.
# Un objeto en Python tiene tres características fundamentales(A,B y C):

# (A)-->   PERTENENCIA A UNA CLASE (tipificación): 
#Si bien no estamos haciendo constante uso de esto es MUY importante tenerlo bien en claro. Y el isinstance puede
# llegar a ser una herramienta muy util en algunos casos.
# Cada objeto en Python pertenece a una clase. 
# La clase define qué atributos y métodos tiene un objeto. Para saber a qué clase pertenece un objeto, podemos usar:
#   1. type(objeto): Devuelve la clase del objeto.
#   2. objeto.__class__: Es equivalente a type(objeto), pero accediendo directamente al atributo.
#   3. isinstance(objeto, Clase): Verifica si un objeto pertenece a una clase o a una subclase. 
# OBS. El insinstance() tambien lo usaremos para verificar si un objeto ya existe (mediante el uso de booleanos)
# o si no pertenece a una dterminada clase comparando un objeto con el otro 
#Ejemplo:
x = 10
print(type(x))           # <class 'int'>
print(x.__class__)       # <class 'int'>
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False
#
#NOTA(Para cuando veamos herencia entre clases y subclases): La diferencia entre type y isinstance es que 
# type(objeto) == Clase solo es verdadero si el objeto es exactamente de esa clase.
# mientras que 
# isinstance(objeto, Clase) también es verdadero si la clase es una subclase de otra.
# Ejemplo(Con herencia):
class Animal: pass
class Perro(Animal): pass
firulais = Perro()
print(type(firulais) == Animal)    # False
print(isinstance(firulais, Animal)) # True


# (B)--> UBICACION EN MEMORIA (identidad):
# Si bien es importante tener en claro teoricamente, no lo terminamos usando tanto en la practica. Leer de todas formas!
# Cada objeto en Python tiene una dirección de memoria única, identificada por su ID. Generalmente cuando tratemos
# este tema de direccion de memoria usaremos:

#   1. id(objeto): Devuelve el identificador único del objeto en la memoria.
#   2. is: Compara si dos variables apuntan al mismo objeto en memoria.
#   3. ==: Compara si dos objetos tienen el mismo valor.
#
#NOTA(Diferencia entre is y ==): 
# is verifica si dos variables hacen referencia al mismo objeto en memoria.
# mientra que 
# == verifica si los valores de los objetos son iguales, pero pueden estar en diferentes ubicaciones en memoria.
#
#Ejemplo:
a = [1, 2, 3]
b = a  # Ambas variables apuntan al mismo objeto
c = [1, 2, 3]  # Es un objeto distinto con el mismo contenido

print(a == c)  # True (mismo contenido)
print(a is c)  # False (diferentes objetos en memoria)
print(a is b)  # True (ambas apuntan al mismo objeto)

print(id(a), id(b), id(c))  # a y b tienen el mismo id, c tiene otro


# (C)--> VALOR Y MUTABILIDAD:
# Ahora bien esta ultima caracteristica es muy importante y se va a usar de forma indirecta durante toda la cursada.
#Los objetos en Python pueden ser mutables o inmutables, dependiendo de si su contenido puede cambiar después
# de la creación.

# Los Objetos Inmutables unas vez creados no pueden ser modificados. Se trata de:
# Números (int, float, complex),
# Cadenas de texto (str),
# Tuplas (tuple),
# etc...
# Ejemplo:
x = "hola"
x[0] = "H"  # Esto dará error porque las cadenas son inmutables

# Por otro lado los Objetos Mutables pueden ser modificados despues de su creacion. Se trata de:
# Listas (list),
# Diccionarios (dict),
# Conjuntos (set),
# etc...
lista = [1, 2, 3]
lista.append(4)  #  Se puede modificar sin problema
print(lista)  # [1, 2, 3, 4]

# OBS. Hay que tener cuidado con los Objetos Mutables ya que si si asignamos un objeto mutable a otra
# variable, ambas variables apuntan al mismo objeto en memoria, por lo que modificar una afectará a la otra.

# Ejemplo:
# a = [1, 2, 3]
# b = a  # Ambas apuntan al mismo objeto
# b.append(4)
# print(a)  # [1, 2, 3, 4] -> ¡a también se modificó!

# Para evitar esto, podemos usar .copy() o copy.deepcopy().

# a = [1, 2, 3]
# b = copy.deepcopy(a)  # Ahora b es una copia independiente
# b.append(4)
# print(a)  # [1, 2, 3] -> No se modificó
# print(b)  # [1, 2, 3, 4]
