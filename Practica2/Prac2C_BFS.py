import time
import tracemalloc
import networkx as nx
import matplotlib.pyplot as plt

# Algoritmo de bÃºsqueda en profundidad (DFS)
def bfs(graph, root, solution):
    print("\tInicia BFS")

    # tracemalloc.start() empieza a medir la memoria
    # start_time = time.time() inicia el tiempo
    tracemalloc.start()
    start_time = time.time()

    # Inicializa la cola
    queue = [root]

    # Inicializa los nodos visitados
    #len(graph) + 1 es el tamaÃ±o del grafo
    visited_nodes = [False] * (len(graph) + 1)

    # Marca el nodo raÃ­z como visitado
    visited_nodes[root] = True

    # Mientras la cola no estÃ© vacÃ­a
    # Obtiene el primer elemento de la cola
    while len(queue) > 0:

        # current_node = queue[0] es el primer elemento de la cola
        current_node = queue[0]
        print("Nodo actual: ", current_node)

        # Elimina el primer elemento de la cola
        # Ejemplo: queue = [1, 2, 3] -> queue = [2, 3]
        queue = queue[1:]

        # Obtiene los valores de la clave current_node
        for child in graph[current_node]:
            # Si el nodo hijo no ha sido visitado
            if not visited_nodes[child]:

                # Marca el nodo hijo como visitado
                visited_nodes[child] = True
                # AÃ±ade el nodo hijo a la cola
                queue = queue + [child]

        if current_node == solution:
            print(f"Solucion encontrada en: {current_node}")
            # VacÃ­a la cola
            queue = []

        plot_graph(graph, root, solution, current_node)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Execution Time: ", end_time - start_time)
    print(f"Max memory: {peak / 10*6} MB  Current memory: {current / 10*6} MB\n\n")

def plot_graph(grafo, nodo_raiz, nodo_sol, nodo_actual):
    G = nx.Graph()

    vecinos_raiz = grafo.get(nodo_raiz, [])

    G.add_node(nodo_raiz)

    for nodo in vecinos_raiz:
        G.add_edge(nodo_raiz, nodo)

    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)

    # Usar el layout de Graphviz a traves de pydot
    pos_raiz = nx.nx_pydot.graphviz_layout(G, prog='dot')
    pos = nx.nx_pydot.graphviz_layout(G, prog='dot')

    # Dibujar el grafo
    nx.draw(G, pos_raiz, with_labels=True, node_color='lightblue', node_size=500, font_size=11, font_weight='bold')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=11, font_weight='bold')

    # Resaltar el nodo solucion y el nodo rai­z
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_sol], node_color='red', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_raiz], node_color='yellow', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_actual], node_color='green', node_size=700)

    plt.show()

grafo = {
    1: [2, 5, 8],
    2: [1, 3, 4],
    3: [2],
    4: [2],
    5: [1, 6, 7],
    6: [5],
    7: [5],
    8: [1, 9, 10],
    9: [8],
    10: [8]
}

root = 1
solution = 10
bfs(grafo, root, solution)