import csv
from io import FileIO

from biblioteca import Biblioteca


class Exportador:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def exportar(self, lista):
        try:
            with open(self.nombre_archivo, "w") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(lista)
        except IOError:
            print("Error al exportar archivo")
            raise FileIO

class ExportadorBiblioteca(Exportador):
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)

    def exportar(self, biblioteca: Biblioteca):
        datos = []
        for libro in biblioteca.get_estanteria():
            atributos = ["titulo", "autor", "editorial"]
            if len(datos) == 0:
                # Agrego el encabezado primero
                datos.append(atributos)
            datos.append([libro.titulo, libro.autor, libro.editorial])
        if len(datos) > 1:
            try:
                # Uso la funcion exportar de la superclase
                super().exportar(datos)
            except Exception as e:
                if isinstance(e, FileIO):
                    print("Error al exportar Biblioteca")
                elif isinstance(e, FileNotFoundError):
                    print("Archivo no encontrado")
                else:
                    print("Error desconocido")
        else:
            print("No hay datos que exportar")
