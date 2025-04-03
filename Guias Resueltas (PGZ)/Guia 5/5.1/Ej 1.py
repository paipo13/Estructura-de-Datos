###EJERCICIO 1###
# Siguiendo el ejercicio de Camión hecho en la actividad anterior, 
# deseamos crear nuevas clases reutilizando la mayor cantidad de código posible

        
# A. Crear la clase Auto, la cual es muy similar al camión, con la diferencia que no tiene carga y que tiene 4 ruedas
# (asumimos que los camiones tienen 8). Recuerde que la restricción de unicidad de patentes debe correr tanto para autos
# y camiones en simultáneo (es decir, no puede haber un auto y un camión con la misma patente).
# Ambos tienen un atributo posicionInicial que comienza en cero al crearse el objeto.
class Transportes():
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def trasladarse(self, desplazamiento):
        pass

    def __str__(self):
        return f'Hola, soy un transporte del anio: {self.anio} y mi marca es {self.marca}.'

class TransportesTerrestres(Transportes):
    lista_patente = []
    lista_TransportesTerrestres = []
    def __init__(self, marca, anio, patente):
        Transportes.__init__(self,marca,anio)
        self.patente = patente
        if patente in TransportesTerrestres.lista_patente:
            raise ValueError("La patente ya existe")
        TransportesTerrestres.lista_patente.append(patente)
        TransportesTerrestres.lista_TransportesTerrestres.append(self)
    def trasladarse(self, desplazamiento):
        pass
    def __str__(self):
        return f'Hola soy un TransportesTerrestres y mi patente es unica. La mia es: {self.patente}'
    
class Camion(TransportesTerrestres):
    def __init__(self, marca, anio, patente, carga):
        TransportesTerrestres.__init__(self, marca, anio, patente)
        self.carga = carga
        self.ruedas = 8
        self.posicionInicial = 0
    
    def __str__(self):
        return f'Hola soy un camion tengo {self.ruedas} y mi carga es:{self.carga}.'
    
    def trasladarse(self,desplazamiento):
        self.posicionInicial += desplazamiento
        return f'Me trasladé por tierra a la posición {self.posicionInicial}'
    
class Auto(TransportesTerrestres):
    def __init__(self,marca,anio,patente,fila_de_asientos):
        TransportesTerrestres.__init__(self,marca,anio,patente)
        self.fila_de_asientos = fila_de_asientos
        self.ruedas = 4
        self.posicionInicial = 0
    
    def __str__(self):
        return f'Hola soy un Auto tengo {self.ruedas} y {self.fila_de_asientos} filas de asientos'
    
    def trasladarse(self,desplazamiento):
        self.posicionInicial += desplazamiento
        return f'Me trasladé por tierra a la posición {self.posicionInicial}'
    

# B. Ambas clases deben implementar el método trasladarse, el cual recibe un desplazamiento (int), actualiza la posición 
# inicial sumándole el desplazamiento y retorna un mensaje diciendo “Me trasladé a la posición xx”.



# C. Luego, incluir una clase Lancha, la cual también puede desplazarse y se inicia con la posición inicial en cero.
# Tiene marca, año y marca de motor pero no tiene ruedas ni carga. Las lanchas tienen sus propias patentes por lo que
# no debe correr la restricción de camiones y autos. Por otra parte, cuando se traslada debe retornar el
# mensaje “Me trasladé por agua a la posición xx”. A su vez, los otros vehículos deben retornar el mensaje 
# “Me trasladé por tierra a la posición xx”.

class TransportesMarinos(Transportes):
    lista_patentes_marinas = []
    lista_TransportesMarinos = []
    def __init__(self,marca,anio,patente):
        Transportes.__init__(self,marca,anio)
        self.patente = patente
        if self.patente in TransportesMarinos.lista_patentes_marinas:
            raise ValueError("La patente ya existe")
        TransportesMarinos.lista_patentes_marinas.append(patente)
        TransportesMarinos.lista_TransportesMarinos.append(self)
    
    def __str__(self):
        return f'Hola soy un Transporte Marino de patente unica en el mar. Y la misma es: {self.patente}'
    
    def trasladarse(self, desplazamiento):
        pass

