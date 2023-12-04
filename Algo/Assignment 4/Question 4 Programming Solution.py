from collections import deque

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


# Variables for BFS
visited = {}
bfs_tree_edges = []
back_edges = []
forward_edges = []
cross_edges = []
bfs_order = {}
traversal_queue = deque()

# Breadth-First Search function
def bfs(vertex):
    global visited, bfs_tree_edges, back_edges, forward_edges, cross_edges, bfs_order, traversal_queue
    time = 1
    visited[vertex] = True
    bfs_order[vertex] = time
    traversal_queue.append((vertex, time))
    print(f"\n At time {time}, we have traversed to the node A and the queue so far is:", ", ".join(bfs_order.keys()))

    while traversal_queue:
        current_vertex, current_time = traversal_queue.popleft()
        time += 1

        for neighbor, weight in adj_list[current_vertex]:
            if neighbor not in visited:
                visited[neighbor] = True
                bfs_tree_edges.append((current_vertex, neighbor, weight))
                bfs_order[neighbor] = time
                traversal_queue.append((neighbor, time))
                # print(f"Queue after adding {neighbor}: {list(traversal_queue)}")
                print(f"\n At time {time}, we have traversed to the node {neighbor} and the queue so far is:", ", ".join(bfs_order.keys()))

            else:
                if bfs_order[neighbor] < bfs_order[current_vertex]:
                    back_edges.append((current_vertex, neighbor))
                elif bfs_order[neighbor] == bfs_order[current_vertex] + 1:
                    forward_edges.append((current_vertex, neighbor))
                else:
                    cross_edges.append((current_vertex, neighbor))

# Perform BFS from vertex A
start_vertex = 'A'
bfs(start_vertex)

# Display orderings of vertices yielded by BFS
print("\nOrderings of vertices yielded by BFS:", ", ".join(bfs_order.keys()))

# Display BFS tree forest and categorized edges
print("\nBFS Tree Forest:")
for edge in bfs_tree_edges:
    print(f"({edge[0]} {edge[2]}({edge[1]}))", end=", ")
print()

print("\nBack Edges:")
for edge in back_edges:
    print(f"({edge[0]}, {edge[1]})", end=", ")
print()

print("\nForward Edges:")
for edge in forward_edges:
    print(f"({edge[0]}, {edge[1]})", end=", ")
print()

print("\nCross Edges:")
for edge in cross_edges:
    print(f"({edge[0]}, {edge[1]})", end=", ")

##For calculating the shortest distance##

def bfs_minimum_weight_path(adj_list, start, end):
    visited = set()
    queue = deque([(start, [])])  # Queue of tuples (vertex, path)
    
    while queue:
        current, path = queue.popleft()
        visited.add(current)
        
        for neighbor, weight in adj_list[current]:
            if neighbor not in visited:
                new_path = path + [(current, neighbor, weight)]
                if neighbor == end:
                    return new_path  # Return the path once 'G' is reached
                queue.append((neighbor, new_path))
                visited.add(neighbor)
    
    return None  # Return None if no path is found

# Call the function to find the minimum weight path from 'A' to 'G'
start_vertex = 'A'
end_vertex = 'G'
minimum_weight_path = bfs_minimum_weight_path(adj_list, start_vertex, end_vertex)

if minimum_weight_path:
    total_weight = sum(edge[2] for edge in minimum_weight_path)
    print(f"\n\nMinimum weight path from {start_vertex} to {end_vertex}:")
    print("Path:", ' -> '.join(f"{edge[0]}-{edge[1]}({edge[2]})" for edge in minimum_weight_path))
    print(f"Total Weight: {total_weight}")
else:
    print(f"No path found between {start_vertex} and {end_vertex}")