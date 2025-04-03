#clases de composicion y clases de agragacion
#clases de herencia. Nos tenemos que preguntar:¿Esta clase es esta otra clase?
#Usando los ejemplos de Ninfa:
# Clases: estudiante() y clase()
#Una clase tiene estudiante. Ahora bien una clase ES un estudiante? NO. Entonces no hay herencia

#Clases: persona() y estudiante()
#Una persona es una estudiante? Si. Entonces hay herencia.

#La herencia sirve para reusar contenido. Ahora bien siempre que halla una clase dentro de otra
#clase esto no quiere decir que halla herencia. Puede ser una clase de composicion o agregacion.
#Notar que una forma facil de distinguir esto es haciendonos la pregunta:
#¿Es esta clase x() una y()?, siendo y() la clase padre.

# si yo pusiese print(estudiante.__bases__)
#me deveria devolver persona.
#Ahora bien si yo pongo print(persona.__bases__)
#me va a devolver object. Obs. Object es la clase padre de todas las clases.

#Ejemplo:
#Creo el padre
#Obs. Para la creacion de la clase padre debemos tener cuidado que los atributos
#que creemos en este deben cumplirse en todas la clases hijas. 
# Es decir deben ser caracteristicas comunes(que existen) en todos los objetos.
# Es decir que las caracteristicas que pedimos en la clase padre deben tenerlas
# TODAS las clases hijas.

class Animal():
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #metodo generico permitira implementacion particular
    def hablar(self):
        #metodo vacio
        pass

    def quesoy(self):
        print("Soy un animal del tipo",Animal.especie, "y tengo",Animal.edad, "años.")

#Creo la hija

class Gato(Animal):
    def __init__(self,especie,edad,raza):
        super().__init__(especie, edad)
        self.raza = raza

    def hablar(self):
        print("Miau")

lena = Gato('Mamifero',1,'siames')
print('Lena es un animal?',Gato.__bases__)
print(f'Lena es un animal de especie {lena.especie}')
print('Lena es un animal de raza {}'.format(lena.raza))

print('Lena habla?...')
print(lena.hablar())
print(Gato.mro())
######
#Ahora bien tenemos 3 tipos de Herencias:
#1. Herencia Simple: En esta tenemos una clase base(clase padre)
# y una o mas clases derivadas (clases hijas).
#Un ejemplo seria tengo la clase Animal y por debajo (como clases hijas)
#las clases Gato y Perro

#2. Herencia Multiple: En esta tenemos una o mas clases bases ( clases padres)
#y una clase derivada (clase hija). En estos casos tenemos que marcar a que clase
#debe peretencer nuestra clase hija. Si no por default ira a la primera qeu hallamos creado.
#EJ: Tengo la clase base 1 y las clase base 2. Y tengo 1 clase derivada que es
#clase hija de ambas clases bases.

#3. Herencia Multinivel: En esta tenemos una clase base que tiene una clase derivada,
# que a su vez es clase de base de otra clase derivada, y asi sucesibamente....
# Ejemplo:
# clase objeto---->clase A ----> clase B ----> clase C ....y asi sigue
# Notar que la clase objeto es padre de la clase A de la Clase B y de la clase C.
# Y notar que la clase B es hija de la clase A (que a su vez es hija de la clase objeto) y es 
# padre de la clase C.




#Obs. Los atributos de las clases Padrs se heredan en las clase hijas esten definidos en el __init__ o no. EJ:
class vehiculo:
    def __init__(self, patente):
        self.combustible=0
        self.patente=patente
class auto(vehiculo):
    def __init__(self, patente):
        super().__init__(patente)
    def cargar_combustible(self, litros):
        self.combustible += litros

auto1=auto('abc123')
auto2=auto('def456')
auto1.cargar_combustible(3)
print(auto1.combustible)
print(auto2.combustible)


#EJEMPLO HERENCIA MULTIPLE:
class Humano():
    def __init__(self, especie):
        self.especie = especie
    
    def __str__(self):
        return f'Soy un animal de la especie: {self.especie}'
    
    def hablar(self):
        pass

class Marciano():
    def __init__(self,PLANETA):
        self.planeta = PLANETA
    def __str__(self):
        return f'Vango del planeta: {self.planeta}'
    
class Pedro(Humano,Marciano):
    def __init__(self,especie,direc,PLANETA):
        Humano.__init__(self,especie)
        Marciano.__init__(self,PLANETA)
        self.nombre = 'Pedro'
        self.apellido = 'Gutierrez Zaldivar'
        self.edad = 19
        self.direccion = direc
    def __str__(self) -> str:
        return f'Mi nombre es {self.nombre} {self.apellido} y mi edad es {self.edad} años'

    def hablar(self):
        return 'Hola, soy Pedro'
    def cambiar_direccion(self,nueva_direccion):
        self.direccion = nueva_direccion
    
    def __eq__(self,other):
        if not isinstance(other,Pedro):
            return False
        else:
            return self.nombre == other.nombre and self.apellido == other.apellido and self.direccion==other.direccion
        
pedro = Pedro('Humano','Av.Santa Fe 955','SATURNO')
print(Pedro.hablar(pedro)) # == print(pedro.hablar)
print(Pedro.__bases__,Humano.__bases__)
print(Pedro.mro())
print(pedro)

juan = Pedro('Humano','Av.Santa Fe955','Jupiter')
alfredo = Pedro('H','La plata', 'Planeta Tierra')
peter = pedro
print(pedro)
print(juan)
print(alfredo)
print(peter)
print(pedro == alfredo)
print(pedro==juan)
pedro.cambiar_direccion('Alamedaslin')
print(peter.direccion)
print(peter == pedro)