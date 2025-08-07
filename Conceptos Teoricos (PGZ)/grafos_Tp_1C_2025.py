def busqueda_profundidad(red, inicio, destino):
    """
    Encuentra todos los caminos sin loops usando DFS iterativo
    """
    if inicio == destino:
        return [[inicio]]

    todos_los_caminos = []
    pila = [(inicio, [inicio])]
    print(pila)
    while pila:
        print(pila)
        nodo_actual, camino = pila.pop()
        print(pila)
        print(nodo_actual, camino)
        for vecino in red[nodo_actual]:
            if vecino not in camino:
                nuevo_camino = camino + [vecino]
                print(nuevo_camino)
                if vecino == destino:
                    todos_los_caminos.append(nuevo_camino)
                else:
                    pila.append((vecino, nuevo_camino))
            print(pila)

    return todos_los_caminos


if __name__ == "__main__":
    red = {
        "BUENOS_AIRES": ["ZARATE", "JUNIN", "AZUL", "MAR_DEL_PLATA"],
        "ZARATE": ["JUNIN", "BUENOS_AIRES"],
        "JUNIN": ["ZARATE", "BUENOS_AIRES", "AZUL"],
        "AZUL": ["JUNIN", "BUENOS_AIRES", "MAR_DEL_PLATA"],
        "MAR_DEL_PLATA": ["AZUL", "BUENOS_AIRES"],
    }

    caminos = busqueda_profundidad(red, "ZARATE", "MAR_DEL_PLATA")

    print("Todos los caminos ZARATE→MAR_DEL_PLATA:")
    for i, camino in enumerate(caminos, 1):
        print(f"  Camino {i}: {' → '.join(camino)} (tramos: {len(camino)})")
