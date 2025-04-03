import csv

#CREAR ARCHIVO CSV
def nuevo_archivo(nombre_archivo,titulos):
    with open(nombre_archivo, "w", newline="" ,encoding="utf-8") as archivo :
            escritor = csv.writer(archivo)
            escritor.writerow(titulos)   # Solo crea archivo CSV y pone los titulos en la primera fila.
def leerarchivoread(file):

    try:
        with open(file,'r',encoding='utf8') as archivo:
            lector=csv.reader(archivo)

    except:
        print("El archivo no existe o no esta ubicado donde lo estas buscando")

def agregar_datos_a_archivo (archivo, lista1, lista2): # Agrega nuevos datos a el archivo CSV. Pueden ser 1 o muchos datos.
    with open(archivo, "a", newline="" ,encoding="utf-8") as file :
        escritor = csv.writer(file)
        for i in range(len(lista1)):
            escritor.writerow([lista1[i], lista2[i]])
def crearlista(file):
    nombrealum=[]
    legajoalum=[]
    notasalum=[]
    try:
        with open(file,'r',encoding='utf8') as archivo:
            lector=csv.reader(archivo)
            for line in lector:
                print(line)
                nombrealum.append(line[0])
                legajoalum.append(line[1])
                notasalum.append(line[2])
        
            return nombrealum,legajoalum,notasalum

    except FileNotFoundError:
        print("El archivo no existe o no esta ubicado donde lo estas buscando")


def escribirarchivo(file,listanombres,listalegajos,listanotas):
    with open(file,'w',newline='',encoding='utf8') as archivo:
        escritor=csv.writer(archivo)
        for i in range(len(listanombres)):
            escritor.writerow([listanombres[i],listalegajos[i],listanotas[i]])
    archivo.close()
    
def escribir_archivo_usuarios(file,lista_usuarios,lista_contraseñas,lista_roles): # Archivo CSV:Sobreescribe todo devuelta, poniendo tiulos y datos de las listas en orden.##Se recomienda usar este.        
    with open(file,'w',newline='',encoding='utf8') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["USUARIO", "CONTRASEÑA", "ROL"])
        for i in range(len(lista_usuarios)):
            escritor.writerow([lista_usuarios[i],lista_contraseñas[i],lista_roles[i]])

###Mas ejemplos

def leer_archivo_tiempos(archivo, encabezado=True):
    tiempo_carrera = []
    nombre_corredor = []
    pais_origen = []
    numero_identificacion = []
    posicion_llegada = []
    tipo_carrera = []
    ciudad_carrera = []
    with open(archivo, "r", newline="" ,encoding="utf-8" ) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if encabezado:
                encabezado = False
            else:
                tiempo_carrera.append(row[0])
                nombre_corredor.append(row[1])
                pais_origen.append(row[2])
                numero_identificacion.append(row[3])
                posicion_llegada.append(row[4])
                tipo_carrera.append(row[5])
                ciudad_carrera.append(row[6])
    return (tiempo_carrera,nombre_corredor,pais_origen,numero_identificacion,posicion_llegada,tipo_carrera,
            ciudad_carrera)
    # Devuelve todas las listas. Las posiciones de cada lista estan "relacionadas"

# Ordeno las listas en base a los tiempos, de MENOR a MAYOR.
def ordenar_tiempos(tiempo_carrera,nombre_corredor,pais_origen,numero_identificacion,posicion_llegada,tipo_carrera,
                    ciudad_carrera):
    for i in range(len(tiempo_carrera)):
        for j in range(i+1,len(tiempo_carrera)):
            if tiempo_carrera[i] > tiempo_carrera[j]:
                
                tiempo_carrera[i],tiempo_carrera[j]  = tiempo_carrera[j],tiempo_carrera[i]
                nombre_corredor[i], nombre_corredor[j] = nombre_corredor[j], nombre_corredor[i]
                pais_origen[i], pais_origen[j] = pais_origen[j], pais_origen[i]
                numero_identificacion[i] , numero_identificacion[j] = numero_identificacion[j] , numero_identificacion[i]
                posicion_llegada[i], posicion_llegada[j] = posicion_llegada[j], posicion_llegada[i]
                tipo_carrera[i], tipo_carrera[j] = tipo_carrera[j], tipo_carrera[i]
                ciudad_carrera[i], ciudad_carrera[j] = ciudad_carrera[j], ciudad_carrera[i]

    # return (tiempo_carrera,nombre_corredor,pais_origen,numero_identificacion,posicion_llegada,tipo_carrera,
    #         ciudad_carrera)     
    # no devuelve nada, solo modifica las listas. No devuelve nada!...puedo hacer que devuelva con el return