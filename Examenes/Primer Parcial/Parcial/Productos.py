##### PGZ #####

import random
class Productos():
    def __init__(self,titulo:str,artista:str,año_lanzamiento:int,codigo_barra: str):
        self.titulo = titulo
        self.artista = artista
        self.año = año_lanzamiento
        self.codigo_barra = codigo_barra
        if Productos.validar(self.año) == False:
            raise ValueError('El año ingresado debe ser positivo.')
        if Productos.validar_codigo(self.codigo_barra) == False:
            raise ValueError('El codigo de barra ingrasado es incorrecto.')
        
    def __str__(self):
        return f'Hola soy un prducto. Mi año de lanzamiento es {self.año}, y mi titulo es: {self.titulo}.'
    
    def __eq__(self,other):
        if not isinstance(other,Productos):
            return False
        else:
            return self.codigo_barra == other.codigo_barra
    
    @staticmethod
    def validar(valor):
        if valor < 0:
            return False
        else:
            return True
    @staticmethod
    def validar_codigo(codigo):
        if len(codigo) != 12 or not codigo.isdigit():
            return False
        checksum = sum(int(digit) * (3 if i % 2 else 1) for i, digit in
    enumerate(codigo[:-1])) % 10
        checksum = (10 - checksum) % 10
        return checksum == int(codigo[-1])
        
    def generar_codigo_barras():
        codigo = [random.randint(0, 9) for _ in range(11)]

        checksum = sum(int(digit) * (3 if i % 2 else 1) for i, digit in
    enumerate(codigo)) % 10
        checksum = (10 - checksum) % 10

        codigo.append(checksum)

        return ''.join(map(str, codigo))
    #Para probar el programa pueden utilizar “123456789012” como código de barra inválido.

class CD(Productos):
    def __init__(self, titulo, artista, año_lanzamiento, codigo_barra,duracion:float):
        super().__init__(titulo, artista, año_lanzamiento, codigo_barra)
        self.duracion = float(duracion)
        if super().validar(duracion) == False:
            raise ValueError ('La duracion del CD debe ser positiva.')
    def __str__(self):
        return f'Hola soy un CD, soy un Producto de la tienda y tengo una duracion de {self.duracion} minutos.'
    
    
class Vinilo(Productos):
    def __init__(self, titulo, artista, año_lanzamiento, codigo_barra,diametro:float):
        super().__init__(titulo, artista, año_lanzamiento, codigo_barra)
        self.diametro = diametro
        if super().validar(diametro) == False:
            raise ValueError ('El diametro del Vinilo debe ser positivo.')
    
    def __str__(self):
        return f'Hola soy un Vinilo, soy un producto, mi diametro es de {self.diametro} cm (es lo que asumi que era la unidad cuando pregunte me dijeron que era m o cm).'
    
#Estos son ejmeplos que use para air probando todo...
# producto1 = Productos('MAGIA BLANCA','Micheal',4,"789755162318")
# cd1 = CD('rey leon','mufasa',2,'402148605419',32)
# print(cd1)
# print(producto1)
# vinilo1 = Vinilo('lentos','julio iglesias',3,'340557116679',4.3)
# print(vinilo1)
# cd2 = CD('j','juna',2,'239002631813',12.4)
# print(type(cd2))
# print(class(cd2))
