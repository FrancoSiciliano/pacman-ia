import heapq
import math

import Util


def calculate_heuristic(position, goal):
    x1, y1 = position
    x2, y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def astar_search(matrix, position, goal, cycle_count):
    visited = set()
    queue = []

    heapq.heappush(queue, (0, position, []))
    visited.add(position)
    cycle_count[0] += 1

    while queue:
        current_cost, current_position, path = heapq.heappop(queue)

        if current_position == goal:
            return path + [current_position]

        actions = Util.acciones_pacman(matrix, visited, current_position)
        for action in actions:
            new_position = Util.obtener_nueva_posicion(current_position, action)
            new_path = path + [current_position]
            new_cost = current_cost + 1  # We consider a uniform cost of 1 by movement
            priority = new_cost + calculate_heuristic(new_position, goal)
            heapq.heappush(queue, (priority, new_position, new_path))
            visited.add(new_position)
            cycle_count[0] += 1

    return None


cycle_count = [0]
pacman = 'P'
pacman_position = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)
food_position = Util.obtener_posicion_objetivo(Util.matriz_pacman, 'F')

solution = astar_search(Util.matriz_pacman, pacman_position, food_position, cycle_count)
print("Number of cycles in A*:", cycle_count[0])

if solution is not None:
    print('Path of A*:', solution)
else:
    print("No solution found for A*.")