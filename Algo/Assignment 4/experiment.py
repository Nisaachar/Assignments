adj_list = {
    'A': [('B', 10), ('K', 3)],
    'B': [('C', 36), ('A', 10)],
    'C': [('B', 36), ('D', 3)],
    'D': [('K', 16), ('X', 1), ('C', 3)],
    'E': [('X', 22), ('I', 3), ('H', 10)],
    'F': [('X', 10)],
    'G': [('t', 9)],
    'H': [('E', 10), ('Z', 13), ('O', 4)],
    'h': [('R', 27), ('P', 17), ('O', 13)],
    'I': [('N', 4), ('n', 1), ('E', 3)],
    'J': [('K', 18), ('n', 1), ('L', 16)],
    'K': [('D', 16), ('A', 3), ('J', 18)],
    'L': [('J', 16), ('Y', 3)],
    'M': [('n', 4), ('N', 21)],
    'N': [('I', 4), ('M', 21), ('Z', 16)],
    'n': [('J', 1), ('I', 1), ('M', 4)],
    'O': [('T', 8), ('H', 4), ('h', 13)],
    'P': [('h', 17), ('Y', 6), ('S', 4)],
    'Q': [('Z', 4)],
    'R': [('h', 27)],
    'S': [('P', 4), ('Y', 8), ('U', 9)],
    'T': [('O', 8), ('V', 16), ('U', 1)],
    't': [('W', 8), ('G', 9), ('U', 1)],
    'U': [('T', 1), ('t', 1), ('S', 9)],
    'V': [('T', 16)],
    'W': [('t', 8)],
    'X': [('D', 1), ('F', 10), ('E', 22)],
    'Y': [('S', 8), ('L', 3), ('P', 6)],
    'Z': [('Q', 4), ('N', 16), ('H', 13)]
}


# Variables for DFS
visited = {}
dfs_tree_edges = []
dfs_order = {}
traversal_stack = []
time_push = 0
time_pop = 0

# Depth-First Search function
def dfs(vertex):
    global visited, dfs_tree_edges, dfs_order, traversal_stack, time_push, time_pop
    visited[vertex] = True
    time_push += 1
    dfs_order[vertex] = (time_push, 0)  # Initialize pop time to 0

    traversal_stack.append((vertex, time_push))

    for neighbor, weight in adj_list[vertex]:
        if neighbor not in visited:
            dfs_tree_edges.append((vertex, neighbor, weight))
            dfs(neighbor)

    # Update pop time when a vertex becomes a dead-end
    _, pop_vertex_time = traversal_stack.pop()
    time_pop += 1
    dfs_order[vertex] = (dfs_order[vertex][0], time_pop)

# Perform DFS from vertex A
start_vertex = 'A'
dfs(start_vertex)

# Display traversal stack with timestamps
print("Traversal's stack with time-stamp:")
for vertex, (push_time, pop_time) in dfs_order.items():
    print(f"{vertex}({push_time}, {pop_time})", end=" -> ")
print("END")

# Display orderings of vertices yielded by DFS
print("\nOrderings of vertices yielded by DFS:", ", ".join(dfs_order.keys()))

# Display DFS tree forest
print("\nDFS Tree Forest:")
for edge in dfs_tree_edges:
    print(f"({edge[0]} {edge[2]}({edge[1]})", end=", ")