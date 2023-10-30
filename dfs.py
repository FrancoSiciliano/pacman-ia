import Utils


def dfs(mapa, visitados, posicion, nodos_visitados):
    # Chequeo si la posicion actual no se visito
    if posicion not in visitados:
        # Agrego la posicion actual como posicion visitada e incremento el contador de nodos visitados
        visitados.append(posicion)
        nodos_visitados[0] += 1     

        # Verifico si logre el objetivo en la posicion actual
        if Utils.objetivo_alcanzado(mapa, posicion, 'F'):
            return visitados
            
        # Calculo posibles acciones del pacman en base a la posicion actual
        movimientos = Utils.get_movimientos_posibles(mapa, visitados, posicion)
        for movimiento in movimientos:
            nueva_posicion = Utils.get_nueva_posicion(posicion, movimiento)
            
            # Llamo recursivamente al método
            resultado = dfs(mapa, visitados[:], nueva_posicion, nodos_visitados)
            
            # Si encontre un resultado en la llamada recursiva, lo devuelvo
            if resultado is not None:
                return resultado
    return None