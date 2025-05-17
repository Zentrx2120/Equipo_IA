import numpy as np
import matplotlib.pyplot as plt
import tracemalloc
import time

# ---------- Laberinto ----------
laberinto = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
])

# ---------- Parámetros ----------
nodo_raiz = (1, 1)
meta = (17, 17)
movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # solo ortogonales

# ---------- Heurísticas ----------
# La heurística utilizada es la distancia Manhattan
# entre el nodo actual y la meta.
def heuristica_manhattan(nodo_actual, objetivo):
    # abs(x2 - x1) + abs(y2 - y1)
    return abs(objetivo[0] - nodo_actual[0]) + abs(objetivo[1] - nodo_actual[1])

# Nueva heurística: distancia Euclidiana
# entre el nodo actual y la meta.
def heuristica_euclidiana(nodo_actual, objetivo):
    # sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return ((objetivo[0] - nodo_actual[0])**2 + (objetivo[1] - nodo_actual[1])**2) ** 0.5

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Se modifica para recibir la heurística como parámetro
def A_estrella(laberinto, punto_inicial, meta, heuristica):
    # Inicia el seguimiento de la memoria
    # y el tiempo de ejecución
    tracemalloc.start()
    start_time = time.time()

    # Inicializa la lista abierta con el nodo inicial
    # y la lista cerrada como una matriz de ceros
    lista_abierta = [(punto_inicial, 0, heuristica(punto_inicial, meta), [])]
    filas, columnas = laberinto.shape
    lista_cerrada = np.zeros((filas, columnas))
    # considerados es una lista para almacenar los nodos considerados
    considerados = []

    # Mientras haya nodos en la lista abierta
    # se sigue buscando la solución
    while lista_abierta:
        # Se obtiene el nodo con menor f
        # y se elimina de la lista abierta
        # Se añade a la lista de considerados
        # Se actualiza la lista cerrada
        nodo_actual, g_actual, f_actual, camino_actual = min(lista_abierta, key=lambda x: x[2])
        lista_abierta.remove((nodo_actual, g_actual, f_actual, camino_actual))
        considerados.append(nodo_actual)

        # Si se encuentra la meta, se detiene el seguimiento de memoria
        if nodo_actual == meta:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print("Tiempo de ejecución:", end_time - start_time)
            print(f"Memoria máxima: {peak / 10**6} MB  Memoria actual: {current / 10**6} MB\n")
            return camino_actual + [nodo_actual], considerados

        lista_cerrada[nodo_actual] = 1

        for dx, dy in movimientos:
            new_pos = (nodo_actual[0] + dx, nodo_actual[1] + dy)
            if (0 <= new_pos[0] < filas) and (0 <= new_pos[1] < columnas):
                if laberinto[new_pos] == 0 and lista_cerrada[new_pos] == 0:
                    g_nuevo = g_actual + 10
                    f_nuevo = g_nuevo + heuristica(new_pos, meta)

                    # Verificar si ya está con mejor g
                    if not any(n == new_pos and g <= g_nuevo for n, g, f, c in lista_abierta):
                        lista_abierta.append((new_pos, g_nuevo, f_nuevo, camino_actual + [nodo_actual]))

    # Si no se encuentra la meta
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("No se encontró solución.")
    print("Tiempo de ejecución:", end_time - start_time)
    print(f"Memoria máxima: {peak / 10**6} MB  Memoria actual: {current / 10**6} MB\n")
    return None, considerados

# ---------- Visualización ----------
def graficar_laberinto(laberinto, considerados, camino, nombre_heuristica):
    # Visualiza el laberinto y el camino encontrado
    plt.imshow(laberinto, cmap='binary')
    for i in considerados:
        plt.plot(i[1], i[0], 'o', color='blue')
    for j in camino:
        plt.plot(j[1], j[0], 'o', color='red')
    plt.title(f"Heurística {nombre_heuristica} - Nodos considerados: {len(considerados)}")
    plt.show()

# ---------- Ejecución principal ----------
if __name__ == "__main__":
    # Comparación con heurística Manhattan
    print("Usando heurística Manhattan:")
    camino_manhattan, considerados_manhattan = A_estrella(laberinto, nodo_raiz, meta, heuristica_manhattan)
    if camino_manhattan:
        graficar_laberinto(laberinto, considerados_manhattan, camino_manhattan, "Manhattan")

    # Comparación con heurística Euclidiana
    print("Usando heurística Euclidiana:")
    camino_euclidiana, considerados_euclidiana = A_estrella(laberinto, nodo_raiz, meta, heuristica_euclidiana)
    if camino_euclidiana:
        graficar_laberinto(laberinto, considerados_euclidiana, camino_euclidiana, "Euclidiana")
