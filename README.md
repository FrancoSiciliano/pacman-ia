# Ejecución de los algoritmos
Para ejecutar todos los algoritmos a la vez ejecutar el script: ```run.py```  
Para ejecutar cada algoritmo individualmente se debe ejecutar cada archivo por separado.

## Precondiciones
### Matriz usada para los algoritmos
Si bien utilizamos la siguiente matriz, puede utilizarse cualquier otra disposición, siempre que 
se respeten las cantidad de P, W y F que se mencionan en la sección **Objetivo**.
```
['-', '-', '-', '-', '-']  
['-', 'W', '-', '-', '-']  
['P', '-', 'W', 'F', '-']  
['-', '-', '-', '-', '-']
```
P: posición de comienzo del Pacman.  
W: posición de obstáculos (walls).  
F: posición del objetivo (food).

Se considera que los limites de la matriz son los limites por donde el Pacman puede moverse.

### Objetivo
El objetivo del Pacman es posicionarse donde se encuentra la 'F' utilizando los siguientes 
movimientos: LEFT, RIGHT, UP, DOWN y evitando las 'W', es decir, no puede posicionarse en dicho 
lugar.  
Solo se tendrá un 'F' por matriz al igual que una 'P'. Si se podrá tener tantas 'W' como se 
quiera.

## Algoritmos utilizados
### Depth First Search (DFS)
- DFS es un algoritmo de búsqueda que explora en profundidad un grafo o un árbol.  
Comienza desde un nodo inicial y continúa explorando todos los nodos vecinos antes de retroceder.  
- Es un tipo de búsqueda no informado, lo que significa que no utiliza información heurística para 
guiar la búsqueda. 

### Breadth First Search (BFS)
- BFS es un algoritmo de búsqueda que explora en anchura un grafo o un árbol.  
Comienza desde un nodo inicial y explora todos los nodos vecinos a una profundidad dada antes de 
avanzar a la siguiente profundidad.  
- Es un tipo de búsqueda no informado.

### Uniform Cost Search (UCS)
- UCS es un algoritmo de búsqueda que encuentra el camino de costo mínimo en un grafo o un árbol 
  con aristas o ramas de costo **no negativo**.  
- En lugar de explorar en profundidad o en anchura, UCS selecciona el camino con el **menor costo
acumulado** en cada paso.
- Utiliza una cola de prioridad, donde los nodos se ordenan según el costo acumulado hasta ese 
  punto.

### A-Star (A*)
- A* es un algoritmo de búsqueda informado que utiliza elementos de búsqueda de costo uniforme.
- Utiliza una función de evaluación heurística para estimar el costo restante hasta la meta.
- A* considera tanto el costo acumulado hasta el momento como la estimación heurística al decidir
qué nodo explorar a continuación.
- Utiliza una cola de prioridad para ordenar los nodos en función del costo acumulado más la
estimación heurística.


## Conclusiones
Tanto UCS como A* son algoritmos óptimos, lo que significa que encuentran la solución óptima si 
existe. En cambio, DFS y BFS pueden no ser óptimos, explorando todo el espacio de búsqueda en el 
peor de los casos.


Aplicando cada uno de los algoritmos mencionados a la matriz que está como precondición 
obtuvimos los siguientes resultados:

```
Number of cycles in DFS: 14
Path of DFS: [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (2, 3)]
```
```
Number of cycles in BFS: 16
Path of BFS: [(2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3)]
```
```
Number of cycles in UCS: 16
Path of Uniform Cost: [(2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3)]
```
```
Number of cycles in A*: 11
Path of A*: [(2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3)]
```

Pudimos observar que el **algortimo A*** fue el más óptimo en cuanto a caminos recorridos gracias 
a la función heurísitica la cual proporciona informacion adicional sobre el camino que conduce a la 
solución.  

Para la matriz utilizada, los algoritmos BFS, UCS y A* encontraron el camino óptimo de la solución 
recorriendo en total **6 nodos**, incluyendo la posición incial del Pacman y del objetivo ('F').  

Respecto al algoritmo DFS si bien tuvo una menor cantidad de nodos recorridos que los algoritmos 
BFS y UCS, tuvo un camino solución más largo, de **14 nodos contra 6 nodos**, siendo este un 
camino no óptimo en término de nodos recorridos.
