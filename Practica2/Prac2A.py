import time
import tracemalloc

# Algoritmo de búsqueda en profundidad (BFS)
def bfs(graph, root, solution):
    print("\tInicia BFS")
    
    # tracemalloc.start() empieza a medir la memoria
    # start_time = time.time() inicia el tiempo
    tracemalloc.start()
    start_time = time.time()

    # Inicializa la cola
    queue = [root]
    
    # Inicializa los nodos visitados
    #len(graph) + 1 es el tamaño del grafo
    visited_nodes = [False] * (len(graph) + 1)
   
    # Marca el nodo raíz como visitado
    visited_nodes[root] = True

    # Mientras la cola no esté vacía
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
                # Añade el nodo hijo a la cola
                queue = queue + [child]

        if current_node == solution:
            print(f"Solucion encontrada en: {current_node}")
            # Vacía la cola
            queue = []

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Execution Time: ", end_time - start_time)
    print(f"Max memory: {peak / 10*6} MB  Current memory: {current / 10*6} MB\n\n")

grafo = {
    1: [3, 2],
    2: [1, 5, 4],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

root = 1
solution = 5
bfs(grafo, root, solution)