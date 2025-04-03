def crear_archivo_txt(nombre, parrafo_a_agregar):
    with open(nombre,"w", encoding="utf-8") as archivo:
        archivo.write(parrafo_a_agregar)
    return # creo un archivo TXT y le agrego el parrafo que quiera.

def leerarchivoreadline(file):
    try:
        archivo=open(file,'r')
        print(archivo)
        data=archivo.readline()
        print(data)
        print(type(data))
        archivo.close()
    except:
        print("El archivo no existe o no esta ubicado donde lo estas buscando")

def split(contenido,separador):
    lista=[]
    cadena=''
    i=0
    while i <len(contenido):
        if contenido[i]!=separador:
            cadena+=contenido[i]
            i+=1
        else:
            lista.append(cadena)
            cadena=''
            i+=1
    if cadena!='':
        lista.append(cadena)
    return lista


# crear listas usando read
def crearlista(file):
    listanomb=[]
    listalegajo=[]
    listanota=[]
    #linea por linea
    try:
        archivo=open(file,'r')
        estudiantes=archivo.read()
        estudiante=split(estudiantes,'\n')
        print(estudiante)
        for i in range(len(estudiante)):
            print(estudiante[i])
            estudiantes=split(estudiante[i],',')
            print(estudiantes)
            listanomb.append(estudiantes[0])
            listalegajo.append(estudiantes[1])
            listanota.append(estudiantes[2])
        archivo.close()
        return listanomb,listalegajo,listanota
    except:
        print("El archivo no existe o no esta ubicado donde lo estas buscando")


def escribirarchivo(file,listanombres,listalegajos,listanotas):
    archivo=open(file,'w')
    for i in range(len(listanombres)):
        archivo.write(listanombres[i]+','+ listalegajos[i]+','+listanotas[i]+'\n')
    archivo.close()