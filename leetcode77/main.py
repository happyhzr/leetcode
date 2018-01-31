#!/usr/bin/env python3


class Solution:
    def __init__(self):
        self.k = 0
        self.n = 0
        self.array = []
        self.result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        self.dfs(1, k)
        return self.result

    def dfs(self, i, k):
        if k == 0:
            self.result.append(self.array[:])
            return
        if self.n - i + 1 < k:
            return
        for j in range(i, self.n + 1):
            self.array.append(j)
            self.dfs(j + 1, k - 1)
            self.array = self.array[:-1]
