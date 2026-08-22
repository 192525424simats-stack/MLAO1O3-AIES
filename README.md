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
            
--------------------------------------------------------------#4 A* PROGRAM-------------------------------------------------------------------------------------

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

------------------------------------------------------#5 GREEDY BEST FIRST SEARCH PROGRAM ---------------------------------------------------------------------------

START

Create the graph
Create the heuristic values

FUNCTION GREEDY_BEST_FIRST(start, goal)

    Create an empty priority queue
    Insert the start node into the queue using its heuristic value

    Create an empty visited set
    Set parent(start) = NULL

    WHILE queue is not empty

        Remove the node with the lowest heuristic value

        IF current node = goal THEN
            Create an empty path

            WHILE current node is not NULL
                Add current node to the path
                Move to its parent
            END WHILE

            Reverse the path
            RETURN path
        END IF

        IF current node is not visited THEN
            Mark current node as visited

            FOR each neighbor of current node

                IF neighbor is not visited THEN
                    Insert neighbor into the queue using its heuristic value
                    Set parent(neighbor) = current node
                END IF

            END FOR

        END IF

    END WHILE

    RETURN "Path not found"

END FUNCTION

Call GREEDY_BEST_FIRST(start, goal)

IF path exists THEN
    Print path
ELSE
    Print "Path not found"
END IF

STOP

-----------------------------------------------------------------#6 MINIMAX PROGRAM--------------------------------------------------------------------------

START

Create the game tree

FUNCTION MINIMAX(node, maximizing)

    IF node is a leaf node THEN
        IF maximizing THEN
            RETURN maximum value of the node
        ELSE
            RETURN minimum value of the node
        END IF
    END IF

    left  = MINIMAX(left child, NOT maximizing)
    right = MINIMAX(right child, NOT maximizing)

    IF maximizing THEN
        RETURN maximum(left, right)
    ELSE
        RETURN minimum(left, right)
    END IF

END FUNCTION

result = MINIMAX(A, TRUE)

Print result

STOP

----------------------------------------------------------------#7 DECISION MAKING PROGRAM---------------------------------------------------------------------

BEGIN

IMPORT math

STORE the Play Tennis dataset in DATA

SET attributes = [Outlook, Temperature, Humidity, Wind]

FUNCTION Entropy(rows)

    COUNT number of Yes values
    COUNT number of No values

    SET total = number of rows
    SET entropy = 0

    IF Yes count > 0 THEN
        SET p_yes = Yes count / total
        entropy = entropy - (p_yes × log2(p_yes))
    END IF

    IF No count > 0 THEN
        SET p_no = No count / total
        entropy = entropy - (p_no × log2(p_no))
    END IF

    RETURN entropy

END FUNCTION


FUNCTION InformationGain(rows, column)

    SET total_entropy = Entropy(rows)

    FIND all unique values of the selected attribute

    SET weighted_entropy = 0

    FOR each value in the attribute

        CREATE subset containing rows with that value

        SET subset_entropy = Entropy(subset)

        weighted_entropy =
            weighted_entropy +
            (size of subset / size of rows) × subset_entropy

    END FOR

    SET information_gain =
        total_entropy - weighted_entropy

    RETURN information_gain

END FUNCTION


CALCULATE total_entropy = Entropy(DATA)

DISPLAY total_entropy

FOR each attribute from Outlook, Temperature, Humidity and Wind

    CALCULATE information gain

    DISPLAY attribute and information gain

END FOR


CREATE a list of all information gain values

FIND the maximum information gain

FIND the attribute having maximum information gain

DISPLAY best attribute

DISPLAY highest information gain

END

----------------------------------------------------------

