import Utils


def bfs(mapa, posicion, nodos_visitados):
    # Defino el objetivo, inicializo el camino y un conjunto para mantener el track de las posiciones visitadas
    objetivo = 'F'  
    camino = []
    recorrido = set()

    # Agrego la posicion actual a las posiciones recorridas
    recorrido.add(posicion)
    # Inicializo una fila donde tengo la posicion actual y el camino vacio  
    cola = [(posicion, camino)]
    
    # Sumo 1 a los nodos visitados
    nodos_visitados[0] += 1    

    while cola:
        # Tomo posicion actual y el camino asociado de la fila 
        posicion_actual, camino = cola.pop(0)

        # En caso de lograr el objetivo en la posicion actual, devuelvo el camino
        if Utils.objetivo_alcanzado(mapa, posicion_actual, objetivo):
            return camino + [posicion_actual]

        # Si no busco las posibles acciones del pacman y las exploro
        movimientos = Utils.get_movimientos_posibles(mapa, recorrido, posicion_actual)
        for movimiento in movimientos:
            # Creo un nuevo camino que incluye la posicion actual
            nuevo_camino = camino + [posicion_actual]
            # Calculo nueva posicion en base a la accion elegida y la agrego al recorrido
            nueva_posicion = Utils.get_nueva_posicion(posicion_actual, movimiento)
            recorrido.add(nueva_posicion)
            # La posicion nueva y su recorrido son agregados a la fila e incremento los nodos visitados
            cola.append((nueva_posicion, nuevo_camino))
            nodos_visitados[0] += 1
    # Si sale por aqui, significa que no se encontro ninguna solucion
    return None