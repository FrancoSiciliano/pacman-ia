import heapq

import Util


def ucs_search(matrix, position, cycle_count):
    visited = set()
    queue = []
    path = []
    cost = 0
    target_to_complete = 'F'

    heapq.heappush(queue, (cost, position, path))
    visited.add(position)
    cycle_count[0] += 1     # Keep track the quantity of nodes visited

    while queue:
        current_cost, current_position, path = heapq.heappop(queue)

        if Util.objetivo_alcanzado(matrix, current_position, target_to_complete):
            return path + [current_position]

        actions = Util.acciones_pacman(matrix, visited, current_position)
        for action in actions:
            new_position = Util.obtener_nueva_posicion(current_position, action)
            new_path = path + [current_position]
            new_cost = current_cost + get_cost(action)
            heapq.heappush(queue, (new_cost, new_position, new_path))
            visited.add(new_position)
            cycle_count[0] += 1

    return None


def get_cost(action):
    if action == 'LEFT':
        return 1
    elif action == 'RIGHT':
        return 1
    elif action == 'UP':
        return 1
    elif action == 'DOWN':
        return 1


cycle_count = [0]
pacman = 'P'
pacman_position = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solution = ucs_search(Util.matriz_pacman, pacman_position, cycle_count)
print("Number of cycles in UCS:", cycle_count[0])

if solution is not None:
    print('Path of Uniform Cost:', solution)
else:
    print("No solution found for Uniform Cost.")