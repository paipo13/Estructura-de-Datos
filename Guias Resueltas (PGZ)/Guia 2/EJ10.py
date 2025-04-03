# Utilice las funciones built-in para que dada una lista de nombres haga una lista donde almacena la cantidad
# de letras ‘a’ o ‘A’ que hay en cada nombre de la lista .
# Ejemplo1
# listaciudad=["Mendoza", "Salta", "Catamarca", "Iguazu",
# "Bariloche", "Purmamarca","Armenia"]
# listaas=[1,2,4,1,1,3,2]


def funciones_built_in(lista):
    #lista = list(map(funcion,lista))
    lista_final = list(map(lambda elemento: elemento.count('a') + elemento.count('A'), lista))
    return lista_final

listaciudad=["Mendoza", "Salta", "Catamarca", "Iguazu", "Bariloche", "Purmamarca","Armenia"]

print(funciones_built_in(listaciudad))