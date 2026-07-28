graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 5]
}

def minimax(node, maximizing):
    if isinstance(graph[node][0], int):
        if maximizing:
            return max(graph[node])
        else:
            return min(graph[node])

    left = minimax(graph[node][0], not maximizing)
    right = minimax(graph[node][1], not maximizing)

    if maximizing:
        return max(left, right)
    else:
        return min(left, right)

result = minimax('A', True)

print("Optimal Value:", result)
