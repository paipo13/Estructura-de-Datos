#Realizar una función que, dada una cadena de caracteres y un carácter como parámetros, 
# encuentre la cantidad de ocurrencias del carácter en la cadena.
#La función creada debe ser llamada a través de una
#ariable para verificar su correcto funcionamiento.

def contar_caracter_en_cadena(cadena, caracter):
    contador = 0
    for elemento in cadena:
        if elemento == caracter:
            contador += 1
        else:
            pass
    return contador

#Testeo la funcion

cadena = "Hola, mundo!"
caracter = "o"
print(f"La letra '{caracter}' se repite {contar_caracter_en_cadena(cadena, caracter)} veces en la cadena.'{cadena}'")

#Solucion usando lambda:

contar_caracter_cadena = lambda cadena, caracter: len([c for c in cadena if c == caracter])

cadena = "Hola, mundo!"
caracter = "o"

print(f"La letra '{caracter}' se repite {contar_caracter_cadena(cadena,caracter)} en la cadena '{cadena}'.")
