game_matrix = [
  ['-', '-', '-', '-', '-'],
  ['-', 'W', '-', '-', '-'],
  ['P', '-', 'W', 'F', '-'],
  ['-', '-', '-', '-', '-']
]


def print_game_matrix():
  for row in game_matrix:
    print(row)
  print()


def is_in_matrix_limits(matrix, position_x, position_y):
  matrix_len_x = len(matrix)
  matrix_len_y = len(matrix[0])

  if (0 <= position_x < matrix_len_x) and (0 <= position_y < matrix_len_y):
    return True

  return False


def is_goal_complete(matrix, position, goal):
  position_x = position[0]
  position_y = position[1]

  return matrix[position_x][position_y] == goal


def get_target_position(matrix, target):
  matrix_size = len(matrix)
  for row in range(matrix_size):
    for column in range(matrix_size):
      if matrix[row][column] == target:
        return row, column


def get_pacman_actions(matrix, visited, pacman_position):
  pacman_position_x = pacman_position[0]
  pacman_position_y = pacman_position[1]

  actions = []

  if is_in_matrix_limits(matrix, pacman_position_x-1, pacman_position_y) and \
      (pacman_position_x-1, pacman_position_y) not in visited and \
      matrix[pacman_position_x-1][pacman_position_y] != 'W':
    actions.append('LEFT')

  if is_in_matrix_limits(matrix, pacman_position_x+1, pacman_position_y) and \
      (pacman_position_x+1, pacman_position_y) not in visited and \
      matrix[pacman_position_x+1][pacman_position_y] != 'W':
    actions.append('RIGHT')

  if is_in_matrix_limits(matrix, pacman_position_x, pacman_position_y+1) and \
      (pacman_position_x, pacman_position_y+1) not in visited and  \
      matrix[pacman_position_x][pacman_position_y+1] != 'W':
    actions.append('UP')

  if is_in_matrix_limits(matrix, pacman_position_x, pacman_position_y-1) and \
      (pacman_position_x, pacman_position_y-1) not in visited and \
      matrix[pacman_position_x][pacman_position_y-1] != 'W':
    actions.append('DOWN')

  return actions


def get_new_position(position, action):
  if action == 'LEFT':
    return position[0] - 1, position[1]
  elif action == 'RIGHT':
    return position[0] + 1, position[1]
  elif action == 'UP':
    return position[0], position[1] + 1
  elif action == 'DOWN':
    return position[0], position[1] - 1