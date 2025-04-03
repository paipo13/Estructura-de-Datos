import datetime

class Vehiculo:
    def __init__(self, patente, marca, anio, carga_maxima):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.posicionInicial = 0
        self.estado = "disponible"
        self.carga_maxima = carga_maxima
        self.viajes_completados = 0

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicionInicial += desplazamiento
        return f'Me trasladé a la posición {self.posicionInicial}'

    def __str__(self) -> str:
        return f'Vehículo #{self.patente}\nMarca: {self.marca}\nAño: {self.anio}\nPosición Inicial: {self.posicionInicial}\nEstado: {self.estado}\nCarga Máxima: {self.carga_maxima}\nViajes Completados: {self.viajes_completados}'

class VehiculoTerrestre(Vehiculo):
    def __init__(self, patente, marca, anio, ruedas, carga_maxima):
        super().__init__(patente, marca, anio, carga_maxima)
        self.ruedas = ruedas

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicionInicial += desplazamiento
        return f'Me trasladé por tierra a la posición {self.posicionInicial}'

    def __str__(self) -> str:
        return f'Vehículo Terrestre #{self.patente}\nMarca: {self.marca}\nAño: {self.anio}\nRuedas: {self.ruedas}\nPosición Inicial: {self.posicionInicial}'

class Nodo:
    def __init__(self, camion):
        self.camion = camion
        self.siguiente = None

class FlotaCamiones:
    def __init__(self):
        self.cabeza = None
    
    def agregar_camion_final(self, camion):
        nuevo_nodo = Nodo(camion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def agregar_camion_inicio(self, camion):
        nuevo_nodo = Nodo(Camion)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_camion(self, patente):
        if not self.cabeza:
            return
        
        if self.cabeza.camion.patente == patente:
            self.cabeza = self.cabeza.siguiente
            return
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.camion.patente == patente:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
    
    def buscar_camion(self, patente):
        actual = self.cabeza
        while actual:
            if actual.camion.patente == patente:
                return actual.camion
            actual = actual.siguiente
        return None
    
    def listar_camiones(self):
        camiones = []
        actual = self.cabeza
        while actual:
            camiones.append(str(actual.camion))
            actual = actual.siguiente
        return camiones

class Camion(VehiculoTerrestre):
    def __init__(self, patente, carga_maxima, marca, anio):
        super().__init__(patente, marca, anio, ruedas=8, carga_maxima=carga_maxima)
        self.carga = 0  # Este atributo puede variar dependiendo de las operaciones de carga/descarga

    def __str__(self):
        return f'Camion #{self.patente}\nCarga: {self.carga}\nMarca: {self.marca}\nAño: {self.anio}\nRuedas: {self.ruedas}\nPosición Inicial: {self.posicionInicial}'


# Tester para el programa corregido

def tester():
    # Crear una flota de camiones
    flota = FlotaCamiones()

    # Crear algunos camiones
    camion1 = Camion(patente="ABC123", carga_maxima=10000, marca="Mercedes", anio=2015)
    camion2 = Camion(patente="DEF456", carga_maxima=15000, marca="Volvo", anio=2018)
    camion3 = Camion(patente="GHI789", carga_maxima=12000, marca="Scania", anio=2017)

    # Agregar los camiones a la flota
    flota.agregar_camion(camion1)
    flota.agregar_camion(camion2)
    flota.agregar_camion(camion3)

    # Listar camiones en la flota
    print("Lista de camiones en la flota:")
    print("\n".join(flota.listar_camiones()))
    print("\n---\n")

    # Buscar un camión en la flota por su patente
    print("Buscar camión con patente DEF456:")
    camion_buscado = flota.buscar_camion("DEF456")
    if camion_buscado:
        print(camion_buscado)
    else:
        print("Camión no encontrado.")
    print("\n---\n")

    # Eliminar un camión de la flota
    print("Eliminar camión con patente ABC123:")
    flota.eliminar_camion("ABC123")
    print("Lista actualizada de camiones en la flota:")
    print("\n".join(flota.listar_camiones()))
    print("\n---\n")

    # Trasladar el camión restante
    print("Trasladar camión con patente GHI789 50 unidades:")
    camion3.trasladarse(50)
    print(camion3)
    print("\n---\n")

    # Agregar más camiones y verificar el manejo de la flota
    camion4 = Camion(patente="JKL123", carga_maxima=9000, marca="MAN", anio=2020)
    flota.agregar_camion(camion4)
    print("Lista de camiones después de agregar uno nuevo:")
    print("\n".join(flota.listar_camiones()))

# Ejecutar el tester
if __name__ == "__main__":
    tester()
