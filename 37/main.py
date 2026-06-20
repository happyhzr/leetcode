class Solution:
    board: list[list[str]] = []
    row_used: list[set[str]] = []
    col_used: list[set[str]] = []
    box_used: list[set[str]] = []

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row_used = [set() for _ in range(9)]
        self.col_used = [set() for _ in range(9)]
        self.box_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                if num == ".":
                    continue
                self.row_used[row].add(num)
                self.col_used[col].add(num)
                self.box_used[(row // 3) * 3 + (col // 3)].add(num)
        self.backtracking(0, 0)
        return self.board

    def backtracking(self, row: int, col: int) -> bool:
        if row == 9:
            return True
        next_row = row
        next_col = col + 1
        if next_col == 9:
            next_row += 1
            next_col = 0
        if self.board[row][col] != ".":
            return self.backtracking(next_row, next_col)
        for num in range(1, 10):
            num_str = str(num)
            if self.is_valid(row, col, num_str):
                self.board[row][col] = num_str
                self.row_used[row].add(num_str)
                self.col_used[col].add(num_str)
                self.box_used[(row // 3) * 3 + (col // 3)].add(num_str)
                if self.backtracking(next_row, next_col):
                    return True
                self.board[row][col] = "."
                self.row_used[row].remove(num_str)
                self.col_used[col].remove(num_str)
                self.box_used[(row // 3) * 3 + (col // 3)].remove(num_str)

    def is_valid(self, row: int, col: int, num: str) -> bool:
        if num in self.row_used[row]:
            return False
        if num in self.col_used[col]:
            return False
        if num in self.box_used[(row // 3) * 3 + (col // 3)]:
            return False
        return True
