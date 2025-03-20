import tracemalloc
import time
import numpy as np
import matplotlib.pyplot as plt

maze1 = [
    [1,0,1,0,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1],
    [1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0],
    [1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1],
    [0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
    [0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0],
    [1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1],
    [0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0],
    [1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0],
    [1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1],
    [0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0],
    [1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
    [1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1],
    [1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0],
    [1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1]
]

maze2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

maze3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0],
    [0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0],
    [0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0],
    [0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0],
    [0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0],
    [0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0],
    [0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

maze = np.array(maze2)

initial_point = (1, 1)
#final_point = (18, 15)
final_point = (23, 23)
#global cont_puntos
no_puntos = []

# Movement types
#movements = [(0, 1), (1, 0), (0, -1), (-1, 0)] Right, down, left, up
movements = [[(0, 1), (1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1), (1, 0)],
            [(1, 0), (-1, 0), (0, 1),  (0, -1)], [(1, 0), (0, -1), (-1, 0), (0, 1)]]

def dfs(maze, root_node, final_point, n):
    print("\t--- Inicio DFS ---")
    # Start time measure and memmory
    tracemalloc.start() # Start memmory mesurement
    start_time = time.time() # Time start referenced
    resources = None

    stack = [(root_node, [])] # Initialize a stack

    # Maze size
    rows = np.shape(maze)[0]
    cols = np.shape(maze)[1]

    # Mirror maze
    visited_nodes = np.zeros((rows, cols))
    visited_nodes[root_node]
    # List for saving rute
    considered_nodes = []

    while len(stack) > 0:
        # Obtain last stack position
        current_node, path = stack[-1]
        # print("Current node: ", current_node)

        # Pop
        stack = stack[:-1]

        considered_nodes += [current_node]

        # En caso de ser la sulución
        if current_node == final_point:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            resources = {
                "time": end_time - start_time,
                "max_mem_MB": peak / 10**6,
                "curr_mem_MB": current / 10**6
            }

            return path + [current_node], considered_nodes, resources

        visited_nodes[current_node[0], current_node[1]] = 1

        for direction in movements[n]:
            # Check if neighbour node is a wall, is visited or inside limits
            new_position = (current_node[0] + direction[0], current_node[1] + direction[1])

            if ((new_position[0] > 0 and new_position[0] < rows)
                and (new_position[1] > 0 and new_position[1] < cols)):
                    if(visited_nodes[new_position[0], new_position[1]] == 0
                       and maze[new_position[0], new_position[1]] == 0):
                         stack += [(new_position, path + [current_node])]

    return None, considered_nodes, resources

def plot_maze(maze, considered, path):
    cont_puntos = 0
    plt.imshow(maze, cmap = 'binary')

    if(considered):
        for i in considered:
            plt.plot(i[1], i[0], 'o', color = 'blue')
            cont_puntos += 1

    if(path):
        for j in path:
            plt.plot(j[1], j[0], 'o', color = 'red')
            cont_puntos += 1

    no_puntos.append(cont_puntos)
    plt.show()

def plot_best_maze(maze, considered, path):
    cont_puntos = 0
    plt.imshow(maze, cmap = 'binary')

    if(considered):
        for i in considered:
            plt.plot(i[1], i[0], 'o', color = 'blue')
            cont_puntos += 1

    if(path):
        for j in path:
            plt.plot(j[1], j[0], 'o', color = 'red')
            cont_puntos += 1

    no_puntos.append(cont_puntos)
    plt.show()

n = 4
no_puntos_mejor = 5000
best_path = None
best_considered = None

for i in range(n):
    path, considered, resources = dfs(maze, initial_point, final_point, i)
    print("Recuros DFS: ", resources)
    plot_maze(maze, considered, path)

    if no_puntos[i] < no_puntos_mejor:
        no_puntos_mejor = no_puntos[i]
        best_path = path
        best_considered = considered

print("Número de puntos explorados para cada orden de movimientos:", no_puntos)
print("Mejor número de puntos explorados:", no_puntos_mejor)
plot_best_maze(maze, best_considered, best_path)