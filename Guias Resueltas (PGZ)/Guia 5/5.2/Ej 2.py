# Realizar una función que dada una lista de palabras  y un diccionario que contiene cuántos puntos
# vale cada letra, devolver  la palabra cuyo puntaje sea máximo.
# El puntaje total, se calcula sumando los puntajes de cada una de las letras que la componen
# (de manera similar a la del juego Scrabble'’).
# Las letras que no están en el diccionario otorgan 1 punto cada una.
# Las letras que sí están en el diccionario otorgan el valor indicado en el diccionario.


# Ejemplo 1
# Palabras=[“cono”,”mazazo”,”fanzine”,”fhan”,”marsupial”]
# Diccionario:
# {‘a’:2,
# ’n’:3,
# ' f ' :  5,
# ' z ' :5}
# La palabra de mayor puntaje es: fanzine

def scrabble(lista_palabras):
    puntos_letra = {'a':2, 'b':2, 'c':3, 'd':3, 'e':2, 'p': 4, 's':4,'o':4,'f':3, 'g':3, 'h':4, 'i':3, 'r':3}
    lista_puntos_por_palabra = []
    for i in range(len(lista_palabras)):
        valor_palabra = 0
        for j in lista_palabras[i]:
            valor = puntos_letra.get(j)
            if valor is None:
                valor_palabra += 1
            else:
                valor_palabra += valor
        lista_puntos_por_palabra.append(valor_palabra)
    maximo_puntaje = max(lista_puntos_por_palabra)
    for i in lista_puntos_por_palabra:
        if i == maximo_puntaje:
            pos_palabra_ganadora = lista_puntos_por_palabra.index(i)
            break
    return f'La palabra de mayor puntaje es: {lista_palabras[pos_palabra_ganadora]}'

lista_palabras = ['ahora', 'juncal', 'paz', 'molinos', 'dinosaurio', 'molecular','posoph']
print(scrabble(lista_palabras))

