import Util


def busqueda_bfs(matriz, posicion, nodos_visitados):
    objetivo = 'F'  
    camino = []
    recorrido = set()
    recorrido.add(posicion)
    fila = [(posicion, camino)]
      
    nodos_visitados += 1    

    while fila:
        posicion_actual, camino = fila.pop(0)

        if Util.objetivo_alcanzado(matriz, posicion_actual, objetivo):
            return camino + [posicion_actual]

        acciones = Util.acciones_pacman(matriz, recorrido, posicion_actual)
        for accion in acciones:
            nuevo_camino = camino + [posicion_actual]
            nueva_posicion = Util.obtener_nueva_posicion(posicion_actual, accion)
            recorrido.add(nueva_posicion)
            fila.append((nueva_posicion, nuevo_camino))
            nodos_visitados += 1

    return None


nodos_visitados = 0
pacman = 'P'
posicion_pacman = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solucion = busqueda_bfs(Util.matriz_pacman, posicion_pacman, nodos_visitados)
print("Cantidad de ciclos:", nodos_visitados)

if solucion is not None:
    print('Camino resultado:', solucion)
else:
    print("No se encontró una solución.")