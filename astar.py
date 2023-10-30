import heapq
import math
import Utils

def astar(mapa, posicion, objetivo, cant_nodos_visitados):
    visitados = set() # conjunto de posiciones ya visitadas
    cola = [] # cola priorizada de las opciones posibles

    heapq.heappush(cola, (0, posicion, [])) #inicializamos la cola con la posición inicial
    
    visitados.add(posicion)
    
    cant_nodos_visitados[0] += 1

    while cola:
        costo_act, posicion_act, camino = heapq.heappop(cola)

        if posicion_act == objetivo: # evaluacion de objetivo
            return camino + [posicion_act]

        movimientos = Utils.get_movimientos_posibles(mapa, visitados, posicion_act) # obtención de posibles movimientos
        
        for movimiento in movimientos:
            
            nueva_pos = Utils.get_nueva_posicion(posicion_act, movimiento)
            nuevo_camino = camino + [posicion_act]
            nuevo_costo = costo_act + 1
            
            prioridad = nuevo_costo + heuristica(nueva_pos, objetivo) # g(x) + h(x)
            
            heapq.heappush(cola, (prioridad, nueva_pos, nuevo_camino))
            
            visitados.add(nueva_pos)
            
            cant_nodos_visitados[0] += 1

    return None

def heuristica(posicion, objetivo):
    x1, y1 = posicion
    x2, y2 = objetivo
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
