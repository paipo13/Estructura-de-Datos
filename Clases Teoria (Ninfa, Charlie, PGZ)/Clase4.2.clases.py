'''Problematización: Hasta ahora solo podemos crear autos de la marca "audi" 
¿Cómo podríamos hacer para permitir crear diferentes marcas de autos?
Consigna: Validar una instancia usando Raise, y cláusula try except
'''

class Auto():

    vel_max = 200 # Todos los autos que creo van a tener su velocidad máxima restringida
    marcas_validas = ["Audi", "Fiat", "BMW"]

    def __init__(self, marca:str):
        if marca not in Auto.marcas_validas:
            raise ValueError(f"Marca {marca} no Permitida")
        self.marca = marca
        self.modelo = "A1"
        self.ruedas = 4
        self.nafta = 0

    # método de instancia debe llevar el parámetro "self", se refiere al objeto que invoca al método.
    def cargar_nafta(self, cantidad:int):
        if Auto.validar_cantidad_nafta(cantidad):
            self.nafta += cantidad
            print(self.nivel_nafta())
        else:
            raise ValueError("La cantidad de nafta debe ser positiva.")

    def nivel_nafta(self):
        return f'Nivel de nafta es: {self.nafta}'
    
    @staticmethod
    def validar_cantidad_nafta(cantidad: int) -> bool:
        """Verifica si la cantidad de nafta es positiva."""
        return cantidad > 0
    
    @classmethod
    def agregar_marca(cls,nueva_marca:str):
        if nueva_marca not in cls.marcas_validas:
            cls.marcas_validas.append(nueva_marca)
            print(f'Se ha agregado la marca {nueva_marca}')
        else:
            print(f'La marca {nueva_marca} ya existe en nuestra tienda')

    def __eq__(self, other) -> bool:
        """Compara dos objetos Auto por marca y modelo."""
        if not isinstance(other, Auto):
            return False
        return self.marca == other.marca and self.modelo == other.modelo
    
# # Ejemplo con marca correcta y ya existe y nafta ok
# try:
#     auto1 = Auto("Fiat")
#     auto1.agregar_marca('Fiat')
#     auto1.cargar_nafta(10)
#     print(auto1.nivel_nafta())
#     # auto2=Auto("Fiat")
#     # print(auto1==auto2)
# except ValueError as error:
#     print(error)
# else:
#     print(f"Auto de la marca {auto1.marca}")
    


# # Ejemplo con marca correcta y No existe y gas no
try:
    auto1 = Auto("Fiat")
    auto1.agregar_marca('Mazda')
    auto1.cargar_nafta(20)
except ValueError as error:
    print(error)
else:
    print(f"Auto de la marca {auto1.marca}")


# print(Auto.marcas_validas)
# print(auto1.marcas_validas)
# # Ejemplo con marca incorrecta y agregar auto
# try:
#     auto2 = Auto("Ford")
#     auto2.agregar_marca('Fiat')     
# except ValueError as error:
#     print(error)
# else:
#     print(f"Auto de la marca {auto2.marca}")
