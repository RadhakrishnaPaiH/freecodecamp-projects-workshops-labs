INF = float('inf')  # Represent infinity (used for no connection between nodes)

# Adjacency matrix representing graph weights
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)  # Number of nodes in the graph

    # Distance from start_node to every other node (initially infinity)
    distances = [INF] * n
    distances[start_node] = 0  # Distance to itself is 0

    # Store path to each node (initially each node is its own path)
    paths = [[node_no] for node_no in range(n)]

    # Track visited nodes to avoid reprocessing
    visited = [False] * n

    # Main loop: runs n times (Dijkstra-like process)
    for _ in range(n):

        # Find the unvisited node with smallest known distance
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # If no reachable node is found, stop early
        if current == -1:
            break

        # Mark current node as visited
        visited[current] = True

        # Relax all neighbors of current node
        for node_no in range(n):
            distance = matrix[current][node_no]  # edge weight

            # If edge exists and node not visited
            if distance != INF and not visited[node_no]:

                # Calculate new possible distance
                new_distance = distances[current] + distance

                # Update if a shorter path is found
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance

                    # Update path to include this node
                    paths[node_no] = paths[current] + [node_no]

    # Decide which nodes to print results for
    targets = [target_node] if target_node is not None else range(n)

    # Print results for each target node
    for node_no in targets:

        # Skip start node and unreachable nodes
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Convert path list into a readable string like "0 -> 1 -> 3"
        string_path = (str(n) for n in paths[node_no])  # NOTE: logical bug here
        path = ' -> '.join(string_path)

        # Print final result
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    return distances, paths


# Run the function
shortest_path(adj_matrix, 0, 5)
