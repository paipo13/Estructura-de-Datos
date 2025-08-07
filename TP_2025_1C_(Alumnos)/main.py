
from escenario import *
from planificador import *

def main():

    # Leemos los CSV, creamos el escenario
    escenario = Escenario("nodos.csv", "conexiones.csv")
    nodos = escenario.nodos
    conexiones = escenario.conexiones

    # Con los nodos y conexiones en mano planificamos las rutas posibles
    # Y concluimos cuales son las mejores en tiempo y costo

    planificador = Planificador(nodos, conexiones, "solicitudes.csv")

    # Tambien se exponen graficos que comparan los caminos posibles segun costo y tiempo

if __name__ == "__main__":
    main()