import csv
from io import FileIO
from Productos import *
class Tienda():
    cant_productos = 0
    lista_productos = []
    diccionario_tienda = {}
    def __init__(self,producto):
        self.producto = producto
        if producto not in Tienda.lista_productos:
            self.diccionario_productos = {producto.codigo_barra:producto} ###Obs. Mi clave ava a ser el codigo de barra y mi value va a ser el objeto en si...
            Tienda.lista_productos.append(producto)
            Tienda.cant_productos += 1
            Tienda.diccionario_tienda.update(self.diccionario_productos)
        else: 
            raise ValueError('Ya se a agregado dicho procuto')
    def __str__(self):
        return f'Hola soy la tienda. Tengo {self.cant_productos}.'

    def agregar_prodcutos_tienda(producto): #Voy a tomar que me pide que agrege el producto a la tienda.
        if (isinstance(producto,Productos)) or (isinstance(producto,CD)) or (isinstance(producto,Vinilo)):
            nuevo_producto_en_la_tienda = Tienda(producto)
            return f'Ha agregado a la tienda exitosamente el producto de codigo de barra: {producto.codigo_barra}'
        else:
            return 'El objeto que esta intentado de agregar a la tienda no pertence a la clase productos.'
        
    # c. eliminar producto por código (la cual debe validar que el Producto con ese código exista).
# [0,25 pts]
    @classmethod
    def eliminar_producto(cls,codigo): #Obs. Lo que voy a tomar aca es que me piden que dado un codigo de barra que elimine un producto de la tienda. Es decir qeu lo quite de los atributos de calse del mismo...un poco como la funcion purgar de la guia
        valor = cls.diccionario_tienda.get(codigo,None)
        if valor != None:
            producto_eliminado = cls.diccionario_tienda.pop(codigo)
            cls.cant_productos -= 1
            nueva_lista = list(filter(lambda x: x.codigo_barra != codigo, cls.lista_productos))
            cls.lista_productos = nueva_lista

            return f'Ha eliminado correctamente el producto de codigo de barra: {codigo}'
        else:
            return f'No existe en la tienda ningun producto con el codigo de barra de la forma : {codigo}'

    @classmethod
    def mostrar_productos(cls): #Obs. Tomo que cuando me piden productos me piden la linea de codigo. Le pregunte a la profesora y me dijo que estaba bien..
        lista = Tienda.lista_productos
        dict_años = {}
        lista_product = []
        lista_años = []
        for producto in lista:
            dict_años[producto.año] = producto
            lista_claves_años = sorted(list(dict_años.keys()))
        for i in lista_claves_años:
            lista_product.append(dict_años.get(i))
            lista_años.append(i)
        return list(zip(lista_años,lista_product)) #Obs. Para que no quede tan raro lo qeu voy a hacer aca es oner el año de lanzamiento de dicho producto y despues el objeto

    @classmethod
    def guardado_csv(cls,nombre_archivo):
        valores_productos = cls.diccionario_tienda.values()
        try:
            with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_nuevo:
                escritor = csv.writer(archivo_nuevo)
                encabezado = ["Título", "Artista", "Año", "Tipo", "Atributo Adicional", "Código"]
                escritor.writerow(encabezado)  

            with open(nombre_archivo, "a", newline="", encoding="utf-8") as file:
                escritor = csv.writer(file)
                for instancia_producto in valores_productos:
                    escritor.writerow([instancia_producto.titulo,instancia_producto.artista,instancia_producto.año
                                       ,type(instancia_producto),cls.atributo_adicional(instancia_producto) ,instancia_producto.codigo_barra]) 
                    #Obs. Tomo como dato que me pedian el tipo de objeto del que se trata (que es un dato que me parece importante ya que hay Herencia...) 
        except IOError:
            print("Error al exportar archivo")
            raise FileIO
        except:
            raise('Ocurrio un error durante la funcion de guardado_csv y no se cual puede ser. Revisar.')
        
    @classmethod
    def atributo_adicional(cls,producto):
        if isinstance(producto,CD):
            return producto.duracion
        elif isinstance(producto,Vinilo):
            return producto.diametro
        else: 
            return 'Ninguno'
#Estos son ejmeplos que use para air probando todo...
# producto1 = Productos('MAGIA BLANCA','Micheal',4,"789755162318")
# producto2 = Productos('MA','Micheal',4,"879247557299")
# cd1 = CD('rey leon','mufasa',2,'402148605419',32)
# cd2 = CD('j','juna',2,'239002631813',12.4)
# tienda1 = Tienda(producto1)
# tienda2 = Tienda(producto2)
# tienda3 = Tienda(cd1)
# print(Tienda.cant_productos)
# print(Tienda.diccionario_tienda)
# Tienda.guardado_csv('Parcial.csv')
# print(Tienda.mostrar_productos())
# print(Tienda.agregar_prodcutos_tienda(cd2))
# print(Tienda.eliminar_producto('402148605419'))