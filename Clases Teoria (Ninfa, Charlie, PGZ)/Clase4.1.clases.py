#CLASE
#Una CLASE es un tipo de dato. Las CLASES son plantillas que me permiten a mi crear un tipo de dato. 
# Tenemos CLASES. Una instancia de una CLASE es un OBJETO. Las CLASES pueden tener ATRIBUTO y METODOS. 
#Obs. Entre las CLASES que ya conosemos se encuentran: Listas, enteros, stings, floats, etc...

# Por ejemplo. Tengo la CLASE auto. ATRIBUTOS de mi clase auto podrian ser: 1.marca 2.patente 3.color 4.nivel_combustible
# Y una instancia especifica de mi CLASE podria ser: mi_auto: 1.ford 2.'376 HUJ' 3.rojo 4. 10
# NOTA: Notar como mi_auto seria el OBJETO ya que es una instancia de mi CLASE.

# Aparte de esto podria agregarle a mi CLASE auto METODO los cuales podrian ser por ejemplo: 1. cargar_combustible(litros)
# Si yo a mi_auto le aplico el METODO cargar_combustible(10).....entonces el ATRIBUTO, en mi_auto, 4. nivel_combustible va a pasar
# a valer 20

# Obs. Una funcion dentro de una clase es lo que llamamos METODO.
# Obs. las clase por convencion arrancan con mayuscula mientras que los objetos con minuscula

# Ejemplo: 
# Consigna: Crear una clase, definir n constructor, definir atribuos. Modificar el valor de un atributo fuera de la calse.

class Auto():                    #crear la clase con mayuscula al principio
    vel_max = 200 #Todos los autos van a tener la misma velocidad maxima, si lo escribimos asi es un ATRIBUTO DE CLASE, los que nosotros llamamos ATRIBUTOS son ATRIBUTOS DE INSTANCIAS
    marcas_validas = ['Ford', 'Peugot','Nissan', 'Audi']
    PRESION_GOMAS = 2.5 #Al ponerlo en MAYUS el atributo es de tipo constante de modo que NO deberian modificarse. Y esta es la diferencia que tiene con los ATRBUTOS de CLASE
    def __init__(self):#se llama a esto METODO CONSTRUCTOR       #def __init__(self,marca:str): 
                                                                                #if marca not in Auto.marcas_validas:
                                                                                    #raise ValueError(f"Marca {marca} no Permitida")
        self._marca = "Audi" #La '_' antes de marca me dice que es un ATRIBUTO privado (es decir que es de los ATRIBUTOS que no quiero modificar, si bien si se puede)
        self.modelo = 'A1'
        self.ruedas = 4 #Todos estos self son ATRIBUTOS de INSTANCIA ya que estan dentro de el __init__
        self.nafta = 8
    def cargar_nafta(self, cantidad): #Estos METODOS se llaman "geters" o METODO MODIFICADOR
        self.nafta += cantidad

    def cargar_nafta_pero_robar_ruedas(self,litros,ruedas_robadas):
        self.nafta += litros -1
        self.ruedas -= ruedas_robadas
        nafta_robada = 1
        return nafta_robada

# Creo una instancia
mi_auto = Auto()
print(mi_auto.nafta)

#Modifico el valor de un atributo (nafta) fuera de la clase
mi_auto.nafta += 10
print(mi_auto.nafta)

#Notar como aunque tenga los mismos valores dos instancias distintas no son iguales. Ej:
auto1 = Auto()
auto2 = Auto()
auto3 = auto1
print(auto1 == auto2)
print(auto1 is auto2)
print(auto1 == auto3)
print(id(auto1))
print(id(auto2))
print(id(auto3))

print(auto1.nafta)
auto3.nafta += 50
print(auto3.nafta) #Notar como si bien uno es auto1 y el otro es auto3 al ser lo mismo (mismo codigo de memoria), toda modificacion que le hagamos a uno se la hacemos al otro sin importar el orden.


#Explicar el concepto 'no se debe modificar el atributo por fuera', Lo que introduce a los metodos de instancia.
# Carlos: "Es una mala practica de phyton modificar los ATRIBUTOS de manera directa. Si no que una buena CLASE nos da los METODOS necesarios 
# para modificar su estado."


#Obs. Metodo de instancia debe llevar el parametro "self", se refiere al objeto que invoca al metodo.

#Creo una instancia
auto5 = Auto()
#cargo nafta a travez del metodo creado:
auto5.cargar_nafta(10)
print(auto5.nafta)

nafta_robada = auto5.cargar_nafta_pero_robar_ruedas(5,1)
print(nafta_robada)
print(auto5.ruedas)


#ATRIBUTO DE CLASE (vel_max)
print(auto1.vel_max)
print(auto2.vel_max)
print(auto3.vel_max)

#Si modifico desda la classe Auto, este cambio impacta en todas las instancias
Auto.vel_max -= 50
print(auto1.vel_max)
print(auto2.vel_max)
print(auto3.vel_max)

#Ahora, si intentamos modificar la vel_max desde alguna instancia...
auto1.vel_max = 100
print(auto1.vel_max)

# Que pasa en auto2? sigue siendo 150
print(auto2.vel_max)

#Y con que valor queda Auto.vel_max? Queda con el que le asignamos en su momento que era = 150
print(Auto.vel_max)


Auto.vel_max -= 20
print(auto1.vel_max > auto2.vel_max)
print(auto1.vel_max)
print(auto2.vel_max)
print(auto3.vel_max)

#SI TOMARAMOS EL CONSTRUCTO QUE ESTA INDENTADO (#), ES DECIR EL QUE PIDE COMO PARAMETROS (self, marca:str), entonces:
# #Ejemplo con marca correcta
# try:
#     auto1 = Auto("Fiat")
# except ValueError as error:
#     print(error)
# else:
#     print(f"Auto de la marca {auto1.marca}")

# # Ejemplo con marca incorrecta
# try:
#     auto2 = Auto("Ford")
# except ValueError as error:
#     print(error)
# else:
#     print(f"Auto de la marca {auto2.marca}")





#CIRCULOS

class Circulo:
    validos = 0
    invalidos = 0

    def __init__(self, radio):
        if self.radio_valido(radio):
            self.radio = radio
            Circulo.validos += 1
        else:
            Circulo.invalidos += 1
            print(f"Radio ({radio})invalido.. no se deberia crear este circulo!")
            #raise ValueError ("radio no valido")
            

    @staticmethod
    def radio_valido(radio):
        return radio > 0
    
CirculoloBueno = Circulo(3)
print(Circulo.validos, Circulo.invalidos)
print(id(CirculoloBueno))

print(Circulo.radio_valido(5))
circulolomalo = Circulo(-1)
print(Circulo.validos, Circulo.invalidos)

# Exepciones y Errores

try: 
    CirculoloBueno = Circulo(3) ##avalua..
except ValueError as val:
    print(f"Error en la instancia: {val}") ## <llega aca si hay arror
else:
    print("Elcirculo fue creado en la aplicacion") ## < llega aca si No hay error
finally:
    print(f"Validos:{Circulo.validos}-invalidos:{Circulo.invalidos}") ## < llega aca indistintamente