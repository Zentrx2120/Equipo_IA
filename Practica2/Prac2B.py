"""
A) Realizar el algoritmo BFS y que aplique para cualquier grafo y nodo raíz
B) Tanto para BFS y DFS seleccionar un nodo aleatorio el cual sea una solución.
    Cuando los algoritmos analicen ese nodo parar el programa y poner donde
    se ecnotró la solución. 
        * Para corroborar, se deberá comenzar poniendo: "La solución está en el nodo: X"
            1
            2
            3
            Sol encontrada en 5
C) Se deberán gráficar los grafos ingresados en un orden por niveles (1, 2, 3, ...)
    y el nodo solución cambia de color y los visitados ponerlos en verde
"""

import networkx as nx
import matplotlib.pyplot as plt
import tracemalloc
import time
import random 


def dfs(graph, root, solution):
    print("\tInicia DFS")
    # Start time measure and memmory
    tracemalloc.start() # Start memmory mesurement
    start_time = time.time() # Time start reference

    stack = [root] # Initialize a stack
    
    visited_nodes = [False] * (len(graph) + 1)
    
    visited_nodes[root] # Set root as visited

    while len(stack) > 0:
        # Obtain last stack position
        current_node = stack[-1]
        print("Current node: ", current_node)

        # Pop
        stack = stack[:-1]

        # Obtain values of the key current_node
        for children in graph[current_node]:
            if not visited_nodes[children]:
                # Mark as visited children not visited
                visited_nodes[children] = True
                # Put children to the stack
                stack = stack + [children]

        if current_node == solution:
            print(f"Solucion encontrada en: {current_node}")
            stack = []

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Execution Time: ", end_time - start_time)
    print(f"Max memory: {peak / 10**6} MB  Current memory: {current / 10**6} MB\n\n")
    

def bfs(graph, root, solution):
    print("\tInicia BFS")
    # Start time measure and memmory
    tracemalloc.start() # Start memmory mesurement
    start_time = time.time() # Time start reference

    queue = [root] # Initialize a stack
    
    visited_nodes = [False] * (len(graph) + 1)
    # Set root as visited
    visited_nodes[root] = True

    while len(queue) > 0:
        current_node = queue[0] # Get first queue position value
        print("Current node: ", current_node)

        # Pop
        queue = queue[1:]

        # Obtain values of the key current_node
        for child in graph[current_node]:
            if not visited_nodes[child]:
                # Mark as visited child not visited
                visited_nodes[child] = True
                # Put child to the queue
                queue = queue + [child]

        if current_node == solution:
            print(f"Solucion encontrada en: {current_node}")
            queue = []

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Execution Time: ", end_time - start_time)
    print(f"Max memory: {peak / 10*6} MB  Current memory: {current / 10*6} MB\n\n")
    

graph_1 = {
    1: [3, 2],
    2: [1, 5, 4],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

graph_2 = {
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

graph = graph_2
root = 1
solution = random.randrange(1, len(graph) + 1)
print(f"La solucion esta en el nodo {solution}\n")

bfs(graph, root, solution)
dfs(graph, root, solution)
