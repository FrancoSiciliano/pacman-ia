import Util


def busqueda_bfs(matriz, posicion, cycle_count):
    recorrido = set()
    camino = []
    fila = [(posicion, camino)]
    objetivo = 'F'    

    recorrido.add(posicion)
    cycle_count[0] += 1     # Keep track the quantity of nodes visited

    while fila:
        posicion_actual, camino = fila.pop(0)

        if Util.objetivo_alcanzado(matriz, posicion_actual, objetivo):
            return camino + [posicion_actual]

        actions = Util.acciones_pacman(matriz, recorrido, posicion_actual)
        for action in actions:
            new_position = Util.obtener_nueva_posicion(posicion_actual, action)
            new_path = camino + [posicion_actual]
            fila.append((new_position, new_path))
            recorrido.add(new_position)
            cycle_count[0] += 1

    return None


cycle_count = [0]
pacman = 'P'
pacman_position = Util.get_target_position(Util.game_matrix, pacman)

solution_path = busqueda_bfs(Util.game_matrix, pacman_position, cycle_count)
print("Number of cycles in BFS:", cycle_count[0])

if solution_path is not None:
    print('Path of BFS:', solution_path)
else:
    print("No solution found for BFS.")