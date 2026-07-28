graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 5]
}

def alphabeta(node, alpha, beta, maximizing):
    if isinstance(graph[node][0], int):
        if maximizing:
            return max(graph[node])
        else:
            return min(graph[node])

    if maximizing:
        value = float('-inf')
        for child in graph[node]:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in graph[node]:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

result = alphabeta('A', float('-inf'), float('inf'), True)

print("alpha-beta prunning optimal value:", result)
