###ARCHVIOS###
import csv
#Notacion: "r": Read, lee el archivo, sirve para sacar info.
#          "w": Write, sobreescrribe el archivo. 
#          "a": Append, agrega en el archivo al final.
#Archivos txt
def crear_archivo_txt(nombre, parrafo_a_agregar): #Crea 'archivo.txt'.
    with open(nombre,"w", encoding="utf-8") as archivo:
        archivo.write(parrafo_a_agregar +'\n') #En este caso seria el encabezado (El 'parrafo_a_agregar').
    return 

def agregar_info_a_archivo_txt(nombre, parrafo_a_agregar):#Agrega informacion a un 'archivo.txt' existente.
    with open(nombre,"a", encoding="utf-8") as archivo:
        archivo.write(parrafo_a_agregar +'\n') #Notar el '\n' para que no se escriba todo en un renglon
    return

def escribirarchivo(file,lista1,lista2):#Y para agregar listas a un 'archivo.txt'....
    archivo=open(file,'w')
    for i in range(len(lista1)):
        archivo.write(lista1[i] + ',' + lista2[i] + '\n')
    archivo.close()

#Archivos csv
def crear_archivo(lista1,lista2): #Crea 'archivos.csv' y les agrea info de lista 1 y lista 2. Notar que podrian ser dos funciones separadas.
    with open('Archivo', "w", newline="" ,encoding="utf-8") as archivo_nuevo :
            escritor = csv.writer(archivo_nuevo)
            escritor.writerow(['Info Lista1','Info Lista2'])
    
    with open('Archivo', "a", newline="" ,encoding="utf-8") as file :
        escritor = csv.writer(file)
        for i in range(len(lista1)):
            escritor.writerow([lista1[i], lista2[i]])
    return 

def crear_listas_archivo_csv(nombre_archivo): #Ahora lo que hacemos es leemos linea por linea la informacion de
    lista1 = []                       # nuestro 'archivo.csv' y agregamos la informacion a listas...
    lista2 = []
    lista3 = []
    encabezado = True
    with open(nombre_archivo, "r", newline="" ,encoding="utf-8" ) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for col in reader:
            if encabezado:
                encabezado = False
            else:
                lista1.append(col[0])
                lista2.append(col[1])
                lista3.append(col[2])            
    return lista1,lista2,lista3
