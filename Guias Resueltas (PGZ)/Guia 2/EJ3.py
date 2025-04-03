#Realizar una función que tenga como parámetro de entrada la función creada en el ejercicio 1 y devuelve
#una cadena formada por todos los caracteres del tipo cuya cantidad total de caracteres es la mayor.
#Si los elementos alfabéticos son los de mayor cantidad la lista creada debe transformar los datos minúsculas
#en mayúsculas y viceversa

#Funcion creada en el ejercicio 1:
def contar_caracteres(cadena):
    contador_alfabéticos = 0
    contador_digitos = 0
    contador_caracteres_especiales = 0
    for caracter in cadena:
        if caracter.isalpha():
            contador_alfabéticos += 1
        elif caracter.isdigit():
            contador_digitos += 1
        elif not caracter.isalnum():
            contador_caracteres_especiales += 1
    return contador_alfabéticos, contador_digitos, contador_caracteres_especiales

