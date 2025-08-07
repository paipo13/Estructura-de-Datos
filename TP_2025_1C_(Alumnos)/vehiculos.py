from validaciones import Validaciones
from math import ceil

class Vehiculo:
    """
    clase base para todos los vehiculos con las caracteristicas comunes y metodos basicos
    """
    lista_modos = ["Automotor","Ferroviario","Aereo","Maritimo"]
    

    def __init__(self, velocidad_nominal, capacidad_carga, costo_fijo, costo_km, costo_kg, modo):
        self.setVelocidad(velocidad_nominal)
        self.setModo(modo)
        self.setCapacidad_carga(capacidad_carga)
        self.setCostoFijo(costo_fijo)
        self.setCostoKm(costo_km)
        self.setCostoKg(costo_kg)

    def setModo(self,modo):
        if modo not in Vehiculo.lista_modos:
            raise ValueError("el modo no existe.")
        self.modo = modo         
        
    def setVelocidad(self,velocidad_nominal):
        num = Validaciones.es_natural(velocidad_nominal)
        self.velocidad_nominal = num

    def setCapacidad_carga(self,capacidad_carga):
        num = Validaciones.es_natural((capacidad_carga))
        self.capacidad_carga = num
            
    @staticmethod
    def setCosto(costo):
        """metodo auxiliar para validar costos"""
        num = Validaciones.es_natural(costo)
        return num
       
    def setCostoFijo(self,costo):
        costo_fijo = self.setCosto(costo)
        self.costo_fijo = costo_fijo
    
    def setCostoKm(self,costo):
        costo_km = self.setCosto(costo)
        self.costo_km = costo_km

    def setCostoKg(self,costo):
        costo_kg = self.setCosto(costo)
        self.costo_kg = costo_kg
    
    def calcular_costo_carga(self,peso_carga):
        """calcula el costo de transportar la carga"""
        return self.costo_kg * peso_carga
    
    def calcular_coste_tiempo_sin_carga(self,conexion, peso_carga):
        """
        calcula el costo y tiempo de un tramo sin incluir el costo de la carga
        tambien calcula cuantos vehiculos se necesitan
        """        
        if self.obtener_modo_vehiculo(conexion.tipo.__name__) != self.modo:
            raise ValueError("Tipo distinto")
        
        # validamos que la capacidad de carga no sea 0 para evitar dividir por 0
        if self.capacidad_carga <= 0 :
            raise ValueError("la capacidad de carga debe ser mayor a 0")
        
        # calculamos cuantos vehiculos necesitamos(se redondea para arriba)
        cant = ceil(peso_carga/self.capacidad_carga)
        velocidad_efectiva = self.velocidad_nominal

        if conexion.restriccion == "velocidad_max":
            if self.velocidad_nominal > conexion.valor_restriccion:
                velocidad_efectiva = conexion.valor_restriccion

        dist = conexion.distancia
        costo_unit = (self.costo_fijo + self.costo_km * dist)
        # costo total = cantidad de vehiculos * costo
        costo_total = cant * costo_unit
        # calculamos el tiempo en horas y lo pasamos a minutos
        tiempo_h = conexion.tiempo_horas(velocidad_efectiva)
        tiempo_min = tiempo_h * 60
        return costo_total, tiempo_min , cant
    
    def calcular_coste_tiempo(self,conexion, peso_carga):
        """
        calcula el costo total incluyendo la carga
        """ 
        costo_sin_carga, tiempo_min, cant = self.calcular_coste_tiempo_sin_carga(conexion,peso_carga)
        costo_carga = self.calcular_costo_carga(peso_carga)
        return costo_sin_carga + costo_carga , tiempo_min, cant
    
    @staticmethod
    def obtener_modo_vehiculo(tipo_conexion):
        """
        mapeo para que coincidan los tipos de conexion con los tipos de vehiculo
        """
        mapeo = {
            "Ferroviaria": "Ferroviario",
            "Aerea": "Aereo",
            "Maritima": "Maritimo",
            "Fluvial": "Maritimo",
            "Automotora": "Automotor"
        }
        return mapeo.get(tipo_conexion, tipo_conexion)
        
    def __repr__(self):
        return f""

class Automotor(Vehiculo):
    """
    vehiculo tipo camion
    tiene costo por kg variable segun peso
    """
    def __init__(self, velocidad_nominal = 80, capacidad_carga = 30000, costo_fijo = 30, costo_km = 5, costo_kg = 1, modo = "Automotor"):
        super().__init__(velocidad_nominal, capacidad_carga, costo_fijo, costo_km, costo_kg, modo)
    
    def calcular_costo_carga(self, peso_carga):
        """
        override del metodo base
        """
        cant = ceil(peso_carga / self.capacidad_carga)
        costo_carga_total = 0
        peso_restante = peso_carga
        
        # calculamos el costo para cada vehiculo
        for i in range(cant):
            # peso que lleva este vehiculo
            peso_este_vehiculo = min(peso_restante,self.capacidad_carga)
            # determinamos el costo por kg segun el peso
            costo_kg_este = 1 if peso_este_vehiculo < 15000 else 2
            
            costo_carga_total += costo_kg_este * peso_este_vehiculo
            peso_restante -= peso_este_vehiculo

        return costo_carga_total

    

class Ferroviario(Vehiculo):
    """
    vehiculo tipo tren
    tiene costo por km variable segun la distancia
    """
    def __init__(self, velocidad_nominal = 100, capacidad_carga = 150000, costo_fijo = 100, costo_km = 20, costo_kg = 3, modo = "Ferroviario"):
        super().__init__(velocidad_nominal, capacidad_carga, costo_fijo, costo_km, costo_kg, modo)
    
    def calcular_coste_tiempo_sin_carga(self, conexion, peso_carga):
        """
        override del base
        """
        if conexion.distancia < 200:
            self.costo_km = 20 
        else:
            self.costo_km = 15
        # llamamos al metodo de la clase padre con el costo actualizado
        return super().calcular_coste_tiempo_sin_carga(conexion, peso_carga)


class Aereo(Vehiculo):
    """
    vehiculo tipo avion
    """
    def __init__(self, velocidad_nominal = 600, capacidad_carga = 5000, costo_fijo = 750, costo_km = 40, costo_kg = 10, modo = "Aereo"):
        super().__init__(velocidad_nominal, capacidad_carga, costo_fijo, costo_km, costo_kg, modo)


class Maritimo(Vehiculo):
    """
    vehiculo tipo barco
    tiene costo fijo diferente para fluvial y maritimo
    """
    def __init__(self, velocidad_nominal = 40, capacidad_carga = 100000, costo_fijo = 500, costo_km = 15, costo_kg = 2, modo = "Maritimo"):
        super().__init__(velocidad_nominal, capacidad_carga, costo_fijo, costo_km, costo_kg, modo)

    def calcular_coste_tiempo_sin_carga(self, conexion, peso_carga):
        """
        override del metodo base
        """
        costo_fijo_original = self.costo_fijo
        
        # si hay restriccion del tipo ajustamos el costo
        if conexion.restriccion == "tipo":
            if conexion.valor_restriccion == "maritimo":
                self.costo_fijo = 1500

            elif conexion.valor_restriccion == "fluvial":
                self.costo_fijo = 500
        #calculamos el costo ajustado
        resultado =  super().calcular_coste_tiempo_sin_carga(conexion, peso_carga)
        #restauramos el costo original para no afectar otros calculos
        self.costo_fijo = costo_fijo_original
        return resultado
