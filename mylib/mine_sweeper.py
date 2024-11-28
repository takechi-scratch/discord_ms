import random


def make_ms(size: int = 10, mines: int = 10):
    size, mines = int(size), min(size ** 2 - 1, int(mines))
    board = [[0 for _ in range(size)] for _ in range(size)]

    setted_mines = 0
    while setted_mines < mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if board[x][y] != -1:
            board[x][y] = -1
            setted_mines += 1

    for i in range(size):
        for j in range(size):
            if board[i][j] == -1:
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= i + dx < size and 0 <= j + dy < size and board[i + dx][j + dy] == -1:
                        board[i][j] += 1

    for i in range(size):
        for j in range(size):
            if board[i][j] == -1:
                board[i][j] = "||💣||"
            else:
                board[i][j] = f"||{["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"][board[i][j]]}||"

    return board
