from collections import deque

maze = [
    "S.#...#",
    "..#.#.#",
    "#...#..",
    "###.##.",
    ".......",
    ".#####.",
    "......G"
]

for r in range(7):
    for c in range(7):
        if maze[r][c] == 'S':
            start = (r, c)
        if maze[r][c] == 'G':
            goal = (r, c)

q = deque([(start, [])])
seen = {start}

while q:
    (r, c), path = q.popleft()

    if (r, c) == goal:
        print("Path:", path + [(r, c)])
        print("Steps:", len(path))
        break

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 7 and 0 <= nc < 7 and
            maze[nr][nc] != '#' and (nr, nc) not in seen):

            seen.add((nr, nc))
            q.append(((nr, nc), path + [(r, c)]))
