import math

ROWS = 6
COLS = 7

board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print("\n  1   2   3   4   5   6   7")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * 29)


def valid_columns():
    return [c for c in range(COLS) if board[0][c] == ' ']


def drop_piece(col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row
    return -1


def check_winner(piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False


def is_full():
    return len(valid_columns()) == 0


def evaluate():
    if check_winner('O'):
        return 100
    if check_winner('X'):
        return -100
    return 0


def minimax(depth, maximizing):
    score = evaluate()

    if score == 100 or score == -100:
        return score

    if depth == 0 or is_full():
        return 0

    if maximizing:
        best = -math.inf

        for col in valid_columns():
            row = drop_piece(col, 'O')

            value = minimax(depth - 1, False)
            board[row][col] = ' '

            best = max(best, value)

        return best

    else:
        best = math.inf

        for col in valid_columns():
            row = drop_piece(col, 'X')

            value = minimax(depth - 1, True)
            board[row][col] = ' '

            best = min(best, value)

        return best


def best_move():
    best_score = -math.inf
    move = valid_columns()[0]

    for col in valid_columns():

        row = drop_piece(col, 'O')

        score = minimax(3, False)

        board[row][col] = ' '

        if score > best_score:
            best_score = score
            move = col

    return move


print("CONNECT FOUR - PLAYER vs AI")

while True:

    print_board()

    # Player move
    try:
        col = int(input("Choose a column (1-7): ")) - 1

        if col not in valid_columns():
            print("Invalid column!")
            continue

        drop_piece(col, 'X')

    except ValueError:
        print("Enter a number from 1 to 7.")
        continue

    if check_winner('X'):
        print_board()
        print("Congratulations! You defeated the AI!")
        break

    if is_full():
        print_board()
        print("Game Draw!")
        break

    # AI move
    ai_col = best_move()
    drop_piece(ai_col, 'O')

    print("AI selected column:", ai_col + 1)

    if check_winner('O'):
        print_board()
        print("AI wins!")
        break

    if is_full():
        print_board()
        print("Game Draw!")
        break
