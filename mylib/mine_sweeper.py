import random


class MSBoard:
    def __init__(self, size: int = 10, mines: int = 10):
        self.size, self.mines = int(size), min(size ** 2 - 1, int(mines))
        self.make_board()

    def make_board(self):
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

        setted_mines = 0
        while setted_mines < self.mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.board[x][y] != -1:
                self.board[x][y] = -1
                setted_mines += 1

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:
                    continue
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= i + dx < self.size and 0 <= j + dy < self.size and self.board[i + dx][j + dy] == -1:
                            self.board[i][j] += 1

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:
                    self.board[i][j] = "||💣||"
                else:
                    self.board[i][j] = f"||{["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"][self.board[i][j]]}||"
