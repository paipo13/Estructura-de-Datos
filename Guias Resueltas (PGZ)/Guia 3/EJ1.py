# Ejercicio 1

# Dada la siguiente Clase:

class Camion:
    lista_patente = set()
    camiones = []
    def __init__(self,patente, carga, marca, anio):
        # if patente in Camion.lista_patente:
        #     raise ValueError("La patente ya existe")
        self.patente=patente
        self.carga= Camion.modificar_carga(self,carga)
        self.marca=marca
        self.anio=anio
        Camion.lista_patente.add(patente)
        Camion.camiones.append(self)
    def __str__(self):
        return f"Camion #{self.patente}\nCarga: {self.carga}\nMarca: {self.marca}\nAnio: {self.anio}"

    def __eq__(self, other):
        if not isinstance(other,Camion):
            return False
        else:
            return self.patente==other.patente 
        
    @classmethod
    def __purgar__(cls):
        patentes_vistas = set()
        camiones_no_repetidos = []
        for i in cls.camiones:
            if i not in patentes_vistas:
                patentes_vistas.add(i.patente)
                camiones_no_repetidos.append(i)
        cls.camiones = camiones_no_repetidos
        cls.lista_patente = patentes_vistas
    def modificar_carga(self,carga_nueva):
        self.carga = carga_nueva

# (A)Indicar qué devuelven las siguientes expresiones. Primero analícelo con su grupo y luego ejecute 
# las instrucciones en la máquina y compruebe su respuesta.

# furgon1==furgon2
# furgon1 is furgon2
# furgon3==furgon4
# furgon3 is furgon4

furgon1 =  Camion('ABC123',2000,'audi',1990)

furgon3 = Camion('XYZ789',3000,'ford',2000)

furgon5 = Camion('ABD456',3000,'ford',2000)

furgon10 = Camion('ABC124',3000,'chevorlet',2000)

furgon11 = Camion('ABC125',3000,'chevorlet',2000)

furgon12 = Camion('ABC126',3000,'chevorlet',2000)

furgon13 = Camion('ABC127',3000,'audi',2000)
furgon2 = furgon1
furgon4 = furgon3
print(furgon1==furgon2) #True
print(furgon1 is furgon2) # True
print(furgon3==furgon4) #True
print(furgon3 is furgon4) #True
# (B) Modificar el código dado para que la comparación de dos objetos de la clase Camion devuelva True 
# cuando todos sus atributos coincidan.

#Rst: Listo fue agregar el def __eq__ (self,other) en la clase

# (C) ¿Será éste el caso real? ¿Qué hace único a nuestros objetos? Identifica el atributo que hace
# único al objeto y modifica el código anterior para que la igualdad se verifique en este caso.

# Rst: No, Los id ( en el caso de camion seria la patente). La patente. Listo

# (D) Si dos personas tienen el mismo DNI, entonces… ¡Son la misma persona! ¿Cómo evitarían asignar el mismo DNI a 
# dos personas (distintas claro)?  Siguiendo esta analogía, adapten el código anterior para el caso de los camiones.
#Rst: Listo..
# (E) Supongamos que ahora permitimos que dos personas tengan el mismo DNI, pero en un momento dado deseamos “purgar” 
# las personas con DNI duplicado (Podríamos escribir un método que realice esta tarea y quedarnos sólo con la primera
# persona que fue registrada con cada DNI. Nosotros seguimos con los camiones ¡Manos a la obra!
#Ya purgamos
# (F) Creen un pequeño menú que les permita:
    # a. Registrar un nuevo camión
    # b. Modificar la carga de un camión
    # c. Mostrar por la terminal la lista de camiones ordenados del más antiguo al más moderno.
    # d. Mostrar por la terminal la marca que más veces ha sido registrada.

def menu():
    # camiones = []
    # patente_camiones = []
    while True:
        print("\nMenú:")
        print("a. Registrar un nuevo camión")
        print("b. Modificar la carga de un camión")
        print("c. Mostrar por la terminal la lista de camiones ordenados del más antiguo al más moderno.")
        print("d. Mostrar por la terminal la marca que más veces ha sido registrada.")
        print("e. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "a":
            patente = input("Ingrese la patente: ")
            carga = (input("Ingrese la carga: "))
            marca = (input("Ingrese la marca: ")).lower()
            anio = int(input("Ingrese el año: "))
            camion = Camion(patente, carga, marca, anio)
            # camiones.append(camion)
            # patente_camiones.append(patente)
            print("Camión registrado correctamente.")
        elif opcion == "b":
            carga_eleguida = input("Ingrese la carga del camion: ")
            pat_camion = input("Ingrese la patente del camion: ")
            encontrado = False
            for i in Camion.camiones:
                if i.patente == pat_camion:
                    i.modificar_carga(carga_eleguida)
                    encontrado = True
                    print(f'Carga modificada correctamente.')
                    print(f'La carga del camion de patente {i.patente} es: {i.carga}.')
                    break
            if not encontrado:
                print("Camion no encontrado")
        elif opcion == "c":
            print("Lista de camiones del mas antiguo al mas reciente(siendo 1. el mas antiguo):")
            for i in range(len(Camion.camiones)):
                print('pos'+ str(i+1))
                print(Camion.camiones[i])
        elif opcion == "d": #Mostrar por la terminal la marca que más veces ha sido registrada
            lista_marcas = []
            lista_cantidad = []
            for i in Camion.camiones:
                if i.marca not in lista_marcas:
                    lista_marcas.append(i.marca)
                    lista_cantidad.append(1)
                else:
                    for k in range(len(lista_marcas)):
                        if i.marca == lista_marcas[k]:
                            pos = k
                    lista_cantidad[pos] += 1
            print(lista_marcas)
            print(lista_cantidad)
            num_max = max(lista_cantidad)
            for j in range(len(lista_cantidad)):
                if lista_cantidad[j] == num_max:
                    marca_mas_repetida = lista_marcas[j]
                    break
            print("La marca mas repetida es: ")
            print(marca_mas_repetida)
        elif opcion == "e": 
            break
        else:
            print("Opción incorrecta. Intente de nuevo.")


menu()

#WOOOOOOOWWWWW VAMOOOOOO
