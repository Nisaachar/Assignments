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


# Extracting vertices from the adjacency list
vertices = sorted(adj_list.keys())

# Initializing the adjacency matrix with zeros
num_vertices = len(vertices)
adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

# Filling in the adjacency matrix with the weights
for i, vertex in enumerate(vertices):
    neighbors = adj_list[vertex]
    for neighbor, weight in neighbors:
        j = vertices.index(neighbor)
        adj_matrix[i][j] = weight

# Displaying the adjacency matrix
print('Weighted adjacency matrix:\n\n ')
for row in adj_matrix:
    print(row)
print('\n\n')

# Variables for DFS
visited = {}
tree_edges = []
back_edges = []
path_weights = {}
traversal_stack = []
time_push = 0
time_pop = 0
dfs_order = {}

# Depth-First Search function for traversal and DFS tree construction
def dfs_traversal(vertex, parent, stack, time):
    global visited, back_edges, time_push, dfs_order, time_pop
    visited[vertex] = True
    
    print(f"Pushing {vertex} onto the stack at time {time}")
    stack.append((vertex, time))
    time += 1
    time_push += 1
    dfs_order[vertex] = (time_push, 0)

    for neighbor, weight in adj_list[vertex]:
        if neighbor not in visited:
            print(f"({vertex} {weight}({neighbor} ... {vertex})", end=" ")
            time = dfs_traversal(neighbor, vertex, stack, time)
        elif neighbor != parent:
            back_edges.append((neighbor, vertex))
    time_pop += 1
    dfs_order[vertex] = (dfs_order[vertex][0], time_pop)

    print(f"Popping {vertex} from the stack at time {time}")
    _, popped_time = stack.pop()
    print(f"Ordering of vertices: {vertex}, ", end="")
    time += 1

    return time

# Depth-First Search function for DFS tree construction and path weights
def dfs_tree(vertex, parent, time, weight_sum):
    global visited, tree_edges, back_edges, path_weights
    visited[vertex] = True

    for neighbor, weight in adj_list[vertex]:
        if neighbor not in visited:
            tree_edges.append((vertex, neighbor, weight))
            path_weights[neighbor] = weight_sum + weight
            dfs_tree(neighbor, vertex, time, path_weights[neighbor])
        elif neighbor != parent:
            back_edges.append((vertex, neighbor))

# Perform DFS traversal from vertex A
start_vertex = 'A'
dfs_traversal(start_vertex, None, traversal_stack, 1)

# Display traversal stack

for vertex, timestamp in traversal_stack:
    print(f"{vertex}({timestamp})", end=" -> ")
print("END")

print("\n\n(FILO Queue) Traversal's stack with time-stamp:")
for vertex, (push_time, pop_time) in dfs_order.items():
    print(f"{vertex}({push_time}, {pop_time})", end=" -> ")
print("END")

# # Display orderings of vertices yielded by DFS traversal
# print("\n\n(FILO Queue) Orderings of vertices yielded by DFS:", ", ".join(visited.keys()))

# Perform DFS tree construction from vertex A
start_vertex = 'A'
dfs_tree(start_vertex, None, 1, 0)


# Display back edges


##displaying weiaghts##

visited = {}
tree_edges = []
back_edges2 = []
path_weights = {}

# Depth-First Search function
def dfs(vertex, parent, time, weight_sum):
    global visited, tree_edges, back_edges2, path_weights
    visited[vertex] = True

    for neighbor, weight in adj_list[vertex]:
        if neighbor not in visited:
            tree_edges.append((vertex, neighbor, weight))
            path_weights[neighbor] = weight_sum + weight
            dfs(neighbor, vertex, time, path_weights[neighbor])
        elif neighbor != parent:
            back_edges2.append((vertex, neighbor))

# Perform DFS from vertex A
start_vertex = 'A'
dfs(start_vertex, None, 1, 0)



#tree edges
print("\nDFS Tree Forest:")
for edge in tree_edges:
    print(f"({edge[0]} {edge[2]}({edge[1]}))", end=", ")
print()

print("\nBack Edges:")
for edge in back_edges:
    print(f"({edge[0]}, {edge[1]})", end=", ")
print()


# Display path weights from source A
print("\nPath Weights from source A:")
for vertex, weight in path_weights.items():
    print(f"Path to {vertex} has total weight {weight}")