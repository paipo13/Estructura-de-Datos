# La recursividad de por si no es una estructura de datos es una 
# tecnica de programacion, en la cual un metodo se llama a si mismo
# como parte de la solucion de un problema.

# Obs. La recursion debe ser finita. Es decir, que debe haber algo que en algun momento pare ese llamado (como en el while). En nuestro caso sera el caso base quein lo frene.
# El caso base es a lo que va a tender para en algun momento frenar. Se debe terminar al menos un caso base.

# Obs. La recursion puede sustituir la iteracion. 

#Obs. Cunado yo itero lo que hago son ciclos. Pero cuando yo hago recursion, lo que hago son 
# llamados a una misma funcion.

# Obs. En recurcion vamos a trabajar con una variable acumulador de productors.

#Ej: 
def factorial(num):
    acum = 1
    i = 1
    while i<= num:
        acum *= i
        i += 1
    return acum

print(factorial(5))

#Notemos que en este caso nuestro caso base es el 0! que siempre va a ser igual a 1
#Implementando mejor el caso base y la recursividad:

def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)


print(factorial_recursivo(5))

# suma los digitos de un numero entero introducido por el usuario, resolver de manera recursiva.

def suma_digitos(num):
    if num == 0:
        return 0
    else:
        return num % 10 + suma_digitos(num // 10)

print(suma_digitos(12345))

# sumar los elementos de una lista

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])