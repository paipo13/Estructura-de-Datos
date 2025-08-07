from lector_archivos import *

class Escenario():
    """
    Esta clase forma el escenario de conexiones y nodos (la red de transporte)
    """
    def __init__(self, archivo_nodos, archivo_conexiones):
        # Creamos los nodos
        self.nodos = self.convertir_nodo(archivo_nodos)
        # Con los nodos ya creados creamos las conexiones
        self.conexiones = self.convertir_conexion(archivo_conexiones, self.nodos)
    
    @staticmethod
    def convertir_nodo(archivo):
        """
        lee el archivo de nodos y crea un diccionario con todos los nodos
        """
        nodos = {}
        lista_nodos = Lector.leer_csv(archivo)
        for nodo in lista_nodos:
            # nodo[0] porque lo unico que tiene cada renglon es el nombre, dentro de una lista
            nodos[nodo[0]] = Nodo(nodo[0])
        return nodos
    
    @staticmethod
    def convertir_conexion(archivo, nodos):
        """
        lee el archivo de conexiones y crea la lista de conexiones
        """
        # El matching se hace con el diccionario de nodos que se pasa como parametro
        lista_conexiones = Lector.leer_csv(archivo)
        conexiones = []
        for conexion in lista_conexiones:
            # Se agregan la ida y la vuelta (porque las conexiones son bidireccionales)
            if (conexion[0] not in nodos.keys() or conexion[1] not in nodos.keys()):
                raise ValueError(f"Alguno de los nodos de la conexion {conexion} no es validos.")
            nueva_conexion_1 = Conexion(nodos[conexion[0]],nodos[conexion[1]], Lector.conversion_tipo_conexion(conexion[2]), int(conexion[3]), conexion[4], conexion[5])
            nueva_conexion_2 = Conexion(nodos[conexion[1]], nodos[conexion[0]], Lector.conversion_tipo_conexion(conexion[2]), int(conexion[3]), conexion[4], conexion[5])
            conexiones.append(nueva_conexion_1)
            conexiones.append(nueva_conexion_2)
        return conexiones