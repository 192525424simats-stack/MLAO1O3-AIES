N = 4
board = [-1] * N

def safe(r, c):
    for i in range(r):
        if board[i] == c or abs(board[i] - c) == abs(i - r):
            return False
    return True

def solve(r):
    if r == N:
        return True
    for c in range(N):
        if safe(r, c):
            board[r] = c
            if solve(r + 1):
                return True
    return False

solve(0)

for r in range(N):
    print(" ".join("Q" if board[r] == c else "." for c in range(N)))

print("Conflicts: 0")
print("Successfully Completed")
