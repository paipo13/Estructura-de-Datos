### LISTAS ENLAZADAS CLASE ###

#Array: Es una estructura de datos que almacena una colección de elementos del mismo tipo en una secuencia
# ordenada. Aunque Python no tiene una estructura de datos llamada "array" en su
# núcleo, normalmente se utilizan listas para comportamientos similares a los arrays. 
# Sin embargo, para trabajar con arrays que sean más eficientes en términos de memoria y velocidad, 
# se usa comúnmente el módulo array o bibliotecas como NumPy.

import array

# Crear un array de enteros
arr = array.array('i', [1, 2, 3, 4, 5])
# print(arr)


### Trenes ###
#Las listas enlazadas pueden verse como listas enlazadas con dos clases distintas. Una clase es la locomotora y otra son los Nodos
#, los Nodos serian los vagones. Todos los Nodos tienen dos datos: La informacion que almacena (dato) y la direccion (enlaze) al 
# proximo vagon. Siempre la clase de nodo se crea antes. Luego se crea la clase de la lista enlazada. 
# Luego se instancia la clase nodo. Y luego se instancia la clase lista enlazada. 
# Obs. El ultimo Nodo tiene direccion = NULL. De esta forma se termina el "tren".

# Ejemplo de clase de Nodo

class Nodo():
    def __init__(self,dato:int):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return f'Almaceno {self.dato}'

if __name__ == '__main__':
    #Creamos un Nodo con el valor 5
    nodo1 = Nodo(5)
    print(nodo1)

# Mi clase lista solo va a tener como atributo la direccion del primer nodo
# Obs. cuando arrancamos es mas facil agregar el primer Nodo. Nos fijamos si
# la lista apunta a None y si es True entonces agregamos el Nodo. Pero cuando
# la lista ya esta asignada a un a un nodo.

class Lista():
    def __init__(self,inicio=None):
        self.inicio=inicio

    def esVacia(self):
        return self.inicio==None
    
    def agregarInicio(self,nodo:Nodo):
        if self.esVacia():
            self.inicio=nodo
        else: #Para agregar el nodo al inicio (a la primera posicion)
            nodo.siguiente=self.inicio
            self.inicio=nodo
            
    def agregarFinal(self,nodo:Nodo):
        if self.esVacia():
            self.inicio=nodo
        else:
            aux=self.inicio
            while aux.siguiente!=None:
                aux=aux.siguiente
            aux.siguiente=nodo
    
    def pop(self):
        if self.esVacia():
            return 'No se puede eliminar el primer dato'
        else:
            dato=self.inicio.dato
            self.inicio=self.inicio.siguiente
            return f'se elimino {dato}'
        
    def __str__(self):
        cadena=''
        aux=self.inicio
        while aux!=None:
            cadena+=str(aux.dato)+' '
            aux=aux.siguiente
        return cadena

if __name__ == '__main__':
    listainicial=Lista()
    nodo=Nodo(5)
    print(nodo)
    listainicial.agregarInicio(nodo)
    nodo=Nodo(15)
    listainicial.agregarInicio(nodo)
    nodo=Nodo(125)
    listainicial.agregarFinal(nodo)
    print(listainicial)
    print(listainicial.pop())
    print(listainicial)