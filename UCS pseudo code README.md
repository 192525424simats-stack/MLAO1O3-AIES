procedure UCS(start, goal):
    create priority_queue frontier
    add (0, start, [start]) to frontier
    create empty set visited

    while frontier is not empty:
        (cost, node, path) ← remove lowest cost from frontier

        if node = goal:
            return path, cost

        if node not in visited:
            add node to visited
            for each (neighbor, edge_cost) in graph[node]:
                new_cost ← cost + edge_cost
                new_path ← path + [neighbor]
                add (new_cost, neighbor, new_path) to frontier

    return None, infinity
