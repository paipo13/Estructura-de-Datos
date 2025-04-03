import csv

class Animal:
    # El animal tiene un nombre, comienza teniendo hambre y por lo tanto no puede producir
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = True
        self.producciones_restantes = 0

    # Método: El animal debe aceptar ser alimentado solo cuando tiene hambre, es decir cuando ya no puede producir.
    def alimentar(self):
        if self.hambre:
            self.hambre = False
            print(f"{self.nombre} dice: gracias por alimentarme!")
            self.producciones_restantes = self.veces_produce
        else:
            print("No tengo hambre, gracias!") 

    # Método: Muesta información del animal: su clase, nombre, si tiene hambre y cuántas veces más puede producir
    def __str__(self):
        return f"{self.tipo} - {self.nombre}, Hambre: {'Sí' if self.hambre else 'No'}. Restantes: {self.producciones_restantes}"


    # METODO: Un animal puede producir cuando no tiene hambre. Devuelve las unidades que produce, de lo contrario devuelve 0 unidades.
    def producir(self):
        pass

    # Método: Es llamado por el método  de la clase GranjaAurelio para obtener las unidades que requiere este animal. Si no tiene hambre devuelve 0.
    def calcular_alimento_necesario(self):
        return self.uni_consumo if self.hambre else 0


class Vaca(Animal):

    # La información de los atributos de clase provienen del archivo
    uni_produce = None
    uni_consumo = None
    veces_produce = None
    tipo = "vaca"

    def __init__(self, nombre):
        super().__init__(nombre)


    # Método que sobreescribe al método de la clase Animal.
    # Devuelve dos datos: El tipo de producto que da el animal y la cantidad producida
    # Si no puede producir, devuelve None como tipo y 0 como cantidad.
    def producir(self):
        produccion = super().producir()
        if produccion > 0:
            return "Leche", produccion
        else:
            return None, 0


class Gallina(Animal):

    uni_produce = None
    uni_consumo = None
    veces_produce = None
    tipo = "gallina"

    def __init__(self, nombre):
        super().__init__(nombre)

    def producir(self):
        produccion = super().producir()
        if produccion > 0:
            return "Huevo", produccion
        else:
            return None, 0


class GranjaAurelio:

    #Lista de animales permitidos en la Granja de Don Aurelio (son clases)
    claseAnimales = [Gallina, Vaca] 


    # Método constructor:
    # Atributos:
    # animales: lista de animales que se agregan a la granja
    # stock_consumo: Stock con el que cuenta la granja para alimentar los animales
    def __init__(self, data):
        self.animales = []
        self.stock_consumo = 0
        self.set_default(data)


    # METODO: Adquiere las n unidades de consumo deseadas.
    # Debe mostrar un mensaje acorde al resultado de su ejecución.
    def adquirir_unidades_consumo(self, n):
        self.stock_consumo += n
        print(f"Se han adquirido {n} unidades. El stock actual es {self.stock_consumo}.")


    # METODO: Agrega el animal a la granja.
    # Debe verificar si es un animal de Granja (de claseAnimales).
    # De no ser posible informarlo y devolver False.
    def agregar_animal(self, animal):
        pass


    # MÉTODO: inicializa los atributos de clase de los distintos animales a partir de la información del archivo.
    def set_default(self, datos):
        for datoAnimal in datos:
            for animal in GranjaAurelio.claseAnimales:
                if datoAnimal[0] == animal.tipo:
                    animal.veces_produce = int(datoAnimal[1])
                    animal.uni_consumo = int(datoAnimal[2])
                    animal.uni_produce = int(datoAnimal[3])
                    break


    # METODO: Recibe el nombre del animal.
    # De no ser posible la acción debe devolver False.
    # Debe mostrar un mensaje acorde al resultado de su ejecución.
    def alimentar_animal(self, nombre_animal):
        pass


    # METODO: Todos los animales intentan una producción.
    # Devuelve una lista con los productos recolectados y sus cantidades.
    # Ejemplo [["Leche", 10], ["Huevo", 2]]
    def recolectar_productos(self):
        pass


    # Método: Muestra la información de todos los animales de la granja.
    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)


    # METODO: Devuelve el stock requerido para alimentar a todos los animales hambrientos.
    # Son las unidades de consumo que deberán comprarse luego para alimentar a todos los animales.
    def calcular_stock_reposicion(self):
        pass


# Función para lectura del archivo csv
def leer_datos(archivo):
    try:
        file = open(archivo, 'r')
        reader = csv.reader(file)
    except FileNotFoundError:
        print("Error de lectura")
        return
    else:
        lista = []
        next(reader)
        for line in reader:
            lista.append(line)
    return lista

########################################################
# Código principal (main) para ejecutar el programa.
# Se provee el archivo "pruebas.txt" para guiarlo en lo que debe mostrar el programa.

archivo_datos = "datosGranja.csv"
# Crear granja
datos_animales = leer_datos(archivo_datos)
granja = GranjaAurelio(datos_animales)

# Agregar 4 animales
granja.agregar_animal(Vaca("Aurora"))
granja.agregar_animal(Gallina("Lolita"))
granja.agregar_animal(Vaca("Lecherita"))
granja.agregar_animal(Gallina("Plumona"))

# Mostrar animales
print("Animales en la granja:")
granja.mostrar_animales()

# Intentamos alimentar  a Lolita pero no tenemos stock de consumo
granja.alimentar_animal("Lolita")

# Entonces calculamos el alimento total que necesitamos reponer.
n = granja.calcular_stock_reposicion()
# Compramos las unidades de alimento necesarias que calculamos.
granja.adquirir_unidades_consumo(n)

# Ahora intentamos alimentar a nuestros animales
granja.alimentar_animal("Lecherita")
granja.alimentar_animal("Plumona")
granja.alimentar_animal("Lolita")
granja.alimentar_animal("Plumona") 
# Ops! Confundí el nombre, Aurora tendrá hambre y no podrá producir!

# Mostramos nuevamente los animales
print("Animales en la granja:")
granja.mostrar_animales()

# Recolectamos los productos
print("\nPrimera recolección de productos:")
granja.recolectar_productos()

# Segunda recolección de productos
print("\nSegunda recolección de productos:")
granja.recolectar_productos()

# Mostrar animales después de producir dos veces
print("\nAnimales después de producir dos veces:")
granja.mostrar_animales()

# Intentar recoger productos una tercera vez
print("\nTercera recolección de productos:")
granja.recolectar_productos()
granja.recolectar_productos()

# Alimentar animales y recoger productos de nuevo
print("\nAlimentar animales y recoger productos de nuevo:")
granja.alimentar_animal("Plumona")
granja.alimentar_animal("Lolita")
granja.alimentar_animal("Lecherita")
n = granja.calcular_stock_reposicion()
granja.adquirir_unidades_consumo(n)
granja.alimentar_animal("Aurora")
granja.recolectar_productos()
granja.recolectar_productos()
