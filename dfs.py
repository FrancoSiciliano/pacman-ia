import Util


def busqueda_dfs(matriz, visitados, posicion, nodos_visitados):
    # Chequeo si la posicion actual no se visito
    if posicion not in visitados:
        objetivo = 'F' 
        # Agrego la posicion actual como posicion visitada e incremento el contador de nodos visitados
        visitados.append(posicion)
        nodos_visitados[0] += 1     

        # Verifico si logre el objetivo en la posicion actual
        if Util.objetivo_alcanzado(matriz, posicion, objetivo):
            return visitados
            
        # Calculo posibles acciones del pacman en base a la posicion actual
        acciones = Util.acciones_pacman(matriz, visitados, posicion)
        for accion in acciones:
            nueva_posicion = Util.obtener_nueva_posicion(posicion, accion)
            # Llamo recursivamente al método
            resultado = busqueda_dfs(matriz, visitados[:], nueva_posicion, nodos_visitados)
            
            # Si encontre un resultado en la llamada recursiva, lo devuelvo
            if resultado is not None:
                return resultado
    return None

# Inicializo cantidad de nodos visitados, el caracter del pacman y la posicion inicial
nodos_visitados = [0]
pacman = 'P'
posicion_pacman = Util.obtener_posicion_objetivo(Util.matriz_pacman, pacman)

solucion = busqueda_dfs(Util.matriz_pacman, [], posicion_pacman, nodos_visitados)
print("Cantidad de ciclos:", nodos_visitados[0])

if solucion is not None:
    print('Camino resultado:', solucion)
else:
    print("No se encontró una solución.")