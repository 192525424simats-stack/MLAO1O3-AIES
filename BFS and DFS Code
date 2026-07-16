graph = {
    1: [2, 7],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

def bfs(start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    print("BFS:", visited)

def dfs(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

visited = []
bfs(1)
dfs(1, visited)
print("DFS:", visited)
