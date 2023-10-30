import Utils
from astar import astar
from bfs import bfs
from dfs import dfs
from ucs import ucs
from copy import deepcopy

cant_nodos_visitados_dfs = [0]
cant_nodos_visitados_bfs = [0]
cant_nodos_visitados_ucs = [0]
cant_nodos_visitados_astar = [0]
juego = [
  [' ', ' ', ' ', ' ', ' '],
  [' ', 'O', 'O', 'O', ' '],
  ['P', ' ', 'O', 'F', ' '],
  [' ', ' ', 'O', ' ', ' ']
]

pos_p = (2, 0)
pos_obj = (2, 3)

# Resultados con cada algoritmo

sol_dfs = dfs(mapa=juego, visitados=[], posicion=pos_p, nodos_visitados=cant_nodos_visitados_dfs);
sol_bfs = bfs(mapa=juego, posicion=pos_p, nodos_visitados=cant_nodos_visitados_bfs);
sol_astar = astar(mapa=juego, posicion=pos_p, objetivo=pos_obj, cant_nodos_visitados=cant_nodos_visitados_astar);
sol_ucs = ucs(mapa=juego, posicion=pos_p, cant_nodos_visitados=cant_nodos_visitados_ucs);

print();

if sol_dfs is not None:
    print('Camino encontrado con DFS:', sol_dfs, '\nSe evaluaron', cant_nodos_visitados_dfs[0], 'nodos')
    Utils.imprimir_solucion(sol_dfs, deepcopy(juego), pos_obj);

else:
    print('No existe solución utilizando DFS')

print()

if sol_bfs is not None:
    print('Camino encontrado con BFS:', sol_bfs, '\nSe evaluaron', cant_nodos_visitados_bfs[0], 'nodos')
    Utils.imprimir_solucion(sol_bfs, deepcopy(juego), pos_obj);

else:
    print('No existe solución utilizando BFS')

print()

if sol_astar is not None:
    print('Camino encontrado con A*:', sol_astar, '\nSe evaluaron', cant_nodos_visitados_astar[0], 'nodos')
    Utils.imprimir_solucion(sol_astar, deepcopy(juego), pos_obj);

else:
    print('No existe solución utilizando A*')

print()

if sol_ucs is not None:
    print('Camino encontrado con UCS:', sol_ucs, '\nSe evaluaron', cant_nodos_visitados_ucs[0], 'nodos')
    Utils.imprimir_solucion(sol_ucs, deepcopy(juego), pos_obj);

else:
    print('No existe solución utilizando UCS')

print()
