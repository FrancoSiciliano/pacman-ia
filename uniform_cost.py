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

        if Util.is_goal_complete(matrix, current_position, target_to_complete):
            return path + [current_position]

        actions = Util.get_pacman_actions(matrix, visited, current_position)
        for action in actions:
            new_position = Util.get_new_position(current_position, action)
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
pacman_position = Util.get_target_position(Util.game_matrix, pacman)

solution = ucs_search(Util.game_matrix, pacman_position, cycle_count)
print("Number of cycles in UCS:", cycle_count[0])

if solution is not None:
    print('Path of Uniform Cost:', solution)
else:
    print("No solution found for Uniform Cost.")