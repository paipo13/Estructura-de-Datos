from validaciones import Validaciones

### CLASE NODO ### 

class Nodo:
    """
    clase que representa un nodo (ciudad) en la red de transporte
    """
    
    def __init__(self, nombre):
        self.nombre = Validaciones.es_cad(nombre)

    def __eq__(self, other):
        return self.nombre == other.nombre

    def __repr__(self):
        return f"Nodo {self.nombre}"

## CLASE CONEXION 

class Conexion():
    """
    clase base para las conexiones entre nodos
    """

    def __init__(self, origen, destino, tipo, distancia, restriccion, valor_restriccion):
        #validamos que la instancia sea un num positivo
        self.distancia = Validaciones.es_natural(distancia)
        self.origen = origen
        self.destino = destino
        #acomodamos las restricciones segun corresponda
        self.restriccion_acomodar(restriccion, valor_restriccion)
        self.tipo = tipo
    
    def __repr__(self):
        return f"{self.tipo}"
    
    def restriccion_acomodar(self, restriccion, valor_restriccion):
        """
        metodo que procesa y valida las restricciones de cada conexion como peso max o velocidad max entre otras
        """
        # Maneja casos vacíos o None
        if not restriccion or restriccion.strip() == "":
            self.restriccion = None
            self.valor_restriccion = None
            return

        r = restriccion.lower()
        vr = valor_restriccion

        # Segun el tipo de restriccion validamos el valor
        if r == "peso_max" or r == "velocidad_max":
            vr = Validaciones.es_natural(vr)
        elif r == "tipo":
            vr = valor_restriccion.lower()
            if vr not in ("fluvial", "maritimo"):
                raise ValueError(f"Valor de tasa inválido: {vr}")
        elif r == "prob_mal_tiempo":
            vr = Validaciones.es_float_positivo(vr)
        else:
            raise ValueError(f"Restricción desconocida: {r}")

        self.restriccion = r
        self.valor_restriccion = vr

    def tiempo_horas(self, velocidad_nominal):
        """
        calcula el tiempo que tarda en recorrer la conexion
        """
        # Caso especial: conexion aerea
        if self.tipo == "Aerea" and self.restriccion == "prob_mal_tiempo":
            prob = self.valor_restriccion
            t_bueno = self.distancia / 600
            t_malo  = self.distancia / 400
            return( (t_bueno * (1 - prob)) + (t_malo * prob))

        if velocidad_nominal <= 0:
            raise ValueError("Velocidad debe ser > 0")
        
        return self.distancia / velocidad_nominal

# Clases hijas para cada tipo de conexion
class Ferroviaria(Conexion):
    def __init__(self, origen, destino, distancia, restriccion, valor_restriccion):
        super().__init__(origen, destino, "Ferroviaria", distancia,restriccion,valor_restriccion)

class Automotora(Conexion):
    def __init__(self, origen, destino, distancia, restriccion, valor_restriccion):
        super().__init__(origen, destino, "Automotor", distancia, restriccion, valor_restriccion)

class Maritima(Conexion):
    def __init__(self, origen, destino, distancia, restriccion, valor_restriccion):
        super().__init__(origen, destino, "Maritima", distancia, restriccion, valor_restriccion)

class Fluvial(Conexion):
    def __init__(self, origen, destino, distancia, restriccion, valor_restriccion):
        super().__init__(origen, destino, "Fluvial", distancia, restriccion, valor_restriccion)

class Aerea(Conexion):
    def __init__(self, origen, destino, distancia, restriccion, valor_restriccion):
        super().__init__(origen, destino, "Aerea", distancia, restriccion, valor_restriccion)


### CLASE SOLICITUD ###
    
class Solicitud():
    """
    representa una solicitud de transporte
    """
    ids = []
    def __init__(self,id,kg,origen,destino):
        self.setId(id)
        self.setPeso(kg)
        self.origen = origen
        self.destino = destino

    def setId(self,id):
        if id is None or id.strip() == "":
            raise ValueError ("El id no puede estar vacío")
        self.id = id
    
    def setPeso (self,kg):
        floatkg = float(kg)
        if floatkg<0:
           raise ValueError ("El peso no puede ser negativo")
        self.kg = floatkg
    
    def __repr__(self):
        return f"Id de carga:{self.id}\nPeso:{self.kg}\nDe {self.origen} a {self.destino}"
    