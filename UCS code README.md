import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def ucs(start, goal):
    frontier = [(0, start, [start])]
    visited = set()
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal: return path, cost
        if node not in visited:
            visited.add(node)
            for n, c in graph[node]:
                heapq.heappush(frontier, (cost+c, n, path+[n]))
    return None, float('inf')

print(ucs('A','D'))
