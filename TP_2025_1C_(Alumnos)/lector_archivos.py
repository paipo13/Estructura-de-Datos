import csv
from conexiones_nodos import *

class Lector():
    """
    esta clase contiene los metodos genericos para leer archivos
    para que la puedan llamar las clases Escenario y Planificador
    """
    @staticmethod
    def leer_csv(archivo):
        contenido = []
        try:
            with open(archivo, 'r', encoding="utf-8") as f:
                reader = csv.reader(f)
                for i in reader:
                    if i: # Por si hay alguna línea vacía
                        contenido.append(i)
                contenido = contenido[1::]
            return contenido
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontro el archivo {archivo}.")
    
    @staticmethod
    def conversion_tipo_conexion(tipo):
        
        if tipo == "Ferroviaria":
            return Ferroviaria
        elif tipo == "Maritima":
            return Maritima
        elif tipo == "Fluvial":
            return Fluvial
        elif tipo == "Aerea":
            return Aerea
        elif tipo == "Automotor":
            return Automotora
        else:
            raise ValueError("Tipo no valido")