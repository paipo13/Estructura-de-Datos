# Utilice las funciones built-in donde dadas dos listas como parámetros devuelva una lista que contenga
# elementos alternados de ambas listas.
# Ejemplo1
# lista1=[1,2,3]
# lista2=["a", "b", "c"]
# resultado = [1, "a", 2, "b", 3, "c"]

def combinacion_listas(lista1, lista2):
    lista_combinada = list(zip(lista1, lista2))
    lista_final = [ j for i in lista_combinada for j in i]
    return lista_final

lista1 = [1, 2, 3]

lista2 = ["a", "b", "c"]

combinacion = combinacion_listas(lista1, lista2)

print(combinacion)


#VAMOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
