#Ahora vamos a hacer un resumen de que son las clases, y porque estan compuestas.
#Tambien clasificaremos las cosas que contine.

#Def: Una clase es una plantilla que contiene los atributos(características) y funcionalidades propias de ellas.

#Obs. Al ser un tipo de dato definido por el ordenador, las clases deben contener todos sus atributos y 
#funciones(metodos) dentro de ella, a la hora de crearla.
#Obs. Una clase permite crear objetos (instanciar) que comparten una estructura y un comportamiento común. Un 
# ejemplo de esto seria crear la clase auto, y yo puedo crear muchos autos (objetos) que van a ser las distintas
#instancias de mi clase. Ej: auto_1, auto_2, auto_3, mi_auto, etc...(todas estos objetos son instancias).

#Ejemplo: ver en Clase4.1.clases.py , la clase seria Auto()

#Obs. Las clases poseen atributos y metodos


#Comienzo de ejemplo 1:
class Auto():                    #crear la clase con letra MAYUS al principio
    vel_max = 200 
    marcas_validas = ['Ford', 'Peugot','Nissan', 'Audi']
    PRESION_GOMAS = 2.5
    def __init__(self, marca:str):
        self._marca = "Audi" 
        self.ruedas = 4 
        self.nafta = 8
    def cargar_nafta(self, cantidad): 
        self.nafta += cantidad
    
    def get_nafta(self):
        return self.nafta
#Fin de ejemplo 1


# #MIEMBROS DE UNA CLASE(Usaremos el ejemplo 1 para explicar):
#     1. ATRIBUTOS:
#                 1.1 Atributo de instancia: Son aquellos atributos que estan definidos con self.(...) = (...).
# Suelen estar dentro de la operacion constructora, es decir, que estan dentro del __init__. Pero tambien pueden estar en otras funciones.
# Su valor varia en la creacion de cada instancia. Esto es porque lo que hace el self es agregar el dato a cada objeto que
# se esta instancianciando en ese momento especifico.
# Ej: "self.nafta = 8"
#                 1.2 Atributo de clase: Son aquellos atributos estan afuera de la operacion constructora. 
# Al estar afuera del __init__ su valor es el mismo inicialmente para todas las instancia. Esto se puede llegar 
# a modificar de ser necesario. 
# Ej: vel_max = 200 
#                 1.3 Atributo constante: Son aquellos atributos que estan afuera de la operacion constructora. 
# Estan completamente escritos en MAYUS, esto significa que no deberia modificarse.
# Ej: PRESION_GOMAS = 2.5

#     2. OPERACIONES:
#                 2.1 Operacion constructora: Es aquella operacion que lleva el def __innit__(self,(...)). 
# Es en ella que se marcara cuales son los atributos de instanicia de cada objeto que salga de la clase.
#                 2.2 Operacion analizadora: Es la operacion que nos permite acceder a los atributos de los objetos
# sin modificarlos. Ej: def get_nafta(self):
                          # return self.nafta
#                 2.3 Operacion modificadora: Tambien llamada "geters" es la operacion que me permitira modificar
# valores de instancias de mi clase sin tener que escribirlo todo de forma manual. Cambian el estado de un objeto.
# Es una funcion (metodo) que nos permite hacer modificaciones. Suelen ser muy utiles y muchas veces
# las creamos sabiendo que se pueden llegar a querer hacer modificaciones. 
# Por lo general sucede cuando tenemos atributos de instancia que tienen a estar variando constantemente.
# Ej: def cargar_nafta(self, cantidad): 
#         self.nafta += cantidad


# TIPOS DE METODOS SEGUN SU ALCANZE (los distintos tipos de funciones que puede tener una clase):
#     1.METODO DE INSTANCIA: Son aquellos metododos que tienen acceso a los atributos de la clase mediante el
# parametro self. Basicamente son las funciones que contienen como parametro self. Modifican instancias.
# Ej: Los ejemplos serian las operaciones constructoras, analizadoras y modificadoras.
#     2.METODO DE CLASE: Son aquellos metodos que operan sobre la clase en si. Operan usando @classmethod y reciben
# el parametro cls. Obs. siempre tienen que tener el 'decorador' @classmethod antes de arrancar.
#                   Ej:   @classmethod
#                         def agregar_marca(cls,nueva_marca:str):
#                             if nueva_marca not in cls.marcas_validas:
#                                 cls.marcas_validas.append(nueva_marca)
#                                 print(f'Se ha agregado la marca {nueva_marca}')
#                             else:
#                                 print(f'La marca {nueva_marca} ya existe en nuestra tienda')

#     3.METODO ESTATICO: Son aquellos metodos que no operan ni sobre una instancia ni sobre una clase. El decorador
# que debe estar si o si antes de codearlo(al metodo) es @staticmethod.
# Ej: @staticmethod
#     def es_valido(valor):
#         return valor > 0




###Excepciones en una clase(ejemplo):
class Circulo:

    validos = 0
    invalidos = 0
    PI=3.1415
    def __init__(self, radio:float):
        if self.radio_valido(radio):
            self.radio = radio
            Circulo.validos += 1
        else:
            Circulo.invalidos +=1
            raise ValueError("Radio no válido")

    @staticmethod
    def radio_valido(radio:float):
        return radio > 0
    
    def areaCirculo(self):
        return Circulo.PI*self.radio**2


try:
    circuloBueno = Circulo(3)
    print(f'El area del circulo es: {circuloBueno.areaCirculo():.2f}')
except ValueError as val:
    print(f"Error en la instancia: {val}")
else:
    print("El circulo fue creado en la aplicación")
finally:    
    print(f"Válidos: {Circulo.validos} - Invalidos: {Circulo.invalidos}")

# try:
#     circuloMalo = Circulo(-1)
# except ValueError as val:
#     print(f"Error en la instancia: {val}")
# else:
#     print("El circulo fue creado en la aplicación")
# finally:    
#     print(f"Válidos: {Circulo.validos} - Invalidos: {Circulo.invalidos}")
