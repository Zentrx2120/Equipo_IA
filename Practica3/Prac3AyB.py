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
final_point = (18, 15)

# Movement types
movements = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, down, left, up

def dfs(maze, root_node, final_point):
    print("\t--- Inicio DFS ---")
    # Start time measure and memmory
    tracemalloc.start() # Start memmory mesurement
    start_time = time.time() # Time start reference
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

        # Check if current node is the solution
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

        for direction in movements:
            # Check if neighbour node is a wall, is visited or inside limits
            new_position = (current_node[0] + direction[0], current_node[1] + direction[1])
            
            if ((new_position[0] > 0 and new_position[0] < rows) 
                and (new_position[1] > 0 and new_position[1] < cols)):
                    if(visited_nodes[new_position[0], new_position[1]] == 0 
                       and maze[new_position[0], new_position[1]] == 0):
                         stack += [(new_position, path + [current_node])]
    
    return None, considered_nodes, resources


def bfs(maze, root_node, final_point):
    print("\t--- Inicio BFS ---")

    # Start time measure and memmory
    tracemalloc.start() # Start memmory mesurement
    start_time = time.time() # Time start reference
    resources = None

    queue = [(root_node, [])] # Initialize a queue

    # Maze size
    rows = np.shape(maze)[0]
    cols = np.shape(maze)[1]
    
    # Mirror maze
    visited_nodes = np.zeros((rows, cols))
    visited_nodes[root_node] = True
    # List for saving route
    considered_nodes = []

    while len(queue) > 0:
        # Obtain first queue position
        current_node, path = queue[0]
        # print("Current node: ", current_node)

        # Deque
        queue = queue[1:]

        considered_nodes += [current_node]

        # Check if current node is the solution
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

        for direction in movements:
            # Check if neighbour node is a wall, is visited or inside limits
            new_position = (current_node[0] + direction[0], current_node[1] + direction[1])
            
            if ((new_position[0] > 0 and new_position[0] < rows) 
                and (new_position[1] > 0 and new_position[1] < cols)):
                    if(visited_nodes[new_position[0], new_position[1]] == 0 
                       and maze[new_position[0], new_position[1]] == 0):
                         queue += [(new_position, path + [current_node])]
    
    return None, considered_nodes, resources


def plot_maze(maze, considered, path):
    plt.imshow(maze, cmap = 'binary')

    if(considered):
        for i in considered:
            plt.plot(i[1], i[0], 'o', color = 'blue')

    if(path):
        for j in path:
            plt.plot(j[1], j[0], 'o', color = 'red')
    
    plt.show()

path, considered, resources = dfs(maze, initial_point, final_point)
print("Recuros DFS: ", resources)
plot_maze(maze, considered, path)

path, considered, resources = bfs(maze, initial_point, final_point)
print("Recuros BFS: ", resources)
plot_maze(maze, considered, path)