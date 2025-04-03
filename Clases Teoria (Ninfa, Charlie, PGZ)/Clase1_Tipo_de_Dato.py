# Tipo De Datos

num = 8
print(type(num))


frase = 'Hola mundo'
print(type(frase))


# print(frase.__class__)
# print(frase.__class__.__name__) #me dice el nombre de la clase directamente sin el class(...)


# print(isinstance(num,float))
# print(isinstance(num,int))
# print(isinstance(num,(float,int)))#le doy dos opciones y como una es correcta devuelve True


print(id(num))
print(id(frase))
otro_numero = 8

# print(id(otro_numero))
# print(num == otro_numero)

# num = num + 3
# print(id(num))

# print(num is otro_numero)
# num = num - 3
# print(num is otro_numero)

# x = 1000
# y = 1000

# print (x is y)
# print (x == y)


# frase[0] = 'h'   LAS CADENAS SON INMUTABLES (al igual que ints floats y otros...)

frase = 'h' + frase[1:0]
print(frase)
print(id(frase))

#Range
r = range (4)
print(r)

for data in r:
    print(data, end = '')
    data += 1
    print(data)
print('\n',r[0])
print(r[0] == -1)


#Mutables
lista = [1,2,'a', True]
print(type(lista))
print(id(lista))
lista.append(2)
print(lista)
print(id(lista)) # notar que aunque le agreguemos un termino sigue teniendo el mismo id

lista2 = lista
print(id(lista2))
print(id(lista))

lista2 = [2,3,5]
print(id(lista2))
print(id(lista))

lista2[2] = 8
print(id(lista2))

lista2.extend(['hola','chau'])
print(lista2)
print(id(lista2))
