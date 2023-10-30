import Util


def busqueda_dfs(matriz, visitados, posicion, nodos_visitados):
    if posicion not in visitados:
        objetivo = 'F' 
        visitados.append(posicion)
        nodos_visitados += 1     

        if Util.objetivo_alcanzado(matriz, posicion, objetivo):
            return visitados
            
        acciones = Util.acciones_pacman(matriz, visitados, posicion)
        for accion in acciones:
            nueva_posicion = Util.obtener_nueva_posicion(posicion, accion)
            resultado = busqueda_dfs(matriz, visitados[:], nueva_posicion, nodos_visitados)

            if resultado is not None:
                return resultado
    return None


nodos_visitados = 0
pacman = 'P'
posicion_pacman = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solucion = busqueda_dfs(Util.matriz_pacman, [], posicion_pacman, nodos_visitados)
print("Cantidad de ciclos:", nodos_visitados)

if solucion is not None:
    print('Camino resultado:', solucion)
else:
    print("No se encontró una solución.")