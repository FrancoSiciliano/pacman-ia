import Util


def busqueda_bfs(matriz, posicion, nodos_visitados):
    recorrido = set()
    camino = []
    fila = [(posicion, camino)]
    objetivo = 'F'    

    recorrido.add(posicion)
    nodos_visitados[0] += 1    

    while fila:
        posicion_actual, camino = fila.pop(0)

        if Util.objetivo_alcanzado(matriz, posicion_actual, objetivo):
            return camino + [posicion_actual]

        acciones = Util.acciones_pacman(matriz, recorrido, posicion_actual)
        for accion in acciones:
            nueva_posicion = Util.obtener_nueva_posicion(posicion_actual, accion)
            nuevo_camino = camino + [posicion_actual]
            fila.append((nueva_posicion, nuevo_camino))
            recorrido.add(nueva_posicion)
            nodos_visitados[0] += 1

    return None


nodos_visitados = [0]
pacman = 'P'
posicion_pacman = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solucion = busqueda_bfs(Util.matriz_pacman, posicion_pacman, nodos_visitados)
print("Number of cycles in BFS:", nodos_visitados[0])

if solucion is not None:
    print('Path of BFS:', solucion)
else:
    print("No solution found for BFS.")