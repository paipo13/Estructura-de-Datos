### EJERCICIO 1 ###
# Crear de Clase Camión usando Lista Enlazada
#  Implementar en la clase ‘Camion’ el manejo de la flota de camiones usando la estructura lista enlazada simple.
class Camion():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return f'Almaceno {self.dato}'
    
class ListaEnlazada():
    def __init__(self):
        self.primero = None
    
    def esVacia(self):
        return self.primero == None
    
    def agregar_camion_inicio(self, nodo: Camion):
        if self.esVacia():
            self.primero=nodo
        else: #Para agregar el nodo al inicio (a la primera posicion)
            nodo.siguiente=self.primero
            self.primero=nodo
    
    def agregar_camion_final(self, nodo: Camion):
        if self.esVacia():
            self.primero=nodo
        else:
            aux=self.primero
            while aux.siguiente is not None:
                aux=aux.siguiente
            aux.siguiente=nodo

    def pop(self):
        if self.esVacia():
            return 'No se puede eliminar el primer dato'
        else:
            dato=self.primero.dato
            self.inicio=self.primero.siguiente
            return f'se elimino {dato}'
    
    def __str__(self):
        cadena=''
        aux=self.primero
        while aux != None:
            cadena += str(aux.dato) + ' ; '
            aux = aux.siguiente
        return cadena 
    
if __name__ == '__main__':
    lista_camiones = ListaEnlazada()
    camion1 = Camion('123 AAA')
    camion2 = Camion('456 BBB')
    camion3 = Camion('789 CCC')
    lista_camiones.agregar_camion_inicio(camion3)
    lista_camiones.agregar_camion_inicio(camion2)
    lista_camiones.agregar_camion_final(camion1)
    print(lista_camiones)
    print(lista_camiones.pop())
    print(lista_camiones)

# Parte 1: Clases "Camion y Listas Enlazadas Simple"
# - Hacer uso de  la clases ya implementadas en Camion y listas enlazadas para modificar la forma de almacenamiento
# de la información en la clase Camion, es decir en lugar de usar listas secuencias debe usar listas enlazadas simple



# Parte 2: Administración Avanzada de Camiones
# Expandir las funcionalidades de la clase `ListaEnlazada` para incluir funcionalidades de administración avanzadas
# de la flota de camiones.

# A- Implementar métodos en `ListaEnlazada` para actualizar el estado de un camión (por ejemplo, de disponible a en viaje).
# B- Añadir un método para calcular la carga total transportada por todos los camiones en un estado específico
# (por ejemplo, todos los camiones en viaje).
# C- Crear un método para encontrar camiones por modelo y estado, y listar sus detalles.



# Parte 3: Gestión de Mantenimiento
# Implementar un sistema de gestión de mantenimiento para los camiones utilizando la lista enlazada..

# A- Añadir un atributo `fechaUltimoMantenimiento` a la clase `Camion`.
# B- Implementar un método en `ListaEnlazada` para listar camiones que requieren mantenimiento 
# (por ejemplo, aquellos que no han tenido mantenimiento en los últimos 6 meses).
# C- Crear un método para actualizar la fecha de último mantenimiento de un camión.




# Parte 4:Optimización de Rutas
# Desarrollar un algoritmo de optimización de rutas que asigna camiones a rutas basándose en su carga máxima y estado.

# A- Implementar una clase `Ruta` con atributos como idRuta, destino, distancia, y cargaRequerida.
# B- Añadir un método en ListaEnlazada para asignar camiones disponibles a rutas basándose en su capacidad y asegurando
# que la carga no exceda la carga máxima del camión, buscando desperdiciar la menor cantidad de carga libre.
# La idea sería asignar a.



# Parte 5: Análisis y Reporte de Flota
# Generar análisis y reportes detallados sobre la flota utilizando las listas enlazadas.

# A- Implementar un método en ListaEnlazada para calcular, mostrar  las estadísticas de la flota: Porcentaje de 
# camiones según su estado.
# B- Crear un método para identificar y visualizar los camiones más utilizados 
# (basado en el número de viajes completados).
