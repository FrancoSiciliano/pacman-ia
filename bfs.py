import Util


def bfs_search(matrix, position, cycle_count):
    visited = set()
    path = []
    queue = [(position, path)]
    target_to_complete = 'F'    # This represents the food to obtain

    visited.add(position)
    cycle_count[0] += 1     # Keep track the quantity of nodes visited

    while queue:
        current_position, path = queue.pop(0)

        if Util.is_goal_complete(matrix, current_position, target_to_complete):
            return path + [current_position]

        actions = Util.get_pacman_actions(matrix, visited, current_position)
        for action in actions:
            new_position = Util.get_new_position(current_position, action)
            new_path = path + [current_position]
            queue.append((new_position, new_path))
            visited.add(new_position)
            cycle_count[0] += 1

    return None


cycle_count = [0]
pacman = 'P'
pacman_position = Util.get_target_position(Util.game_matrix, pacman)

solution_path = bfs_search(Util.game_matrix, pacman_position, cycle_count)
print("Number of cycles in BFS:", cycle_count[0])

if solution_path is not None:
    print('Path of BFS:', solution_path)
else:
    print("No solution found for BFS.")