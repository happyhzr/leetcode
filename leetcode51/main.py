#!/usr/bin/env python


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.results = []
        self.vector = [-1] * n
        self.n = n
        self.find(0)
        return self.results

    def find(self, i):
        if i == self.n:
            self.results.append(self.gen_map())
            return
        for j in range(0, self.n):
            if self.is_valid(i, j):
                self.vector[i] = j
                self.find(i + 1)
                self.vector[i] = -1

    def gen_map(self):
        map = []
        for i in self.vector:
            old = '.' * len(self.vector)
            new = old[:i] + 'Q' + old[i + 1:]
            map.append(new)
        return map

    def is_valid(self, i, j):
        for k in range(0, i):
            if self.vector[k] == j:
                return False
            dy = i - k
            dx = self.vector[k] - j
            if dx < 0:
                dx = -dx
            if dx == dy:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
