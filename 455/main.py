class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = len(s) - 1
        result = 0
        for j in range(len(g) - 1, -1, -1):
            if i >= 0 and s[i] >= g[j]:
                result += 1
                i -= 1
        return result
