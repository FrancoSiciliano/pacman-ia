import Util


def dfs_search(matrix, visited, position, cycle_count):
    if position not in visited:
        visited.append(position)
        cycle_count[0] += 1     # Keep track the quantity of nodes visited
        target_to_complete = 'F'  # This represents the food to obtain

        if Util.objetivo_alcanzado(matrix, position, target_to_complete):
            return visited
            
        actions = Util.acciones_pacman(matrix, visited, position)
        for action in actions:
            new_position = Util.obtener_nueva_posicion(position, action)
            result = dfs_search(matrix, visited[:], new_position, cycle_count)

            if result is not None:
                return result
    return None


cycle_count = [0]
pacman = 'P'
pacman_position = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solution_path = dfs_search(Util.matriz_pacman, [], pacman_position, cycle_count)
print("Number of cycles in DFS:", cycle_count[0])

if solution_path is not None:
    print('Path of DFS:', solution_path)
else:
    print("No solution found for DFS.")