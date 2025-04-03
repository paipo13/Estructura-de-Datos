#EJERCICIO BIBLIOTECA
import csv
def crear_archvio_con_ambas_listas(nombre_archivo,lista_autores,lista_libros,lista_año,titulos):
    try:
        with open(nombre_archivo,"w", newline="" ,encoding="utf-8") as file :
            escritor = csv.writer(file)
            escritor.writerow(titulos)
            for i in range(len(lista_libros)):
                escritor.writerow([lista_autores[i],lista_libros[i],lista_año[i]])
    except Exception as e:
        return f'Error {e}'
    else:
        return f'Archivo {nombre_archivo} creado con éxito.'
def crear_nuevas_lineas(nombre_archivo):
    cant = input('¿Cuantas lineas desea agregar?: ')
    if int(cant) >= 1:
        try: 
            with open(nombre_archivo, 'a',newline="",encoding="utf-8")as archivo:
                escritor = csv.writer(archivo)
                # while cant =! 0:
                for i in range(int(cant)):
                    autores = input(f'Ingrese el autor {i+1}: ')
                    libros = input(f'Ingrese el libro {i+1}: ')
                    años = input(f'Ingrese el año {i+1}: ')
                    escritor.writerow([autores,libros,años])
        except Exception as e:
            return f'Error {e}'
        else:
            return f'Archivo {nombre_archivo} modificado con éxito.'    

def buscar_titulos_en_base_a_años(nombre_archivo,año_menor,año_mayor):
    try:
        encabezado = True
        with open(nombre_archivo, 'r', newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            resultado = []
            for fila in lector:
                if encabezado:
                    encabezado = False
                elif int(fila[2]) >= año_menor and int(fila[2]) <= año_mayor:
                    resultado.append(fila)
            return resultado
    except Exception as e:
        return f'Error {e}'

autores = ['PGZ','Pedro GZ','marcelo palitos','juan perez','pepe sanches']
libros = ['Hola mundo','La reina batata','paz y gloria','Hacha','Samuraista']
años = [2017,2008,2005,2002,2006]

crear_archvio_con_ambas_listas('biblioteca.csv',autores,libros, años, ['Autores','Libros','Años'])
crear_nuevas_lineas('biblioteca.csv')
lista = buscar_titulos_en_base_a_años('biblioteca.csv',2004,2020)
print(lista)