###  POO = Programacion Orientada a Objetos ###


# 1. CONCEPTO TEORICO
# La Programación Orientada a Objetos (POO) es un paradigma de programación basado en la
# creación de "objetos" que representan entidades del mundo real y que interactúan entre sí. Cada objeto tiene:

# -->   Atributos (datos o características)
# -->   Métodos (funciones que ejecutan acciones sobre los datos)

# En lugar de programar en bloques de código sueltos, la POO permite organizar mejor los programas, 
# promoviendo la reutilización y la escalabilidad del código. Y no solo esto al trbaajar con POOs lo que 
# vamos a lograr es darle una estructura, un cuerpo, a nuestro codigo. De esta forma todo estara mas ordenado
# y funcionara de la mejor manera ahorrandonos escribir cientos de lineas de codigo para lograr el 
# mismo resultado.

# Ejemplo del mundo real: Un auto es un objeto que tiene atributos (marca, modelo, color) y 
# métodos (arrancar, frenar, acelerar).


# 2. PRINCIPIOS FUNDAMENTALES DE LA POO 
# La POO se basa en cuatro pilares fundamentales:

# -->   Encapsulamiento
# Protege los datos dentro de un objeto y solo permite acceder a ellos a través de métodos específicos.
# Ejemplo: No podemos cambiar directamente la velocidad de un auto, sino que usamos el método acelerar().

# -->   Abstracción
# Oculta los detalles internos de la implementación y solo expone lo necesario.
# Ejemplo: Al conducir, solo usamos el volante y los pedales, sin preocuparnos por cómo funciona el motor.

# -->   Herencia
# Permite que una clase (subclase) herede atributos y métodos de otra (superclase), evitando repetir código.
# Ejemplo: Un "AutoDeportivo" hereda de "Auto", pero puede agregar más características.

# -->   Polimorfismo
# Permite que un mismo método tenga diferentes comportamientos según el contexto.
# Ejemplo: Un método hacer_sonido() puede hacer que un perro ladre y un gato maúlle.


# 3. EJEMPLO:
# Definimos una clase Auto
class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} está encendido.")
    
    def apagar(self):
        self.encendido = False
        print(f"El {self.marca} {self.modelo} está apagado.")

# Herencia: la clase AutoDeportivo hereda de Auto
class AutoDeportivo(Auto):
    def __init__(self, marca, modelo, color, turbo):
        super().__init__(marca, modelo, color)
        self.turbo = turbo

    def activar_turbo(self):
        if self.encendido:
            print(f"Turbo activado en el {self.marca} {self.modelo}!")
        else:
            print("El auto debe estar encendido para activar el turbo.")

# Polimorfismo: redefinimos un método en la subclase
class AutoElectrico(Auto):
    def encender(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} eléctrico se encendió en modo silencioso.")

# Creamos instancias de las clases
auto1 = Auto("Toyota", "Corolla", "Rojo")
auto1.encender()

deportivo = AutoDeportivo("Ferrari", "488", "Rojo", True)
deportivo.encender()
deportivo.activar_turbo()

electrico = AutoElectrico("Tesla", "Model S", "Negro")
electrico.encender()
