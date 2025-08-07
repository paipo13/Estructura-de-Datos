#   Una pila es una estructura de datos abstracta que sigue el principio de el ultimo
# adentro y el primero afuera. Este principioi establece qu el ultimo elemento que se agrega
# a la pila es el primero en ser eliminado. 

# Obs. Vamos a tenes funciones especiales para el uso de las pilas.
# Obs. Estas funciones/metodos los tendremos que importar de collection, deque

#Ejemplo:
from collections import deque

class Pila():
    def __call__(self):
        self.pila = deque()

    def push(self, elemento):
        self.pila.append(elemento)

    def pop(self):
        if self.is_empty():
            return 'La pila esta vacia'
        else:
            return self.pila.pop()
        
    def esta_vacia_pregunta(self):
        return len(self.pila) == 0
    
    def tamaño(self):
        return len(self.pila)
    
    def peek(self):
        if self.is_empty():
            return 'La pila esta vacia'
        else:
            return self.pila[-1]
        
#Implementacion
# Crear una instancia de la clase Pila
mi_pila = Pila()

# Agregar elementos a la pila
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(3)

# Imprimir la pila
print(list(mi_pila.pila))  # Output: [1, 2, 3]

# Eliminar y devolver el último elemento agregado a la pila
ultimo_elemento = mi_pila.pop()
print(ultimo_elemento)  # Output: 3

# Imprimir la pila después de eliminar el último elemento
print(list(mi_pila.pila))  # Output: [1, 2]

# Comprobar si la pila está vacía
if mi_pila.esta_vacia_pregunta():
    print("La pila está vacía")
else:
    print("La pila no está vacía")  # Output: La pila no está vacía

# Obtener el último elemento agregado a la pila sin eliminarlo
elemento_superior = mi_pila.peek()
print(elemento_superior)  # Output: 2

# Obtener el número de elementos en la pila
tamaño_pila = mi_pila.size()
print(tamaño_pila)  # Output: 2