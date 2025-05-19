import numpy as np
import matplotlib.pyplot as plt
import tracemalloc
import time
import random

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
movimientos_base = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # solo ortogonales

# ---------- Heurística ----------
def heuristica(nodo_actual, objetivo):
    return abs(objetivo[0] - nodo_actual[0]) + abs(objetivo[1] - nodo_actual[1])

# ---------- A* ----------
def A_estrella(laberinto, punto_inicial, meta):
    tracemalloc.start()
    start_time = time.time()

    lista_abierta = [(punto_inicial, 0, heuristica(punto_inicial, meta), [])]
    filas, columnas = laberinto.shape
    lista_cerrada = np.zeros((filas, columnas))
    considerados = []
    energia_total = 0  # Inicializar la energía total

    while lista_abierta:
        nodo_actual, g_actual, f_actual, camino_actual = min(lista_abierta, key=lambda x: x[2])
        lista_abierta = [
            item for item in lista_abierta
            if item != (nodo_actual, g_actual, f_actual, camino_actual)]
        considerados += [nodo_actual]
        energia_total += g_actual  # Sumar el costo g del nodo actual a la energía total

        if nodo_actual == meta:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return camino_actual + [nodo_actual], considerados, energia_total

        lista_cerrada[nodo_actual] = 1

        for dx, dy in movimientos_base:
            new_pos = (nodo_actual[0] + dx, nodo_actual[1] + dy)
            if (0 <= new_pos[0] < filas) and (0 <= new_pos[1] < columnas):
                if laberinto[new_pos] == 0 and lista_cerrada[new_pos] == 0:
                    g_nuevo = g_actual + 10
                    f_nuevo = g_nuevo + heuristica(new_pos, meta)

                    if not any(n == new_pos and g <= g_nuevo for n, g, f, c in lista_abierta):
                        lista_abierta = lista_abierta + [(new_pos, g_nuevo, f_nuevo, camino_actual + [nodo_actual])]

    return None, considerados, energia_total

# ---------- Visualización ----------
def graficar_resultados(laberinto, resultados):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs = axs.flatten()

    for i, (camino, considerados, energia_total) in enumerate(resultados):
        axs[i].imshow(laberinto, cmap='binary')
        for nodo in considerados:
            axs[i].plot(nodo[1], nodo[0], 'o', color='blue')
        for nodo in camino:
            axs[i].plot(nodo[1], nodo[0], 'o', color='red')
        axs[i].set_title(f"Iteración {i+1}\nNodos considerados: {len(considerados)}\nLongitud del camino: {len(camino)}\nEnergía total: {energia_total}")

    plt.tight_layout()
    plt.show()

# ---------- Ejecución principal ----------
if __name__ == "__main__":
    resultados = []
    for _ in range(4):
        random.shuffle(movimientos_base)  # Barajar los movimientos
        camino, considerados, energia_total = A_estrella(laberinto, nodo_raiz, meta)
        resultados.append((camino, considerados, energia_total))

    graficar_resultados(laberinto, resultados)
