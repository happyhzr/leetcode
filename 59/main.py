class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        m = [[0] * n for _ in range(n)]
        loop = n // 2
        i = 0
        j = 0
        a = 1
        for k in range(loop):
            while j <= n - 2 - k:
                m[i][j] = a
                a += 1
                j += 1
            while i <= n - 2 - k:
                m[i][j] = a
                a += 1
                i += 1
            while j >= 1 + k:
                m[i][j] = a
                a += 1
                j -= 1
            while i >= 1 + k:
                m[i][j] = a
                a += 1
                i -= 1
            i += 1
            j += 1
        if n % 2 == 1:
            m[i][j] = a
        return m
