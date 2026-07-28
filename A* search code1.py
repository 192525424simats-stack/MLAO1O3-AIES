import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

def a_star(start, goal):
    queue = []
    heapq.heappush(queue, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while queue:
        f, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (f_cost, neighbor))
                parent[neighbor] = current

    return None

start = 'A'
goal = 'G'

result = a_star(start, goal)

if result:
    path, cost = result
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found")
