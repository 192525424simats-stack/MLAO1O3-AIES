import heapq

graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 4), ('D', 7)],
    'B': [('D', 1)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 7,
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 1,
    'G': 0
}

def astar(start, goal):
    queue = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while queue:
        f, node = heapq.heappop(queue)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, cost[goal]

        for neighbor, weight in graph[node]:
            new_cost = cost[node] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = node

    return None, None

path, total_cost = astar('S', 'G')

if path:
    print("Path:", " -> ".join(path))
    print("Cost:", total_cost)
else:
    print("Path not found")
