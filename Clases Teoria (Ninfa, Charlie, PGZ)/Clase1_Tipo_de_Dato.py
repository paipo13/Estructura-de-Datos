### TIPO DE DATOS ###

num = 8
print(type(num))

frase = 'Hola mundo'
print(type(frase))


print(frase.__class__)          # .__class__ lo que hace es darme el nombre de la clase (clase es lo mismo que tipo) del objeto
print(frase.__class__.__name__) # me dice el nombre de la clase directamente sin el class(...)


print(isinstance(num,float))        # isinstance es una funcion en la que en el primer terminoj ponemos el objeto que
                                    # deseamos analizar y en el segundo termino un nombre de clase. Si la clase que pusimos 
                                    # en el segundo termino es correcta devuelve True, de lo contrario devuelve False (obs. Booleanos...)
print(isinstance(num,int))
print(isinstance(num,(float,str))) #le doy dos opciones y como una es correcta devuelve True


print(id(num))          # El id es la direccion de memoria, de la computadora, en la cual se guardo el objeto. Luego veremos que en algunos objetos
                        # denominado mutables si yo hago ciertas modificaciones al objeto la direccion (el id) no cambia, mientras que en los
                        # inmutables si hago modificaciones al objeto la dirreccion de memoria cambia (Es decir TENEMOS OTRO OBJETO!!!)
print(id(frase))

### INMUTABLES ###

otro_numero = 8
print(id(otro_numero))    # Obs. Notar como el id de "otro_numero" es el mismo que "num".
print(num == otro_numero) # Da True ya que en valor son lo mismo.
print(id(num)==id(otro_numero)) # Da True ya que son la misma direccion de memoria
num = num + 3 # CAMBIA LA DIRECCION DE MEMORIA (int es un objeto inmutable!!!)
print(id(num)) # El id (direccion de memoria) es otro...

print(num is otro_numero) # Devuelve false
num = num - 3 # Vuelve a la misma direccion de memoria
print(num is otro_numero) # True

x = 1000
y = 1000

print (x is y)
print (x == y)

frase = "hola mundo"
print(id(frase))
frase = "h" #  LAS CADENAS (str´s) SON INMUTABLES (al igual que ints, floats y otros...)
print(id(frase)) # Como son inmutables aqui observamos como la direccion de memoria cambia...
frase = frase + "ola mundo"
print(frase)
print(id(frase)) # Notar como el str sigue siendo el mismo que al principio pero despues devido a los cambios sufridos el id no es el mismo...

### RANGE ###

r = range(4)
print(r)

for data in r:
    print(data, end = ' ')
    data += 1
    print(data)
print('\n',r[0]) # Devuelve 0 (int)
print(r[0] == -1) # Devuelve False


### MUTABLES ###
lista = [1,2,'a', True]
print(type(lista))
print(id(lista))
lista.append(2)
print(lista)
print(id(lista)) # notar que aunque le agreguemos un termino sigue teniendo el mismo id

lista2 = lista
print(id(lista2))
print(id(lista)) #Ambos valores de id son los mismos!!! 

lista2 = [2,3,5] #Ahora la direccion de memoria de lista2 va a variar ya que la definimos como algo totalmenete nuevo
print(id(lista2))
print(id(lista))

lista2[2] = 8
print(id(lista2)) # No varia el id... (inmutable)

lista2.extend(['hola','chau'])
print(lista2)
print(id(lista2)) # No varia el id... (inmutable)
