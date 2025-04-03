# Realizar una función que dada una cadena que es una estructura de Datos no mutable, me permita 
# modificarla en una posición y un valor dados para esa posición

def cambio_no_mutable ():
    string = input('Ingrese el str que desee: ')
    num = int(input('ingrese la posicion que desea cambiar: '))
    valor = input('Cual es el valor que desea agregar en dicha posicion?: ')
    print(string)
    print(id(string))
    nuevo_string = string [:num] + valor + string[num + 1:]
    return nuevo_string

str = cambio_no_mutable()
print(str)
print(id(str))