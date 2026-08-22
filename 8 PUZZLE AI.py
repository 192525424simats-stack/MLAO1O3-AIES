import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan(state):
    distance = 0

    for i, value in enumerate(state):

        if value == 0:
            continue

        goal_index = GOAL.index(value)

        current_row = i // 3
        current_col = i % 3

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, action in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(
                (tuple(new_state), action)
            )

    return neighbors


def a_star(start):

    priority_queue = []

    h = manhattan(start)

    heapq.heappush(
        priority_queue,
        (h, 0, start, [])
    )

    visited = set()

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        if state == GOAL:
            return path

        for next_state, action in get_neighbors(state):

            if next_state not in visited:

                new_g = g + 1
                new_h = manhattan(next_state)
                new_f = new_g + new_h

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        next_state,
                        path + [action]
                    )
                )

    return None


# Initial scrambled state
start = (
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
)

solution = a_star(start)

print("Initial State:")
print(start[0:3])
print(start[3:6])
print(start[6:9])

print("\nGoal State:")
print(GOAL[0:3])
print(GOAL[3:6])
print(GOAL[6:9])

print("\nSolution:")
print(solution)

print("Minimum moves:", len(solution))
