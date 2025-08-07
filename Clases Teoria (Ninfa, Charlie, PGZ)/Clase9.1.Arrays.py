import numpy as np

#crear vector

vector = np.array({1,2,3,4})
print(vector)

vector1 = np.array((11,12,13,14))
print(vector1)

#crear matriz
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)

#Metodos Comunes:
#1. Len:
print(len(vector1))

#2. Append:
print(id(vector1))
vector1 = np.append(vector1,5)
print(vector1)
print(id(vector1))

#3. Delete:
print(id(vector1))
vector1 = np.delete(vector1, 4)
print(vector1)
print(id(vector1))


#4. Range version np
vectordato = np.arange(0,20) #Obs. va a crear un array del 0 al 19.
print(vectordato)


#5. Creacion de matriz usando UN SOLO vector
vectordato2 = np.arange(0,9).reshape(3,3) #Obs. va a crear una matriz con un solo vector y organizando este vecotr con reshape
print(vectordato2)


#6. array de una n (en este caso 5) cant de elementos entre 0 y x (en este caso 8)
vectoricito = np.random.randint(8,size=5)
print(vectoricito)

#7. Multiplicar un vector por un escalar

vector_escalar = np.array([1,2,3,4,5])
escalar = 2
vector_escalar_multiplicado = vector_escalar * escalar
print(vector_escalar_multiplicado)

#8. Sumar dos vectores

vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
vector_sumado = vector1 + vector2
print(vector_sumado)

# obs. Notemos la diferencia con listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
print(lista1 +lista2)
print(lista1*3)

#9. Concatenar vectores

vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
vector_concatenado = np.concatenate((vector1,vector2))
print(vector_concatenado)

#10. Matriz Identidad. de X*X, en este caso X = 4.
print(np.eye(4))
print(np.ones((4,4), dtype=int)) #Ponemos el dtype = ... para especificar el tipo de dato que ira en cada espacio de la matriz.
print(np.zeros((3,3))) #matriz de 3*3, todos los elementos son 0. Tal que es la matriz nula. Notar igual que me da un float.
