class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = [0] * 26
        for c in s:
            hash[ord(c) - ord("a")] += 1
        for c in t:
            hash[ord(c) - ord("a")] -= 1
        for n in hash:
            if n != 0:
                return False
        return True
