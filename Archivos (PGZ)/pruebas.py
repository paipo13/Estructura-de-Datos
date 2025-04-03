nombre_archiv = 'sube/viajes_sube_datos.csv'
import csv
def crear_archivo_csv(nombre_archivo,titulos):
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(titulos)

lista_nombres = ['Pedro', 'Facundo', 'Felipe','Tomas']
lista_edades = [20,12,24,53]
Titulos = ['Nombre','Edad']

crear_archivo_csv('Prueba_de_arvhivo', Titulos)

with open('Prueba_de_arvhivo', 'a', newline='') as file:
    writer = csv.writer(file)
    for i in lista_nombres:
        writer.writerow([i, lista_edades[lista_nombres.index(i)]])

# Para ver el archivo creado

with open('Prueba_de_arvhivo', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

diccionario = {}

