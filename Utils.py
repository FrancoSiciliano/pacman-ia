def get_movimientos_posibles(matriz, visitados, act_pos):
  pos_x = act_pos[0]
  pos_y = act_pos[1]

  movimientos = []

  if is_dentro_de_la_matriz(matriz, pos_x - 1, pos_y) and (pos_x - 1, pos_y) not in visitados and matriz[pos_x - 1][pos_y] != 'O':
    movimientos.append('IZQUIERDA')

  if is_dentro_de_la_matriz(matriz, pos_x + 1, pos_y) and (pos_x + 1, pos_y) not in visitados and matriz[pos_x + 1][pos_y] != 'O':
    movimientos.append('DERECHA')

  if is_dentro_de_la_matriz(matriz, pos_x, pos_y + 1) and (pos_x, pos_y + 1) not in visitados and  matriz[pos_x][pos_y + 1] != 'O':
    movimientos.append('ARRIBA')

  if is_dentro_de_la_matriz(matriz, pos_x, pos_y - 1) and (pos_x, pos_y-1) not in visitados and matriz[pos_x][pos_y - 1] != 'O':
    movimientos.append('ABAJO')

  return movimientos

def is_dentro_de_la_matriz(matriz, pos_x, pos_y):
  long_x = len(matriz)
  long_y = len(matriz[0])

  if (0 <= pos_x < long_x) and (0 <= pos_y < long_y):
    return True

  return False

def get_nueva_posicion(posicion, accion):
  if accion == 'IZQUIERDA':
    return posicion[0] - 1, posicion[1]
  elif accion == 'DERECHA':
    return posicion[0] + 1, posicion[1]
  elif accion == 'ARRIBA':
    return posicion[0], posicion[1] + 1
  elif accion == 'ABAJO':
    return posicion[0], posicion[1] - 1
  
def imprimir_solucion(solucion, juego, pos_final):
    simbolos = ['|', '-']
    aux = juego.copy()

    for i in range(0, len(solucion)):
        if i != 0 and i != len(solucion) - 1:
            if solucion[i] != pos_final and (solucion[i][0] != solucion[i + 1][0]):
                aux[solucion[i][0]][solucion[i][1]] = simbolos[0]
            else:
                aux[solucion[i][0]][solucion[i][1]] = simbolos[1]

    for col in aux:
        print(col)

def objetivo_alcanzado(matriz, posicion, objetivo):
  pos_x = posicion[0]
  pos_y = posicion[1]

  return matriz[pos_x][pos_y] == objetivo