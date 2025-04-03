#ABRIR UN ARCHIVO EXISTENTE EN MI MAQUINA
import traceback
from io import UnsupportedOperation


def existe(patharchivo):
    try:
        archivo=open(patharchivo,'w')
        archivo.write("Hola como estas")
        return archivo
    except FileNotFoundError:
        traceback.print_exc()
        return None
    except UnsupportedOperation:
        print("El archivo esta tratando de realizar una tarea no permitida")
    

if __name__=="__main__":
    patharchivo=r"C:\Users\ninfa\OneDrive\Documentos\Cuatrimestre 1 2022\Materia 71.45 Estructuras\Ejemplos_EstructurasDatos\matriz.txt"
    manejararchivo=existe(patharchivo)
    if manejararchivo!= None:
        print("Archivo Existe")
        for linea in manejararchivo:
            print(linea)
    else:
        print("El archivo no existe")
        