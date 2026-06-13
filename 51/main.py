class Solution:
    result: list[list[str]]
    board: list[str]

    def __init__(self) -> None:
        self.result = []
        self.board = []

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.result = []
        self.board = ["." * n for _ in range(n)]
        self.backtracking(0)
        return self.result

    def backtracking(self, row: int) -> None:
        if row == len(self.board):
            self.result.append(self.board.copy())
            return
        for col in range(0, len(self.board)):
            if self.is_valid(row, col):
                self.board[row] = (
                    self.board[row][:col] + "Q" + self.board[row][col + 1 :]
                )
                self.backtracking(row + 1)
                self.board[row] = (
                    self.board[row][:col] + "." + self.board[row][col + 1 :]
                )

    def is_valid(self, row: int, col: int) -> bool:
        for i in range(0, row):
            if self.board[i][col] == "Q":
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < len(self.board):
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
