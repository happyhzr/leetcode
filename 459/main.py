class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length == 0:
            return False
        next = self.get_next(s)
        max = next[length - 1]
        if max > -1 and length % (length - max - 1) == 0:
            return True
        return False

    def get_next(self, s: str) -> list[int]:
        next = [0] * len(s)
        next[0] = -1
        j = -1
        i = 1
        while i < len(s):
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
            i += 1
        return next
