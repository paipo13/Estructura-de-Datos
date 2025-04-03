# Realizar una función nombrada afuera que tenga como único parámetro de entrada la función
# contarCaracteres y debe devolver la cantidad de cada uno de los caracteres de la cadena pedida en la
# función afuera.
# La función contarCaracteres cuenta la cantidad de cada uno de los caracteres que se encuentran en una
# cadena.
#Al ejecutar la función afuera debe hacerlo a través de una variable, el resultado debe verse como en el
#ejemplo.

def contarCaracteres(cadena, caracter):
    return cadena.count(caracter)
def afuera(contarCaracteres):
    cadena = input('ingrese la cadena: ')
    caracteres_ya_procesados = []
    for i in cadena.lower():
        if i not in caracteres_ya_procesados:
            cantidad = contarCaracteres(cadena,i)
            print(f'El caracter {i} se repite {cantidad} veces.')
            caracteres_ya_procesados.append(i)

afuera(contarCaracteres)