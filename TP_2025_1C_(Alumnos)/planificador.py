from lector_archivos import *
from vehiculos import *
import matplotlib.pyplot as plt

class Planificador():
    """
    clase principal que planifica las rutas
    busca todos los caminos posibles y determina el mejor por costo y tiempo
    """

    def __init__(self, nodos, conexiones, archivo_solicitudes):
        self.solicitudes = self.convertir_solicitudes(archivo_solicitudes, nodos)
        # 1) Se instancia un vehículo por modo
        self.vehiculos = {"Automotor": Automotor(),"Ferroviario": Ferroviario(),"Aereo": Aereo(),"Maritimo": Maritimo()}

        for solicitud in self.solicitudes:
            # 2) Se printea la solicitud que se va a evaluar en este ciclo del for
            print(f"\nSolicitud {solicitud.id}: {solicitud.origen.nombre} --> {solicitud.destino.nombre}")

            # 3) Rutas posibles
            rutas = self.buscar_caminos(solicitud.origen, solicitud.destino, conexiones,peso_carga=solicitud.kg)
            print(f"Peso: {solicitud.kg} kg")
            print(f"Rutas posibles: {len(rutas)}\n")

            # 4) Se muestran distancia y tramos de cada ruta
            
            for i, info in enumerate(self.info_caminos(rutas)):
                # Armamos un string con toda la info de cada ruta
                string = f"Ruta {int(i+1)}: modo {info[0][0].tipo.__name__.lower()}, distancia {info[1]} km, Tramos que la forman: "
                for idx in range(len(info[0])):
                    if idx != len(info[0])-1:
                        string += info[0][idx].origen.nombre + " --> "
                    else:
                        string += info[0][idx].origen.nombre + " --> "
                        string += info[0][idx].destino.nombre + "."
                print(string)
            print("\n")

            # 5) Calculamos y mostramos costos asociados a cada posible camino
            costos = self.costo_por_camino(rutas, self.vehiculos, solicitud.kg)
            if costos:
                for i, c in enumerate(costos):
                    print(f"Costo Ruta {i+1}: ${c}")
                # Buscamos el indice del menor costo
                idx = min(range(len(costos)), key=lambda x: costos[x])
                print(f"--> Mejor costo: Ruta {idx+1} (${costos[idx]})\n")
            else:
                print("no hay costos para mostrar \n")
            # 6) Calculamos y mostramos tiempos
            tiempos = self.tiempo_por_camino(rutas, self.vehiculos, solicitud.kg)
            if tiempos:
                for i, t in enumerate(tiempos):
                    print(f"Tiempo Ruta {i+1}: {round(t,2)} min")
                # buscamos el indice del menor tiempo
                idx = min(range(len(tiempos)), key=lambda x: tiempos[x])
                print(f"--> Mejor tiempo: Ruta {idx+1} ({tiempos[idx]} min)")
            
            # 7) Generamos los graficos
            if rutas:
                self.generar_graficos(rutas, self.vehiculos, float(solicitud.kg), solicitud.id, costos, tiempos)
            else:
                print("\n No se encontraron rutas posibles para esta solicitud \n")
             

    @staticmethod
    def convertir_solicitudes(archivo,nodos):
        """
        lee el archivo de solicitudes y crea objetos solicitud
        valida que los nodos existan
        """
        solicitudes = Lector.leer_csv(archivo)
        lista_solicitudes = []
        for solicitud in solicitudes:
            if (solicitud[2] not in nodos.keys() or solicitud[3] not in nodos.keys()):
                    raise ValueError(f"Alguno de los nodos de la solicitud {solicitud} no es validos.")
            solicitud_n = Solicitud(solicitud[0], float(solicitud[1]), nodos[solicitud[2]], nodos[solicitud[3]])
            lista_solicitudes.append(solicitud_n)
        return lista_solicitudes

    @staticmethod
    def conexion_es_valida_para_carga(conexion,peso_carga):
        """
        verifica si una conexion puede soportar el peso de la carga
        """
        if conexion.restriccion == "peso_max":
            return peso_carga <= conexion.valor_restriccion
        return True

    def buscar_caminos(self, origen, destino, conexiones, camino_actual = None, caminos_encontrados = None, nodos_visitados = None, tipo_actual = None, peso_carga = None):
        """
        busca todos los caminos posibles entre el origen y destino
        importante: mantiene el mismo tipo de transporte todo el camino
        usa recursion para encontrar todas las posibilidades
        """
        #inicializamos parametros en la primera llamada
        if camino_actual is None:
            camino_actual = []
        if caminos_encontrados is None:
            caminos_encontrados = []
        if nodos_visitados is None:
            nodos_visitados = []

        # si es el inicio, marca el origen como visitado
        if not camino_actual:
            nodo_actual = origen
            nodos_visitados.append(origen)
        else:
            nodo_actual = camino_actual[-1].destino # ultimo nodo del camino
        
        # caso base: destino
        if nodo_actual == destino:
            caminos_encontrados.append(list(camino_actual))
            return caminos_encontrados

        # funcion recursiva
        for conexion in conexiones:
            # Primero, se establecen las variables que verifican que se mantiene el tipo y que cada conexion es valida para la carga solicitada
            mismo_tipo = tipo_actual is None or conexion.tipo == tipo_actual
            conexion_valida = peso_carga is None or self.conexion_es_valida_para_carga(conexion,peso_carga) 
            # Ahora, agrega la conexion (si se cumple la validacion)
            if conexion.origen == nodo_actual and conexion.destino not in nodos_visitados and mismo_tipo and conexion_valida:
                # agregamos la conexion al camino actual
                camino_actual.append(conexion)
                nodos_visitados.append(conexion.destino)
                # llamada recursiva para seguir explorando
                self.buscar_caminos(origen,destino,conexiones,camino_actual,caminos_encontrados,nodos_visitados,tipo_actual or conexion.tipo,peso_carga)
                # sacamos la conexion para probar otros caminos
                camino_actual.pop()
                nodos_visitados.remove(conexion.destino)

        return caminos_encontrados

    @staticmethod
    def info_caminos(caminos):
        """
        solo para printear informacion de cada camino
        """
        largo = 0
        info = []
        for camino in caminos:
            for conexion in camino:
                largo += conexion.distancia
            info.append((camino, largo))
            largo = 0
        return info

    @staticmethod
    def costo_por_camino(caminos,vehiculos,peso_carga):
        """
        calcula el costo total de cada camino
        incluye costo fijo, por km y por kg
        """
        costos = []
        for camino in caminos:
            if not camino:
                costos.append(0.0)
            else:
                tipo_conexion = camino[0].tipo.__name__
                modo_vehiculo=Vehiculo.obtener_modo_vehiculo(tipo_conexion)   
                vt = vehiculos.get(modo_vehiculo)
                if vt is None:
                    raise ValueError(f"No existe vehículo para modo '{tipo_conexion}' (tipo conexion: '{tipo_conexion}')")
                costo_dist_total = 0
                cant_vehiculos=0
                # calculamos el costo de cada tramo
                for c in camino:
                    costo_tramo, _, cant = vt.calcular_coste_tiempo_sin_carga(c, peso_carga)
                    costo_dist_total += costo_tramo
                    # nos quedamos con la minima cantidad de vehiculos necesarios
                    cant_vehiculos=max(cant_vehiculos,cant)
                # sumamos el costo de la carga (se calcula una sola vez)
                costo_carga=vt.calcular_costo_carga(peso_carga)
                costo_total=costo_dist_total+costo_carga
                costos.append(costo_total)
        return costos

    @staticmethod
    def tiempo_por_camino(caminos, vehiculos, peso_carga):
        """
        calcula el tiempo total de cada camino
        sumando los tiempos de cada tramo
        """
        tiempos = []
        for camino in caminos:
            if not camino:
                tiempos.append(0.0)
                continue
            # obtenemos el vehiculo correspondiente
            tipo_conexion = camino[0].tipo.__name__
            modo_vehiculo=Vehiculo.obtener_modo_vehiculo(tipo_conexion)
            vt = vehiculos.get(modo_vehiculo)
            if vt is None:
                raise ValueError(f"No existe vehículo para modo '{modo_vehiculo}' (tipo conexion: '{tipo_conexion}')")
            acum = 0.0
            # sumamos el tiempo de cada conexion
            for c in camino:
                _, t_min, _ = vt.calcular_coste_tiempo(c, peso_carga)
                acum += t_min
            tiempos.append(acum)
        return tiempos

    @staticmethod
    def velocidad_segun_conexion(conexion, velocidad_nominal):
        """
        calcula la velocidad real en una conexion ya que puede ser
        diferente de la nominal si hay restricciones"""
        t_h = conexion.tiempo_horas(velocidad_nominal)
        if t_h <= 0:
            raise ValueError("Tiempo calculado inválido")
        return conexion.distancia / t_h

    def calcular_valores_acumulados(self, camino, vehiculos, peso_carga):
        """
        calcula distancia, tiempo y costo acumulados para 
        un camino para poder hacer los graficos
        """

        if not camino:
            return [0], [0], [0]
        
        tipo_conexion = camino[0].tipo.__name__
        modo_vehiculo = Vehiculo.obtener_modo_vehiculo(tipo_conexion)   
        vt = vehiculos.get(modo_vehiculo)
        
        # inicializamos las listas con 0 al principio
        distancias_acum = [0]
        tiempos_acum = [0]
        costos_acum = [0]
        
        dist_total = 0
        tiempo_total = 0
        costo_dist_total = 0
        
        # calculamos valores acumulados para cada tramo
        for c in camino:
            # distancia
            dist_total += c.distancia
            distancias_acum.append(dist_total)
            
            # tiempo
            costo_tramo, t_min, cant = vt.calcular_coste_tiempo_sin_carga(c, peso_carga)
            tiempo_total += t_min
            tiempos_acum.append(tiempo_total)
            
            # costo
            costo_dist_total += costo_tramo
            costos_acum.append(costo_dist_total)
        
        # agregamos el costo de carga al final
        costo_carga = vt.calcular_costo_carga(peso_carga)
        costos_acum = [c + costo_carga for c in costos_acum]
        
        return distancias_acum, tiempos_acum, costos_acum
    
    def generar_graficos(self, rutas, vehiculos, peso_carga, id_solicitud, costos_totales, tiempos_totales):
        """
        genera los graficos 
        son 4 graficos en total 
        para visualizar mejor la comparacion entre las rutas posibles
        """
        
        if not rutas:
            print("No hay rutas para graficar")
            return
        
        # colores para diferentes rutas
        colores = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
        
        # GRAFICO 1: distancia acumulada vs tiempo acumulado
        plt.figure(figsize=(10, 6))
        
        for i, camino in enumerate(rutas):
            # obtenemos los valores acumulados
            distancias, tiempos, _ = self.calcular_valores_acumulados(camino, vehiculos, peso_carga)
            # elegimos un color de la lista
            color = colores[i % len(colores)]
            plt.plot(tiempos, distancias, color=color, linewidth=2, label=f'Ruta {i+1}', marker='o')
        
        plt.title(f'Distancia Acumulada vs Tiempo Acumulado - Solicitud {id_solicitud}')
        plt.xlabel('Tiempo Acumulado (minutos)')
        plt.ylabel('Distancia Acumulada (km)')
        plt.legend()
        plt.show()
        
        # GRAFICO 2: costo acumulado vs distancia acumulada
        plt.figure(figsize=(10, 6))
        
        for i, camino in enumerate(rutas):
            distancias, _, costos = self.calcular_valores_acumulados(camino, vehiculos, peso_carga)
            color = colores[i % len(colores)]
            plt.plot(distancias, costos, color=color, linewidth=2, label=f'Ruta {i+1}', marker='o')
        
        plt.title(f'Costo Acumulado vs Distancia Acumulada - Solicitud {id_solicitud}')
        plt.xlabel('Distancia Acumulada (km)')
        plt.ylabel('Costo Acumulado ($)')
        plt.legend()
        plt.show()
        
        # GRAFICO 3 (ADICIONAL): comparacion de costos totales
        plt.figure(figsize=(10, 6))
        
        etiq_rutas = [f'Ruta {i+1}' for i in range(len(rutas))]
        # un color diferente para cada barra
        colores_barras = [colores[i % len(colores)] for i in range(len(rutas))]
        
        plt.bar(etiq_rutas, costos_totales, color=colores_barras)
        plt.title(f'Comparación de Costos Totales por Ruta - Solicitud {id_solicitud}')
        plt.xlabel('Rutas')
        plt.ylabel('Costo Total ($)')
        plt.show()
        
        # GRAFICO 4 (ADICIONAL): comparacion de tiempos totales
        plt.figure(figsize=(10, 6))
        
        plt.bar(etiq_rutas, tiempos_totales, color=colores_barras)
        plt.title(f'Comparación de Tiempos Totales por Ruta - Solicitud {id_solicitud}')
        plt.xlabel('Rutas')
        plt.ylabel('Tiempo Total (minutos)')
        plt.show()
    
        plt.close('all')