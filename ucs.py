import heapq
import Utils


def ucs(mapa, posicion, cant_nodos_visitados):
    
    visitados = set() # conjunto de posiciones ya visitadas
    cola = [] # cola de los próximos nodos a visitar
    camino = [] # camino final
    costo = 0 # costo final
    

    heapq.heappush(cola, (costo, posicion, camino))
    visitados.add(posicion)
    cant_nodos_visitados[0] += 1

    while cola:
        costo_act, pos_act, camino = heapq.heappop(cola) # datos del nodo a evaluar

        if Utils.objetivo_alcanzado(mapa, pos_act, 'F'): # evaluación de objetivo
            return camino + [pos_act]

        movimientos = Utils.get_movimientos_posibles(mapa, visitados, pos_act) # obtención de posibles movimientos
        for movimiento in movimientos:
            
            nueva_pos = Utils.get_nueva_posicion(pos_act, movimiento)
            nuevo_camino = camino + [pos_act]
            nuevo_costo = costo_act + 1 # el costo de cualquier acción es 1
            
            heapq.heappush(cola, (nuevo_costo, nueva_pos, nuevo_camino))
            
            visitados.add(nueva_pos)
            
            cant_nodos_visitados[0] += 1

    return None