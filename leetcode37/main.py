#!/usr/bin/env python3


class Solution:
    def __init__(self):
        self.mark = []
        self.mark_v = []
        self.mark_h = []

        self.board = []
        self.n = 0

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.prepare(board)
        self.find(0, 0)

    def prepare(self, board):
        self.board = board
        self.n = len(self.board)

        n1 = self.n // 3
        self.mark = [[]] * n1
        for i in range(n1):
            self.mark[i] = [[]] * n1
        for i in range(n1):
            for j in range(n1):
                self.mark[i][j] = [0] * 9
        self.mark_h = [[]] * self.n
        self.mark_v = [[]] * self.n
        for i in range(self.n):
            self.mark_v[i] = [0] * 9
            self.mark_h[i] = [0] * 9

        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == '.':
                    continue
                k = int(self.board[i][j]) - 1
                i1 = i // 3
                j1 = j // 3
                self.mark[i1][j1][k] = 1
                self.mark_h[i][k] = 1
                self.mark_v[j][k] = 1

    def find(self, i, j):
        if i == self.n and j == 0:
            return True

        if self.board[i][j] != '.':
            i1, j1 = self.next_pos(i, j)
            return self.find(i1, j1)

        for k in range(9):
            if self.check(i, j, k):
                self.board[i][j] = str(k + 1)
                self.set_mark(i, j, k)
                i1, j1 = self.next_pos(i, j)
                if self.find(i1, j1):
                    return True
                self.unset_mark(i, j, k)
                self.board[i][j] = '.'
        return False

    def check(self, i, j, k):
        i1 = i // 3
        j1 = j // 3
        if self.mark[i1][j1][k] == 1:
            return False
        if self.mark_h[i][k] == 1:
            return False
        if self.mark_v[j][k] == 1:
            return False
        return True

    def next_pos(self, i, j):
        j += 1
        if j == self.n:
            i += 1
            j = 0
        return (i, j)

    def set_mark(self, i, j, k):
        self.mark[i // 3][j // 3][k] = 1
        self.mark_h[i][k] = 1
        self.mark_v[j][k] = 1

    def unset_mark(self, i, j, k):
        self.mark[i // 3][j // 3][k] = 0
        self.mark_h[i][k] = 0
        self.mark_v[j][k] = 0


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    s = Solution()
    s.solveSudoku(board)
    for row in board:
        print(row)
