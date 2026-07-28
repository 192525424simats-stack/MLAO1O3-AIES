                                                             #PSEUDO CODES 

----------------------------------------------------------- #1 BFS PROGRAM--------------------------------------------------------------------
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


 ------------------------------------------------------------#2 UCS PROGRAM-------------------------------------------------------------

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

---------------------------------------------------------------#3 SWI PROLOG PROGRAM---------------------------------------------------------

START

1. Declare Marcus as a man.
2. Declare Marcus as a Pompeian.
3. Declare Caesar as a ruler.
4. Declare that Marcus tried to assassinate Caesar.

5. IF a person is a Pompeian
      THEN the person is a Roman.

6. IF a person is a man
      THEN the person is a person.

7. Every person is loyal to someone.

8. IF a person tries to assassinate a ruler
      THEN the person is not loyal to that ruler.

9. IF a person is not loyal to Caesar
      THEN the person hates Caesar.

10. Check whether Marcus is loyal to Caesar.
      IF loyal
         Display "Marcus is loyal to Caesar."
      ELSE
         Display "Marcus is not loyal to Caesar."

11. Check whether Marcus hates Caesar.
      IF hates
         Display "Marcus hates Caesar."
      ELSE
         Display "Marcus does not hate Caesar."

STOP
            
--------------------------------------------------------------#4 A* PROGRAMS-------------------------------------------------------------------------------------

START

Create graph and heuristic values

Define A_STAR(start, goal)

    Create an empty priority queue
    Insert start node into the queue

    Set cost(start) = 0
    Set parent(start) = NULL

    WHILE queue is not empty

        Remove node with lowest priority

        IF current node = goal THEN
            Display path
            Display total cost
            STOP
        END IF

        FOR each neighbor of current node

            Calculate new_cost = current_cost + edge_cost

            IF neighbor is not visited
               OR new_cost is smaller than previous cost THEN

                Update neighbor cost
                Calculate priority = new_cost + heuristic(neighbor)
                Insert neighbor into queue
                Set parent of neighbor = current node

            END IF

        END FOR

    END WHILE

    Display "Path not found"

END

Call A_STAR(start, goal)

STOP

-----------------------------------------------------#5 GREEDY BEST FIRST SEARCH---------------------------------------------------------------------------



