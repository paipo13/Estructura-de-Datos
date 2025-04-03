# Cree una función que permita almacenar la información de un diccionario en un archivo csv 
# y posteriormente leerlo.
import csv
from funciones import *
def nuevo_archivo(nombre_archivo,titulos):
    with open(nombre_archivo, "w", newline="" ,encoding="utf-8") as archivo :
            escritor = csv.writer(archivo)
            escritor.writerow(titulos)
def leer_archivo_dict_de_dict(nombre_archivo):
    ingredientes = {}
    encabezado = True
    try:
        with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if encabezado == True:
                    encabezado = False
                else:
                    clave = fila[0]
                    valor = fila[1]
                    if clave not in ingredientes:
                        ingredientes[clave] = valor
                    else:
                        ingredientes[clave].add(valor)
    except FileNotFoundError as e:
        return f'Error, archivo no encontrado {e}'
    else:
        return ingredientes
def crear_archivo_dict_de_dict(nombre_archivo, diccionario,titulos):
    nuevo_archivo(nombre_archivo,titulos)
    try:
        with open(nombre_archivo,"a", newline="" ,encoding="utf-8") as file :
            escritor = csv.writer(file)
            for clave, valor in diccionario.items():
                escritor.writerow([clave, valor])
    except Exception as e:
        return f'Error, {e}'
    else:
        return 'Archivo creado con éxito'
titulo = ['Ingredientes']
diccionario = {'Pan': {28.0, 22.8, 23.55}, 'Pollo': {33.85, 34.6}, 'Mermelada': {42.5}, 'Tomate': {18.3, 19.5}}

crear_archivo_dict_de_dict('Desayuno.csv',diccionario,titulo)
diccionario_de_ingredientes = leer_archivo_dict_de_dict('Desayuno.csv')
print(diccionario_de_ingredientes)
