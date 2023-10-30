import Util


def dfs_search(matrix, visited, position, cycle_count):
    if position not in visited:
        visited.append(position)
        cycle_count[0] += 1     # Keep track the quantity of nodes visited
        target_to_complete = 'F'  # This represents the food to obtain

        if Util.is_goal_complete(matrix, position, target_to_complete):
            return visited
            
        actions = Util.get_pacman_actions(matrix, visited, position)
        for action in actions:
            new_position = Util.get_new_position(position, action)
            result = dfs_search(matrix, visited[:], new_position, cycle_count)

            if result is not None:
                return result
    return None


cycle_count = [0]
pacman = 'P'
pacman_position = Util.get_target_position(Util.game_matrix, pacman)

solution_path = dfs_search(Util.game_matrix, [], pacman_position, cycle_count)
print("Number of cycles in DFS:", cycle_count[0])

if solution_path is not None:
    print('Path of DFS:', solution_path)
else:
    print("No solution found for DFS.")