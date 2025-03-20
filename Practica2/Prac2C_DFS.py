import time
import tracemalloc
import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, root, solution):
    print("\tInicia DFS")
    tracemalloc.start()
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

        plot_graph(grafo, root, solution, current_node)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Execution Time: ", end_time - start_time)
    print(f"Max memory: {peak / 10**6} MB  Current memory: {current / 10**6} MB\n\n")

def plot_graph(grafo, nodo_raiz, nodo_sol, nodo_actual):
    G = nx.Graph()

    vecinos_raiz = grafo.get(nodo_raiz, [])

    G.add_node(nodo_raiz)

    for nodo in vecinos_raiz:
        G.add_edge(nodo_raiz, nodo)

    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)

    pos_raiz = nx.nx_pydot.graphviz_layout(G, prog='dot')
    pos = nx.nx_pydot.graphviz_layout(G, prog='dot')

    nx.draw(G, pos_raiz, with_labels=True, node_color='lightblue', node_size=500, font_size=11, font_weight='bold')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=11, font_weight='bold')

    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_sol], node_color='red', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_raiz], node_color='yellow', node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_actual], node_color='green', node_size=700)

    plt.show()

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

root = 10
#solution = random.randrange(1, len(graph) + 1)
solution = 3
print(f"La solucion esta en el nodo {solution}\n")
dfs(graph_2, root, solution)