import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def greedy_best_first(start, goal):
    visited = set()
    queue = [(heuristic[start], start)]
    parent = {start: None}

    while queue:
        h, node = heapq.heappop(queue)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic[neighbor], neighbor))
                    parent[neighbor] = node

    return None

path = greedy_best_first('A', 'G')

if path:
    print("Path:", " -> ".join(path))
else:
    print("Path not found")
