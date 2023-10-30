import Util


def busqueda_bfs(matriz, posicion, nodos_visitados):
    # Defino el objetivo, inicializo el camino y un conjunto para mantener el track de las posiciones visitadas
    objetivo = 'F'  
    camino = []
    recorrido = set()

    # Agrego la posicion actual a las posiciones recorridas
    recorrido.add(posicion)
    # Inicializo una fila donde tengo la posicion actual y el camino vacio  
    fila = [(posicion, camino)]
    
    # Sumo 1 a los nodos visitados
    nodos_visitados[0] += 1    

    while fila:
        # Tomo posicion actual y el camino asociado de la fila 
        posicion_actual, camino = fila.pop(0)

        # En caso de lograr el objetivo en la posicion actual, devuelvo el camino
        if Util.objetivo_alcanzado(matriz, posicion_actual, objetivo):
            return camino + [posicion_actual]

        # Si no busco las posibles acciones del pacman y las exploro
        acciones = Util.acciones_pacman(matriz, recorrido, posicion_actual)
        for accion in acciones:
            # Creo un nuevo camino que incluye la posicion actual
            nuevo_camino = camino + [posicion_actual]
            # Calculo nueva posicion en base a la accion elegida y la agrego al recorrido
            nueva_posicion = Util.obtener_nueva_posicion(posicion_actual, accion)
            recorrido.add(nueva_posicion)
            # La posicion nueva y su recorrido son agregados a la fila e incremento los nodos visitados
            fila.append((nueva_posicion, nuevo_camino))
            nodos_visitados[0] += 1
    # Si sale por aqui, significa que no se encontro ninguna solucion
    return None

# Inicializo cantidad de nodos visitados, el caracter del pacman y la posicion inicial
nodos_visitados = [0]
pacman = 'P'
posicion_pacman = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solucion = busqueda_bfs(Util.matriz_pacman, posicion_pacman, nodos_visitados)
print("Cantidad de ciclos:", nodos_visitados[0])

if solucion is not None:
    print('Camino resultado:', solucion)
else:
    print("No se encontró una solución.")