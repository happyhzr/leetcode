class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hash = [0] * 26
        for i, c in enumerate(s):
            hash[ord(c) - ord("a")] = i
        result = []
        left = 0
        right = 0
        for i, c in enumerate(s):
            right = max(right, hash[ord(c) - ord("a")])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
