FUNCTION BFS(start):
    visited ← empty list
    queue ← list containing start

    WHILE queue is not empty:
        node ← remove first element from queue
        IF node not in visited:
            add node to visited
            add all neighbors of node to queue

    PRINT "BFS:", visited
FUNCTION DFS(node, visited):
    IF node not in visited:
        add node to visited
        FOR each neighbor in graph[node]:
            CALL DFS(neighbor, visited)
