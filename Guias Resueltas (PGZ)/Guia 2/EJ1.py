#Realizar una función que permita contar la cantidad total de caracteres alfabéticos, dígitos y caracteres
#especiales en una cadena.

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

#Pruebo la función

string = 'Hola mn7399898,**¿s!!!"""oy un R0b0t'
count_alfa,count_digit,count_caracter = contar_caracteres(string)
print (count_alfa,count_digit,count_caracter)