# Ejercicio 2


# En este ejercicio modelamos una computadora, creando la clase Computadora para ello.
# En primer lugar, piensen por un rato en todas las características que mirarían al 
# momento de comprar una. ¿Cómo llamamos a las características en el paradigma de la programación OOP? 
# Rst: ATRIBUTOS Y METODOS
# Luego de que hayan pensado continúen con la consigna.

# (A) El objeto computador debe ser instanciado con todos sus atributos pasados como parámetros 
# al método constructor. Al momento de crear el equipo asígnenles a los atributos valores por defecto. 
# ¿Qué criterio tuvieron en cuenta para elegir estos valores?
# Rst: TUBE COMO CRITERIO QUE SON CONDICIONES QUE RARA EZ VAN A CAMBIAR EN EL MONITOR.

class Computadora:
    cantidad = 0
    lista_set_computadoras = set()
    procesador = 'Intel core i5'
    RAM = '8GB'
    stickers = None
    def __init__(self,os,monitor,pantalla,fecha_creacion,color,marca,modelo):
        encontrado = False
        for i in Computadora.lista_set_computadoras:
            if Computadora.__eq__(self,i):
                encontrado = True
                raise ValueError("La computadora ya existe")
        if not encontrado:
            Computadora.cantidad += 1
            # Computadora.lista_set_computadoras.add(self)     ¿¿¿¿¿ SI LO DEJO ME TIRA ERROR NO SE PORQUE ?????
        self.os = os
        self.monitor = monitor
        self.pantalla = pantalla
        self.fecha_creacion = fecha_creacion
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def __eq__(self, other):
        if not isinstance(other,Computadora):
            return False
        else:
            return self.marca == other.marca and self.modelo == other.modelo and self.fecha_creacion == other.fecha_creacion 
    
    def cambio_sistema_operatico(self, nuevo_os):
        if Computadora.validar_os(nuevo_os):
            self.os = nuevo_os
            print(f"El sistema operativo ha sido cambiado a {self.os}")
        else: 
            raise ValueError("El sistema operarivo no existe")
    
    @classmethod
    def nuevo_RAM(cls, nuevo_ram):
        cls.RAM = nuevo_ram
        print(f"La memoria RAM ha sido modificada a {cls.RAM}")
    
    @staticmethod
    def validar_os(os):
        if os.lower() in ['windows','linux','macos']:
            return True
        else:
            return False
# (B) El método __str__ nos ayuda a conocer la información esencial de nuestros objetos. 
# ¡Impleméntenlo! Recuerden que siempre debería estar presente en las clases que están creando.
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
# (C) Instancien 3 computadoras y asígnenles distintos valores a sus atributos
compu1 = Computadora('windows','pantalla LED','194X104','10/11/2004','negro','Lenovo','super')

compu2 = Computadora('windows','pantalla LED','198X108','15/12/2005','rojo','HP','elite')

compu3 = Computadora('windows','pantalla LED','200X100','01/01/2006','azul','Acer','Aspire')
# (D) ¿Cómo podrían llevar la cuenta de la cantidad de computadoras creadas? 
# ¿Qué tipo de variable resuelve lo pedido?


print(Computadora.cantidad)

# (E) Implementen al menos 2 de los siguientes métodos en la clase Computador:
    # a. updateOS: Actualiza el sistema operativo -----ESTE-----
    # b. PM: Brinda un mantenimiento programado al HW del equipo.
    # c. addRAM: Instala un nuevo módulo RAM al computador. ------Y ESTE------
    # d. getCapacity: Muestra la capacidad del componente de HW que se desea conocer.






# Nota: Pidan ayuda a su monitor para pensar cómo implementar los métodos solicitados. 
# Piensen en aquellos atributos creados u otros adicionales que les confieran funcionalidad y practicidad a 
# dichos métodos. 
# Si fuera necesario pueden investigar el uso de datetime u otra librería que requieran. 
# Recuerden informar siempre al usuario sobre las acciones realizadas sobre el sistema. 
# Prueben todos los métodos creados para testear su funcionamiento.
# Elijan algún componente de Hardware o Software de la máquina (atributo) y denle identidad. 
# Para ello, hagan otra clase, definan el constructor, el __str__ y piensen en al menos una función que 
# sea aplicable al componente elegido. 
# Codifiquen el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? 
# ¿Una lectura (read)? ¿Una escritura (write)? ¿Una actualización (update) de los atributos?