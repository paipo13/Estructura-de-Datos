import csv
#Buenos Aires,Lima,Santiago de Chile,Sucre,Asunción
paises = ['Argentina','Perú','Chile','Bolivia','Paraguay']
capitales = ['Buensos Aires','Lima','Santiago de Chile','Sucre','Asunción']
def crear_archivo(lista,nombre_archivo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_nuevo:
        escritor = csv.writer(archivo_nuevo)
        titulo = input('Ingrese el titulo de los datos que va a agregar: ')
        escritor.writerow([titulo])  # Updated header row

    with open(nombre_archivo, "a", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)
        for i in lista:
            escritor.writerow([i])  # Added country names as the second column
# crear_archivo(paises,'Paises.csv')
# crear_archivo(capitales,'Capitales.csv')
def nuevo_archivo(nombre_archivo,titulos):
    with open(nombre_archivo, "w", newline="" ,encoding="utf-8") as archivo :
            escritor = csv.writer(archivo)
            escritor.writerow(titulos)
def crear_archvio_con_ambas_listas(nombre_archivo,lista_paises,lista_capitales,titulos):
    nuevo_archivo(nombre_archivo,titulos)
    with open(nombre_archivo,"a", newline="" ,encoding="utf-8") as file :
        escritor = csv.writer(file)
        for i in range(len(lista_paises)):
            if lista_paises[i] == 'Bolivia':
                escritor.writerow([lista_paises[i],'La Paz'])
            else:
                escritor.writerow([lista_paises[i],lista_capitales[i]])
titulos = ['Paises', 'Capitales']
#crear_archvio_con_ambas_listas('Paises_Capitales.csv',paises,capitales,titulos)

def leer_archivo(nombre_archivo):
    lista_paises = []
    lista_capitales = []
    encabezado = True
    try:
        with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if encabezado ==True:
                    encabezado = False
                else:
                    lista_paises.append(fila[0])
                    lista_capitales.append(fila[1])
    except FileNotFoundError as e:
        return f'Error, archivo no encontrado {e}'
    else:
        return lista_paises, lista_capitales

# paises_leidos, capitales_leidos = leer_archivo('Paises_Capitales.csv')
# print(paises_leidos, capitales_leidos)

#Ahora debemos hacer lo mismo pero con diccionarios en vez de listas

Mundo = {'Argentina': 'Buenos Aires','Peru': 'Lima', 'Chile': 'Santiago de Chile', 'Bolivia': 'La Paz', 'Paraguay': 'Asuncion'}
titulos = ['Paises','Capitales']
def crear_archivo_dict(nombre_archivo, diccionario,titulos):
    try:
        with open(nombre_archivo,"a", newline="" ,encoding="utf-8") as file :
            escritor = csv.writer(file)
            escritor.writerow(titulos)
            for clave, valor in diccionario.items():
                escritor.writerow([clave, valor])
    except Exception as e:
        return f'Error, {e}'
    else:
        return 'Archivo creado con éxito'
crear_archivo_dict('Mundi.csv',Mundo,titulos)


def leer_archivo_dict(nombre_archivo):
    diccionario_final = {}
    encabezado = True
    try:
        with open(nombre_archivo,'r', newline="" ,encoding="utf-8") as file:
            lector = csv.reader(file)
            for fila in lector:
                if encabezado == True:
                    encabezado = False
                else:
                    for i in range(len(fila)):
                        diccionario_final[fila[0]] = fila[1]
    except FileNotFoundError as e:
        return f'Error, archivo no encontrado {e}'
    else:
        return diccionario_final

diccionario_mundi = leer_archivo_dict('Mundi.csv')
print(diccionario_mundi)