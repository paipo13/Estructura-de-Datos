### FUNCIONES DE INFORMATICA GENERAL ###


#funcion normal
# suma de dos numeros
def sumar(dato1,dato2):
    return dato1+dato2
suma=sumar(3,5)
print(suma)
# cuadrado de un numero
def cuadrados(num):
    return num**2
print(cuadrados(5))

#Lambda
##Ej1. Suma de dos numero
sumarLam=lambda dato1,dato2:dato1+dato2
suma=sumarLam(3,5)
print(suma)

##Ej2. cuadrado de un numero
cuadrado=lambda x: x**2
print(cuadrado(5))

# funcion map
#Ej1. Elevar al cuadrado cada numero de una lista
listanum=[3,5,2,1,0]
## usando funcion normal
iterable=map(cuadrados,listanum)
listacuadrado=list(iterable)
print(listacuadrado)

## usando llamado a lambda
iterable=map(cuadrado,listanum)
listacuadrado=list(iterable)
print(listacuadrado)

## usando lambda
iterable=map(lambda x:x**2,listanum)
listacuadrado=list(iterable)
print(listacuadrado)

# funcion filter
#Ej1. Generar una lista con los numeros pares de una lista

filtrada=list(filter(lambda x:x%2==0,listacuadrado))
print(filtrada)

#Ej2. Generar una lista con los numeros pares mayores a CERO de una lista
filtrada=list(filter(lambda x:x%2==0 and x>0,listacuadrado))
print(filtrada)

# funcion zip
# Ej1. generar una lista de lista con dos listas dadas de distintas longitudes
# usando zip


lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b']

# Ej1. No emparejamos el tamaño de las lista
resultado = zip(lista1, lista2)
# Convertimos el resultado a una lista de tuplas y lo imprimimos
lista=list(resultado)

# Convertimos el resultado a una lista de tuplas en una lista de listas. Usando Map
listafinal=list(map(list,lista))
print(listafinal)

# Ej2. Usamos zip para emparejar los elementos
from itertools import zip_longest
resultado = zip_longest(lista1, lista2)
resultado = zip_longest(lista1, lista2, fillvalue='-1')# fillvalue puede ser cualquier tipo
# Convertimos el resultado a una lista de tuplas y lo imprimimos
lista=list(resultado)

# Convertimos el resultado a una lista de tuplas en una lista de listas. Sin Usar Map
listafinal=[list(tupla) for tupla in lista]
print(listafinal)

# Ej3. Generar una lista con la suma de los elementos de la misma posicion de las listas dadas
# Ejemplo:
# lista1 = [1, 2, 3, 4]
# lista2 = [5, 6, 7, 8]
# resultado = [6, 8, 10, 12]

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

## Usando funcion sum()
resultado1=list(zip(lista1,lista2))
print(resultado1)
resultado=list(map(sum,resultado1))
print(resultado)

## Usando funcion lambda
resultado=list(map(lambda x:x[0]+x[1],resultado1))
print(resultado)

# Usando *args
# Sumar los elementos correspondientes de varias listas, filtrar los elementos
# solo para ver los numeros pares mayores a cero y luego multiplicar cada numero
# por 2 y visualizar la suma total de los elementos de la lista final

#armar lista a trabajar

def listaInicial(*args):
    return list(map(sum,zip(*args)))

lista1 = [1, 2, 3, 4]
# lista2 = [5, 6, 7, 8]
# lista3 = [5, 6, 7, 8]

#lista1=listaInicial(lista1,lista2,lista3)
lista1=listaInicial(lista1)
print(lista1)

#filtrado de los numeros
pares=list(filter(lambda x:x>0 and x%2==0, lista1))
print(pares)

#suma lista 1 usando reduce
from functools import reduce
sumalista1=reduce(lambda x,y: x+y,lista1)
print(sumalista1)

#suma lista 1 usando sum
sumalista2=sum(pares)
print(sumalista2)