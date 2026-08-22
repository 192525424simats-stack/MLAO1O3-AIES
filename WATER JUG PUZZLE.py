from collections import deque

A, B, target = 11, 9, 8
q = deque([((0, 0), [])])
seen = {(0, 0)}

while q:
    (a, b), path = q.popleft()

    if a == target or b == target:
        print("Solution:", path)
        print("Moves:", len(path), "Final:", (a, b))
        break

    states = [
        ((A, b), "Fill 11L"),
        ((a, B), "Fill 9L"),
        ((0, b), "Empty 11L"),
        ((a, 0), "Empty 9L")
    ]

    x = min(a, B-b)
    states.append(((a-x, b+x), "Pour 11L -> 9L"))

    x = min(b, A-a)
    states.append(((a+x, b-x), "Pour 9L -> 11L"))

    for state, action in states:
        if state not in seen:
            seen.add(state)
            q.append((state, path + [action]))