class Lancha(TransportesMarinos):
    def __init__(self, marca, anio, patente,color):
        TransportesMarinos.__init__(self,marca,anio,patente)
        self.color = color
        self.posicionInicial = 0
    def __str__(self):
        return f'Hola soy una Lancha de color {self.color}'
    
    def trasladarse(self, desplazamiento):
        self.posicionInicial += desplazamiento
        return f'Me trasladé por agua (a motor) a la posición {self.posicionInicial}'

# D. Además, se debe crear una clase Velero, la cual también se desplaza por agua pero a diferencia de la lancha, 
# tiene cierta cantidad de velas, en vez de tener un motor. Su mensaje debe ser “Me trasladé por agua (a vela) a la
# posición xx”, mientras que el de la lancha debe ser “Me trasladé por agua (a motor) a la posición xx”.

class Velero(TransportesMarinos):
    def __init__(self, marca, anio, patente, cantidad_velas):
        TransportesMarinos.__init__(self,marca,anio,patente)
        self.cantidad_velas = cantidad_velas
        self.posicionInicial = 0

    def __str__(self):
        return f'Hola soy un Velero con {self.cantidad_velas} velas'
    
    def trasladarse(self, desplazamiento):
        self.posicionInicial += desplazamiento
        return f'Me trasladé por agua (a vela) a la posición {self.posicionInicial}'

# E. Crear una clase Anfibio. Es un vehículo que puede transportarse tanto por tierra como por agua (a motor).
# En caso que se le pida trasladarse, por defecto lo debe hacer por tierra.
# Se debe crear otra función para trasladarse por agua.

class Anfibio(TransportesTerrestres,TransportesMarinos):
    lista_patentes_marinas = TransportesMarinos.lista_patentes_marinas 
    lista_patentes_terrestres = TransportesTerrestres.lista_patente
    def __init__(self, marca, anio, patente, modelo,velas):
        TransportesTerrestres.__init__(self, marca, anio, patente)
        TransportesMarinos.__init__(self, marca, anio,patente)
        self.modelo = modelo
        self.posicionInicial = 0
        self.cant_velas = velas
    def __str__(self):
        return f'Hola soy un Anfibio de modelo {self.modelo}'
    
    def trasladarse(self, desplazamiento):
        self.posicionInicial += desplazamiento
        return f'Me trasladé por tierra a la posición {self.posicionInicial}'
    
    def trasladarse_por_agua(self, desplazamiento):
        if self.cant_velas == 0:
            self.posicionInicial += desplazamiento
            return f'Me trasladé por agua (a motor) a la posición {self.posicionInicial}'
        else:
            self.posicionInicial += desplazamiento
            return f'Me trasladé por agua (a vela) a la posición {self.posicionInicial}'

# F. Crear un diccionario para almacenar instancias de Auto y Camión, utilizando sus patentes como claves.
# Asegúrese de que, al intentar agregar un nuevo vehículo, se verifique que la patente no exista ya en el diccionario.
# Si existe, debe retornar un mensaje indicando que la patente ya está en uso.

def crear_diccionario():
    lista_patentes_Autos_y_Camion = TransportesTerrestres.lista_patente
    lista_objetos_Autos_y_Camion = TransportesTerrestres.lista_TransportesTerrestres
    diccionario = {}
    for clave in lista_patentes_Autos_y_Camion:
        if clave not in diccionario:
            diccionario[clave] = lista_objetos_Autos_y_Camion[lista_patentes_Autos_y_Camion.index(clave)]
        else:
            return f'La patente {clave} ya está en uso'
    return diccionario

auto1 = Auto('Audi',1985,'AAA 000',3)

auto2 = Auto('Ford',1990,'BBB 111',5)

camion1 = Camion('Mercedes',2000,'CCC 222','maiz')

camion2 = Camion('Volvo',2010,'DDD 333','soja')

diccionario_vehiculos = crear_diccionario()

print(diccionario_vehiculos)

print(auto1.trasladarse(100))

print(auto2.trasladarse(200))

print(camion1.trasladarse(300))

print(auto1.trasladarse(-50))