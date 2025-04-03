# Utilice funciones built-in para crear una nueva lista añadiendo la palabra ‘Hola’ a cada uno de los nombres
# de las personas que están en una lista dada.
# Ejemplo 1
# Listanombre=["Ninfa","Nicolas","Juan","Pedro"]
# Listasaludo=["Hola Ninfa","Hola Nicolas","Hola Juan","Hola Pedro"]

listasaludoslambda = lambda lista: ['Hola '+ i for i in lista]

listanombre = ["Ninfa","Nicolas","Juan","Pedro"]

print(listasaludoslambda(listanombre))

#SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
