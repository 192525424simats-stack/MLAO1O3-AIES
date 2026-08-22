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

-------------------------------------------------------------#8 AI MAZE GAME PROGRAM-----------------------------------------------------------------------------

START

Define the maze
Find the position of S as START
Find the position of G as GOAL

Create an empty queue
Add (START, empty path) to the queue

Create a set SEEN
Add START to SEEN

WHILE queue is not empty

    Remove the first element from the queue
    Get current position and path

    IF current position is GOAL THEN
        Display the path
        Display number of steps
        STOP
    END IF

    For each direction:
        Down
        Up
        Right
        Left

        Calculate the new position

        IF new position is inside the maze
           AND new position is not a wall
           AND new position is not already SEEN THEN

            Add new position to SEEN
            Add new position and updated path to the queue

        END IF

    END FOR

END WHILE

END

--------------------------------------------------------------------#9 4-QUEENS GAME PROGRAM----------------------------------------------------------------------

START

Set N = 4
Create BOARD of size N and initialize all positions to -1

FUNCTION SAFE(row, column)

    FOR each previous row i from 0 to row - 1

        IF BOARD[i] = column THEN
            RETURN FALSE
        END IF

        IF |BOARD[i] - column| = |i - row| THEN
            RETURN FALSE
        END IF

    END FOR

    RETURN TRUE

END FUNCTION


FUNCTION SOLVE(row)

    IF row = N THEN
        RETURN TRUE
    END IF

    FOR column from 0 to N - 1

        IF SAFE(row, column) THEN

            Place queen at BOARD[row] = column

            IF SOLVE(row + 1) = TRUE THEN
                RETURN TRUE
            END IF

        END IF

    END FOR

    RETURN FALSE

END FUNCTION


Call SOLVE(0)

FOR each row from 0 to N - 1

    FOR each column from 0 to N - 1

        IF BOARD[row] = column THEN
            PRINT "Q"
        ELSE
            PRINT "."
        END IF

    END FOR

END FOR

PRINT "Conflicts: 0"
PRINT "Successfully Completed"

END

------------------------------------------------------------------#10 WATER JUG PUZZLE GAME---------------------------------------------------------------------

START

Set capacities:
    A = 11
    B = 9
    TARGET = 8

Create a queue
Add initial state (0, 0) with an empty path to the queue

Create a SEEN set
Add (0, 0) to SEEN

WHILE queue is not empty

    Remove the first state from the queue
    Get amounts (a, b) and current path

    IF a = TARGET OR b = TARGET THEN
        PRINT solution path
        PRINT number of moves
        PRINT final state
        STOP
    END IF

    Generate possible states:

        Fill 11L jug
        Fill 9L jug
        Empty 11L jug
        Empty 9L jug

        Pour water from 11L jug to 9L jug
            Amount transferred = minimum of
            (water in 11L jug, empty space in 9L jug)

        Pour water from 9L jug to 11L jug
            Amount transferred = minimum of
            (water in 9L jug, empty space in 11L jug)

    FOR each new state

        IF new state is not in SEEN THEN
            Add new state to SEEN
            Add new state and updated path to queue
        END IF

    END FOR

END WHILE

END

--------------------------------------------------------------------#11 CONNECT FOUR AI VS HUMAN--------------------------------------------------------------

START

Create 6 × 7 Connect Four board

FUNCTION CHECK_WINNER(piece)
    Check horizontal, vertical, and diagonal groups of 4
    Return TRUE if four pieces match
    Otherwise return FALSE
END FUNCTION

FUNCTION MINIMAX(depth, maximizing)
    Evaluate the board

    IF game is won OR depth = 0 OR board is full
        Return score
    END IF

    Generate all valid moves

    IF maximizing
        Return maximum score of possible moves
    ELSE
        Return minimum score of possible moves
    END IF
END FUNCTION

FUNCTION BEST_MOVE
    Check all valid columns
    Use MINIMAX to calculate each move's score
    Select the move with highest score
    Return best column
END FUNCTION

WHILE game is not over

    Display board

    Get player's column
    Place X

    IF player wins
        Display "Player Wins"
        STOP
    END IF

    AI selects BEST_MOVE
    Place O

    IF AI wins
        Display "AI Wins"
        STOP
    END IF

    IF board is full
        Display "Game Draw"
        STOP
    END IF

END WHILE

END

-------------------------------------------------------------#12 8-PUZZLE GAME PROGRAM---------------------------------------------------------------------------

START

Define GOAL state as:
1 2 3
4 5 6
7 8 0

FUNCTION MANHATTAN(state)
    Set distance = 0
    FOR each tile except 0
        Find current position and goal position
        Add row and column distance
    END FOR
    RETURN distance
END FUNCTION

FUNCTION GET_NEIGHBORS(state)
    Find position of 0
    Generate possible moves: Up, Down, Left, Right
    Swap 0 with the valid neighboring tile
    Return new states and actions
END FUNCTION

FUNCTION A_STAR(start)

    Create priority queue
    Insert start state with:
        g = 0
        h = MANHATTAN(start)
        f = g + h

    Create VISITED set

    WHILE priority queue is not empty

        Remove state with lowest f

        IF state is already visited
            CONTINUE
        END IF

        Add state to VISITED

        IF state = GOAL
            RETURN solution path
        END IF

        Generate neighboring states

        FOR each neighbor
            Calculate:
                g = current cost + 1
                h = MANHATTAN(neighbor)
                f = g + h

            Add neighbor to priority queue
        END FOR

    END WHILE

    RETURN no solution
END FUNCTION

Set initial scrambled state

Call A_STAR(initial state)

Display Initial State
Display Goal State
Display Solution Path
Display Minimum Moves

END

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
