# Investigar 5 métodos que le permitan modificar una lista dada, haga un ejercicio con cada uno de los 
# métodos investigados y demuestre en cada uno de estos ejercicios que la lista es un tipo de dato mutable.

# Los 5 metodos podrian ser:
# 1. Append 2.Extend 3.Insert 4.Remove 5.Clear 6.Pop
# Tomamos la lista de ejemplo:
lista = [2,'hola',None, 'Ordenas',10]
print(id(lista))
# 1. 
lista.append(['Ahora'])
print(lista)
print(id(lista))
# 2. 
lista.extend(['hola',7,8])
print(lista)
print(id(lista))
# 3.
lista.insert(0,'primero')
print(lista)
print(id(lista))
# 4.
lista.remove('hola')
print(lista)
print(id(lista))
# 5.
a = lista.pop(3)
print(a)
print(lista)
print(id(lista))
# 6. 
lista.clear()
print(lista)
print(id(lista))