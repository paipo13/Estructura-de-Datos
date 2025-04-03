### TUPLAS ###


# Si bien no es lo que mas usamos, las tuplas son una parte fundamntal de la materia y es importante
# entenderlas y llegado el caso optimo aplicarlas.
# Una tupla en Python es una estructura de datos inmutable que permite almacenar una colección ordenada de elementos.
# Se representan con paréntesis () y pueden contener cualquier tipo de dato:
mi_tupla = (1, "Hola", 3.14, True)

# Las tuplas son útiles cuando queremos almacenar datos que no deben modificarse después de su creación.
# Se utilizan por varias razones:

# Seguridad: Evitan modificaciones accidentales en los datos. (IMPORANTE)
# Eficiencia: Ocupan menos espacio en memoria que las listas y son más rápidas en operaciones de acceso. 
# Claves en diccionarios: Como son inmutables, pueden usarse como claves en un dict, a diferencia de las listas. (IMPORTANTE)

# Ejemplo 1: Las tuplas permiten retornar varios valores de una función de forma sencilla.
def coordenadas():
    return (10, 20)  # Devuelve una tupla con coordenadas

x, y = coordenadas()  # Desempaquetado de tupla
print(x, y)  # 10 20


# Ejemplo 2: Las tuplas pueden usarse como claves en diccionarios porque son inmutables.
poblaciones = {
    ("Argentina", "Buenos Aires"): 15000000,
    ("España", "Madrid"): 3200000
}

print(poblaciones[("Argentina", "Buenos Aires")])  # 15000000


# Ejemplo 3: La función enumerate() devuelve una tupla (índice, valor), facilitando la iteración sobre listas.
frutas = ["Manzana", "Banana", "Cereza"]

for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# Este ultimo ejemplo si lo corremos nos devolvera: 
# 0: Manzana
# 1: Banana
# 2: Cereza



# Informacion Relevante:

# 1. Las tuplas son inmutables por lo tanto:
mi_tupla = (1, 2, 3)
mi_tupla[0] = 10  # Error: las tuplas no pueden modificarse

# 2. Las tuplas pueden contener cualquier tipo de dato:
mi_tupla = (1, "Hola", 3.14, True)

# 3. Las tuplas se pueden convertir en listas y viceversa:
lista = [1, 2, 3]
tupla = tuple(lista)  # Convierte lista en tupla
print(tupla)  # (1, 2, 3)

lista_nueva = list(tupla)  # Convierte tupla en lista
print(lista_nueva)  # [1, 2, 3]

